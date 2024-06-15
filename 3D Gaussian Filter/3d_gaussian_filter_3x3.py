#import libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt

#upload image
image = cv2.imread('/content/splash.jpg')

#split image channels
r = image[:,:,0]
g = image[:,:,1]
b = image[:,:,2]

gaussian_filter = np.zeros(shape=(height, width,3))

#put these channels in a list
channel_list = [r, g, b]

#define Gaussian Kernel
kernel = [[1/16, 1/8, 1/16],
          [1/8,  1/4, 1/8],
          [1/16, 1/8, 1/16]]

for channel, img in enumerate(channel_list):
  #define height and width
  height=img.shape[0]
  width=img.shape[1]

  #zero padding
  gauss=np.zeros((height+2,width+2))
  gauss[1:height+1,1:width+1] = img

  #convolution
  for i in range (0,height-2):
    for j in range(0,width-2):
      block = gauss[i:i+3 , j:j+3]
      convolution=np.sum(np.multiply(block,kernel))
      gaussian_filter[i][j][channel]=convolution

#change image data type to unsigned integer (8 bits)
gaussian_filter=np.uint8(gaussian_filter)      

#change image channel from rgb to bgr for display on matplotlib.  
bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
bgr_gaussian_filter_3d3x3 = cv2.cvtColor(gaussian_filter, cv2.COLOR_RGB2BGR)

#display result through matplotlib
fig = plt.figure(figsize=(10, 7))
fig.add_subplot(1, 2, 1)
plt.imshow(bgr_image)
plt.title("Original Image")

fig.add_subplot(1, 2, 2)
plt.imshow(bgr_gaussian_filter_3d3x3 )
plt.title("3x3 Gaussian Blurred Image")

#save result
plt.savefig('/content/3d_gauss_3x3.png', bbox_inches='tight')
