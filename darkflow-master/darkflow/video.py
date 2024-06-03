import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import winsound

options = {
    'model': 'cfg/yolov2-tiny.cfg',
    'load': 'bin/yolov2-tiny_3000.weights',
    'labels': 'bin/labels.txt',
    'threshold': 0.3,
    'gpu': 0.5
}

tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

def play_alert_sound():
    winsound.Beep(1000, 1000)

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    stime = time.time()
    ret, frame = capture.read()
    if ret:
        results = tfnet.return_predict(frame)
        helmet_detected = False
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence = result['confidence']
            text = '{}: {:.0f}%'.format(label, confidence * 100)
            frame = cv2.rectangle(frame, tl, br, color, 5)
            frame = cv2.putText(frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            if label == 'Helmet':
                helmet_detected = True
        
        cv2.imshow('frame', frame)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))

        if not helmet_detected:
            play_alert_sound()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
