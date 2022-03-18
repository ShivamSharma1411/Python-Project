import cv2
import cv2.cv2
import easyocr

#################################################
frameWidth = 640
frameHeight = 480
plateCascade = cv2.CascadeClassifier("Resources/PlateDetector.xml")
minArea = 1000
nearCities=["CG", "JH", "HR", "MP", "BR", "DL", "UK", "UA"]
modCities=["PB", "HP", "JK", "LA", "GJ", "MH", "WB", "OR", "OD", "SK"]
#################################################
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count1=0
count2=0
bill=0
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            imgcrop = img[y:y + h, x:x + w]
            cv2.imshow("Crop Image", imgcrop)




    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('s'):

        render = easyocr.Reader(["en"])
        result = render.readtext(imgcrop)
        text = result[0][-2]
        if(text[0]=='U' or text[1]=='P'):
            bill=0
            message="""Local Vehicle, No Toll Imposed and plate number saved"""
            cv2.imwrite("Resources/recordWithoutToll/NoPlate_" + str(count1) + ".jpg", imgcrop)
        else:
            message="""Not a Local Vehicle, Toll Imposed and plate number saved"""
            cv2.imwrite("Resources/recordWithToll/NoPlate_" + str(count2) + ".jpg", imgcrop)

            for city in nearCities:
                if city in text:
                    bill=1000
            for city in modCities:
                if city in text:
                    bill=2000
                else:
                    if(bill!=1000):
                        bill=3000
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, message, (150, 265), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 0, 255), 2)
        cv2.imshow("Result",img)
        cv2.waitKey(2000)
        print(bill)
