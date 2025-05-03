import cv2

def show_frame(frame, window_name="Pose Detection"):
    # Creating a resizeable window.
    cv2.namedWindow("Pose Detection", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Pose Detection", 800, 600)

    cv2.imshow(window_name, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): # PRESS 'q' TO EXIT
        return False
    return True