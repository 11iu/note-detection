from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('note-model.pt')

# Run inference on an image
results = model('notes/note3.jpg')  # results list

# View results
for r in results:
    print(r.boxes)  # print the Boxes object containing the detection bounding boxes