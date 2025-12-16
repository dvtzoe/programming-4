import cv2

img = cv2.imread(r"/home/dvtzoe/Pictures/Wallpapers/inaiinaiisonshou_phone.png")

if img is not None:
    grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Image", grayscaled_img)
    _ = cv2.waitKey(0)
    cv2.destroyAllWindows()
