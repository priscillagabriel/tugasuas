import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('google.jpeg')
print('Type: ', type(img), 'Dimension: ', img.shape)

img_copy = np.copy(img)
img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)
plt.imshow(img_copy)

low_green = np.array([0, 230, 0])
upp_green = np.array([200, 255, 240])

mask = cv2.inRange(img_copy, low_green, upp_green)
plt.imshow(mask, cmap='gray')

masked_img = np.copy(img_copy)
masked_img[mask != 0] = [0, 0, 0]
plt.imshow(masked_img)

bg_img = cv2.imread('moon2.jpeg')
bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2RGB)

crop_bg = bg_img[0:800, 0:1280]
crop_bg[mask == 0] = [0, 0, 0]

fin_img = crop_bg + masked_img
plt.imshow(fin_img)
plt.show()
