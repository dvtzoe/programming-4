import cv2

img = cv2.imread(r"/home/dvtzoe/Pictures/Wallpapers/inaiinaiisonshou_phone.png")

if img is not None:
    resized_img = cv2.resize(img, (256, 144))
    cv2.imshow("Image", resized_img)
    _ = cv2.waitKey(0)
    cv2.destroyAllWindows()
