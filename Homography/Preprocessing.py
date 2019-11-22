import cv2
import numpy as np

MAX_FEATURES = 1000
GOOD_MATCH_PERCENTAGE = 0.20

#calculates and applies homography
def alignImages(image, reference):
	#get grayscale
	imgG = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	refG = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)

	#apply ORB for features and descriptors
	orb = cv2.ORB_create(MAX_FEATURES)
	imgKeyPoints, imgDescriptors = orb.detectAndCompute(imgG, None)
	refKeyPoints, refDescriptors = orb.detectAndCompute(refG, None)

	#match features from image to reference
	matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
	matches = matcher.match(imgDescriptors, refDescriptors, None)

	#sort matches by score for filtering
	matches.sort(key=lambda x: x.distance, reverse=False)
	goodMatcheTotal = int(len(matches) * GOOD_MATCH_PERCENTAGE)
	matches = matches[:goodMatcheTotal]

	#draw top matches of reference points
	topMatches = cv2.drawMatches(image, imgKeyPoints, reference, refKeyPoints, matches, None)
	cv2.imwrite("matches.jpg", topMatches)

	#Gather coords for best matches
	imgPoints = np.zeros((len(matches), 2), dtype = np.float32)
	refPoints = np.zeros((len(matches), 2), dtype = np.float32)

	for i, match in enumerate(matches):
		imgPoints[i, :] = imgKeyPoints[match.queryIdx].pt
		refPoints[i, :] = refKeyPoints[match.trainIdx].pt

	#calculate homography
	homography, mask = cv2.findHomography(imgPoints, refPoints, cv2.RANSAC)

	#apply homography
	height, width, channels = image.shape

	#frame = np.float32([[0,0], [0,height], [width,height], [width, 0]]).reshape(-1,1,2)
	#result = cv2.perspectiveTransform(frame, homography)

	result = cv2.warpPerspective(image, homography, (width, height))


	return result, homography

#calls align images, crops result, returns resulting image
def getAlignedImage(image, reference):
	#align image
	result, homography = alignImages(image, reference)

	#gather width, height of resulting shape
	height, width, channels = reference.shape
	
	#get contours
	imgG = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(src = imgG, ksize = (5,5), sigmaX = 0)
	t, binary = cv2.threshold(src = blur,thresh = 127, maxval = 255, type = cv2.THRESH_BINARY)
	_image, contours, _hierarchy = cv2.findContours(image = binary, mode = cv2.RETR_EXTERNAL, method = cv2.CHAIN_APPROX_SIMPLE)

	#Get biggest contour by area(should be the paper)
	areas = []
	for c in contours:
		areas.append(cv2.contourArea(c))

	sortedAreas = sorted(zip(areas, contours), key = lambda x: x[0], reverse = True)
	biggestContour = sortedAreas[0][1] #0 = largest area, 1 = contour

	#update bounding rectangles
	cornerMinX = 0
	cornerMinY = 0
	
	#find bounded rect for cropping boundaries
	x, y, w, h = cv2.boundingRect(biggestContour)
	cornerMinX = x
	cornerMinY = y

	print("x: ", x, "; y: ", y)

	#crop the image
	crop = result[cornerMinY:cornerMinY+height, cornerMinX:cornerMinX+width]

	return crop


if __name__ == '__main__':

	#load reference image
	refFilename = "template.jpg"
	reference = cv2.imread(refFilename, cv2.IMREAD_COLOR)

	#load new image
	imgFilename = "newForm.jpg"
	image = cv2.imread(imgFilename, cv2.IMREAD_COLOR)

	#call function to get result and homography
	result = getAlignedImage(image, reference)

	#save output
	outputFilename = "Aligned.jpg"
	cv2.imwrite(outputFilename, result)

	print("Done :)\n")