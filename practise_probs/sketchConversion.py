import cv2
import numpy as np
import random

# Load the image
image = cv2.imread('images.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted_gray = cv2.bitwise_not(gray_image)

# Blur the inverted grayscale image
blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)

# Invert the blurred image
inverted_blurred = cv2.bitwise_not(blurred)

# Create the sketch image by dividing the grayscale image by the inverted blurred image
sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

# Introduce randomness and imperfections
height, width = sketch.shape
for y in range(height):
    for x in range(width):
        if random.random() < 0.0:  # Adjust the probability as needed
            sketch[y, x] = 255 - sketch[y, x]  # Invert the pixel value

# Introduce line thickness variations
line_thickness = np.random.randint(1, 4, size=sketch.shape, dtype=np.uint8)
varied_sketch = cv2.bitwise_and(sketch, sketch, mask=line_thickness)

# Add texture overlays
texture = cv2.imread('images.jpg', cv2.IMREAD_GRAYSCALE)
texture = cv2.resize(texture, (width, height))
final_sketch = cv2.bitwise_and(varied_sketch, texture)

# Adjust gamma to introduce varying shades of gray
gamma = random.uniform(0.6, 1.2)
table = np.array([((i / 255.0) ** gamma) * 255 for i in range(256)]).astype('uint8')
final_sketch = cv2.LUT(final_sketch, table)

# Resize the final sketch image if needed
# final_sketch = cv2.resize(final_sketch, (800, 600))

# Display the final sketch image
cv2.imshow('Final Sketch', final_sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the final sketch image if needed
cv2.imwrite('images.jpg', final_sketch)