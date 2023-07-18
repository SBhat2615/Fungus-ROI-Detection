import cv2
import numpy as np
import os
import glob

# Mask Image Path
dir = 'Annotations/Images/mask/'

# Original Image Path
odir = 'Annotations/Images/original/'

# List of all Images
imgFiles = glob.glob(os.path.join(dir, '*.jpg'))

# For all Images
for imgPath in imgFiles:
    # Mask
    img1 = cv2.imread(imgPath)
    grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    npImg = np.asarray(grayImg)

    #print(npImg.shape)
    np.set_printoptions(threshold=np.prod(img1.shape))
    #print(npImg)

    # Get coordinates
    x1, y1 = 500, 500
    x2, y2 = 0, 0
    for x in range(npImg.shape[0]):
        for y in range(npImg.shape[1]):
            #print(npImg[x,y], end=' ')
            if npImg[x, y] == 255:
                x1, y1 = min(x1, y), min(y1, x)
                x2, y2 = max(x2, y), max(y2, x)
        #print()

    # x1, y1 = 50, 50
    # x2, y2 = 250, 250
    # print('x1 : ', x1, ' -- y1 : ', y1)
    # print('x2 : ', x2, ' -- y2 : ', y2)

    if x1 == 0:
        x1 += 1
    if y1 == 0:
        y1 += 1

    if x2 == 255:
        x2 -= 1
    if y2 == 255:
        y2 -= 1

    # Draw Images
    maskImg = img1.copy()
    orgImgPath = odir + imgPath.split('/')[-1]
    orgImg = cv2.imread(orgImgPath)

    # Draw bounding box
    try:
      color = (0, 0, 255)
      thickness = 2
      cv2.rectangle(maskImg, (x1, y1), (x2, y2), color, thickness)
      cv2.rectangle(orgImg, (x1, y1), (x2, y2), color, thickness)
    except:
        pass
    
    # cv2.imshow('Image', grayImg)
    cv2.imshow('Mask Image', maskImg)
    cv2.imshow('Original Image', orgImg)

    # Dump the coordinates to text/json
    with open('Annotations/annote.txt', 'a') as file:
        val = '1' + '\t' + str(x1) + '\t' + str(y1) + '\t' + str(x2) + '\t' + str(y2)
        file.write(val + '\n')

    cv2.waitKey(5000)
    cv2.destroyAllWindows()