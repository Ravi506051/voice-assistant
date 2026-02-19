import cv2
import mediapipe as mp
import pyautogui

# Camera setup
cap = cv2.VideoCapture(0)

# MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)

mp_draw = mp.solutions.drawing_utils

# Screen size
screen_width, screen_height = pyautogui.size()

# Disable fail-safe
pyautogui.FAILSAFE = False

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

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

            # Index finger tip
            index_finger = landmarks[8]
            index_x = int(index_finger.x * frame_width)
            index_y = int(index_finger.y * frame_height)

            # Thumb tip
            thumb = landmarks[4]
            thumb_x = int(thumb.x * frame_width)
            thumb_y = int(thumb.y * frame_height)

            # Draw circles
            cv2.circle(frame, (index_x, index_y), 10,
                       (0, 255, 255), -1)
            cv2.circle(frame, (thumb_x, thumb_y), 10,
                       (0, 255, 255), -1)

            # Convert to screen coordinates
            screen_x = screen_width / frame_width * index_x
            screen_y = screen_height / frame_height * index_y

            # Move mouse with index finger
            pyautogui.moveTo(screen_x, screen_y)

            # Click when thumb & index close
            distance = abs(index_y - thumb_y)

            if distance < 30:
                pyautogui.click()
                pyautogui.sleep(0.3)

    cv2.imshow("Virtual Mouse", frame)

    # Exit when 'q' pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
