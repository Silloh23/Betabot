from ultralytics import YOLO

model = YOLO("models/weights/yolov8n.pt")
model.train(
    data="data/climbing/data.yaml",
    epochs=50,
    imgsz=640,
    project="models/runs",
    name="train-1"
)