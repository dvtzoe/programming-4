import cv2

img = cv2.imread(r"/home/dvtzoe/Pictures/Wallpapers/inaiinaiisonshou_phone.png")

if img is not None:
    img = cv2.resize(img, (600, 600))

    cv2.rectangle(img, (0, 0), (100, 100), (255, 0, 0), 5)

    print(img.shape)  # pyright: ignore[reportAny]

    cv2.imshow("test open picture", img)

    cv2.imwrite("output_ex08.png", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
