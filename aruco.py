import cv2
import numpy as np
import cv2.aruco as aruco
import os

def loadAugImages(path):
    myList = os.listdir(path)
    augDict= {}
    for imgPath in myList:
        key = int(os.path.splitext(imgPath)[0])
        imgAug = cv2.imread(f'{path}/{imgPath}')
        augDict[key] = imgAug
    return augDict

def findArucoMarkers(img, markerSize=6, totalMarkers=250,draw=True):
    imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejected = aruco.detectMarkers(imgGray, arucoDict, parameters=arucoParam)
    #print(ids)
    if draw:
        aruco.drawDetectedMarkers(img, bboxs)
        
    return [bboxs, ids]
    
 
def augmentAruco(bbox, idi, img, imgAug, drawId=True):
    tl = bbox[0][0][0], bbox[0][0][1]  #topleft
    tr = bbox[0][1][0], bbox[0][1][1]  #topright
    br = bbox[0][2][0], bbox[0][2][1]  #bottomright
    bl = bbox[0][3][0], bbox[0][3][1]  #bottomleft
    
    h, w, c = imgAug.shape
    
    pts1 = np.array([tl,tr,br,bl])
    pts2 = np.float32([[0,0],[w,0],[w,h],[0,h]])
    matrix, _ = cv2.findHomography(pts2, pts1)
    imgOut = cv2.warpPerspective(imgAug, matrix, (img.shape[1], img.shape[0]))
    cv2.fillConvexPoly(img, pts1.astype(int), (0,0,0))
    imgOut = img + imgOut
    
    return imgOut
    

def main():
    cap = cv2.VideoCapture()
    address = "https://192.168.0.103:8080/video"
    cap.open(address)
    #imgAug = cv2.imread('photos/23.jpg')
    augDict = loadAugImages('photos')
    while True:
        success, img = cap.read()
        arucoFound = findArucoMarkers(img)
        if len(arucoFound[0]) != 0:
            for bbox, idi in zip(arucoFound[0], arucoFound[1]):
                if int(idi) in augDict.keys():
                    img = augmentAruco(bbox, idi, img, augDict[int(idi)])
                
                
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == '__main__':
    main()
