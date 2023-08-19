# Generate a 2-bit image
# apply basic image processing operations 
## thresholding 
## inversion 
## visualize 
### importing libraries
``` python
import numpy as np
import matplotlib.pyplot as plt 
```

These lines import the necessary libraries: numpy for numerical operations and array handling, and matplotlib.pyplot for plotting images and graphs.
### image dimensions
``` python
width = 8
height = 8
```
Here, we define the dimensions of the image. In this case, the image is 8x8 pixels.
### 2D numpy array 
``` python
image_data = np.array([[0, 1, 2, 3, 0, 1, 2, 3],
                       [1, 2, 3, 0, 1, 2, 3, 0],
                       [2, 3, 0, 1, 2, 3, 0, 1],
                       [3, 0, 1, 2, 3, 0, 1, 2],
                       [0, 1, 2, 3, 0, 1, 2, 3],
                       [1, 2, 3, 0, 1, 2, 3, 0],
                       [2, 3, 0, 1, 2, 3, 0, 1],
                       [3, 0, 1, 2, 3, 0, 1, 2]], dtype=np.uint8)

```
This creates a 2D NumPy array image_data representing the 2-bit image. Each element of the array corresponds to a pixel value in the image. The values range from 0 to 3, representing the different intensity levels.
### displaying the image
``` python
plt.figure(figsize=(6, 3))
```
This sets up a figure for displaying the images. The figsize parameter specifies the dimensions of the figure in inches (width, height).
### displays the original image using Matplotlib
``` python
plt.subplot(131)
plt.imshow(image_data, cmap='gray', vmin=0, vmax=3)
plt.title('Original Image')
plt.axis('off')
```
This code displays the original image using Matplotlib. The subplot function creates a subplot layout with 1 row and 3 columns, and the number 131 indicates that we're working with the first subplot. imshow is used to display the image with the specified colormap (gray) and intensity range (vmin and vmax). We set the title of the subplot using title and turn off axis labels and ticks using axis('off').
### Threshold
``` python
threshold_value = 2
binary_image = (image_data >= threshold_value).astype(np.uint8) * 3
```
Here, we set a threshold value of 2. The line (image_data >= threshold_value) creates a binary mask where True corresponds to pixels with intensity greater than or equal to the threshold. The astype(np.uint8) converts the boolean mask to a binary image of type uint8. Finally, we multiply the binary image by 3 to map True to the maximum intensity value (3) and False to the minimum intensity value (0).
### thresholded binary image
``` python
plt.subplot(132)
plt.imshow(binary_image, cmap='gray', vmin=0, vmax=3)
plt.title('Binary Image (Thresholding)')
plt.axis('off')
```
This code displays the thresholded binary image using the same approach as before.
### generates an inverted binary image
``` python
inverted_image = 3 - binary_image
```
This line generates an inverted binary image by subtracting the binary image from the maximum intensity value (3). This effectively swaps the intensities: areas that were white (intensity 3) become black (intensity 0), and vice versa.
### displays the inverted binary image
``` python
plt.subplot(133)
plt.imshow(inverted_image, cmap='gray', vmin=0, vmax=3)
plt.title('Inverted Image')
plt.axis('off')
```
This code displays the inverted binary image.
### entire figure with the three subplots
``` python
plt.tight_layout()
plt.show()
```
Finally, tight_layout() ensures that the subplots are nicely arranged within the figure, and show() displays the entire figure with the three subplots.

