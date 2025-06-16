import cv2
import numpy as np
import AudioUtilities, IAudioEndpointVolume
import CLSCTX_ALL
from ctypes import cast, POINTER

# Initialize PyCaw for volume control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Get the volume range
min_vol, max_vol, _ = volume.GetVolumeRange()


def calculate_distance(pt1, pt2):
    """Calculate the Euclidean distance between two points."""
    return int(((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2) ** 0.5)


# Initialize OpenCV video capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame to avoid mirror effect
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define HSV range for detecting hand (use skin tone range)
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Create mask for skin color
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # Find the largest contour
        max_contour = max(contours, key=cv2.contourArea)

        # Approximate the contour
        epsilon = 0.01 * cv2.arcLength(max_contour, True)
        approx = cv2.approxPolyDP(max_contour, epsilon, True)

        # Find convex hull and defects
        hull = cv2.convexHull(max_contour, returnPoints=False)
        if len(hull) > 3:  # Avoid errors if hull is too small
            defects = cv2.convexityDefects(max_contour, hull)

            # Store fingertip positions
            fingertips = []
            if defects is not None:
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(max_contour[s][0])
                    end = tuple(max_contour[e][0])
                    far = tuple(max_contour[f][0])

                    # Consider only large defects as fingertip gaps
                    if d > 10000:
                        fingertips.append(start)

                # Draw detected fingertips
                for fingertip in fingertips:
                    cv2.circle(frame, fingertip, 5, (255, 0, 0), -1)

                # Volume control logic
                if len(fingertips) >= 2:
                    # Use the first two fingertips to control volume
                    pt1, pt2 = fingertips[:2]
                    distance = calculate_distance(pt1, pt2)

                    # Map the distance to volume range
                    vol = np.interp(distance, [50, 300], [min_vol, max_vol])
                    volume.SetMasterVolumeLevel(vol, None)

                    # Display volume level on screen
                    cv2.putText(frame, f"Volume: {int((vol - min_vol) / (max_vol - min_vol) * 100)}%",
                                (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Volume Control", frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
