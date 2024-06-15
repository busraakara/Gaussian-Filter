#import libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt

#upload image
image = cv2.imread('/content/splash.jpg')

#convert image colour bgr to gray scale
img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

#define height and width
height=img.shape[0]
width=img.shape[1]

#define kernel
kernel = [[0/1003, 0/1003,  1/1003,  2/1003,   1/1003,  0/1003,  0/1003],
          [0/1003, 3/1003,  13/1003, 22/1003,  13/1003, 3/1003,  0/1003],
          [1/1003, 13/1003, 59/1003, 97/1003,  59/1003, 13/1003, 1/1003],
          [2/1003, 22/1003, 97/1003, 159/1003, 97/1003, 22/1003, 2/1003],
          [1/1003, 13/1003, 59/1003, 97/1003,  59/1003, 13/1003, 1/1003],
          [0/1003, 3/1003,  13/1003, 22/1003,  13/1003, 3/1003,  0/1003],
          [0/1003, 0/1003,  1/1003,  2/1003,   1/1003,  0/1003,  0/1003]]

#zero padding
gauss=np.zeros((height+6,width+6))
gauss[3:height+3,3:width+3] = img

gaussian_filter = np.zeros(shape=(height, width))

#convolution
for i in range (0,height-6):
    for j in range (0,width-6):
        block = gauss[i:i+7 , j:j+7]
        convolution=np.sum(np.multiply(block,kernel))
        gaussian_filter[i][j]=convolution

#change image data type to unsigned integer (8 bits)
#because that is all digital images data type
gaussian_filter_2d7x7=np.uint8(gaussian_filter)

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
plt.imshow(gaussian_filter, cmap='gray')
plt.title("7x7 Gaussian Blurred Image")

#save result
plt.savefig('/content/2d_gauss_7x7.png', bbox_inches='tight')
