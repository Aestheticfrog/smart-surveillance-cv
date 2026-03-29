import cv2
import argparse
from preprocessing import preprocess
from motion import frame_diff, optical_flow
from detection import detect_people
from features import extract_features
from tracking import Tracker
#CLI
parser = argparse.ArgumentParser()
parser.add_argument("--input",required=True, help="Input video path")
parser.add_argument("--output",default="output.mp4")
args = parser.parse_args()
#Video
cap = cv2.VideoCapture(args.input)
ret, frame1 = cap.read()
if not ret:
    print("Error reading video")
    exit()
tracker = Tracker()
# Video Writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(args.output, fourcc,20,(int(cap.get(3)), int(cap.get(4))))
prev_gray, prev_blur = preprocess(frame1)
# MAIN LOOP
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    gray, blur = preprocess(frame)
    # Motion Detection
    motion_mask = frame_diff(prev_blur, blur)
    # Optical Flow
    flow_mask = optical_flow(prev_gray, gray)
    frame[flow_mask] = [0, 0, 255]
    # Contours
    contours, _ = cv2.findContours(motion_mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    boxes = []
    for cnt in contours:
        if cv2.contourArea(cnt) < 1000:
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        boxes.append((x,y,w,h))
        cv2.rectangle(frame,(x, y),(x+w, y+h),(0,255,0),2)
    # Person Detection
    people = detect_people(frame)
    for (x, y, w, h) in people:
        cv2.rectangle(frame,(x, y),(x+w, y+h),(255, 0, 0),2)
    # Tracking
    objects = tracker.update(boxes)
    for obj_id, (cx, cy) in objects.items():
        cv2.putText(frame,f"ID {obj_id}",(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0, 255, 255),2)
    # Feature Extraction
    kp = extract_features(gray)
    frame = cv2.drawKeypoints(frame,kp,None,color=(0,255,255))
    # Show
    cv2.imshow("Final Output", frame)
    cv2.imshow("Motion Mask", motion_mask)
    # Save
    out.write(frame)
    prev_gray = gray
    prev_blur = blur
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
