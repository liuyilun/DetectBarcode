# import the necessary packages
from pyimagesearch import simple_barcode_detection
import argparse
import cv2

camera = cv2.VideoCapture(0);
#camera = cv2.VideoCapture("video1.mov")

# keep looping over the frames
while True:
	# grab the current frame
	(grabbed, frame) = camera.read()

	# check to see if we have reached the end of the
	# video
	if not grabbed:
		break


	# detect the barcode in the image
	box = simple_barcode_detection.detect(frame)

	# if a barcode was found, draw a bounding box on the frame
	cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)

	# show the frame and record if the user presses a key
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(30)

	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
