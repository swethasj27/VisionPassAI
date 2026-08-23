import cv2


blink_counter = 0
eye_closed = False


def detect_blink(frame, face_landmarks):

    global blink_counter
    global eye_closed

    top = face_landmarks.landmark[159]
    bottom = face_landmarks.landmark[145]

    h, w, _ = frame.shape

    top_y = int(top.y * h)
    bottom_y = int(bottom.y * h)

    distance = abs(bottom_y - top_y)

    cv2.putText(
        frame,
        "Challenge : BLINK ONCE",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,255),
        2
    )

    cv2.putText(
        frame,
        f"Eye Distance : {distance}",
        (20,130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,255,0),
        2
    )

    if distance < 6:

        if not eye_closed:

            blink_counter += 1
            eye_closed = True

    else:

        eye_closed = False


    if blink_counter >= 1:

        cv2.putText(
            frame,
            "BLINK SUCCESS",
            (20,170),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            3
        )

        return True

    return False