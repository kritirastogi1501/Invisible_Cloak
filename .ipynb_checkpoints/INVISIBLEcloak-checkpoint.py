import cv2
import numpy as np
import time

# Initialize the webcam
capture_video = cv2.VideoCapture(0)
time.sleep(2)  # Give the camera time to warm up

# Capture background frame
print("Capturing background... Please stay still.")
background = None
for i in range(60):
    ret, background = capture_video.read()
    if not ret:
        continue
    background = np.flip(background, axis=1)  # Flip to mirror image

print("Background captured!")

# Start real-time video capture
print("Starting invisibility effect. Press ESC to exit.")
while capture_video.isOpened():
    ret, img = capture_video.read()
    if not ret:
        break

    img = np.flip(img, axis=1)  # Flip for a mirror-like view

    # Convert to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Red color range mask
    lower_red1 = np.array([100, 40, 40])
    upper_red1 = np.array([100, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

    lower_red2 = np.array([155, 40, 40])
    upper_red2 = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # Combine masks
    mask = mask1 + mask2

    # Clean up the mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)
    mask_inv = cv2.bitwise_not(mask)

    # Segment out the red color part by replacing with background
    res1 = cv2.bitwise_and(background, background, mask=mask)
    res2 = cv2.bitwise_and(img, img, mask=mask_inv)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisibility Cloak", final_output)

    if cv2.waitKey(1) == 27:  # ESC key to exit
        break

# Release and destroy windows
capture_video.release()
cv2.destroyAllWindows()
