import click
import json
import os
import re
import sys
import requests
from concurrent.futures import ThreadPoolExecutor
from xml.etree import ElementTree as ET
from nomad_media_cli.helpers.capture_click_output import capture_click_output
from nomad_media_cli.helpers.utils import initialize_sdk
from nomad_media_cli.helpers.get_id_from_url import get_id_from_url
from nomad_media_cli.commands.common.asset.list_assets import list_assets
from nomad_media_cli.commands.common.asset.get_asset_details import get_asset_details

@click.command()
@click.option("--id", help="Asset ID, collection id, or saved search id to list the assets for.")
@click.option("--url", help="The Nomad URL of the Asset (file or folder) to download the archive for (bucket::object-key).")
@click.option("--object-key", help="Object-key only of the Asset (file or folder) to download the archive for. This option assumes the default bucket that was previously set with the `set-bucket` command.")
@click.option("--destination", default = ".", help="Local OS folder path specifying the location to download into. If this is not specified then it assumes the current folder")
@click.option("--threads", default=3, type=click.INT, help="The number of simultaneous downloads to perform. Default is 3.")
@click.option("--include-empty-folders", is_flag=True, help="Include empty folders in the download.")
@click.option("-r", "--recursive", is_flag=True, help="Download the assets in the subfolders also.")
@click.pass_context
def download_assets(ctx, id, url, object_key, destination, threads, include_empty_folders, recursive):
    """Download archive asset"""
    initialize_sdk(ctx)
    nomad_sdk = ctx.obj["nomad_sdk"]

    if not id and not url and not object_key:
        click.echo(json.dumps({ "error": "Please provide an id, url or object-key" }))
        sys.exit(1)
        
    if url or object_key:
        id = get_id_from_url(ctx, url, object_key, nomad_sdk)

    try:
        offset = 0
        filtered_assets = []
        while True:
            assets = capture_click_output(
                ctx,
                list_assets,
                id = id,
                page_size = 100, 
                page_offset = offset,
                order_by = "url",
                order_by_type = "ascending",
                recursive = recursive)

            if not assets or assets["totalItemCount"] == 0:
                break
                
            id_details = capture_click_output(
                ctx,
                get_asset_details,
                id = id, 
                object_key = None, 
                url = None) 

            asset_items = assets["items"]
            for asset in asset_items:
                if not include_empty_folders:
                    if asset["assetTypeDisplay"] == "Folder":
                        folder_details = capture_click_output(
                            ctx,
                            get_asset_details,
                            id = asset["id"])

                        if folder_details["assetStats"]["totalContentLength"] == 0:
                            continue

                filtered_assets.append(asset)
                    
            offset += 1
        
        download_assets_exec(filtered_assets, id_details, destination, threads)

    except Exception as e:
        click.echo(json.dumps({"error": f"Error downloading asset: {e}"}))
        sys.exit(1)
        
def download_assets_exec(assets, id_details, destination, threads):
    """Download assets"""
    num_file_assets = len([asset for asset in assets if asset["assetTypeDisplay"] == "File"])    
    is_folder_asset = id_details["properties"]["assetTypeDisplay"] == "Folder"
    
    if is_folder_asset:
        path = sanitize_path(id_details["properties"]["name"])
        os.makedirs(path, exist_ok=True)
        destination += f"/{path}"

    idx = 0
    with ThreadPoolExecutor(max_workers=threads) as executor:
        for asset in assets:
            url = asset["fullUrl"]
            
            if is_folder_asset:
                id_url = id_details["properties"]["url"]
                asset_url = asset["url"]
                path = asset_url.replace(id_url, "")            
                path = sanitize_path(path)
            else:
                path = sanitize_path(asset["name"])

            # is folder
            if not url:
                os.makedirs(f"{destination}/{path}", exist_ok=True)
            else:
                file_name = asset["name"]
                if destination:
                    file_name = f"{destination}/{path}"                

                print(f"({idx + 1}/{num_file_assets}) Downloading {file_name}", file=sys.stderr)

                response = requests.get(asset["fullUrl"])

                if response.status_code == 200:
                    with open(file_name, "wb") as f:
                        f.write(response.content)
                        
                    asset["downloadStatus"] = "Downloaded"
                    
                else:
                    asset["downloadStatus"] = "Failed"
                    downloadErrorMessage = None
                    try:
                        root = ET.fromstring(response.text)
                        error_code = root.find("Code").text
                        error_message = root.find("Message").text
                        downloadErrorMessage = f"{error_code}: {error_message}"
                    except ET.ParseError:
                        downloadErrorMessage = response.text
                        
                    asset["downloadErrorMessage"] = downloadErrorMessage
                    
                idx += 1

    click.echo(json.dumps(assets, indent=4))
    
def sanitize_path(path):
    """Sanitize the path by replacing invalid characters with _."""
    if path[-1] == "/":
        path = path[:-1]    

    if os.name == "nt":
        invalid_chars = r'[<>:"/\\|?*.]'
    else:
        invalid_chars = r'[/]'
        
    sanitized_path = re.sub(invalid_chars, '_', path)
    return sanitized_path
            
