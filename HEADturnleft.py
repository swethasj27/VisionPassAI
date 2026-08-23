import cv2


def detect_left(frame, face_landmarks):

    global challenge_completed

    h, w, _ = frame.shape

    nose = face_landmarks.landmark[1]

    nose_x = int(nose.x * w)

    cv2.putText(
        frame,
        "Challenge : TURN LEFT",
        (20,90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,255),
        2
    )

    cv2.putText(
        frame,
        f"Nose X : {nose_x}",
        (20,130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,255,0),
        2
    )

    if nose_x > 400:
        cv2.putText(
            frame,
            "LEFT VERIFIED",
            (20,170),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            3
        )
        return True

    return False
