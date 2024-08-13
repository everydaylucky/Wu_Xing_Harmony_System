import cv2
import time

# Open the default camera (usually the first one)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Set the start time
start_time = time.time()

# Variables to store the last frame
last_frame = None

# Capture video for 5 seconds and display the video feed
while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture video frame.")
        break

    # Display the current frame
    cv2.imshow("Camera Feed", frame)

    # Store the frame
    last_frame = frame

    # Check if 5 seconds have passed
    if time.time() - start_time >= 3:
        break

    # Break the loop if the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
cap.release()

# Check if the last frame was captured
if last_frame is not None:
    # Save the last frame to a file
    cv2.imwrite("last_frame.jpg", last_frame)
    print("Last frame saved to 'last_frame.jpg'.")
else:
    print("Error: No frame captured.")

# Close the OpenCV window
cv2.destroyAllWindows()
