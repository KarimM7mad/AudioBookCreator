import sys, subprocess, os
import time
import cv2
import numpy as np
from screenReader import ParsePDF
from OCR_Pipline import TextDetection

filename = "sample.pdf"

# print(sys.platform)

pdfText = ""
if subprocess.run(["xdg-open", filename]).returncode == 0:
    print("opened the PDF, 3ash")
    time.sleep(3.0)
    pdfText = ParsePDF(filename)

# time.sleep(3.0)
# grepResult, _ = subprocess.Popen("wmctrl -Gl | grep " + filename, stdout=subprocess.PIPE, shell=True,text=True).communicate()
#
#
# print(grepResult)
# time.sleep(3.0)
# subprocess.run(["wmctrl", "-r", filename, "-b", "remove,maximized_vert,maximized_horz"])


# print(x.returncode)
#
# if (x.returncode == 0):
#     print(x.stdout)
# else:
#     print(x.stderr)

#
# time.sleep(3.0)
# subprocess.Popen("wmctrl -r " + filename.split(".pd")[0] + " -e 0,0,100,1440,900")

# capp = cv2.VideoCapture(0)
#
# _, frame = capp.read()
# cv2.imshow('frame', np.array(frame))
# time.sleep(10.0)
#
# capp.release()
# cv2.destroyAllWindows()


print(pdfText)
