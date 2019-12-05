import cv2
import matplotlib.pyplot as plt
'''
raw = cv2.VideoCapture(r'F:\testImg\testVideo.mp4')
a = 1

#start = time.time()
while 1:
    a = a+1
    check, colorFrame = raw.read()
    grayFrame = cv2.cvtColor(colorFrame, 0)
    #cv2.imshow('testFrames', colorFrame)
    print(check)
    cv2.imshow('grayFrames', grayFrame)
    quitKey = cv2.waitKey(1)
    cv2.imwrite(r'F:\testImg\Frames\cvtest' +
                str(a)+'.jpg', grayFrame)
    if quitKey == ord('q'):
        break

print(a)
raw.release()
cv2.destroyAllWindows()
'''
import matplotlib.image as mpimg
dim = (1920, 1080)

im1 = cv2.imread(r'F:\testImg\Frames\cvtest38.jpg', cv2.IMREAD_COLOR)
im1 = cv2.resize(im1, dim, interpolation=cv2.INTER_AREA)
im2 = cv2.imread(r'F:\testImg\Frames\cvtest170.jpg', cv2.IMREAD_COLOR)
im2 = cv2.resize(im2, dim, interpolation=cv2.INTER_AREA)
im3 = cv2.imread(r'F:\testImg\Frames\cvtest340.jpg', cv2.IMREAD_COLOR)
im3 = cv2.resize(im3, dim, interpolation=cv2.INTER_AREA)
im4 = cv2.imread(r'F:\testImg\Frames\cvtest460.jpg', cv2.IMREAD_COLOR)
im4 = cv2.resize(im4, dim, interpolation=cv2.INTER_AREA)
im5 = cv2.imread(r'F:\testImg\Frames\cvtest500.jpg', cv2.IMREAD_COLOR)
im5 = cv2.resize(im5, dim, interpolation=cv2.INTER_AREA)
im6 = cv2.imread(r'F:\testImg\Frames\cvtest580.jpg', cv2.IMREAD_COLOR)
im6 = cv2.resize(im6, dim, interpolation=cv2.INTER_AREA)
#cv2.imshow('test1', im1)
#cv2.imshow('test2', im2)
#cv2.waitKey()

arr = []
arr.append(im1)
arr.append(im2)
arr.append(im3)
arr.append(im4)
arr.append(im5)
arr.append(im6)
s = cv2.Stitcher.create()
status, FinalFrame = s.stitch(arr)

#cv2.imshow('stitched',FinalFrame)
plt.imshow(FinalFrame)
plt.waitforbuttonpress()
#cv2.waitKey()
#cv2.destroyAllWindows()



print("done")