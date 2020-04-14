import  cv2, time



'''
video = cv2.VideoCapture(0)
check, frame = video.read()
time.sleep(5)

cv2.imshow('video',frame)


cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()

'''
image_classifier = cv2.CascadeClassifier("/Users/soumyaranjanmohanty/Desktop/AIDocs/OpenCV/haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)
a = 1

while True:
    a = a+1
    chek, frame = video.read()
    gray_image = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
    faces = image_classifier.detectMultiScale(gray_image, 1.1, 3)
    for x, y, w, h in faces:
        cv2.rectangle(gray_image, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imshow("video",gray_image)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break



video.read()
cv2.destroyAllWindows()