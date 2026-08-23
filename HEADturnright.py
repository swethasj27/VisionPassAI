import cv2

baseline_nose_x = None

def detect_right(frame, face_landmarks):

    global baseline_nose_x

    h, w, _ = frame.shape

    nose = face_landmarks.landmark[1]

    nose_x = int(nose.x * w)

    if baseline_nose_x is None:
        baseline_nose_x = nose_x

    movement = nose_x - baseline_nose_x

    cv2.putText(
        frame,
        "Challenge : TURN RIGHT",
        (20,90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,255),
        2
    )

    cv2.putText(
        frame,
        f"Movement : {movement}",
        (20,130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,255,0),
        2
    )

    if movement < -80:

        cv2.putText(
            frame,
            "RIGHT VERIFIED",
            (20,170),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            3
        )

        return True

    return False