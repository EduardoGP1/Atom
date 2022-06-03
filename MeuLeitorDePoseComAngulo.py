import cv2
import serial
import mediapipe as mp
import numpy as np
import math
import time
from tkinter import *

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

#arduino = serial.Serial('COM6', 2000000)

a = 0

def getAngle(cotovelo, ombro, pulso):
    #SegA = [ombro[0] - cotovelo[0], ombro[1] - cotovelo[1], ombro[2] - cotovelo[2]]
    #SegB = [pulso[0] - cotovelo[0], pulso[1] - cotovelo[1], pulso[2] - cotovelo[2]]
    #ProdEscalar = SegA[0]*SegB[0]+SegA[1]*SegB[1]+SegA[2]*SegB[2]
    #Comp_SegA = math.sqrt(SegA[0]**2+SegA[1]**2+SegA[2]**2)
    #Comp_SegB = math.sqrt(SegB[0]**2+SegB[1]**2+SegB[2]**2)
    #angulo = math.acos(ProdEscalar/(Comp_SegA*Comp_SegB))*180/3#formula original se dividia por 3,14
    #angulo = round(angulo)
    #angulo = str(angulo)

    vetor_cotombro = [cotovelo[0] - ombro[0], cotovelo[1] - ombro[1], cotovelo[2] - ombro[2]]

    vetor_cotpulso = [cotovelo[0] - pulso[0], cotovelo[1] - pulso[1], cotovelo[2] - pulso[2]]

    modulo_cotombro = math.sqrt((vetor_cotombro[0]) ** 2 +
        (vetor_cotombro[1]) ** 2 + (vetor_cotombro[2]) ** 2)

    modulo_cotpulso = math.sqrt((vetor_cotpulso[0]) ** 2 +
        (vetor_cotpulso[1]) ** 2 + (vetor_cotpulso[2]) ** 2)

    angulo_cotovelo = math.degrees(math.acos(((vetor_cotombro[0]*vetor_cotpulso[0])+(vetor_cotombro[1]*vetor_cotpulso[1])+(vetor_cotombro[2]*vetor_cotpulso[2]))/
                                             (modulo_cotombro*modulo_cotpulso)))

    print (cotovelo[0], cotovelo[1], cotovelo[2], ombro[0], ombro[1], ombro[2], pulso[0], pulso[1], pulso[2], angulo_cotovelo)
    #if cv2.waitKey(1) & 0xFF == 27:
        #arduino.write((angulo + '\0').encode())
    #cv2.putText(image, str(angulo), (10, 60), cv2.FONT_HERSHEY_COMPLEX,
                #2, (0, 0, 255), 2, cv2.LINE_AA)#Colocar o angulo por escrito na imagem do vídeo

while a == 0:
    cap = cv2.VideoCapture("videos/testepatom1.mp4")
    with mp_pose.Pose(
            min_detection_confidence=0.1,
            min_tracking_confidence=0.1) as pose:
        while cap.isOpened():
            success, image = cap.read()
            if cv2.waitKey(1) & 0xFF == ord('e'):
                a=1
                break

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = pose.process(image)
            landmarks = results.pose_landmarks.landmark
            ombro = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y,
                     landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].z]
            cotovelo = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y,
                        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].z]
            pulso = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y,
                     landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].z]

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
#arduino.close()