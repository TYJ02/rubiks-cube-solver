import math
import numpy as np
import cv2 as cv


'''
top_view() is for the camera looking from top down on the cube
1. actually i am planning to move both the cameras to the bottom.
!!! top camera is only at 20 degrees not 45 degrees
'''



def top_view(radius, center):
    ver_t = [center, center - radius]
    ver_tl = [center - radius*math.sin(math.pi/3), center - radius*math.cos(math.pi/3)]
    ver_bl = [center - radius*math.sin(math.pi/3), center + radius*math.cos(math.pi/3)*0.9]
    ver_b = [center, center + radius]
    ver_br = [center + radius*math.sin(math.pi/3)*0.9, center + radius*math.cos(math.pi/3)*0.9]
    ver_tr = [center + radius*math.sin(math.pi/3), center - radius*math.cos(math.pi/3)]
    pts = np.array([ver_t, ver_tl, ver_bl, ver_b, ver_br, ver_tr], np.int32)
    pts = pts.reshape((-1, 1, 2))
    vertex_coor = pts.ravel()
    return pts, vertex_coor


def bottom_view(radius ,center):
    ver_t = [center, center - radius*0.9]
    ver_tl = [center - radius*math.sin(math.pi/3)*0.8, center - radius*math.cos(math.pi/3)*0.9]
    ver_bl = [center - radius*math.sin(math.pi/3)*0.8, center + radius*math.cos(math.pi/3)*0.8]
    ver_b = [center, center + radius*0.5]
    ver_br = [center + radius*math.sin(math.pi/3)*0.8, center + radius*math.cos(math.pi/3)*0.8]
    ver_tr = [center + radius*math.sin(math.pi/3)*0.7, center - radius*math.cos(math.pi/3)*0.9]
    pts = np.array([ver_t, ver_tl, ver_bl, ver_b, ver_br, ver_tr], np.int32)
    pts = pts.reshape((-1, 1, 2))
    vertex_coor = pts.ravel()
    return pts, vertex_coor


def bottom_view1(radius, center):
    ver_t = [center, 300 - radius*0.9]
    ver_tl = [center - radius*math.sin(math.pi/3)*0.8, center - radius*math.cos(math.pi/3)*0.9]
    ver_bl = [center - radius*math.sin(math.pi/3), center + radius*math.cos(math.pi/3)]
    ver_b = [center, center + radius]
    ver_br = [center + radius*math.sin(math.pi/3), center + radius*math.cos(math.pi/3)]
    ver_tr = [center + radius*math.sin(math.pi/3)*0.8, center - radius*math.cos(math.pi/3)*0.9]
    pts = np.array([ver_t, ver_tl, ver_bl, ver_b, ver_br, ver_tr], np.int32)
    pts = pts.reshape((-1, 1, 2))
    vertex_coor = pts.ravel()
    return pts, vertex_coor


def top_view_test(radius, center):
    ver_t = [center, center - radius]
    ver_tl = [center - radius*math.sin(math.pi/3)*1.1, center - radius*math.cos(math.pi/3)*1.1]
    ver_bl = [center - radius*math.sin(math.pi/3), center + radius*math.cos(math.pi/3)*0.9]
    ver_b = [center, center + radius*1.1]
    ver_br = [center + radius*math.sin(math.pi/3)*0.9, center + radius*math.cos(math.pi/3)*0.9]
    ver_tr = [center + radius*math.sin(math.pi/3), center - radius*math.cos(math.pi/3)*1.1]
    pts = np.array([ver_t, ver_tl, ver_bl, ver_b, ver_br, ver_tr], np.int32)
    pts = pts.reshape((-1, 1, 2))
    vertex_coor = pts.ravel()
    return pts, vertex_coor


def bottom_inter():
    ver_t = [230,93]
    ver_tl = [168,183]
    ver_bl = [158,314]
    ver_b = [233,379]
    ver_br = [304,315]
    ver_tr = [297,181]
    center = [225,228]
    pts = np.array([ver_t, ver_tl, ver_bl, ver_b, ver_br, ver_tr, center], np.int32)
    pts = pts.reshape((-1, 1, 2))
    vertex_coor = pts.ravel()
    return pts, vertex_coor


def top_inter():
    ver_t = [238,112]
    ver_tl = [164,189]
    ver_bl = [176,329]
    ver_b = [247,423]
    ver_br = [313,320]
    ver_tr = [322,179]
    center = [245,280]
    pts = np.array([ver_t, ver_tl, ver_bl, ver_b, ver_br, ver_tr, center], np.int32)
    pts = pts.reshape((-1, 1, 2))
    vertex_coor = pts.ravel()
    return pts, vertex_coor


def cursor_coor(event, x, y, flags, param):
    if event ==cv.EVENT_LBUTTONDBLCLK:
        print(f"({x},{y})")


def main():
    while True: 
        top_image = cv.imread("D:/Pictures/Camera Roll/bottom.jpg")
        top_image = cv.resize(top_image, (500,500))
        cv.namedWindow("top view")
        cv.setMouseCallback("top view", cursor_coor)
        cv.circle(top_image, (250, 250), 1 , (0, 0, 255), 10)
        pts_top, vertex_top = top_view(150, 250)
        cv.polylines(top_image, [pts_top], True, (0, 255, 0))
        cv.imshow("top view", top_image)
        if cv.waitKey(20) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()
