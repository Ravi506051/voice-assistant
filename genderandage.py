import cv2
import numpy as np

# -----------------------------
# Labels
# -----------------------------
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)',
           '(25-32)', '(38-43)', '(48-53)', '(60-100)']

genderList = ['Male', 'Female']

# -----------------------------
# Load Models Directly
# -----------------------------
faceNet = cv2.dnn.readNet(
    "opencv_face_detector_uint8.pb",
    "opencv_face_detector.pbtxt"
)

ageNet = cv2.dnn.readNet(
    "age_net.caffemodel",
    "age_deploy.prototxt"
)

genderNet = cv2.dnn.readNet(
    "gender_net.caffemodel",
    "gender_deploy.prototxt"
)

print("All Models Loaded Successfully ✅")

# -----------------------------
# Face Detection Function
# -----------------------------
def detectFace(net, frame, conf_threshold=0.7):
    frameCopy = frame.copy()
    h, w = frame.shape[:2]

    blob = cv2.dnn.blobFromImage(
        frameCopy, 1.0, (300, 300),
        [104, 117, 123], swapRB=False, crop=False
    )

    net.setInput(blob)
    detections = net.forward()
    faceBoxes = []

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * w)
            y1 = int(detections[0, 0, i, 4] * h)
            x2 = i
