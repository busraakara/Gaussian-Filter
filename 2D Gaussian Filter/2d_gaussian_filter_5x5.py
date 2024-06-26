#import libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt

#upload image
image = cv2.imread('/content/splash.jpg')

#convert image colour bgr to gray scale
img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

#define height and width
height = img.shape[0]
width = img.shape[1]

#define kernel
kernel = [[1/273, 4/273,  7/273,  4/273,  1/273],
          [4/273, 16/273, 26/273, 16/273, 4/273],
          [7/273, 26/273, 41/273, 26/273, 7/273],
          [4/273, 16/273, 26/273, 16/273, 4/273],
          [1/273, 4/273,  7/273,  4/273,  1/273]]

#zero padding
gauss=np.zeros((height+4, width+4))
gauss[2:height+2, 2:width+2] = img

gaussian_filter = np.zeros(shape=(height, width))

#convolution
for i in range (0, height-4):
    for j in range (0, width-4):
        block = gauss[i:i+5, j:j+5]
        convolution=np.sum(np.multiply(block, kernel))
        gaussian_filter[i][j]=convolution

#change image data type to unsigned integer (8 bits)
#because that is all digital images data type
gaussian_filter_2d5x5=np.uint8(gaussian_filter)

#change image channel from rgb to bgr for display on matplotlib.  
bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

#display result through matplotlib
fig = plt.figure(figsize=(10, 7))
fig.add_subplot(1, 3, 1)
plt.imshow(bgr_image)
plt.title("Original Image")

fig.add_subplot(1, 3, 2)
plt.imshow(img, cmap='gray')
plt.title("Gray Image")

fig.add_subplot(1, 3, 3)
plt.imshow(gaussian_filter_2d5x5, cmap='gray')
plt.title("5x5 Gaussian Blurred Image")

#save result
plt.savefig('/content/2d_gauss_5x5.png', bbox_inches='tight')
