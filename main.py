import cv2

# Load the image
image = cv2.imread("Ayesha.png")

# Convert the image to grayscale
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
invert = cv2.bitwise_not(gray_img)

# Apply Gaussian blur
blur = cv2.GaussianBlur(invert, (21, 21), 0)

# Invert the blurred image
inverted_blur = cv2.bitwise_not(blur)

# Create the pencil sketch
sketch = cv2.divide(gray_img, inverted_blur, scale=256.0)

# Save the sketch
cv2.imwrite("Sketch.png", sketch)
