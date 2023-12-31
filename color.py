import cv2 as cv
import numpy as np



def match_colour(imgvar, imgshow, lower_bound, upper_bound, colour):

    global coordinate
    coordinate = []
    masked_img = imgvar.copy()
    colour_lower = lower_bound
    colour_upper = upper_bound
    frameHSV = cv.cvtColor(masked_img, cv.COLOR_BGR2HSV)
    colour_mask = cv.inRange(frameHSV, colour_lower, colour_upper)
    sumofpixels = 0
    dominant_color  = (0,0)
    nonzero_pixel_coor = cv.findNonZero(colour_mask)
    #print(nonzero_pixel_coor)
    if not nonzero_pixel_coor is None:
        nonzero_pixel_coor  = nonzero_pixel_coor.tolist()
        for coors in nonzero_pixel_coor:
            for i in range(3):
                if 70+((i)*500)/3< coors[0][0] < -70+((i+1)*500)/3 :
                    for j in range(3):
                        if 70 + ((j)*500)/3 < coors[0][1] < -70 + ((j+1)*500)/3 :
                            cv.rectangle(imgshow,(coors[0][0],coors[0][1]),(coors[0][0]+10, coors[0][1]+10),(0,255,255),1)
                            sumofpixels += 1
                            #print(sumofpixels)
                    
                        if sumofpixels > 600:
                            cv.putText(imgshow, colour, (int(50+((i)*500)/3),int(50 + ((j)*500)/3)), cv.FONT_HERSHEY_DUPLEX, 1, (125, 246, 55), 3)
                            coordinate.append([j,i])
                            #print(coordinate)
                            sumofpixels = 0
                            break
    return coordinate



