
# Gaussian Filter

### What is Gaussian Filter?
A Gaussian filter is a linear filter that is typically used to blur images and remove noise. It is based on the Gaussian distribution and applies a convolution kernel to the image, smoothing the pixel values.

### What is Gaussian Filter used for?
Gaussian Filters are mostly used in:
image processing and computer vision application as pre-processing step, 
photoshop applications for smooth images.

### What is the difference between 2D and 3D Gaussian Filter?
Well the main difference is 'Digital Image Dimension'. 
2D image consist of x and y axes. The x-axis represents the length and the y-axis represents the width. That makes 2D images gray scale because they have only 1 channel. (gray channel)
3D images consist of x, y and z axes. z-axes represents the 3 channels and color images are formed by the combination of these B, G, R channels.

We use convolution in image processing to filter imges. 

**Keep in mind!** : Do not think of the dimensions in the pictures as in real life. In digital pictures, 2 dimensions represent the gray image and 3 dimensions represent the colored image. There is a concept of depth in both pictures. In real life, we express depth with 3 dimensions, but in the picture, the pixel values ​​​​are between 0-255 and these express depth.

### How do we apply 2D and 3D Gaussian Filters?
For this first look at the formula of the Gaussian Filter.

The Gaussian filter can be expressed as:

\[ G(x, y) = \frac{1}{2 \pi \sigma^2} e^{-\frac{x^2 + y^2}{2 \sigma^2}} \]

Here,
- \( G(x, y) \): Value of the Gaussian filter at position (x, y),
- \( \sigma \): Standard deviation parameter,
- \( x \) and \( y \): Coordinates considered as distances from the center of the filter.

**Are we gonna use this formula?**
No :)
We are just gonna use the Convolution between matrices.

We can represent these Gauss formulas using kernels. Gaussian formulas are also 3D graphs, and you can turn these 3D graphs into 2D kernels to use in convolution. 
Here is the reperesentation of turning Gauss graph into 2d kernel. If we look at the Gaussian Graph from above, we see the picture on the right. 

![1_PaZx8eCc7bWaERP6eP5JjA](https://github.com/busraakara/Gaussian-Filter/assets/105877486/91a93e51-7b7d-436c-8e16-d1c7c8524c8b)



Gaussian filters are primarily used for:
- **Noise Reduction:** They effectively reduce noise and graininess in images by averaging pixel values.
- **Blur Effect:** They create a blur effect which can be used for artistic purposes or to prepare images for further processing.
- **Scale Space Representation:** They are fundamental in scale-space theory for representing images at different scales.

## Differences between 2D Gauss Filter and 3D Gauss Filter

### 2D Gaussian Filter:
- **Application:** Used for processing 2D images, such as photographs or frames of videos.
- **Kernel Shape:** Uses a 2D Gaussian distribution for convolution.
- **Output:** Produces a smoothed 2D image where each pixel is a weighted average of its neighbors based on Gaussian weights.

### 3D Gaussian Filter:
- **Application:** Primarily used in processing 3D volumetric data, such as medical imaging (CT scans, MRI).
- **Kernel Shape:** Uses a 3D Gaussian distribution for convolution, considering neighboring voxels.
- **Output:** Smoothes volumetric data, reducing noise and providing a blurred representation in the 3D space.

In summary, while both filters operate on the principle of Gaussian distribution and convolution, the main difference lies in their application domains (2D images vs. 3D volumes) and the dimensionality of their convolution kernels.


# Gaussian-Filter
Implementation of Gaussian Blur Filter on Images

## What is Gaussian Filter?
A Gaussian filter, in the context of image processing and signal processing, is a type of linear filter used to blur images or reduce noise by averaging out the intensity values of pixels. It is named after the Gaussian function (bell curve) that defines its shape.

Here are some key characteristics and uses of a Gaussian filter:

1. **Smoothing Effect**: Gaussian filters are primarily used for smoothing images. They achieve this by applying a convolution operation with a Gaussian kernel, which gives more weight to the central pixels (near the filter's center) and less weight to pixels farther away, following the Gaussian distribution.

2. **Noise Reduction**: By averaging the pixel values in a neighborhood around each pixel, Gaussian filters effectively reduce high-frequency noise in images. High-frequency noise often appears as small, rapid changes in intensity, which can be smoothed out by the filter.

3. **Kernel Size**: The size of the Gaussian kernel determines the extent of the smoothing effect. A larger kernel will blur the image more, while a smaller kernel will provide less smoothing.

4. **Mathematical Formulation**: The Gaussian kernel \( G(x, y, \sigma) \) is defined as:
   \[ G(x, y, \sigma) = \frac{1}{2\pi \sigma^2} e^{-\frac{x^2 + y^2}{2\sigma^2}} \]
   Here, \( \sigma \) controls the standard deviation of the Gaussian distribution, determining the spread or width of the filter.

5. **Application**: Gaussian filters are used in various applications including image processing (e.g., edge detection after smoothing), computer vision (e.g., feature extraction), and noise reduction in signals.

6. **Properties**: They are linear, shift-invariant filters, which means they preserve the overall shape and structure of the image while reducing noise and details.

In summary, a Gaussian filter is a versatile tool for image enhancement and noise reduction, leveraging the smooth, symmetric properties of the Gaussian function to achieve effective results in various applications.

## What is the difference between 2D Gauss Filter and 3D Gauss Filter?

The difference between a 2D Gaussian filter and a 3D Gaussian filter lies primarily in their dimensions and application domains:

1. **Dimensions**:
   - **2D Gaussian Filter**: Operates on 2-dimensional images where each pixel has two spatial dimensions (typically x and y coordinates). The filter is applied across these two dimensions to smooth or blur the image.
   
   - **3D Gaussian Filter**: Operates on 3-dimensional data where each voxel (volume pixel) has three spatial dimensions (x, y, and z coordinates). This is commonly used in volumetric data such as medical imaging (CT scans, MRI) or video processing where each frame has depth information.

2. **Kernel Shape**:
   - **2D Gaussian Kernel**: The kernel is a 2D matrix defined by the Gaussian function \( G(x, y, \sigma) \):
     \[ G(x, y, \sigma) = \frac{1}{2\pi \sigma^2} e^{-\frac{x^2 + y^2}{2\sigma^2}} \]
     This kernel is applied to each pixel neighborhood in the x and y directions of the image.

   - **3D Gaussian Kernel**: The kernel is a 3D volume defined similarly, extending into the z direction:
     \[ G(x, y, z, \sigma) = \frac{1}{(2\pi \sigma^2)^{3/2}} e^{-\frac{x^2 + y^2 + z^2}{2\sigma^2}} \]
     Here, \( x, y, z \) are the spatial coordinates in the 3D space. The filter is applied across three spatial dimensions, smoothing in all directions.

3. **Application**:
   - **2D Gaussian Filter**: Used primarily for image processing tasks on 2D images, such as blurring, noise reduction, edge detection (often after smoothing), and feature extraction in computer vision.
   
   - **3D Gaussian Filter**: Applied to 3D data like volumetric images (medical scans, 3D reconstructions from multiple viewpoints), video sequences where depth is considered, or any data that extends into three spatial dimensions. It is used for similar purposes as the 2D version but in 3D space.

4. **Implementation**:
   - Both filters are implemented similarly using convolution operations, where the Gaussian kernel is convolved with the image or volumetric data to achieve the desired smoothing or blurring effect.

In summary, the key difference between 2D and 3D Gaussian filters is the number of spatial dimensions they operate on: 2D for images and 3D for volumetric data. They both leverage the Gaussian function to apply smoothing or blurring effects, tailored to their respective dimensional contexts.

