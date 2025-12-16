import cv2

img = cv2.imread(r"/home/dvtzoe/Pictures/Wallpapers/inaiinaiisonshou_phone.png")

if img is not None:
    print(img.shape)  # pyright: ignore[reportAny]
    print(img.ndim)
    print(img)
    cv2.imshow("Image", img)
    _ = cv2.waitKey(0)
    cv2.destroyAllWindows()
