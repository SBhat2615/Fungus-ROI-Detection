import os, cv2
import numpy as np
from glob import glob
from tqdm import tqdm
from skimage.measure import label, regionprops, find_contours


# Convert a mask to border image
def mask_to_border(mask):
    h, w = mask.shape
    border = np.zeros((h, w))

    contours = find_contours(mask, 250)

    # canvas = np.zeros_like(mask)
    # cv2.polylines(canvas, contours, isClosed=True, color=255, thickness=2)
    # cv2.imshow('Contours', canvas)

    for contour in contours:
        for c in contour:
            x = int(c[0])
            y = int(c[1])
            border[x][y] = 255
    return border


# Mask to bounding boxes
def mask_to_bbox(mask):
    bboxes = []

    mask = mask_to_border(mask)
    lbl = label(mask)
    props = regionprops(lbl)
    for prop in props:
        x1 = prop.bbox[1]
        y1 = prop.bbox[0]
        x2 = prop.bbox[3]
        y2 = prop.bbox[2]
        bboxes.append([x1, y1, x2, y2])
    return bboxes


def parse_mask(mask):
    mask = np.expand_dims(mask, axis=-1)
    mask = np.concatenate([mask, mask, mask], axis=-1)
    return mask


if __name__ == "__main__":
    
    images = sorted(glob(os.path.join("Images", "original", "*")))
    masks = sorted(glob(os.path.join("Images", "mask", "*")))

    if not os.path.exists("results"):
        os.makedirs("results")

    # Loop over the dataset
    for x, y in tqdm(zip(images, masks), total=len(images)):
        # Extract the name
        name = x.split("/")[-1].split(".")[0]

        # Read image and mask
        x = cv2.imread(x, cv2.IMREAD_COLOR)
        y = cv2.imread(y, cv2.IMREAD_GRAYSCALE)

        print(x.shape, y.shape)

        # Detecting bounding boxes
        bboxes = mask_to_bbox(y)

        ''' NORMALIZE THE VALUES ?? '''
        # Marking bounding box on image
        for bbox in bboxes:
            x = cv2.rectangle(x, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 0, 255), 1)

            # Calculate & store bounding boxes
            height = bbox[3]-bbox[1]
            width = bbox[2]-bbox[0]
            x1 = bbox[0] + (width/2)
            y1 = bbox[1] + (height/2)

            height, width, x1, y1 = round(height/256,2), round(width/256,2), round(x1/256,2), round(y1/256,2)
            ''' VERIFY THE COORDINATES '''

            with open('annote.txt', 'a') as file:
                # print('Image : ', name)
                val = '0' + '\t' + str(x1) + '\t' + str(y1) + '\t' + str(height) + '\t' + str(width)
                file.write(name + ' ' + val + '\n')

        # Saving the image
        cat_image = np.concatenate([x, parse_mask(y)], axis=1)
        cv2.imwrite(f"results/{name}.png", cat_image)
