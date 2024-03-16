import subprocess
import argparse
import os
import sys

def PROMPT(obj):
    return f"""
[INST] \
<<SYS>> \
\nYou are a helpful, respectful and concise assistant.\
You are to be deployed in a big pipeline.\
Reply to each question in a concise matter, include only the answer.\
ONLY ANSWER WITH THE REPLY, DO NOT INCLUDE ANY BOILERPLATE.\n\
Here is an example answer you could give for a flower described as standing in the grass:\
\"Dressed in pink, \n I sway in the breeze, Amidst a sea of green, my beauty never cease. \n What am I?\".\
<</SYS>>\n\
Create a riddle for a {obj}. \
THE REPLY SHOULD ONLY CONTAIN THE RIDDLE!\
You are in a large pipeline, so you should only reply with the answer riddle in quotes.\
[/INST]
"""

def classify_image(img):
    process = subprocess.Popen(['python3', 'image_classify/image_classify.py', '--img', img], stdout=subprocess.PIPE)
    out, err = process.communicate()
    out = out.decode('ascii').strip().split('\n')
    return out

def create_riddle(obj, mock=False):
    if mock:
        return "\"Who am' I?\""

    process = subprocess.Popen([
        'word2riddle/llama.cpp/main',
        '-ngl',
        '64', 
        '-m', 
        os.path.abspath('word2riddle/models/llama-2-70b-chat.Q2_K.gguf'),
        '--color',
        '-c',
        '4096',
        '--temp',
        '0.7',
        '--repeat_penalty',
        '1.1',
        '-n',
        '-1',
        '-p',
        PROMPT(obj),
        '--no-display-prompt'
    ], stdout=subprocess.PIPE)
    out, err = process.communicate()

    return out.decode('ascii').strip()

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--img', type=str, help='image source')
    parser.add_argument('--mock', type=bool, help='is it mock', default=False)
    args = parser.parse_args()

    img = args.img

    if img is None:
        print("No image source given")
        return

    img = os.path.abspath(img)
    
    objects = classify_image(img)

    ret = []
    for obj in objects:
        ret.append({ "name": obj, "riddle": create_riddle(obj, args.mock) })

    print(ret)

if __name__ == "__main__":
    main()
