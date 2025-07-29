import os

import requests

from lesson_19_2.images_api_client import ImagesApiClient
from requests import Response


images_api_client = ImagesApiClient()

# Uploading the image with POST request
response: Response = images_api_client.post_image(file_path="files/Screenshot_1.jpg")

post_response_code: int = response.status_code
post_response_dict: dict = response.json()
print(post_response_code)
print(post_response_dict)

#Receiving image data with "text" content type with GET request
content_type_txt: str = "text"
response: Response = images_api_client.get_image(content_type=content_type_txt, filename="Screenshot_1.jpg")

response_dict: dict = response.json()
response_code: int = response.status_code
print(response_code)
print(response_dict)

#Receiving binary image data with "image" content type with GET request
content_type_img: str = "image"
filename: str = "Screenshot_1.jpg"
response: Response = images_api_client.get_image(content_type=content_type_img, filename=filename)

image_data: dict = {}
image_data[filename] = response
# print(image_data)

#Removing image by provided image filename with DELETE request
response: Response = images_api_client.delete_image(filename="Screenshot_1.jpg")

delete_response_code: int = response.status_code
delete_response_dict: dict = response.json()
print(delete_response_code)
print(delete_response_dict)