import cv2
import time
from ultralytics import YOLO

# Load the trained model
model = YOLO("best.pt")

# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FPS, 30)

prev_frame_time = 0
new_frame_time = 0

while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame")
        break

    # Run detection on the frame
    results = model(img)
    
    # Draw the detections on the frame
    annotated_frame = results[0].plot()

    # Calculate and display FPS
    new_frame_time = time.time()
    fps = 1/(new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    fps = int(fps)
    fps = "FPS: " + str(fps)
    cv2.putText(annotated_frame, fps, (7, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3, 2)

    # Show the frame
    cv2.imshow('Webcam', annotated_frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
