import cv2
import numpy as np

# Create blank black images (306x300)
rectangle = np.zeros((300, 300), dtype="uint8")
circle = np.zeros((300, 300), dtype="uint8")
# Draw filled rectangle (white)
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)
# Draw filled circle (white)
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)
# Bitwise AND -> pixels white in BOTH images
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwise_and)
# Bitwise OR -> pixels white in EITHER image
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwise_or)
# Bitwise XOR -> pixels white in one image BUT NOT both
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwise_xor)
# Bitwise NOT -> invert black/white of the rectangle
bitwise_not = cv2.bitwise_not(rectangle)
cv2.imshow("NOT", bitwise_not)

cv2.waitKey(0)
cv2.destroyAllWindows()
