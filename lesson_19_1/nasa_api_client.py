import os
import requests
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class BaseApiClient:

    BASE_URL = os.getenv("base_api_url")

    def __init__(self):
        self.__api_key = os.getenv("api_key")
        self._session = requests.Session()
        # self.__authenticate()

    # def __authenticate(self):
    #     header: dict = {"api_key": self.__api_key}
    #     self._session.headers.update(header)

    def _get(self, endpoint: str, params: dict = None):
        params['api_key'] = self.__api_key
        return self._session.get(url=endpoint, params=params)

    def _post(self, endpoint: str, data:dict):
        return self._session.post(url=endpoint, json=data)


class PhotosApiClient(BaseApiClient):

    ENDPOINT: str = f"{BaseApiClient.BASE_URL}/rovers/curiosity/photos"

    def get_photo_data(self, sol: int, camera: str):
        params: dict = {'sol': f'{sol}', 'camera': f'{camera}'}
        return self._get(endpoint=self.ENDPOINT, params=params)

    def download_photo_by_url(self, image_urls: str | list, filenames: str | list, folder: Path):
        for url, filename in zip(image_urls, filenames):
            try:
                response = requests.get(url)
                response.raise_for_status()

                file_path = folder / filename
                file_path.write_bytes(response.content)

                print(f"Image downloaded: {filename}")
            except requests.RequestException as e:
                print(f"Failed to download image {url}: {e}")


# if __name__ == '__main__':