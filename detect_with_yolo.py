from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('note-model.pt')

# Run inference on an image
results = model('notes/note3.jpg')

# Show the bounding boxes overlayed and save
#results = model.predict('notes/note3.jpg', show=True, conf=0.5, save=True)

# print the Boxes object containing the detection bounding boxes
for r in results:
    print(r.boxes)  