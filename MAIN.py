import cv2
import mediapipe as mp
from BLINKdetect import detect_blink
from HEADturnleft import detect_left
from faceCENTER import detect_center
from HEADturnright import detect_right
from MOUTHopen import detect_mouth

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True
)

cap = cv2.VideoCapture(0)
current_step = 1

while True:

    success, frame = cap.read()

    if not success:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        face_landmarks = results.multi_face_landmarks[0]
        if current_step == 1:
            attendance_verified = False

            if detect_blink(frame, face_landmarks):
                current_step = 2

        elif current_step == 2:

            if detect_left(frame, face_landmarks):
                current_step = 3

        elif current_step == 3:

            if detect_center(frame, face_landmarks):
                current_step = 4

        elif current_step == 4:

            if detect_right(frame, face_landmarks):
                current_step = 5

        elif current_step == 5:

            if detect_center(frame, face_landmarks):
                current_step = 6

        elif current_step == 6:

            if detect_mouth(frame, face_landmarks):
                attendance_verified = True
                current_step = 7
        if attendance_verified:

            cv2.putText(
                frame,
                "ATTENDANCE VERIFIED",
                (40,250),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (0,255,0),
                4
            )

    cv2.imshow("AI Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()