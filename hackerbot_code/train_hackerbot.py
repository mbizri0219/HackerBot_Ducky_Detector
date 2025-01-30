from ultralytics import YOLO
import multiprocessing

def main():
    # Load a pretrained YOLOv8 model
    model = YOLO("yolov8n.pt")  # Using pretrained YOLOv8 nano model

    # Train the model on your rubber duck dataset
    results = model.train(
        data="rubber_duck.yaml",
        epochs=100,  # Increase epochs for better training
        imgsz=640,  # Image size
        batch=16,    # Batch size
        patience=50,  # Early stopping patience
        save=True    # Save best model
    )

    # Evaluate the model's performance
    results = model.val()

    # Test on a single image (fixed path format)
    results = model("C:\Users\Guest1\Documents\hackerbot\rubber_duck_dataset\images\train\image_7_jpg.rf.7b3e160b9cf247e19347f74cf0d96a71.jpg")
    # OR using double backslashes:
    # results = model("C:\\Users\\Guest1\\Documents\\hackerbot\\rubber_duck_dataset\\images\\train\\duck1.jpg")

    # Export the model
    success = model.export(format="onnx")

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()