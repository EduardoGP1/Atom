import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

# For webcam input:
a = 0
while a == 0:
    cap = cv2.VideoCapture("videos/testeatom.mp4")
    with mp_pose.Pose(
            min_detection_confidence=0.1,
            min_tracking_confidence=0.1) as pose:
        while cap.isOpened():
            success, image = cap.read()
            if cv2.waitKey(5) & 0xFF == 27:
                cap.isOpened(0)
            if not success:
                print(cap)
                break

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = pose.process(image)

    # Draw the pose annotation on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    # Flip the image horizontally for a selfie-view display.
            cv2.imshow('Atom', image)
            if cv2.waitKey(5) & 0xFF == 27:
                break
    cap.release()