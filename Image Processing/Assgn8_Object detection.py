import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/stop.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Use a pre-trained Haar Cascade (e.g., frontal face cascade)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
found = face_cascade.detectMultiScale(img_gray, minSize=(20, 20))

amount_found = len(found)
if amount_found != 0:
    for (x, y, width, height) in found:
        cv2.rectangle(img_rgb, (x, y), (x + width, y + height), (0, 255, 0), 5)

plt.imshow(img_rgb)
plt.show()