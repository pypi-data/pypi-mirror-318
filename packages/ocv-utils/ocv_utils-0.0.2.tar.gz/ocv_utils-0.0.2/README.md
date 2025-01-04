# OCV_Utils 

Simplifies OpenCV functionalities for image and video i/o and debug-windows.

**Main Features:**
- uses _rgb_ instead of _bgr_ by default for image and video i/o
- adds a loop and boomerang mode for video player
- imshow() accepts lists of images that will be automatically displayed next to each other, independent of their formats
- easier trackbar integration

## Install

```bash
pip3 install ocv_utils
```

## Usage

### Image Loading

Load image and convert it to a certain channel type definition. Supported types `rgb`, `rgba`, `gray`

```python
from ocv_utils import load_image

img = load_image("my_image.png", channels="rgba")
```

### Video Reading

Play modes: ["normal", "loop", "boomerang"]

```python
from ocv_utils import VideoReader

video = VideoReader("video.mp4", play_mode="normal")

# cv2 like
while True:
    ret, frame = video.read()
    if not ret: # CAUTION: for play_mode "loop" and "boomerang" `ret` is the frame id, so break will be called at frame 0.
        break   # Don't use this with play_mode "loop" or "boomerang"

# Or read certain frame
ret, frame = video.read(frame_id=42)
```

### Video Writing

```python
from ocv_utils import VideoWriter
import numpy as np

img = np.zeros((512, 512, 3))

video_writer = VideoWriter(path="video.mp4", fps=30, channels="rgb")
for i in range(1000):
    video_writer.add_frame(img)

# or with horizontal stacking 
video_writer = VideoWriter("hstack.mp4")
for i in range(1000):
    video_writer.add_frame([img, img])
```


### Window
```python
import numpy as np
from ocv_utils import Window

window = Window(delay=0)
window.add_trackbar("x", 1, 255)
window.add_key_action(ord('h'), lambda: print("Hello World!"))

img1 = np.zeros((256, 256), dtype=np.uint8)
img2 = np.random.random((256, 256, 3))

trackbar_values = window.imshow([img1, img2])
print("Trackbar Values:", trackbar_values) # Trackbar Values: {'x': 1}

```