import os
import pandas as pd
from ultralytics import YOLO
from pathlib import Path

# Root image folder (contains channel subfolders)
ROOT_IMAGE_FOLDER = Path('data/raw/telegram_images/2025-07-16')
OUTPUT_CSV = 'data/processed/image_detections.csv'

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")

# Store detections
detections = []

# Recursively search for image files in all subfolders
for image_path in ROOT_IMAGE_FOLDER.rglob("*.[jp][pn]g"):  # matches .jpg, .jpeg, .png
    image_path = str(image_path)
    filename = os.path.basename(image_path)
    results = model(image_path)

    for result in results:
        boxes = result.boxes
        for box in boxes:
            class_id = int(box.cls[0].item())
            class_name = model.names[class_id]
            confidence = round(box.conf[0].item(), 4)

            # Extract message_id from filename
            message_id = Path(filename).stem

            detections.append({
                "message_id": message_id,
                "image_name": filename,
                "detected_class": class_name,
                "confidence_score": confidence
            })

# Save to CSV
df = pd.DataFrame(detections)
df.to_csv(OUTPUT_CSV, index=False)
print(f"Detections saved to {OUTPUT_CSV}")
