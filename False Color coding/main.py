import cv2
import numpy as np

# Load the RGB image (replace with your image path)
image_path = "F:/CyberHub/Neural Network/False Color coding/image.jpg"
image = cv2.imread(image_path)

# Create a copy of the image
fcc_image = image.copy()

# Enhance green channel to highlight vegetation
fcc_image[:, :, 2] = fcc_image[:, :, 2] * 4 #Increasing the green channel intensity

#fcc_image[:, :, 0] = fcc_image[:, :, 1] * 3 #Increasing the green channel intensit#y
#fcc_image[:, :, 1] = fcc_image[:, :, 1] * 0 #Increasing the green channel intensity

# Display the original and FCC images
cv2.imshow("Original RGB Image", image)
cv2.imshow("FCC with Highlighted Vegetation", fcc_image)

cv2.waitKey(0)
cv2.destroyAllWindows()