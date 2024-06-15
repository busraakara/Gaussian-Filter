
# Gaussian Filter

Hii! 

In this repository, i wanted to explain how convolution work on Gaussian Filter that we use in image processing. You may think that I have explained too much but since the Gaussian Filter is fundemental and basic operation in image processing, I wanted to explain it in detail and make it easier for those who are new to this field.

### What is Gaussian Filter?
A Gaussian filter is a linear filter that is typically used to blur images and remove noise. It is based on the Gaussian distribution and applies a convolution kernel to the image, smoothing the pixel values.

### What is Gaussian Filter used for?
Gaussian Filters are mostly used in:
image processing and computer vision application as pre-processing step, 
photoshop applications for smooth images.

### What is the difference between 2D and 3D Gaussian Filter?
Well the main difference is 'Digital Image Dimension'. 
2D image consist of x and y axes. The x-axis represents the length and the y-axis represents the width. That makes 2D images gray scale because they have only 1 channel. (gray channel)
3D images consist of x, y and z axes. z-axes represents the 3 channels and color images are formed by the combination of these B, G, R channels. We use convolution in image processing to filter imges. And we perform convolution on channels. If we perform convolution on 1 channel gray image, than it is 2D Filtering and if we perform it on 3 channel color image, than it is 3D Filteirng.

**Keep in mind!** : Do not think of the dimensions in the pictures as in real life. In digital pictures, 2 dimensions represent the gray image and 3 dimensions represent the colored image. There is a concept of depth in both pictures. In real life, we express depth with 3 dimensions, but in the picture, the pixel values ​​​​are between 0-255 and these express depth.

## How do we apply 2D and 3D Gaussian Filters?

For this first look at the formula of the Gaussian Filter.

The Gaussian filter can be expressed as:

$`G(x, y) = \frac{1}{2 \pi \sigma^2} e^{-\frac{x^2 + y^2}{2 \sigma^2}}`$

Here,
- $`G(x, y)`$ : Value of the Gaussian filter at position (x, y),
- $` σ `$ : Standard deviation parameter,
- $x$ and $y$ : Coordinates considered as distances from the center of the filter.

**Are we gonna use this formula?**

No :)
We use convolution in image processing to filter imges. We are just gonna use the Convolution with Gaussian kernel that we get from Gaussian Graph.
We can represent this Gauss formula using kernels. Gaussian is also 3D graphs, and you can turn this 3D graph into 2D kernel to use in convolution. 

Here is the reperesentation of turning Gauss graph into 2d kernel. If we look at the Gaussian Graph from above, we see the picture on the right. We can think this image as a matrix that every pixel is representing a value that Gaussian graph takes. 

![1_PaZx8eCc7bWaERP6eP5JjA](https://github.com/busraakara/Gaussian-Filter/assets/105877486/91a93e51-7b7d-436c-8e16-d1c7c8524c8b)

Here are some Gaussian kernels we get from Graph. They can be 3x3, 5x5, 7x7, 9x9 and any odd matrix size. But in image processing, we mostly use 3x3, 5x5 or 7x7.

!!!You can also get these kernels using Gaussian formula.

![Discrete-approximation-of-the-Gaussian-kernels-3x3-5x5-7x7](https://github.com/busraakara/Gaussian-Filter/assets/105877486/dc8736bd-f842-4dc3-8b7a-869d9f02bd37)

**How do we perform convolution?**

Here is a representaition of convolution. Input image is our original image channel, filter is our kernel (Gaussian kernel in this case) and output image is our filtered image channel. Let's assume we are using 3x3 Gaussian kernel. Starting from the 3x3 piece in the upper left corner of the original image, we first move to the right one by one and come to the end, then move down one row and move from left to right one by one again. In each shift, we multiply each index pixel of the kernel matrix by the corresponding index pixel in the image matrix, then we add the multiplied 9 values, this result gives the new value of the pixel in the middle of the piece we are in. And we continue this process until the entire image is scanned. 

![Image-convolution-with-an-input-image-of-size-7-7-and-a-filter-kernel-of-size-3-3](https://github.com/busraakara/Gaussian-Filter/assets/105877486/7f65b9e8-6e97-456a-835d-cfa536d5d098)

But if you noticed, the output image size is smaller than the original image because of the convolution. Therefore, before starting the convolution, we add extra pixels around the image to make the size the same and this called zero padding. And thats how you perform convolution on single channel. For 3D Gaussian Filter, you have to perform convolution for each channel and merge  them together.

## Let's look at the filtered image results from my code.

**2D GAUSSIAN FILTER**

![2d_gauss](https://github.com/busraakara/Gaussian-Filter/assets/105877486/8f14931d-11f4-41df-9339-424c9d40357a)

**3D GAUSSIAN FILTER**

![3d_gauss](https://github.com/busraakara/Gaussian-Filter/assets/105877486/90358bc2-af37-405c-aeac-f7f6748b64cb)

This was a summary of how to perform 2D and 3D Gaussian Filters using Convolution. If you have any questions, don't hesitate to ask me.
