import os, json
import click
import sys
import uuid
import concurrent.futures
from nomad_media_cli.helpers.utils import initialize_sdk

@click.command()
@click.option("--source", help="Local OS file or folder path specifying the files or folders to upload. For example: file.jpg or folderName/file.jpg or just folderName.")
@click.option("--id", help="Nomad ID of the Asset Folder to upload the source file(s) and folder(s) into.")
@click.option("--url", help="The Nomad URL of the Asset (file or folder) to list the assets for (bucket::object-key).")
@click.option("--object-key", help="Object-key of the Asset (file or folder) to list the assets for. This option assumes the default bucket that was previously set with the `set-bucket` command.")
@click.option("-r", "--recursive", is_flag=True, help="Recursively upload a folder")
@click.pass_context
def upload_assets(ctx, source, id, url, object_key, recursive):
    """Upload assets"""
    
    initialize_sdk(ctx)
    nomad_sdk = ctx.obj["nomad_sdk"]
    config = ctx.obj["config"]

    if not id and not url and not object_key:
        click.echo(json.dumps({"error": "Please provide an id, url, or object-key."}))
        sys.exit(1)

    try:
        parent_id = None        

        if not source:
            click.echo(json.dumps({ "error": "Please provide a file or folder to upload." }))
            sys.exit(1)
            
        if not os.path.exists(source):
            click.echo(json.dumps({ "error": "Source path does not exist." }))
            sys.exit(1)
            
        if not id and not url and not object_key:
            click.echo(json.dumps({ "error": "Please provide a parent id, url, or objectKey." }))
            sys.exit(1)
            
        if id and not is_valid_uuid(id):
            click.echo(json.dumps({ "error": "Please provide a valid UUID." }))
            sys.exit(1)

        if url and "::" not in url:
            click.echo(json.dumps({ "error": "Please provide a valid path." }))
            sys.exit(1)

        if object_key:
            if not object_key.endswith("/"):            
                object_key = f"{object_key}/"
                
            if "bucket" in config:
                url = f"{config['bucket']}::{object_key}"
            else:
                click.echo(json.dumps({ "error": "Please set bucket using `set-bucket` or use url." }))
                sys.exit(1)
            
        if url:
            if not url.endswith("/"):
                url = f"{url}/"            

            id_search_response = nomad_sdk.search(None, None, None,
                [
                    {
                        "fieldName": "url",
                        "operator": "equals",
                        "values": url
                    }
                ], None, None, None, None, None, None, None, None, None, None, None)
            
            if len(id_search_response["items"]) == 0:
                click.echo(json.dumps({ "error": "No asset found with the provided URL." }))
                sys.exit(1)
                
            parent_id = id_search_response["items"][0]["identifiers"]["parentId"]
        elif id:
            parent_id = id
            
        response = nomad_sdk.get_asset(parent_id)
        if not response:
            click.echo(json.dumps({ "error": f"Parent folder not found: {parent_id}." }))
            sys.exit(1)
            
        if response["assetType"] != 1:
            click.echo(json.dumps({ "error": "Asset must be a folder" }))
            sys.exit(1)
            
        if os.path.isdir(source):
            if recursive:

                source_name = os.path.basename(source)
                folder_id = find_folder_id(parent_id, source_name, 1, nomad_sdk)                  

                folder_id_map = {source: folder_id}
                
                for root, dirs, files in os.walk(source):
                    folder_name = os.path.basename(root)
                    folder_id = folder_id_map.get(root)

                    if not folder_id:
                        parent_folder_id = folder_id_map[os.path.dirname(root)]

                        folder_id = find_folder_id(parent_folder_id, folder_name, 1, nomad_sdk)

                        folder_id_map[root] = folder_id

                    for name in files:
                        if find_folder_id(folder_id, name, 2, nomad_sdk):
                            continue

                        file_path = os.path.join(root, name)
                        if os.path.getsize(file_path) == 0:
                            continue
                        
                        try:
                            upload_with_retry(file_path, folder_id, nomad_sdk)
                        except Exception as e:
                            click.echo(json.dumps({ "error": f"Error uploading file: {file_path} - {e}" }))
                    
            else:
                click.echo(json.dumps({ "error": "Please use the --recursive option to upload directories." }))
                sys.exit(1)
        else:
            if os.path.getsize(source) == 0:
                click.echo(json.dumps({ "error": "File is empty." }))
                sys.exit(1)                
            
            asset_id = upload_with_retry(source, parent_id, nomad_sdk)
            click.echo(json.dumps(asset_id, indent=4))
                
    except Exception as e:
        click.echo(json.dumps({ "error": f"Error uploading assets: {e}" }))
        sys.exit(1)
        
def find_folder_id(parent_id, folder_name, asset_type, nomad_sdk):
    offset = 0
    folder_id = None
    while True:
        nomad_folders = nomad_sdk.search(None, offset, None,
            [
                {
                    "fieldName": "parentId",
                    "operator": "equals",
                    "values": parent_id
                },
                {
                    "fieldName": "assetType",
                    "operator": "equals",
                    "values": asset_type
                }
            ],
            None, None, None, None, None, None, None, None, None, None, None)                     

        if len(nomad_folders["items"]) == 0:
            break

        folder = next((nomad_folder for nomad_folder in nomad_folders["items"] if nomad_folder["title"] == folder_name), None)
        if folder:
            folder_id = folder["id"]
            break

        offset += 1
        
    if not folder_id and asset_type == 1:
        folder = nomad_sdk.create_folder_asset(parent_id, folder_name)
        folder_id = folder["id"]
        
    return folder_id
        
def upload_with_retry(file_path, folder_id, nomad_sdk, retries=3):
    for attempt in range(retries):
        try:
            response = nomad_sdk.upload_asset(None, None, None, "replace", file_path, folder_id, None)
            return response
        except Exception as e:
            if attempt == retries - 1:
                raise e
            
def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False