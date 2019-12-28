import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random

raw = cv2.VideoCapture(r'F:\testImg\t4.mp4')
a = 1

#start = time.time()
'''
while 1:
    a = a+1
    check, colorFrame = raw.read()
    grayFrame = cv2.cvtColor(colorFrame, 0)
    #cv2.imshow('testFrames', colorFrame)
    print(check)
    cv2.imshow('grayFrames', grayFrame)
    quitKey = cv2.waitKey(1)
    cv2.imwrite(r'F:\testImg\f2\cvtest' +
                str(a)+'.jpg', grayFrame)
    if quitKey == ord('q'):
        break

print(a)
raw.release()
cv2.destroyAllWindows()
'''

arr = []
dim = (1920, 1080)
d = {}
for i in range(2, 633, 63):
    d["im{0}".format(i)] = cv2.imread(
        r'F:\testImg\f2\cvtest'+str(i)+'.jpg', cv2.IMREAD_COLOR)
    d["im{0}".format(i)] = cv2.resize(d["im{0}".format(i)],
                                      dim, interpolation=cv2.INTER_AREA)
# print(d)
#s = cv2.Stitcher.create()
#status, FinalFrame = s.stitch(arr)
'''for i in range(2,5):
    arr.append(d["im{0}".format(i)])
'''
# arr.append(d["im2"])
# arr.append(d["im10"])
for i in range(2, 633, 63):
    arr.append(d["im{0}".format(i)])
''''''
s = cv2.Stitcher.create()
status, FinalFrame = s.stitch(arr)
# cv2.imshow('stitched',FinalFrame)
plt.imshow(FinalFrame)
plt.waitforbuttonpress()
# cv2.waitKey()
# cv2.destroyAllWindows()
# print(FinalFrame)
print(len(arr))
