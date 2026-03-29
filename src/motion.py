import cv2
import numpy as np
def frame_diff(prev, curr):
    diff = cv2.absdiff(prev, curr)
    x , thresh = cv2.threshold(diff,25,255,cv2.THRESH_BINARY)
    thresh = cv2.dilate(thresh, None, iterations=2)
    return thresh
def optical_flow(prev, curr):
    flow = cv2.calcOpticalFlowFarneback(prev,curr,None,0.5, 3, 15, 3, 5, 1.2, 0)
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    mask = mag > 2
    return mask
