import numpy as np 
import cv2

cascade = cv2.CascadeClassifier('cascade.xml')

img = cv2.imread('orange.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
oranges = cascade.detectMultiScale(gray, 1.05, 15, 0, (150,150))
for (x,y,w,h) in oranges:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
imgs = cv2.resize(img, (img.shape[1] / 5, img.shape[0] / 5))
cv2.imshow('img',imgs)
cv2.waitKey(0)
cv2.destroyAllWindows()

# # show image thats being collected

# $ for filename in Positives/*.jpg; 
# $ do opencv_createsamples -img ${filename} -bg negatives.txt -num 25 -bgcolor 255 -w 60 -h 60 -vec output${filename}.vec -maxzangle 0.5 -maxyangle 0.3 -maxxangle 0.3; 
# $ done

# $ opencv_traincascade -data Classifier -vec allvecs.vec -bg negatives.txt -numNeg 1000 -numPos 3000 -numStages 11 -h 60 -w 60 -minHitRate 0.99 -maxFalseAlarmRate 0.5 -featureType HAAR -precalcValBufSize 2048 -precalcIdxBufSize 2048
