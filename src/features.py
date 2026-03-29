import cv2
orb = cv2.ORB_create()
def extract_features(frame):
    kp,des = orb.detectAndCompute(frame,None)
    return kp
