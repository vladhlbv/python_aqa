from lesson_19_1.nasa_api_client import PhotosApiClient
from requests import Response
from pathlib import Path

# Sending request to API to get photo URLs
photos_api_client = PhotosApiClient()

response: Response = photos_api_client.get_photo_data(sol=1000, camera="fhaz")
response_dict: dict = response.json()

# Preparing URL data from previous request response
image_urls: list = [value["img_src"] for value in response_dict["photos"]]
# Preparing filename data
filenames: list = [f"photo{i}.jpg" for i in range(1, len(image_urls) + 1)]

# Making sure that image_url and filenames count is equal before using it in next request
if len(image_urls) != len(filenames):
    raise ValueError("The number of URLs and filenames should be the same.")

# Creating directory for image files
folder = Path("files")
folder.mkdir(exist_ok=True)

# Sending request to download image files to target folder by provided URLs
photos_api_client.download_photo_by_url(image_urls=image_urls, filenames=filenames, folder=folder)