import cv2
print(cv2.__version__)

import mediapipe as mp
import numpy as np
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize Camera
cap = cv2.VideoCapture(0)

# MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)

mp_draw = mp.solutions.drawing_utils

# Volume Control Setup (Windows)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

volume = cast(interface, POINTER(IAudioEndpointVolume))

vol_min, vol_max = volume.GetVolumeRange()[:2]

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            landmarks = hand_landmarks.landmark

            # Thumb tip
            x1 = int(landmarks[4].x * w)
            y1 = int(landmarks[4].y * h)

            # Index finger tip
            x2 = int(landmarks[8].x * w)
            y2 = int(landmarks[8].y * h)

            # Draw circles
            cv2.circle(frame, (x1, y1), 10, (255, 0, 0), -1)
            cv2.circle(frame, (x2, y2), 10, (255, 0, 0), -1)
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

            # Distance between fingers
            length = math.hypot(x2 - x1, y2 - y1)

            # Map distance to volume range
            vol = np.interp(length, [20, 200], [vol_min, vol_max])
            volume.SetMasterVolumeLevel(vol, None)

            # Volume Bar
            vol_bar = np.interp(length, [20, 200], [400, 150])
            vol_percent = np.interp(length, [20, 200], [0, 100])

            cv2.rectangle(frame, (50, 150), (85, 400), (0, 255, 0), 3)
            cv2.rectangle(frame, (50, int(vol_bar)), (85, 400),
                          (0, 255, 0), -1)

            cv2.putText(frame, f'{int(vol_percent)} %',
                        (40, 450), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 3)

    cv2.imshow("Volume Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
