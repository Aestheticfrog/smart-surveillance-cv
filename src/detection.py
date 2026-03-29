import cv2
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
def detect_people(frame):
    boxes,_ = hog.detectMultiScale(frame,winStride=(8, 8))
    return boxes
