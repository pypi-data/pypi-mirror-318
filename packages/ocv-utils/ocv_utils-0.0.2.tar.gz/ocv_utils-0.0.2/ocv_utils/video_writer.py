import cv2
import numpy as np
from ocv_utils.ops.img_concatenating import concat_imgs


class VideoWriter:
    """
    Simplifies exporting videos with opencv
    """

    def __init__(self, path="./output_video.mp4", fps=30, channels="rgb"):

        self._path = path
        self._fps = fps
        self._cv_videowriter = None
        self._channels = channels

        self._format = cv2.VideoWriter_fourcc(*'mp4v')  # TODO add support for mp4 and avi

    def add_frame(self, frame):

        if isinstance(frame, list):
            frame = concat_imgs(frame)

        if self._cv_videowriter is None:
            height, width = frame.shape[0], frame.shape[1]
            self._cv_videowriter = cv2.VideoWriter(self._path, self._format, self._fps, (width, height))

        if frame.dtype == np.float32 or frame.dtype == np.float64:
            frame = (frame * 255).astype(np.uint8)

        if self._channels == "rgb":
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        self._cv_videowriter.write(frame)

    def release(self):
        self._cv_videowriter.release()


if __name__ == "__main__":

    img = np.ones((512, 512, 3))
    video_writer = VideoWriter()

    for i in range(1000):
        video_writer.add_frame(img)

    video_writer = VideoWriter("hstack.mp4")

    for i in range(1000):
        video_writer.add_frame([img, img])
