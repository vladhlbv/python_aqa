import requests
from dotenv import load_dotenv
from pathlib import Path

from requests import Response

load_dotenv()


class ImagesApiClient:

    BASE_URL: str = "http://127.0.0.1:8080"

    def get_image(self, content_type: str, filename: str):
        image_path: str = f'/image/{filename}'
        headers: dict = {"content-type": f'{content_type}'}
        response: Response =  requests.get(url=self.BASE_URL+image_path, headers=headers)

        if content_type == "image" and response.status_code == 200:
            return response.content
        return response

    def post_image(self, file_path: str):
        full_file_path: Path = Path.cwd() / file_path
        with open(full_file_path, "rb") as f:
            files = {"image": (full_file_path.name, f)}
            return requests.post(url=f"{self.BASE_URL}/upload", files=files)

    def delete_image(self, filename: str):
        image_path: str = f'/delete/{filename}'
        return requests.delete(url=self.BASE_URL+image_path)

# if __name__ == '__main__':