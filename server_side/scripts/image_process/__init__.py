from ultralytics import YOLO
import imagesize
import subprocess
import os
from openai import OpenAI

class ImageClassifier():
    def __init__(self) -> None:
        self.model = YOLO('yolov8n.pt')

    def get_objects(self, img_path, req_perc=0.1):
        results = self.model(img_path, verbose=False) 

        classes = results[0].boxes.cls.cpu().tolist() 
        confs = results[0].boxes.conf.float().cpu().tolist()
        boxes = results[0].boxes.xywh.float()

        width, height = imagesize.get(img_path)

        def get_percentage(box):
            return (box[2] * box[3]) / (width * height)

        ret = [
            results[0].names[int(cls)]
            for conf, cls, box in zip(confs, classes, boxes)
            if conf >= 0.5 and get_percentage(box) >= req_perc
        ]

        return list(set(ret))

    def compare_guess(self, img_path, guess):
        objects = self.get_objects(img_path, 0.2)
        return guess in objects


SYSTEM_PROMPT = f"""
\nYou are a helpful, respectful and concise assistant.\
You are to be deployed in a big pipeline.\
Reply to each question in a concise matter, include only the answer.\
ONLY ANSWER WITH THE REPLY, DO NOT INCLUDE ANY BOILERPLATE.\n\
Here is an example answer you could give for a flower described as standing in the grass:\
\"Dressed in pink, \n I sway in the breeze, Amidst a sea of green, my beauty never cease. \n What am I?\".\
"""


def USER_PROMPT(obj):
    return f"""
Create a riddle for a {obj}. \
THE REPLY SHOULD ONLY CONTAIN THE RIDDLE!\
You are in a large pipeline, so you should only reply with the answer riddle in quotes.\
"""


def LOCAL_PROMPT(obj):
    return f"""
[INST]<<SYS>>{SYSTEM_PROMPT}<</SYS>>{USER_PROMPT(obj)}[/INST]
"""


def create_riddle(obj, mode):
    if mode == 'mock':
        return "Who am I?"

    elif mode == 'chatgpt':
        client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME"))

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT(obj)}
            ]
        )

        return completion.choices[0].message.content

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
        LOCAL_PROMPT(obj),
        '--no-display-prompt'
    ], stdout=subprocess.PIPE)
    out = process.communicate()[0]

    return out.decode('ascii').strip()


def create_riddle_all(images, mode):
    objects = list(set([
        obj
        for img in images
        for obj in ImageClassifier().get_objects(img)
    ]))

    ret = [
        { 
            "name": obj,
            "riddle": create_riddle(obj, mode) 
        }
        for obj in objects
    ]

    return ret

__all__ = ["ImageClassifier", "create_riddle_all"]
