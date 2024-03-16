from ultralytics import YOLO

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--img', type=str, help='path to image')
    args = parser.parse_args()

    model = YOLO('yolov8n.pt')

    results = model(args.img, verbose=False) 

    classes = results[0].boxes.cls.cpu().tolist() 
    confs = results[0].boxes.conf.float().cpu().tolist()

    ret = [
        results[0].names[int(cls)]
        for conf, cls in zip(confs, classes)
        if conf >= 0.5
    ]

    ret = list(set(ret))

    print(ret)
