import cv2 as cv
import numpy as np
import serial

def capture_cube():
    img_counter = 1
    expected_return = "capture"
    capture = cv.VideoCapture(0)
    while True:
        #cv.imshow( "webcam feed", capvar)
        serial_msg = read_serial(arduino)
        print(f"serial msg is {serial_msg}")
        if serial_msg == expected_return:
            isTrue, capvar = capture.read()
            img_name = "./picture_{}.png".format(img_counter)
            print(img_name)
            cv.imwrite(img_name, capvar)
            img_counter +=1
        key = cv.waitKey(20)
        if key == 27: # exit on ESC
            break

def read_serial(arduino):
    data = arduino.readline().decode("utf-8").strip()
    print(f'read {data}')
    return data

