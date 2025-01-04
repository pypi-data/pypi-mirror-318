import os
import unittest
import cv2
import numpy as np
from ocv_utils import VideoWriter


class TestVideoWriter(unittest.TestCase):

    def setUp(self):
        self.video_writer = VideoWriter("test_output.mp4")

    def tearDown(self):
        os.remove("test_output.mp4")

    def test_single_img(self):
        img = np.ones((512, 512, 3))
        for i in range(100):
            self.video_writer.add_frame(img)
        self.video_writer.release()

        cap = cv2.VideoCapture("test_output.mp4")

        height, width = cap.get(cv2.CAP_PROP_FRAME_HEIGHT), cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.assertEqual(width, 512)
        self.assertEqual(height, 512)

        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.assertEqual(length, 100)

    def test_hstack_imgs(self):
        img = np.ones((512, 512, 3))
        for i in range(100):
            self.video_writer.add_frame([img, img])
        self.video_writer.release()

        cap = cv2.VideoCapture("test_output.mp4")

        height, width = cap.get(cv2.CAP_PROP_FRAME_HEIGHT), cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.assertEqual(width, 1024)
        self.assertEqual(height, 512)

        length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.assertEqual(length, 100)


if __name__ == "__main__":
    unittest.main()
