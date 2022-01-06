import cv2
qr, _, _=cv2.QRCodeDetector().detectAndDecode(cv2.imread('qr.jpg'))
print(f"The decoded text is : {qr}")