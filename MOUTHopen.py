import cv2

def detect_mouth(frame, face_landmarks):

    h, w, _ = frame.shape

    upper_lip = face_landmarks.landmark[13]
    lower_lip = face_landmarks.landmark[14]

    upper_y = int(upper_lip.y * h)
    lower_y = int(lower_lip.y * h)

    mouth_gap = abs(lower_y - upper_y)

    cv2.putText(
        frame,
        "Challenge : LOWER YOUR JAW",
        (20,90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,255),
        2
    )

    cv2.putText(
        frame,
        f"Mouth Gap : {mouth_gap}",
        (20,130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,255,0),
        2
    )

    if mouth_gap > 20:

        cv2.putText(
            frame,
            "MOUTH VERIFIED",
            (20,170),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            3
        )

        return True

    return False