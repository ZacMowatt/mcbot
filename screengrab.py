import numpy as np
from PIL import ImageGrab
import cv2
import time

last_time = time.time()

while(True):
    screen = ImageGrab.grab(bbox=(0, 23, 855, 525))

    print("Loop took {} seconds".format(time.time() - last_time))
    last_time = time.time()
    cv2.imshow("Window", np.array(screen))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
