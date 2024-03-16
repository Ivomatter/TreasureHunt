from ultralytics import YOLO
import imagesize

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

__all__ = ["ImageClassifier"]
