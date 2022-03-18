# Python-Project-> Vehicle number plate detector and Toll calculator
In this project we fetch images or video from our camera and with the help of haar-cascade calssifier  and OpenCV  in python, we spot the number plate in the image 
and then with the help of easyOCR we extract the characters and numbers of our number plate. After extracting the characters we impose toll on the vehicle 
on the basis of the state, i.e the first two characters of number plate represents the code for state in india by which we can know that from which
state our vehicle is and then according to that we can decide the amount of toll to be imposed on vehicle.
In this project we also keeps a log of scanned plates by saving the picture of number plates.


// Tecnical terms -

1. haar-cascade calssifier =   Our Classifier which is used here for detecting number plate.
2. OpenCV =   Python module with the help of which we can work on images and video and manipulate them.
3. easyOCR =  Python Module which is used for Optical charcter recognition.In simple words it will recognize the characters from a image.
