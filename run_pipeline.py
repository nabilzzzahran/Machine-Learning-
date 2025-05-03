import cv2
from src.pipeline import PoseDetectionPipeLine
from src.visualization import show_frame

def main():
    pipeline = PoseDetectionPipeLine()

    video_path = "C:\Users\User\Downloads\Exercise-Form-Checker-main\Exercise-Form-Checker-main\Assets\test_video.mp4"
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could Not Open Video")
        return
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = pipeline.process_frame(frame)

        frame = pipeline.draw_pose(frame, results)

        if not show_frame(frame):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__== "__main__":
    main()