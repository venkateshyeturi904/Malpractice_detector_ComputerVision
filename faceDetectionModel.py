import cv2
import numpy as np

print("[INFO] loading face detection model...")
net = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "res10_300x300_ssd_iter_140000.caffemodel")

cap = cv2.VideoCapture(0)
while 1:
    ret, frame = cap.read()
    if ret:
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
        net.setInput(blob)
        detections = net.forward()
        print(detections.shape)
        area=0
        startX=0
        for i in range(detections.shape[2]):
                confidence = detections[0, 0, i, 2]        # extract the confidence (i.e., probability) associated with the prediction
                if confidence<0.5:
                        continue
                print(confidence)
                try:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    text = "{:.2f}%".format(confidence * 100)+ " face"
                    (startX, startY, endX, endY) = box.astype("int")
                    face = frame[startY:endY,startX:endX]
                    face = cv2.resize(face,(200,200))
                    cv2.imshow("frame",frame)
                    cv2.rectangle(frame, (startX, startY), (endX, endY),  (0, 0, 255), 2)
                    cv2.putText(frame, text, (startX, startY-10), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                    cv2.waitKey(50)
                except:
                      print('error')