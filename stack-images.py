import numpy as np
import cv2
import glob
import os
import matplotlib.pyplot as plt
from PIL import Image

path = f'/Users/siddhartha/Desktop/PROJECTS/Fungus-ROI-Detection/predimages'

imgFiles = glob.glob(os.path.join(path, '*.jpg'))

# finalimg1 = None
# finalimg2 = None
# finalimg3 = None
# finalimg4 = None
# count = 0

# # print(imgFiles)
# imageSet = set()
# for p in imgFiles:
#   # print(p)
#   p = p.split('/')[-1]
#   imageSet.add(p[:7])


# allpatches = dict()

# # print(imageSet)
# # print(imgFiles)

# for img1 in imageSet:
#   for img2 in imgFiles:
#     img2check = img2.split('/')[-1]
#     # print(img1, img2check)
#     if img1 == img2check[:7]:
#       if img2check[9] == '.':
#         allpatches[int(img2check[8])] = img2
#       else:
#         allpatches[int(img2check[8:10])] = img2

# # print(allpatches)

# # for key, ipath in allpatches.items():
# for i in range(1,25):
#     key = i
#     print(allpatches)
#     ipath = allpatches[i]
#     print('path ', key, ipath)
#     img = cv2.imread(ipath)
#     # print(img.shape)
#     if key <= 6:
#         if key == 1:
#           finalimg1 = img
#         else:
#           finalimg1 = np.hstack((finalimg1, img))
#     elif key <= 12:
#         if key == 7:
#           finalimg2 = img
#         else:
#           finalimg2 = np.hstack((finalimg2, img))
#     elif key <= 18:
#         if key == 13:
#           finalimg3 = img
#         else:
#           finalimg3 = np.hstack((finalimg3, img))
#     else:
#         if key == 19:
#           finalimg4 = img
#         else:
#           finalimg4 = np.hstack((finalimg4, img))

#     if key == 24:
#       finalimg = np.vstack((np.vstack((finalimg1, finalimg2)), np.vstack((finalimg3, finalimg4))))
#       print('fshape ',finalimg.shape)
#       print(type(finalimg))
#       #  data = Image.fromarray(finalimg)
#       #  data.save('final.png')
#       finalimg = cv2.cvtColor(finalimg, cv2.COLOR_BGR2RGB)
#       cv2.imwrite('final2.png', finalimg)
#       #  plt.imsave()
#       #  plt.saveconfig() - dimension
#       cv2.imshow('frame3', finalimg)
#       cv2.waitKey(10000)
#     # cv2.imshow('frame2', finalimg1)
#     # cv2.waitKey(1000)


lst = [None]*6
for img in imgFiles:
  inumber = img.split('/')[-1][8]
  lst[int(inumber)] = img


finalimage1 = None
finalimage2 = None

for i, img in enumerate(lst):
  nxtimage = cv2.imread(lst[i])
  height, width, _ = nxtimage.shape
  half_width = width // 2
  if i == 0:
    finalimage1 = nxtimage
  elif i < 3:
    finalimage1 = np.hstack((finalimage1, nxtimage[:, half_width:, :]))
  elif i == 3:
    finalimage2 = nxtimage
  else:
    finalimage2 = np.hstack((finalimage2, nxtimage[:, half_width:, :]))

finalimage = np.vstack((finalimage1, finalimage2))
cv2.imshow('frame', finalimage)
cv2.waitKey(100000)
