# Install required libraries
pip install mediapipe opencv - python - headless
from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode

# Import libraries
import cv2
import mediapipe as mp

# Initialize Mediapipe Hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

# Open webcam
cap = cv2.VideoCapture(0)  # Use 0 for default webcam

while cap.isOpened():
    ret, frame = cap.read()  # Capture a frame
    if not ret:
        break

    # Flip the frame for a natural selfie view
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB (Mediapipe works with RGB images)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    results = hands.process(rgb_frame)

    # Draw hand landmarks if detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the frame
    cv2.imshow('Webcam Hand Detection', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
