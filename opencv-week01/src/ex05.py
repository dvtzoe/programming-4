import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"/home/dvtzoe/Pictures/Wallpapers/inaiinaiisonshou_phone.png")

if img is not None:
    cv2.imshow("Image", img)

    plt.imshow(img)  # pyright: ignore[reportUnknownMemberType]
    plt.show()
