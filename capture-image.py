import cv2

def capture_and_save_image(output_file):
    # Open a connection to the camera (0 is the default camera)
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture a single frame
    ret, frame = cap.read()

    # Release the camera capture object
    cap.release()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not capture frame.")
        return

    # Save the captured frame to a file
    cv2.imwrite(output_file, frame)

    print(f"Image captured and saved to {output_file}.")

# Specify the output file path
output_file_path = "captured_image.jpg"

# Capture and save the image
capture_and_save_image(output_file_path)
