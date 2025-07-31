from lesson_19_2.console_logger_setup import console_logger
from lesson_19_2.images_api_client import ImagesApiClient
from requests import Response


images_api_client = ImagesApiClient()


# Uploading the image with POST request
response: Response = images_api_client.post_image(file_path="files/Screenshot_1.jpg")

post_response_code: int = response.status_code
post_response_dict: dict = response.json()
console_logger.info(f"POST request completed with Code: {post_response_code}")
console_logger.info(f"POST request completed with Response: {post_response_dict}")


#Receiving image data with "text" content type with GET request
content_type_txt: str = "text"
response: Response = images_api_client.get_image(content_type=content_type_txt, filename="Screenshot_1.jpg")

get_response_dict: dict = response.json()
get_response_code: int = response.status_code
console_logger.info(f"GET request with content-type: {content_type_txt} completed with Code: {get_response_code}")
console_logger.info(f"GET request with content-type: {content_type_txt} completed with Response: {get_response_dict}")


#Receiving binary image data with "image" content type with GET request
content_type_img: str = "image"
filename: str = "Screenshot_1.jpg"
response: Response = images_api_client.get_image(content_type=content_type_img, filename=filename)

image_data: dict = {}
image_data[filename] = response
if image_data:
    console_logger.info(f"Image was successfully received for GET request with content-type: {content_type_img}")
else:
    console_logger.info(f"Image was not received for GET request with content-type: {content_type_img}")


#Removing image by provided image filename with DELETE request
response: Response = images_api_client.delete_image(filename="Screenshot_1.jpg")

delete_response_code: int = response.status_code
delete_response_dict: dict = response.json()
console_logger.info(f"DELETE request completed with Code: {delete_response_code}")
console_logger.info(f"DELETE request completed with Response: {delete_response_dict}")