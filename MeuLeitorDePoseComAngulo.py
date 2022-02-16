import cv2
import mediapipe as mp
import numpy as np
import math

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

a = 0

def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:]
    m1 = (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])
    m2 = (pt3[1] - pt1[1]) / (pt3[0] - pt1[0])
    angR = math.atan((m2 - m1) / (1 + (m2 * m1)))
    angD = round(math.degrees(angR))
    cv2.putText(image, str(angD), (10, 60), cv2.FONT_HERSHEY_COMPLEX,
                2, (0, 0, 255), 2, cv2.LINE_AA)
    print(angD)

while a == 0:
    cap = cv2.VideoCapture("videos/videoangulo.mp4")
    with mp_pose.Pose(
            min_detection_confidence=0.1,
            min_tracking_confidence=0.1) as pose:
        while cap.isOpened():
            success, image = cap.read()
            if cv2.waitKey(1) & 0xFF == 27:
                cap.isOpened(0)
                a=1
                break
            if not success:
                break

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = pose.process(image)
            landmarks = results.pose_landmarks.landmark
            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            angle = [shoulder, elbow, wrist]

            getAngle(angle)
    # Draw the pose annotation on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
            cv2.imshow('Atom', image)

