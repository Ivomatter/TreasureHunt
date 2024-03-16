import argparse
import requests
import os
from PIL import Image

SYSTEM_PROMPT = "A chat between a pedantic human and an artificaial intelligence assistant. The assistant gives helpful answer to the human in a json format." 
USER_PROMPT = "Find all main objects in the image. Serialize them in a json format. Print name and location for each of them. The format should be: [{name: location}*]. Each name should be a single word, use location as a description of the object in the scene."

def post_image(image_path):
    url = "http://localhost:8080/llava"  # replace with your url

    # Open the image file in binary mode
    with open(image_path, "rb") as image_file:
        payload = {
            "system_prompt": (None, SYSTEM_PROMPT),
            "user_prompt": (None, USER_PROMPT),
            "image_file": (os.path.basename(image_path), image_file, "image/jpeg"),
        }

        # Send POST request with the payload
        response = requests.post(url, files=payload)

        # Processing the response
        response_data = response.json()
        if 'error' in response_data and response_data['error']: 
            print(f"error: {response_data['description']}")
        else:
            print(response_data['content'])

def main():
    parser = argparse.ArgumentParser(description='Post an image with user prompts.')
    parser.add_argument('image_path', type=str, help='The path of the image file to upload')

    args = parser.parse_args()

    post_image(args.image_path)

if __name__=='__main__':
    main()
