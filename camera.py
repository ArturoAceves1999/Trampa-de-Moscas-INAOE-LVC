import cv2

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

start_time = cv2.getTickCount()  # Get the start time

while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame.")
        break

    # Display the frame
    cv2.imshow('Video Capture', frame)

    # Check if a key is pressed and break if it's within 2 seconds
    if cv2.waitKey(1) & 0xFF != 255:  # 255 is the "no key pressed" value
        break

    # Check elapsed time in seconds
    elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
    if elapsed_time >= 2:  # 2 seconds
        print("2 seconds elapsed, breaking the loop")
        break

# Release the webcam and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()

