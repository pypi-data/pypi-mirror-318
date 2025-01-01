import json
import os
import time
import unittest
from click.testing import CliRunner
from contextlib import redirect_stdout
from nomad_media_cli.cli import cli
from nomad_media_cli.helpers.get_content_definition_id import get_content_definition_id

class TestAssetBase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.runner = CliRunner()

        with open("nomad_media_cli/tests/test-config.json", "r") as file:
            test_config = json.load(file)
            cls.test_dir_id = test_config["testDirId"]
        
        result = cls.runner.invoke(cli, [
            "upload-assets", 
            "--source", "README.md",
            "--id", cls.test_dir_id
        ])
        
        if result.exit_code != 0:
            raise Exception(f"Failed to upload asset: {result.output}")
        
        cls.asset_id = result.output.replace('"', "").strip()
        time.sleep(5)

    @classmethod
    def setup_config(cls):
        config_path_result = cls.runner.invoke(cli, ["list-config-path"])
        if config_path_result.exit_code != 0:
            raise Exception(f"Need to run `nomad-media-cli init` before running tests")
        
        config_path = json.loads(config_path_result.output.strip())

        with open(config_path["path"], "r") as file:
            config = json.load(file)
            cls.config = config
            cls.config_path = config_path["path"]
            
    @classmethod
    def tearDownClass(cls):
        result = cls.runner.invoke(cli, [
            "delete-asset", 
            "--id", cls.asset_id
        ])
        
        if result.exit_code != 0:
            raise Exception(f"Failed to delete asset: {result.output}")
        
        print(f"Deleted asset with id: {cls.asset_id}")

class TestAssetDownload(unittest.TestCase):
    """Tests for downloading assets"""
    
    @classmethod
    def setUpClass(cls):
        cls.runner = CliRunner()

    def test_download_asset_by_id(self):
        """Test asset is downloaded successfully"""
        result = self.runner.invoke(cli, [
            "download-assets", 
            "--id", "cc35aa44-6d4a-407c-a1af-32a1fd465693"
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        output = result.output.split("[")[1].split("]")[0]
        asset_info = json.loads(f"[{output}]")
        
        self.assertTrue(os.path.exists(asset_info[0]["name"]))
        os.remove(asset_info[0]["name"])
        
    def test_download_asset_by_destination(self):
        """Test asset is downloaded to a destination successfully"""
        result = self.runner.invoke(cli, [
            "download-assets", 
            "--id", "cc35aa44-6d4a-407c-a1af-32a1fd465693",
            "--destination", "nomad_media_cli/tests/test_files"
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        output = result.output.split("[")[1].split("]")[0]
        asset_info = json.loads(f"[{output}]")
        
        self.assertTrue(os.path.exists(f"nomad_media_cli/tests/test_files/{asset_info[0]['name']}"))
        os.remove(f"nomad_media_cli/tests/test_files/{asset_info[0]['name']}")
        
    def test_download_asset_by_id_invalid(self):
        """Test invalid ID returns an error"""
        result = self.runner.invoke(cli, [
            "download-assets", 
            "--id", "invalid-id"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_download_asset_by_url(self):
        """Test asset is downloaded successfully"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", "cc35aa44-6d4a-407c-a1af-32a1fd465693"
        ])
        
        asset_details = json.loads(asset_details_result.output)
        url = asset_details["properties"]["url"]
        
        result = self.runner.invoke(cli, [
            "download-assets", 
            "--url", url
        ])
        
        self.assertEqual(result.exit_code, 0)
        
    def test_download_asset_by_url_invalid(self):
        """Test invalid URL returns an error"""
        result = self.runner.invoke(cli, [
            "download-assets", 
            "--url", "invalid-url"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_download_asset_by_object_key(self):
        """Test asset is downloaded successfully"""
        self.setup_config()

        bucket = self.config.get("bucket")
        if not bucket:
            self.skipTest("No default bucket set")
            
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", "cc35aa44-6d4a-407c-a1af-32a1fd465693"
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "download-assets", 
            "--object-key", object_key
        ])
        
        self.assertEqual(result.exit_code, 0)
        
    def test_download_asset_by_object_key_no_bucket(self):
        """Test missing bucket returns an error"""
        self.setup_config()

        bucket = self.config.get("bucket")
        if bucket:
            self.skipTest("Default bucket set")
            
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", "cc35aa44-6d4a-407c-a1af-32a1fd465693"
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "download-assets", 
            "--object-key", object_key
        ])
        
        self.assertNotEqual(result.exit_code, 0)

    def test_download_asset_by_object_key_invalid(self):
        """Test invalid object key returns an error"""
        result = self.runner.invoke(cli, [
            "download-assets", 
            "--object-key", "invalid-object-key"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_download_asset_folder(self):
        """Test folder is downloaded successfully"""
        result = self.runner.invoke(cli, [
            "download-assets", 
            "--id", "18a4acd4-95e5-46db-ac85-4cb5fddec085"
        ])
        
        self.assertEqual(result.exit_code, 0)
        
    def test_download_asset_folder_recursive(self):
        """Test folder is downloaded successfully"""
        result = self.runner.invoke(cli, [
            "download-assets", 
            "--id", "18a4acd4-95e5-46db-ac85-4cb5fddec085",
            "--recursive"
        ])
        
        self.assertEqual(result.exit_code, 0)

class TestAssetUpload(TestAssetBase):
    """Tests for uploading assets"""

    @classmethod
    def tearDownClass(cls):
        result = cls.runner.invoke(cli, [
            "delete-asset", 
            "--id", cls.asset_upload_id
        ])
        
        if result.exit_code != 0:
            raise Exception(f"Failed to delete asset: {result.output}")
        
        print(f"Deleted asset with id: {cls.asset_upload_id}")
    
    def test_upload_asset(self):
        """Test asset is uploaded successfully"""
        result = self.runner.invoke(cli, [
            "upload-assets", 
            "--source", "nomad_media_cli/tests/test_files/vid.mp4",
            "--id", self.test_dir_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_id = result.output.replace('"', "").strip()
        self.assertIsNotNone(asset_id)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", asset_id
        ])
        
        self.assertEqual(asset_details_result.exit_code, 0)
        
        self.asset_upload_id = asset_id
        
    def test_upload_asset_invalid_file(self):
        """Test invalid file returns an error"""
        result = self.runner.invoke(cli, [
            "upload-assets", 
            "--source", "nomad_media_cli/tests/test_files/invalid-file",
            "--id", self.test_dir_id
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_upload_asset_empty_file(self):
        """Test empty file returns an error"""
        result = self.runner.invoke(cli, [
            "upload-assets", 
            "--source", "nomad_media_cli/tests/__init__.py",
            "--id", self.test_dir_id
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_upload_asset_invalid_id(self):
        """Test invalid ID returns an error"""
        result = self.runner.invoke(cli, [
            "upload-assets", 
            "--source", "nomad_media_cli/tests/test_files/vid.mp4",
            "--id", "invalid-id"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_upload_asset_directory_flat(self):
        """Test uploading a directory of files with no subdirectories"""
        result = self.runner.invoke(cli, [
            "upload-assets", 
            "--source", "nomad_media_cli/tests/test_files",
            "--id", self.test_dir_id,
            "-r"
        ])
        
        self.assertEqual(result.exit_code, 0)
        num_files_in_dir = sum([len(files) + len(dirs) for _, dirs, files in os.walk("nomad_media_cli/tests/test_files")])
        
        list_assets_parent_result = self.runner.invoke(cli, [
            "list-assets", 
            "--id", self.test_dir_id
        ])
        
        self.assertEqual(list_assets_parent_result.exit_code, 0)
        
        output_json = json.loads(list_assets_parent_result.output)
        dir_id = next((item["id"] for item in output_json["items"] if item["name"] == "test_files/"), None)
        
        if not dir_id:
            self.fail("Directory not found")
            
        list_assets_result = self.runner.invoke(cli, [
            "list-assets", 
            "--id", dir_id
        ])

        self.assertEqual(list_assets_result.exit_code, 0)
        
        output_json = json.loads(list_assets_result.output)
        self.assertEqual(len(output_json["items"]), num_files_in_dir)
        
        self.asset_upload_id = dir_id
        
    def test_upload_asset_directory_small(self):
        """Test uploading a directory of files with a small number of files"""
        dir_path = "nomad_media_cli/tests"        

        result = self.runner.invoke(cli, [
            "upload-assets", 
            "--source", "nomad_media_cli/tests",
            "--id", self.test_dir_id,
            "-r"
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        list_assets_parent_result = self.runner.invoke(cli, [
            "list-assets", 
            "--id", self.test_dir_id
        ])
        
        self.assertEqual(list_assets_parent_result.exit_code, 0)
        
        output_json = json.loads(list_assets_parent_result.output)
        dir_id = next((item["id"] for item in output_json["items"] if item["name"] == f"{dir_path.split("/")[-1]}/"), None)
        self.asset_upload_id = dir_id      

        list_assets_result = self.runner.invoke(cli, [
            "list-assets", 
            "--id", dir_id,
            "-r"
        ])

        self.assertEqual(list_assets_result.exit_code, 0)
        
        output_json = json.loads(list_assets_result.output)
        items = output_json["items"]

        check_dir_structure(self, items, dir_path)
        
    def test_upload_asset_directory_large(self):
        """Test uploading a directory of files with a large number of files"""
        dir_path = "nomad_media_cli/commands"        

        result = self.runner.invoke(cli, [
            "upload-assets", 
            "--source", dir_path,
            "--id", self.test_dir_id,
            "-r"
        ])
        
        self.assertEqual(result.exit_code, 0)
            
        list_assets_parent_result = self.runner.invoke(cli, [
            "list-assets", 
            "--id", self.test_dir_id
        ])
        
        self.assertEqual(list_assets_parent_result.exit_code, 0)
        
        output_json = json.loads(list_assets_parent_result.output)
        dir_id = next((item["id"] for item in output_json["items"] if item["name"] == f"{dir_path.split("/")[-1]}/"), None)     
        self.asset_upload_id = dir_id   

        items = None
        page_offset = 0
        dir_assets = []

        while True:
            list_assets_result = self.runner.invoke(cli, [
                "list-assets", 
                "--id", dir_id,
                "--page-offset", page_offset, 
                "-r"
            ])

            self.assertEqual(list_assets_result.exit_code, 0)
            if list_assets_result.exit_code != 0:
                return

            output_json = json.loads(list_assets_result.output.replace("'", '"').replace("False", "false"))
            items = output_json["items"]
            dir_assets.extend(items)

            if len(items) == 0:
                break

            page_offset += 1
            
        check_dir_structure(self, dir_assets, dir_path)
        
    def test_upload_asset_directory_not_recursive(self):
        """Test directory returns an error"""
        result = self.runner.invoke(cli, [
            "upload-assets", 
            "--source", "nomad_media_cli/tests/test_files",
            "--id", self.test_dir_id
        ])
        
        self.assertNotEqual(result.exit_code, 0)

def check_dir_structure(self, dir_assets, path):
    remote_structure = {}
    path_var = path
    for item in dir_assets:
        path = item["url"].split("::")[1]
        parts = path.split("/")
        current = remote_structure
        for part in parts:
            if part == "":
                continue
            if part not in current:
                current[part] = {}
            current = current[part]
            
    path_dir_found = False
    while True:
        remote_dir_name = list(remote_structure.keys())[0]
        if remote_dir_name == path_var.split("/")[-1]:
            path_dir_found = True
            break
        remote_structure = remote_structure[remote_dir_name]
        
        if remote_structure == {}:
            break
        
    self.assertTrue(path_dir_found)

    local_structure = {}
    for root, dirs, files in os.walk(path_var):
        parts = root.split(os.sep)
        current = local_structure
        for part in parts:
            if part not in current:
                current[part] = {}
            current = current[part]
        for file in files:
            if os.path.getsize(os.path.join(root, file)) == 0:
                continue
            current[file] = {}

    remote_root = list(remote_structure.keys())[0]
    local_root = path_var.replace(os.sep, "/")

    remote_structure = remote_structure[remote_root]
    local_structure = local_structure[local_root]

    remote_structure = dict(sorted(remote_structure.items()))
    local_structure = dict(sorted(local_structure.items()))

    print(json.dumps(remote_structure, indent=4))
    print(json.dumps(local_structure, indent=4))
    self.assertEqual(remote_structure, local_structure)
    

class TestBucketCommands(TestAssetBase):
    def test_list_buckets(self):
        
        result = self.runner.invoke(cli, ["list-buckets"])
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json, list))
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")
        
    def test_set_default_bucket(self):
        
        self.setup_config()
        bucket = self.config.get("bucket")
            
        buckets_response = self.runner.invoke(cli, ["list-buckets"])
        buckets = json.loads(buckets_response.output)

        if len(buckets) == 0:
            self.skipTest("No buckets available")

        result = self.runner.invoke(cli, [
            "set-default-bucket",
            "--bucket", buckets[0]])
        
        self.assertEqual(result.exit_code, 0)
        
        with open(self.config_path, "r") as file:
            config = json.load(file)
            new_config_bucket = config.get("bucket")
            
        self.assertEqual(new_config_bucket, buckets[0])
        
        if bucket:
            result = self.runner.invoke(cli, [
                "set-default-bucket",
                "--bucket", bucket])

class TestAssetList(TestAssetBase):
    """Tests for listing assets"""
    
    def test_list_assets_file_by_id(self):
        
        result = self.runner.invoke(cli, [
            "list-assets", 
            "--id", self.asset_id,
            "--order-by", None,
            "--order-by-type", None
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json["items"], list))
            self.assertTrue(len(output_json["items"]) > 0)
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")
            
    def test_list_assets_folder_by_id(self):
        
        asset_parent_id = self.test_dir_id

        result = self.runner.invoke(cli, [
            "list-assets", 
            "--id", asset_parent_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json["items"], list))
            self.assertTrue(len(output_json["items"]) > 0)
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")
            
    def test_list_assets_folder_recursive(self):
        
        asset_parent_id = self.test_dir_id

        result = self.runner.invoke(cli, [
            "list-assets", 
            "--id", asset_parent_id,
            "--recursive"
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json["items"], list))
            self.assertTrue(len(output_json["items"]) > 0)
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")

    def test_list_assets_by_id_invalid(self):
        
        result = self.runner.invoke(cli, [
            "list-assets", 
            "--id", "invalid-id"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

    def test_list_assets_file_by_url(self):
        
        list_buckets_result = self.runner.invoke(cli, ["list-buckets"])
        buckets = json.loads(list_buckets_result.output)
        
        if len(buckets) == 0:
            self.skipTest("No buckets available")
            
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        url = asset_details["properties"]["url"]
            
        result = self.runner.invoke(cli, [
            "list-assets", 
            "--url", url
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json["items"], list))
            self.assertTrue(len(output_json["items"]) > 0)
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")
            
    def test_list_assets_folder_by_url(self):
        
        list_buckets_result = self.runner.invoke(cli, ["list-buckets"])
        buckets = json.loads(list_buckets_result.output)
        
        if len(buckets) == 0:
            self.skipTest("No buckets available")
            
        asset_parent_id = self.test_dir_id
        asset_parent_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", asset_parent_id
        ])
        
        asset_parent_details = json.loads(asset_parent_details_result.output)
        url = asset_parent_details["properties"]["url"]
            
        result = self.runner.invoke(cli, [
            "list-assets", 
            "--url", url
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json["items"], list))
            self.assertTrue(len(output_json["items"]) > 0)
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")

    def test_list_assets_by_url_invalid(self):
        
        result = self.runner.invoke(cli, [
            "list-assets", 
            "--url", "invalid-url"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
            
    def test_list_assets_by_file_object_key(self):
        
        self.setup_config()

        bucket = self.config.get("bucket")
        if not bucket:
            self.skipTest("No default bucket set")
            
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
            
        result = self.runner.invoke(cli, [
            "list-assets", 
            "--object-key", object_key
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json["items"], list))
            self.assertTrue(len(output_json["items"]) > 0)
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")
            
    def test_list_assets_by_folder_object_key(self):
        
        self.setup_config()

        bucket = self.config.get("bucket")
        if not bucket:
            self.skipTest("No default bucket set")
            
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "list-assets", 
            "--object-key", object_key
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json["items"], list))
            self.assertTrue(len(output_json["items"]) > 0)
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")
            
    def test_list_assets_by_object_key_no_bucket(self):
        
        self.setup_config()

        bucket = self.config.get("bucket")
        if bucket:
            self.skipTest("Default bucket set")
            
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "list-assets", 
            "--object-key", object_key
        ])
        
        self.assertNotEqual(result.exit_code, 0)
            
    def test_list_assets_by_object_key_invalid(self):
        
        result = self.runner.invoke(cli, [
            "list-assets", 
            "--object-key", "invalid-object-key"
        ])

        self.assertNotEqual(result.exit_code, 0)

    def test_list_assets_page_size(self):
        result = self.runner.invoke(cli, [
            "list-assets",
            "--id", self.asset_id,
            "--page-size", "10",
            "--page-offset", "0"
        ])
        self.assertEqual(result.exit_code, 0)
        output = json.loads(result.output)
        self.assertTrue(len(output["items"]) <= 10)
        
    def test_list_assets_invalid_page_size(self):
        result = self.runner.invoke(cli, [
            "list-assets",
            "--id", self.asset_id,
            "--page-size", "-1"
        ])
        self.assertNotEqual(result.exit_code, 0)

    def test_list_assets_page_offset(self):
        result = self.runner.invoke(cli, [
            "list-assets",
            "--id", self.asset_id,
            "--page-size", "1",
            "--page-offset", "0"
        ])
        self.assertEqual(result.exit_code, 0)

    def test_list_assets_invalid_offset(self):
        result = self.runner.invoke(cli, [
            "list-assets",
            "--id", self.asset_id,
            "--page-offset", "-1"
        ])
        self.assertNotEqual(result.exit_code, 0)
        
    def test_list_assets_page_offset_token(self):

        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])

        asset_details = json.loads(asset_details_result.output)
        parent_id = asset_details["properties"]["parentId"]        

        result = self.runner.invoke(cli, [
            "list-assets",
            "--id", parent_id,
            "--page-size", "1",
        ])
        
        result_json = json.loads(result.output)
        next_page_offset = result_json.get("nextPageOffset")

        if not next_page_offset:
            self.skipTest("No next page offset")
            
        result = self.runner.invoke(cli, [
            "list-assets",
            "--id", self.asset_id,
            "--page-offset-token", next_page_offset
        ])
        
        self.assertEqual(result.exit_code, 0)
        
    def test_list_asset_page_offset_token_invalid(self):
        result = self.runner.invoke(cli, [
            "list-assets",
            "--id", self.asset_id,
            "--page-offset-token", "invalid-token"
        ])
        self.assertNotEqual(result.exit_code, 0)
    
    def test_list_assets_sorting(self):
        result = self.runner.invoke(cli, [
            "list-assets",
            "--id", self.asset_id,
            "--order-by", "name",
            "--order-by-type", "desc"
        ])
        self.assertEqual(result.exit_code, 0)
        output = json.loads(result.output)
        
        names = [item["name"] for item in output["items"]]
        self.assertEqual(names, sorted(names, reverse=True))
    
    def test_list_assets_missing_params(self):
        result = self.runner.invoke(cli, ["list-assets"])
        self.assertNotEqual(result.exit_code, 0)

class TestAssetDetails(TestAssetBase):
    """Tests for getting asset details"""

    def test_get_asset_details_by_id(self):
        """Test full asset details are returned"""
        result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json, dict))
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")
            
    def test_get_asset_details_by_id_invalid(self):
        """Test invalid ID returns an error"""
        result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", "invalid-id"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
            
    def test_get_asset_details_by_url(self):
        """Test full asset details are returned"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        url = asset_details["properties"]["url"]
        
        result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--url", url
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json, dict))
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")
            
    def test_get_asset_details_by_url_invalid(self):
        """Test invalid URL returns an error"""
        result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--url", "invalid-url"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_get_asset_details_by_object_key(self):
        """Test full asset details are returned"""
        self.setup_config()

        bucket = self.config.get("bucket")
        if not bucket:
            self.skipTest("No default bucket set")
            
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--object-key", object_key
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json, dict))
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")
            
    def test_get_asset_details_by_object_key_no_bucket(self):
        """Test missing bucket returns an error"""
        self.setup_config()

        bucket = self.config.get("bucket")
        if bucket:
            self.skipTest("Default bucket set")
            
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--object-key", object_key
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_get_asset_details_by_object_key_invalid(self):
        """Test invalid object key returns an error"""
        result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--object-key", "invalid-object-key"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
class TestAssetAddAssetProperties(TestAssetBase):
    """Tests for adding asset properties"""
    
    def test_add_asset_properties(self):
        """Test asset properties are added successfully"""
        result = self.runner.invoke(cli, [
            "add-asset-properties", 
            "--id", self.asset_id,
            "--properties", '{"test": "test"}'
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        self.assertEqual(asset_details["customAttributes"]["test"], "test")
        
    def test_add_asset_properties_invalid_json(self):
        """Test invalid JSON returns an error"""
        result = self.runner.invoke(cli, [
            "add-asset-properties", 
            "--id", self.asset_id,
            "--properties", "invalid-json"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_add_asset_properties_name(self):
        """Test asset properties are added successfully"""
        result = self.runner.invoke(cli, [
            "add-asset-properties", 
            "--id", self.asset_id,
            "--name", "test",
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        self.assertEqual(asset_details["properties"]["displayName"], "test")
        
    def test_add_asset_properties_date(self):
        """Test asset properties are added successfully"""
        result = self.runner.invoke(cli, [
            "add-asset-properties", 
            "--id", self.asset_id,
            "--date", "2025-01-01T00:00:00Z",
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        self.assertEqual(asset_details["properties"]["displayDate"], "2025-01-01T00:00:00Z")
        
    def test_add_asset_properties_invalid_date(self):
        """Test invalid date returns an error"""
        result = self.runner.invoke(cli, [
            "add-asset-properties", 
            "--id", self.asset_id,
            "--date", "invalid-date",
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
class TestAssetAddAssetCollection(TestAssetBase):
    """Tests for adding asset collections"""
    
    def test_add_asset_collection_with_id(self):
        """Test asset collection is added successfully"""
        result = self.runner.invoke(cli, [
            "add-asset-collection", 
            "--id", self.asset_id,
            "--collection-name", "test-collection"
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        collections = asset_details["collections"]
        self.assertTrue(any(collection["description"] == "test-collection" for collection in collections))
        
    def test_add_asset_collection_with_id_invalid(self):
        """Test invalid ID returns an error"""
        result = self.runner.invoke(cli, [
            "add-asset-collection", 
            "--id", "invalid-id",
            "--collection-name", "test-collection"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_add_asset_collection_with_url(self):
        """Test asset collection is added successfully"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        url = asset_details["properties"]["url"]
        
        result = self.runner.invoke(cli, [
            "add-asset-collection", 
            "--url", url,
            "--collection-name", "test-collection1"
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--url", url
        ])
        
        asset_details = json.loads(asset_details_result.output)
        collections = asset_details["collections"]
        self.assertTrue(any(collection["description"] == "test-collection1" for collection in collections))
        
    def test_add_asset_collection_with_url_invalid(self):
        """Test invalid URL returns an error"""
        result = self.runner.invoke(cli, [
            "add-asset-collection", 
            "--url", "invalid-url",
            "--collection-name", "test-collection"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

    def test_add_asset_collection_with_object_key(self):
        """Test asset collection is added successfully"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "add-asset-collection", 
            "--object-key", object_key,
            "--collection-name", "test-collection2"
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--object-key", object_key
        ])
        
        asset_details = json.loads(asset_details_result.output)
        collections = asset_details["collections"]
        self.assertTrue(any(collection["description"] == "test-collection2" for collection in collections))
        
    def test_add_asset_collection_with_object_key_no_bucket(self):
        """Test missing bucket returns an error"""
        self.setup_config()

        bucket = self.config.get("bucket")
        if bucket:
            self.skipTest("Default bucket set")

        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])

        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]

        result = self.runner.invoke(cli, [
            "add-asset-collection", 
            "--object-key", object_key,
            "--collection-name", "test-collection"
        ])

        self.assertNotEqual(result.exit_code, 0)

    def test_add_asset_collection_with_object_key_invalid(self):
        """Test invalid object key returns an error"""
        result = self.runner.invoke(cli, [
            "add-asset-collection", 
            "--object-key", "invalid-object-key",
            "--collection-name", "test-collection"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

    def test_add_asset_collection_with_collection_id(self):
        """Test asset collection is added successfully"""
        collections = self.runner.invoke(cli, [
            "get-content-definition-contents",
            "--name", "Collection"
        ])

        collections = json.loads(collections.output)["items"]
        if len(collections) == 0:
            self.skipTest("No collections available")

        collection_id = collections[0]["id"]
        collection_name = collections[0]["title"]

        result = self.runner.invoke(cli, [
            "add-asset-collection", 
            "--id", self.asset_id,
            "--collection-id", collection_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        collections = asset_details["collections"]
        self.assertTrue(any(collection["description"] == collection_name for collection in collections))
        
    def test_add_asset_collection_with_collection_id_invalid(self):
        """Test invalid collection ID returns an error"""
        result = self.runner.invoke(cli, [
            "add-asset-collection", 
            "--id", self.asset_id,
            "--collection-id", "invalid-id"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
class TestAssetListAssetCollection(TestAssetBase):
    """Tests for listing asset collections"""
    
    def test_list_asset_tag_with_id(self):
        """Test asset collections are returned"""
        result = self.runner.invoke(cli, [
            "list-asset-collections", 
            "--id", self.asset_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json, list))
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")

    def test_list_asset_tag_with_id_invalid(self):
        """Test invalid ID returns an error"""
        result = self.runner.invoke(cli, [
            "list-asset-collections", 
            "--id", "invalid-id"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

    def test_list_asset_tag_with_url(self):
        """Test asset collections are returned"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        url = asset_details["properties"]["url"]
        
        result = self.runner.invoke(cli, [
            "list-asset-collections", 
            "--url", url
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json, list))
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")

    def test_list_asset_tag_with_url_invalid(self):
        """Test invalid URL returns an error"""
        result = self.runner.invoke(cli, [
            "list-asset-collections", 
            "--url", "invalid-url"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

    def test_list_asset_tag_with_object_key(self):
        """Test asset collections are returned"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "list-asset-collections", 
            "--object-key", object_key
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json, list))
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")

    def test_list_asset_tag_with_object_key_no_bucket(self):
        """Test missing bucket returns an error"""
        self.setup_config()

        bucket = self.config.get("bucket")
        if bucket:
            self.skipTest("Default bucket set")

        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])

        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]

        result = self.runner.invoke(cli, [
            "list-asset-collections", 
            "--object-key", object_key
        ])

        self.assertNotEqual(result.exit_code, 0)

    def test_list_asset_tag_with_object_key_invalid(self):
        """Test invalid object key returns an error"""
        result = self.runner.invoke(cli, [
            "list-asset-collections", 
            "--object-key", "invalid-object-key"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

class TestAssetRemoveAssetCollection(TestAssetBase):
    """Tests for removing asset collections"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        collections = cls.runner.invoke(cli, [
            "get-content-definition-contents",
            "--name", "Collection"
        ])

        collections = json.loads(collections.output)["items"]
        if len(collections) == 0:
            cls.skipTest("No collections available")

        cls.collection_id = collections[0]["id"]
        cls.collection_name = collections[0]["title"]

    def test_remove_asset_collection_id(self):
        """Test asset collection is removed successfully"""
        result = self.runner.invoke(cli, [
            "add-asset-collection", 
            "--id", self.asset_id,
            "--collection-id", self.collection_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        result = self.runner.invoke(cli, [
            "remove-asset-collection", 
            "--id", self.asset_id,
            "--collection-id", self.collection_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        collections = asset_details["collections"]
        self.assertFalse(self.collection_name in collections)
        
    def test_remove_asset_collection_id_invalid(self):
        """Test invalid collection ID returns an error"""
        result = self.runner.invoke(cli, [
            "remove-asset-collection", 
            "--id", self.asset_id,
            "--collection-id", "invalid-id"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_remove_asset_collection_with_url(self):
        """Test asset collection is removed successfully"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        url = asset_details["properties"]["url"]
        
        result = self.runner.invoke(cli, [
            "add-asset-collection", 
            "--url", url,
            "--collection-id", self.collection_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        result = self.runner.invoke(cli, [
            "remove-asset-collection", 
            "--url", url,
            "--collection-id", self.collection_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--url", url
        ])
        
        asset_details = json.loads(asset_details_result.output)
        collections = asset_details["collections"]
        self.assertFalse(self.collection_name in collections)
        
    def test_remove_asset_collection_with_url_invalid(self):
        """Test invalid URL returns an error"""
        result = self.runner.invoke(cli, [
            "remove-asset-collection", 
            "--url", "invalid-url",
            "--collection-name", "test-collection"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_remove_asset_collection_with_object_key(self):
        """Test asset collection is removed successfully"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "add-asset-collection", 
            "--object-key", object_key,
            "--collection-id", self.collection_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        result = self.runner.invoke(cli, [
            "remove-asset-collection", 
            "--object-key", object_key,
            "--collection-id", self.collection_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--object-key", object_key
        ])
        
        asset_details = json.loads(asset_details_result.output)
        collections = asset_details["collections"]
        self.assertFalse(self.collection_name in collections)
        
    def test_remove_asset_collection_with_object_key_no_bucket(self):
        """Test missing bucket returns an error"""
        self.setup_config()

        bucket = self.config.get("bucket")
        if bucket:
            self.skipTest("Default bucket set")

        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])

        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]

        result = self.runner.invoke(cli, [
            "add-asset-collection", 
            "--object-key", object_key,
            "--collection-id", self.collection_id
        ])

        self.assertNotEqual(result.exit_code, 0)

    def test_remove_asset_collection_with_object_key_invalid(self):
        """Test invalid object key returns an error"""
        result = self.runner.invoke(cli, [
            "remove-asset-collection", 
            "--object-key", "invalid-object-key",
            "--collection-name", "test-collection"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

class TestAssetAddAssetTag(TestAssetBase):
    """Tests for adding asset tags"""

    def test_add_asset_tag_with_id(self):
        """Test asset tag is added successfully"""
        result = self.runner.invoke(cli, [
            "add-asset-tag", 
            "--id", self.asset_id,
            "--tag-name", "test-tag"
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        tags = asset_details["tags"]
        self.assertTrue(any(tag["description"] == "test-tag" for tag in tags))
        
    def test_add_asset_tag_with_id_invalid(self):
        """Test invalid ID returns an error"""
        result = self.runner.invoke(cli, [
            "add-asset-tag", 
            "--id", "invalid-id",
            "--tag-name", "test-tag"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_add_asset_tag_with_url(self):
        """Test asset tag is added successfully"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        url = asset_details["properties"]["url"]
        
        result = self.runner.invoke(cli, [
            "add-asset-tag", 
            "--url", url,
            "--tag-name", "test-tag1"
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--url", url
        ])
        
        asset_details = json.loads(asset_details_result.output)
        tags = asset_details["tags"]
        self.assertTrue(any(tag["description"] == "test-tag1" for tag in tags))
        
    def test_add_asset_tag_with_url_invalid(self):
        """Test invalid URL returns an error"""
        result = self.runner.invoke(cli, [
            "add-asset-tag", 
            "--url", "invalid-url",
            "--tag-name", "test-tag"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

    def test_add_asset_tag_with_object_key(self):
        """Test asset tag is added successfully"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "add-asset-tag", 
            "--object-key", object_key,
            "--tag-name", "test-tag2"
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--object-key", object_key
        ])
        
        asset_details = json.loads(asset_details_result.output)
        tags = asset_details["tags"]
        self.assertTrue(any(tag["description"] == "test-tag2" for tag in tags))
        
    def test_add_asset_tag_with_object_key_no_bucket(self):
        """Test missing bucket returns an error"""
        self.setup_config()

        bucket = self.config.get("bucket")
        if bucket:
            self.skipTest("Default bucket set")

        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])

        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]

        result = self.runner.invoke(cli, [
            "add-asset-tag", 
            "--object-key", object_key,
            "--tag-name", "test-tag"
        ])

        self.assertNotEqual(result.exit_code, 0)

    def test_add_asset_tag_with_object_key_invalid(self):
        """Test invalid object key returns an error"""
        result = self.runner.invoke(cli, [
            "add-asset-tag", 
            "--object-key", "invalid-object-key",
            "--tag-name", "test-tag"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

    def test_add_asset_tag_with_tag_id(self):
        """Test asset tag is added successfully"""
        tags = self.runner.invoke(cli, [
            "get-content-definition-contents",
            "--name", "Tag"
        ])

        tags = json.loads(tags.output)["items"]
        if len(tags) == 0:
            self.skipTest("No tags available")

        tag_id = tags[0]["id"]
        tag_name = tags[0]["title"]

        result = self.runner.invoke(cli, [
            "add-asset-tag", 
            "--id", self.asset_id,
            "--tag-id", tag_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        tags = asset_details["tags"]
        self.assertTrue(any(tag["description"] == tag_name for tag in tags))

    def test_add_asset_tag_with_tag_id_invalid(self):
        """Test invalid tag ID returns an error"""
        result = self.runner.invoke(cli, [
            "add-asset-tag", 
            "--id", self.asset_id,
            "--tag-id", "invalid-id"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

class TestAssetListAssetTag(TestAssetBase):
    """Tests for listing asset tags"""

    def test_list_asset_tag_with_id(self):
        """Test asset tags are returned"""
        result = self.runner.invoke(cli, [
            "list-asset-tags", 
            "--id", self.asset_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json, list))
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")

    def test_list_asset_tag_with_id_invalid(self):
        """Test invalid ID returns an error"""
        result = self.runner.invoke(cli, [
            "list-asset-tags", 
            "--id", "invalid-id"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

    def test_list_asset_tag_with_url(self):
        """Test asset tags are returned"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        url = asset_details["properties"]["url"]
        
        result = self.runner.invoke(cli, [
            "list-asset-tags", 
            "--url", url
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json, list))
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")

    def test_list_asset_tag_with_url_invalid(self):
        """Test invalid URL returns an error"""
        result = self.runner.invoke(cli, [
            "list-asset-tags", 
            "--url", "invalid-url"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

    def test_list_asset_tag_with_object_key(self):
        """Test asset tags are returned"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "list-asset-tags", 
            "--object-key", object_key
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json, list))
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")

    def test_list_asset_tag_with_object_key_no_bucket(self):
        """Test missing bucket returns an error"""
        self.setup_config()

        bucket = self.config.get("bucket")
        if bucket:
            self.skipTest("Default bucket set")

        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])

        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]

        result = self.runner.invoke(cli, [
            "list-asset-tags", 
            "--object-key", object_key
        ])

        self.assertNotEqual(result.exit_code, 0)

    def test_list_asset_tag_with_object_key_invalid(self):
        """Test invalid object key returns an error"""
        result = self.runner.invoke(cli, [
            "list-asset-tags", 
            "--object-key", "invalid-object-key"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

class TestAssetRemoveAssetTag(TestAssetBase):
    """Tests for removing asset tags"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        tags = cls.runner.invoke(cli, [
            "get-content-definition-contents",
            "--name", "Tag"
        ])

        tags = json.loads(tags.output)["items"]
        if len(tags) == 0:
            cls.skipTest("No tags available")

        cls.tag_id = tags[0]["id"]
        cls.tag_name = tags[0]["title"]
        
        tag_result = cls.runner.invoke(cli, [
            "add-asset-tag", 
            "--id", cls.asset_id,
            "--tag-id", cls.tag_id
        ])
        
        if tag_result.exit_code != 0:
            cls.skipTest("Failed to add tag")

    def test_remove_asset_tag_id(self):
        """Test asset tag is removed successfully"""
        result = self.runner.invoke(cli, [
            "add-asset-tag", 
            "--id", self.asset_id,
            "--tag-id", self.tag_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        result = self.runner.invoke(cli, [
            "remove-asset-tag", 
            "--id", self.asset_id,
            "--tag-id", self.tag_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        tags = asset_details["tags"]
        self.assertFalse(self.tag_name in tags)
        
    def test_remove_asset_tag_id_invalid(self):
        """Test invalid tag ID returns an error"""
        result = self.runner.invoke(cli, [
            "remove-asset-tag", 
            "--id", self.asset_id,
            "--tag-id", "invalid-id"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_remove_asset_tag_with_url(self):
        """Test asset tag is removed successfully"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        url = asset_details["properties"]["url"]
        
        result = self.runner.invoke(cli, [
            "add-asset-tag", 
            "--url", url,
            "--tag-id", self.tag_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        result = self.runner.invoke(cli, [
            "remove-asset-tag", 
            "--url", url,
            "--tag-id", self.tag_id
        ])
        
        self.assertEqual(result.exit_code, 0)

        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--url", url
        ])

        asset_details = json.loads(asset_details_result.output)
        tags = asset_details["tags"]
        self.assertFalse(self.tag_name in tags)

    def test_remove_asset_tag_with_url_invalid(self):
        """Test invalid URL returns an error"""
        result = self.runner.invoke(cli, [
            "remove-asset-tag", 
            "--url", "invalid-url",
            "--tag-id", self.tag_id
        ])
        
        self.assertNotEqual(result.exit_code, 0)

    def test_remove_asset_tag_with_object_key(self):
        """Test asset tag is removed successfully"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "add-asset-tag", 
            "--object-key", object_key,
            "--tag-id", self.tag_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        result = self.runner.invoke(cli, [
            "remove-asset-tag", 
            "--object-key", object_key,
            "--tag-id", self.tag_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--object-key", object_key
        ])
        
        asset_details = json.loads(asset_details_result.output)
        tags = asset_details["tags"]
        self.assertFalse(self.tag_name in tags)

    def test_remove_asset_tag_with_object_key_no_bucket(self):
        """Test missing bucket returns an error"""
        self.setup_config()

        bucket = self.config.get("bucket")
        if bucket:
            self.skipTest("Default bucket set")

        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])

        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]

        result = self.runner.invoke(cli, [
            "add-asset-tag", 
            "--object-key", object_key,
            "--tag-id", self.tag_id
        ])

        self.assertNotEqual(result.exit_code, 0)

    def test_remove_asset_tag_with_object_key_invalid(self):
        """Test invalid object key returns an error"""
        result = self.runner.invoke(cli, [
            "remove-asset-tag", 
            "--object-key", "invalid-object-key",
            "--tag-id", self.tag_id
        ])
        
        self.assertNotEqual(result.exit_code, 0)

class TestAssetAddRelatedContent(TestAssetBase):
    """Tests for adding related content"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        series_result = cls.runner.invoke(cli, [
            "get-content-definition-contents",
            "--name", "Series"
        ])

        countries = json.loads(series_result.output)["items"]
        if len(countries) == 0:
            cls.skipTest("Content definition not available")

        cls.series_id = countries[0]["id"]
        cls.series_name = countries[0]["title"]

    def test_add_related_content_with_id(self):
        """Test related content is added successfully"""
        result = self.runner.invoke(cli, [
            "add-asset-related-content", 
            "--id", self.asset_id,
            "--related-content-id", self.series_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        related_contents = asset_details["relatedContent"]
        self.assertTrue(any(content["id"] == self.series_id for content in related_contents))
        
    def test_add_related_content_with_id_invalid(self):
        """Test invalid ID returns an error"""
        result = self.runner.invoke(cli, [
            "add-asset-related-content", 
            "--id", "invalid-id",
            "--related-content-id", self.series_id
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_add_related_content_with_url(self):
        """Test related content is added successfully"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        url = asset_details["properties"]["url"]
        
        result = self.runner.invoke(cli, [
            "add-asset-related-content", 
            "--url", url,
            "--related-content-id", self.series_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--url", url
        ])
        
        asset_details = json.loads(asset_details_result.output)
        related_contents = asset_details["relatedContent"]

        self.assertTrue(any(content["id"] == self.series_id for content in related_contents))

    def test_add_related_content_with_url_invalid(self):
        """Test invalid URL returns an error"""
        result = self.runner.invoke(cli, [
            "add-asset-related-content", 
            "--url", "invalid-url",
            "--related-content-id", self.series_id
        ])
        
        self.assertNotEqual(result.exit_code, 0)

    def test_add_related_content_with_object_key(self):
        """Test related content is added successfully"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "add-asset-related-content", 
            "--object-key", object_key,
            "--related-content-id", self.series_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--object-key", object_key
        ])
        
        asset_details = json.loads(asset_details_result.output)
        related_contents = asset_details["relatedContent"]
        self.assertTrue(any(content["id"] == self.series_id for content in related_contents))

    def test_add_related_content_with_object_key_no_bucket(self):
        """Test missing bucket returns an error"""
        self.setup_config()

        bucket = self.config.get("bucket")
        if bucket:
            self.skipTest("Default bucket set")

        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])

        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]

        result = self.runner.invoke(cli, [
            "add-asset-related-content", 
            "--object-key", object_key,
            "--related-content-id", self.series_id
        ])

        self.assertNotEqual(result.exit_code, 0)

    def test_add_related_content_with_object_key_invalid(self):
        """Test invalid object key returns an error"""
        result = self.runner.invoke(cli, [
            "add-asset-related-content", 
            "--object-key", "invalid-object-key",
            "--related-content-id", self.series_id
        ])
        
        self.assertNotEqual(result.exit_code, 0)

    def test_add_related_content_with_content_id_invalid(self):
        """Test invalid content ID returns an error"""
        result = self.runner.invoke(cli, [
            "add-asset-related-content", 
            "--id", self.asset_id,
            "--related-content-id", "invalid-id"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

class TestAssetListRelatedContent(TestAssetBase):
    """Tests for listing related content"""

    def test_list_related_content_with_id(self):
        """Test related content is returned"""
        result = self.runner.invoke(cli, [
            "list-asset-related-contents", 
            "--id", self.asset_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json, list))
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")

    def test_list_related_content_with_id_invalid(self):
        """Test invalid ID returns an error"""
        result = self.runner.invoke(cli, [
            "list-asset-related-contents", 
            "--id", "invalid-id"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

    def test_list_related_content_with_url(self):
        """Test related content is returned"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        url = asset_details["properties"]["url"]
        
        result = self.runner.invoke(cli, [
            "list-asset-related-contents", 
            "--url", url
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json, list))
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")

    def test_list_related_content_with_url_invalid(self):
        """Test invalid URL returns an error"""
        result = self.runner.invoke(cli, [
            "list-asset-related-contents", 
            "--url", "invalid-url"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

    def test_list_related_content_with_object_key(self):
        """Test related content is returned"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "list-asset-related-contents", 
            "--object-key", object_key
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        try:
            output_json = json.loads(result.output)
            self.assertTrue(isinstance(output_json, list))
        except json.JSONDecodeError:
            self.fail("Output is not valid JSON")
            
    def test_list_related_content_with_object_key_no_bucket(self):
        """Test missing bucket returns an error"""
        self.setup_config()

        bucket = self.config.get("bucket")
        if bucket:
            self.skipTest("Default bucket set")
            
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "list-asset-related-contents", 
            "--object-key", object_key
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_list_related_content_with_object_key_invalid(self):
        """Test invalid object key returns an error"""
        result = self.runner.invoke(cli, [
            "list-asset-related-contents", 
            "--object-key", "invalid-object-key"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
class TestAssetRemoveRelatedContent(TestAssetBase):
    """Tests for removing related content"""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        series_result = cls.runner.invoke(cli, [
            "get-content-definition-contents",
            "--name", "Series"
        ])

        countries = json.loads(series_result.output)["items"]
        if len(countries) == 0:
            cls.skipTest("Content definition not available")

        cls.series_id = countries[0]["id"]
        cls.series_name = countries[0]["title"]
        
        related_content_result = cls.runner.invoke(cli, [
            "add-asset-related-content", 
            "--id", cls.asset_id,
            "--related-content-id", cls.series_id
        ])
        
        if related_content_result.exit_code != 0:
            cls.skipTest("Failed to add related content")

    def test_remove_related_content_id(self):
        """Test related content is removed successfully"""
        result = self.runner.invoke(cli, [
            "remove-asset-related-content", 
            "--id", self.asset_id,
            "--related-content-id", self.series_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        related_contents = asset_details["relatedContent"]
        self.assertFalse(self.series_name in related_contents)
        
    def test_remove_related_content_id_invalid(self):
        """Test invalid ID returns an error"""
        result = self.runner.invoke(cli, [
            "remove-asset-related-content", 
            "--id", self.asset_id,
            "--related-content-id", "invalid-id"
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_remove_related_content_with_url(self):
        """Test related content is removed successfully"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        url = asset_details["properties"]["url"]
        
        result = self.runner.invoke(cli, [
            "remove-asset-related-content", 
            "--url", url,
            "--related-content-id", self.series_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--url", url
        ])
        
        asset_details = json.loads(asset_details_result.output)
        related_contents = asset_details["relatedContent"]
        
        self.assertFalse(self.series_name in related_contents)
        
    def test_remove_related_content_with_url_invalid(self):
        """Test invalid URL returns an error"""
        result = self.runner.invoke(cli, [
            "remove-asset-related-content", 
            "--url", "invalid-url",
            "--related-content-id", self.series_id
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_remove_related_content_with_object_key(self):
        """Test related content is removed successfully"""
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "remove-asset-related-content", 
            "--object-key", object_key,
            "--related-content-id", self.series_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--object-key", object_key
        ])
        
        asset_details = json.loads(asset_details_result.output)
        related_contents = asset_details["relatedContent"]
        
        self.assertFalse(self.series_name in related_contents)
        
    def test_remove_related_content_with_object_key_no_bucket(self):
        """Test missing bucket returns an error"""
        self.setup_config()

        bucket = self.config.get("bucket")
        if bucket:
            self.skipTest("Default bucket set")
            
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", self.asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "remove-asset-related-content", 
            "--object-key", object_key,
            "--related-content-id", self.series_id
        ])
        
        self.assertNotEqual(result.exit_code, 0)
        
    def test_remove_related_content_with_object_key_invalid(self):
        """Test invalid object key returns an error"""
        result = self.runner.invoke(cli, [
            "remove-asset-related-content", 
            "--object-key", "invalid-object-key",
            "--related-content-id", self.series_id
        ])
        
        self.assertNotEqual(result.exit_code, 0)

class TestDeleteAsset(TestAssetBase):
    """Tests for deleting assets"""
    def test_delete_asset_with_id(self):
        """Test asset is deleted successfully"""
        result = self.runner.invoke(cli, [
            "upload-assets",
            "--source", "setup.py",
            "--id", self.test_dir_id
        ])

        asset_id = result.output.replace('"', "").strip()      

        result = self.runner.invoke(cli, [
            "delete-asset", 
            "--id", asset_id
        ])
        
        self.assertEqual(result.exit_code, 0)
        time.sleep(3)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", asset_id
        ])
        
        self.assertNotEqual(asset_details_result.exit_code, 0)
        
        self.runner.invoke(cli, [
            "delete-asset", 
            "--id", asset_id
        ])

    def test_delete_asset_with_id_invalid(self):
        """Test invalid ID returns an error"""    
        result = self.runner.invoke(cli, [
            "delete-asset", 
            "--id", "invalid-id"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

    def test_delete_asset_with_url(self):
        """Test asset is deleted successfully"""
        result = self.runner.invoke(cli, [
            "upload-assets",
            "--source", "requirements.txt",
            "--id", self.test_dir_id
        ])

        asset_id = result.output.replace('"', "").strip()   

        time.sleep(3)     

        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", asset_id
        ])
        
        asset_details = json.loads(asset_details_result.output)

        url = asset_details["properties"]["url"]
        
        result = self.runner.invoke(cli, [
            "delete-asset", 
            "--url", url
        ])
        
        self.assertEqual(result.exit_code, 0)
        time.sleep(3)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--url", url
        ])
        
        self.assertNotEqual(asset_details_result.exit_code, 0)

    def test_delete_asset_with_url_invalid(self):
        """Test invalid URL returns an error"""            
        result = self.runner.invoke(cli, [
            "delete-asset", 
            "--url", "invalid-url"
        ])
        
        self.assertNotEqual(result.exit_code, 0)


    def test_delete_asset_with_object_key(self):
        """Test asset is deleted successfully"""
        result = self.runner.invoke(cli, [
            "upload-assets",
            "--source", "publish.bat",
            "--id", self.test_dir_id
        ])

        asset_id = result.output.replace('"', "").strip()        

        time.sleep(3)

        asset_details_result = self.runner.invoke(cli, [
                "get-asset-details", 
                "--id", asset_id
            ])
    
        asset_details = json.loads(asset_details_result.output)      

        object_key = asset_details["properties"]["displayPath"]
        
        result = self.runner.invoke(cli, [
            "delete-asset", 
            "--object-key", object_key
        ])
        
        self.assertEqual(result.exit_code, 0)
        time.sleep(3)
        
        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--object-key", object_key
        ])
        
        self.assertNotEqual(asset_details_result.exit_code, 0)

    def test_delete_asset_with_object_key_no_bucket(self):
        self.setup_config()
        
        bucket = self.config.get("bucket")
        if bucket:
            self.skipTest("Default bucket set")
        
        result = self.runner.invoke(cli, [
            "upload-assets",
            "--source", "setup.py",
            "--id", self.test_dir_id
        ])

        asset_id = result.output.replace('"', "").strip()
        
        time.sleep(3)

        asset_details_result = self.runner.invoke(cli, [
            "get-asset-details", 
            "--id", asset_id
        ])

        asset_details = json.loads(asset_details_result.output)
        object_key = asset_details["properties"]["displayPath"]
        
        time.sleep(3)

        result = self.runner.invoke(cli, [
            "delete-asset", 
            "--object-key", object_key
        ])

        self.assertNotEqual(result.exit_code, 0)

    def test_delete_asset_with_object_key_invalid(self):
        """Test invalid object key returns an error"""
        result = self.runner.invoke(cli, [
            "delete-asset", 
            "--object-key", "invalid-object-key"
        ])
        
        self.assertNotEqual(result.exit_code, 0)

if __name__ == "__main__":
    unittest.main()
        
