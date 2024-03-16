import argparse
import requests
import os
from PIL import Image

SYSTEM_PROMPT = """
A chat between a human and an artificaial intelligence backend, so it should communicate in a json format.
The assistant is a backend to a riddle game, it is given an image and should respond with riddle.
"""

USER_PROMPT = """
Here is the image.
You should pick an interesting object in the image and describe it using a riddle.
You should try to keep it simple, the answer should be a single word. 
An example for you is {"tree": "big, brown and standing on the grass"}.
THE ANSWER SHOULD NOT APPEAR IN THE RIDDLE.
"""

def post_image(image_path):
    url = "http://localhost:8080/llava"  

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
