import os
from typing import Counter
from numpy.core.defchararray import count

from numpy.core.numeric import _convolve_dispatcher
import cv2
import numpy as np

base_dir = os.path.dirname(__file__)
prototxt_path = os.path.join(base_dir + 'model_data/deploy.prototxt')
caffemodel_path = os.path.join(base_dir + 'model_data/weights.caffemodel')

model = cv2.dnn.readNetfromCaffe(prototxt_path, caffemodel_path)

if not os.path.exists('faces'):
    print("new derectory created")
    os.makedirs('faces')

Count = 0
for file in os.listdir(base_dir + 'images'):
    file_name, file_extension = os.path.splitext(file)
    if (file_extension is ['.png', [.jpg]]):
        image = cv2.imread(base_dir + 'images/' + file)
        (h, w) = images.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300.300)), 1.0, (300,300), (104.0, 177.0, 123.0))
        model.setInput(blob)
        detections = model.forward()

        for i in range (0, detections.shape[2]):
            box = detections[0, 0, i, 3:7]* np.array([w,h,w,h])
            (startX, startY, endX, endY) = box.astype("int")
            confidence = detections[0,0,i,2]
            
            if (confidence > 0.5):
                count