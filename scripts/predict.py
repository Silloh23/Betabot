from ultralytics import YOLO

model = YOLO("runs/detect/models/runs/train-1-2/weights/best.pt")
model.predict(
    source="data/climbing/images/unlabelled/",
    save_txt=True,
    save_conf=True,
    conf=0.25,
    project="models/runs",
    name="predictions"
)