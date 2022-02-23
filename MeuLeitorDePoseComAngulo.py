import cv2
import serial
import mediapipe as mp
import numpy as np
import math

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

ser = serial.Serial('COM6', 9600)

a = 0

def getAngle(cotovelo, ombro, pulso):
    SegA = [ombro[0] - cotovelo[0], ombro[1] - cotovelo[1]]
    SegB = [pulso[0] - cotovelo[0], pulso[1] - cotovelo[1]]
    ProdEscalar = SegA[0]*SegB[0]+SegA[1]*SegB[1]
    Comp_SegA = math.sqrt(SegA[0]**2+SegA[1]**2)
    Comp_SegB = math.sqrt(SegB[0]**2+SegB[1]**2)
    angulo = math.acos(ProdEscalar/(Comp_SegA*Comp_SegB))*180/3#formula original se dividia por 3,14
    #ser.write(b"angulo")
    cv2.putText(image, str(angulo), (10, 60), cv2.FONT_HERSHEY_COMPLEX,
                2, (0, 0, 255), 2, cv2.LINE_AA)
    print (ser.read(20))


while a == 0:
    cap = cv2.VideoCapture("videos/videoangulo.mp4")
    with mp_pose.Pose(
            min_detection_confidence=0.1,
            min_tracking_confidence=0.1) as pose:
        while cap.isOpened():
            success, image = cap.read()
            if cv2.waitKey(1) & 0xFF == 27:
                a=1
                break

            #elif cv2.waitKey(1) & 0xFF == ord("s"):


    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = pose.process(image)
            landmarks = results.pose_landmarks.landmark
            ombro = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            cotovelo = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            pulso = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            getAngle(cotovelo, ombro, pulso)
    # Draw the pose annotation on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
            image = cv2.resize(image, (700, 500))
            cv2.imshow('Atom', image)
ser.close()