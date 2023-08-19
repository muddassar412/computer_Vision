import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions of the image
width = 8
height = 8

# Create a 2-bit image (values: 0, 1, 2, 3)
image_data = np.array([[0, 1, 2, 3, 0, 1, 2, 3],
                       [1, 2, 3, 0, 1, 2, 3, 0],
                       [2, 3, 0, 1, 2, 3, 0, 1],
                       [3, 0, 1, 2, 3, 0, 1, 2],
                       [0, 1, 2, 3, 0, 1, 2, 3],
                       [1, 2, 3, 0, 1, 2, 3, 0],
                       [2, 3, 0, 1, 2, 3, 0, 1],
                       [3, 0, 1, 2, 3, 0, 1, 2]], dtype=np.uint8)

# Display the original image
plt.figure(figsize=(6, 3))
plt.subplot(131)
plt.imshow(image_data, cmap='gray', vmin=0, vmax=3)
plt.title('Original Image')
plt.axis('off')

# Apply thresholding to create a binary image
threshold_value = 2
binary_image = (image_data >= threshold_value).astype(np.uint8) * 3

# Display the binary image
plt.subplot(132)
plt.imshow(binary_image, cmap='gray', vmin=0, vmax=3)
plt.title('Binary Image (Thresholding)')
plt.axis('off')

# Invert the binary image
inverted_image = 3 - binary_image

# Display the inverted image
plt.subplot(133)
plt.imshow(inverted_image, cmap='gray', vmin=0, vmax=3)
plt.title('Inverted Image')
plt.axis('off')

plt.tight_layout()
plt.show()
