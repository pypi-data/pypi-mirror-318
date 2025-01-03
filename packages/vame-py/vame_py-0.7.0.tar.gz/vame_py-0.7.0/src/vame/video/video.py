import cv2
from typing import List
import numpy as np


def get_video_frame_rate(video_path):
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        raise Exception(f"Unable to open video file: {video_path}")
    frame_rate = int(video.get(cv2.CAP_PROP_FPS))
    video.release()
    return frame_rate


# def play_aligned_video(
#     a: List[np.ndarray],
#     n: List[List[np.ndarray]],
#     frame_count: int,
# ) -> None:
#     """
#     Play the aligned video.

#     Parameters
#     ---------
#     a : List[np.ndarray]
#         List of aligned images.
#     n : List[List[np.ndarray]]
#         List of aligned DLC points.
#     frame_count : int
#         Number of frames in the video.
#     """
#     colors = [
#         (255, 0, 0),
#         (0, 255, 0),
#         (0, 0, 255),
#         (255, 255, 0),
#         (255, 0, 255),
#         (0, 255, 255),
#         (0, 0, 0),
#         (255, 255, 255),
#     ]
#     for i in range(frame_count):
#         # Capture frame-by-frame
#         ret, frame = True, a[i]
#         if ret is True:
#             # Display the resulting frame
#             frame = cv2.cvtColor(frame.astype("uint8") * 255, cv2.COLOR_GRAY2BGR)
#             im_color = cv2.applyColorMap(frame, cv2.COLORMAP_JET)
#             for c, j in enumerate(n[i]):
#                 cv2.circle(im_color, (j[0], j[1]), 5, colors[c], -1)
#             cv2.imshow("Frame", im_color)
#             # Press Q on keyboard to exit
#             # Break the loop
#             if cv2.waitKey(25) & 0xFF == ord("q"):
#                 break
#         else:
#             break
#     cv2.destroyAllWindows()
