import cv2

img = cv2.imread(r"/home/dvtzoe/Pictures/Wallpapers/inaiinaiisonshou_phone.png")

if img is not None:
    b, g, r = cv2.split(img)

    cv2.imshow("Original", img)

    cv2.imshow("Blue Channel (Gray)", b)
    cv2.imshow("Green Channel (Gray)", g)
    cv2.imshow("Red Channel (Gray)", r)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
