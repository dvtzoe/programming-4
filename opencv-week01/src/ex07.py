import cv2

img = cv2.imread(r"/home/dvtzoe/Pictures/Wallpapers/inaiinaiisonshou_phone.png")

if img is not None:
    cv2.rectangle(img, (50, 50), (300, 300), (0, 0, 255), 3)

    cv2.circle(img, (200, 500), 80, (255, 0, 0), 3)

    cv2.line(img, (100, 700), (500, 900), (0, 255, 0), 4)

    cv2.putText(
        img,
        "<racial-slur>",
        (50, 450),
        cv2.FONT_HERSHEY_SIMPLEX,
        2,
        (255, 255, 255),
    )

    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
