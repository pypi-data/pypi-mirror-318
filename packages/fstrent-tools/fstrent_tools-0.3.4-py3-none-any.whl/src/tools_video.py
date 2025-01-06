import cv2

__all__ = [
    'play_video',
    'record_video'
]

def play_video(video_file):
    """
    Plays a video file.

    Args:
        video_file (str): The path to the video file to play.
    """
    cap = cv2.VideoCapture(video_file)

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow("Video", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

def record_video(duration=5, output_file="output.avi", fps=30.0):
    """
    Records a video from the default camera.

    Args:
        duration (int, optional): The duration of the recording in seconds. Defaults to 5.
        output_file (str, optional): The path to the output video file. Defaults to 'output.avi'.
        fps (float, optional): The frames per second of the video. Defaults to 30.0.
    """
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output_file, fourcc, fps, (640, 480))

    start_time = cv2.getTickCount()
    while int((cv2.getTickCount() - start_time) / cv2.getTickFrequency()) < duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows() 