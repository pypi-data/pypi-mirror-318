import numpy as np
import cv2


def concat_imgs(imgs):
    for i, img in enumerate(imgs):

        # Convert to Uint8
        if img.dtype == np.float32 or img.dtype == np.float64:
            img = (img * 255).astype(np.uint8)

        # Grayscale to color
        if len(img.shape) == 2 or img.shape[2] == 1:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

        imgs[i] = img

    img = np.concatenate(imgs, axis=1)
    return img