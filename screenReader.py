import subprocess
import sys
import time

import cv2
import numpy as np
from PIL import ImageGrab


# capp = cv2.VideoCapture(0)
# cv2.VideoCapture()

def ParsePDF(filename):
    print(filename)

    last_time = time.time()
    if (sys.platform == "linux"):

        print("obaaaa")
        grepResult = subprocess.Popen("wmctrl -Gl | grep " + filename, stdout=subprocess.PIPE, shell=True, text=True)
        time.sleep(3.0)
        print("=============ALL IS READ NICELY IN THE VARIABLE!===============")
        stdout, stderr = grepResult.communicate()

        stdout = stdout.strip()
        # stderr = stderr.strip()
        print(("var1=|" + stdout.strip()) + "|")
        # print(("var2=|" + stderr.strip()) + "|")

        stdoutArr = stdout.split(" ")
        x = stdoutArr.count('')
        for i in range(x):
            stdoutArr.remove('')

        print("=============processing the command Result!===============")

        xPos = int(stdoutArr[2])
        yPos = int(stdoutArr[3])
        width = int(stdoutArr[4])
        height = int(stdoutArr[5])

        printScreen_pil = ImageGrab.grab(bbox=(0,0,1440,900))

        printScreen_numpy = np.array(printScreen_pil, dtype='uint8')

        cv2.imshow('window', cv2.cvtColor(printScreen_numpy, cv2.COLOR_BGR2RGB))

        # cv2.imshow('window', printScreen_numpy)

        cv2.imwrite("assets/imgs/xx.png", printScreen_numpy)

        # if cv2.waitKey(25) & 0xFsF == ord('q'):
        #     cv2.destroyAllWindows()
        #     print("session Terminated")
        #     # break

    print("loop took: {} sec".format(time.time() - last_time))
    last_time = time.time()
    return "kaaaaaaa"
