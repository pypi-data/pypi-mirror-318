import requests
import json
from typing import Union


class CloudIgniteSDK:
    """
    A Python SDK for interacting with the CloudIgnite file storage service.
    """

    def __init__(self, base_url: str, token: str):
        """
        Initialize the CloudIgniteSDK with a base URL and authorization token.

        :param base_url: The base URL for the CloudIgnite API.
        :param token: The authorization token for accessing the API.
        """
        self.base_url = base_url.rstrip("/")
        self.token = token

    def _headers(self) -> dict:
        """
        Returns the common headers for all API requests.

        :return: A dictionary containing HTTP headers.
        """
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def upload_file(self, bucket: str, file_path: str) -> str:
        """
        Upload a file to a specific bucket.

        :param bucket: The bucket ID where the file should be uploaded.
        :param file_path: The local file path of the file to be uploaded.
        :return: Response string from the server.
        :raises Exception: If the upload request fails.
        """
        url = f"{self.base_url}/s3/object-storage/api/v1/upload"
        with open(file_path, "rb") as file_data:
            files = {
                "bucketID": (None, bucket),
                "file": (file_path.split("/")[-1], file_data),
            }
            response = requests.post(url, headers={"Authorization": f"Bearer {self.token}"}, files=files)

        if response.status_code != 200:
            raise Exception(f"Failed to upload file: {response.text}")
        return response.text

    def list_files(self, bucket: str) -> str:
        """
        List files in a specific bucket.

        :param bucket: The bucket ID whose files are to be listed.
        :return: JSON response string from the server.
        :raises Exception: If the list files request fails.
        """
        url = f"{self.base_url}/s3/object-storage/api/v1/files"
        payload = {"bucketId": bucket}
        response = requests.post(url, headers=self._headers(), data=json.dumps(payload))

        if response.status_code != 200:
            raise Exception(f"Failed to list files: {response.text}")
        return response.text

    def get_file(self, bucket: str, filename: str) -> str:
        """
        Get the download URL for a file in a specific bucket.

        :param bucket: The bucket ID where the file is located.
        :param filename: The name of the file to fetch.
        :return: JSON response string from the server.
        :raises Exception: If the get file request fails.
        """
        url = f"{self.base_url}/s3/object-storage/{bucket}/{filename}"
        response = requests.get(url, headers=self._headers())

        if response.status_code != 200:
            raise Exception(f"Failed to fetch file: {response.text}")
        return response.text

    def delete_file(self, bucket: str, filename: str) -> str:
        """
        Delete a file from a specific bucket.

        :param bucket: The bucket ID where the file is located.
        :param filename: The name of the file to delete.
        :return: JSON response string from the server.
        :raises Exception: If the delete file request fails.
        """
        url = f"{self.base_url}/s3/object-storage/api/v1/delete"
        payload = {"file_id": filename, "bucketId": bucket}
        response = requests.post(url, headers=self._headers(), data=json.dumps(payload))

        if response.status_code != 200:
            raise Exception(f"Failed to delete file: {response.text}")
        return response.text
