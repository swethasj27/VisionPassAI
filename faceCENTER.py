import cv2

def detect_center(frame, face_landmarks):

    h, w, _ = frame.shape

    nose = face_landmarks.landmark[1]

    nose_x = int(nose.x * w)

    cv2.putText(
        frame,
        "RETURN FACE TO CENTER",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Nose X : {nose_x}",
        (20, 130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    if 290 <= nose_x <= 350:

        cv2.putText(
            frame,
            "FACE CENTERED",
            (20,170),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            3
        )

        return True

    return False