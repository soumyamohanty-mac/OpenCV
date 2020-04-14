import  cv2

image_classifier = cv2.CascadeClassifier("/Users/soumyaranjanmohanty/Desktop/AIDocs/OpenCV/haarcascade_frontalface_default.xml")
eyeCascade= cv2.CascadeClassifier('/Users/soumyaranjanmohanty/Desktop/AIDocs/OpenCV/haarcascade_eye.xml')
img = cv2.imread("/Users/soumyaranjanmohanty/Desktop/Soumya/DSC_0062.jpg")

resized_image = cv2.resize(img,(700,700))

gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

faces = image_classifier.detectMultiScale(gray_image, 1.1,3)
print(type(faces))
print(faces)

for x,y,w,h in faces:
    cv2.rectangle(resized_image,(x,y),(x+w,y+h),(0,0,255),3)
    roi = resized_image[y:y + h, x:x + w]

    eyes = eyeCascade.detectMultiScale(roi)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi, (ex, ey), (ex + ew, ey + eh), 255, 2)


cv2.imshow("window",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
0