# vision.py

# objective: uses 2 webcam to detect colors of 6 faces simultaneously using isometric view

# domain knowledge needed about Rubik's cube
# my cube : U-blue F-W R-red B-yellow L-orange D-green

# we are represent the cube as a 6x3x3 array
# face 1 [ [[],[],[]],
#          [[],[],[]],
#          [[],[],[]]  ]

# python library needed - opencv, numpy

# structure of the programme
# match_'color'() functions - matches color of each cubelet

# index of vertices of our hexagon cube (starting from the top vertice and rotate anti- clockwise)
# approx.ravel() = [n[0],n[1], ... ,n[10],n[11]]


import time
import cv2 as cv
import numpy as np
import math
from color import match_colour
from hexagon_outline import top_inter, bottom_inter


green_lower = np.array([50, 100, 50])
green_upper = np.array([80, 255, 255])
blue_lower = np.array([90, 100, 50])
blue_upper = np.array([125, 255, 255])
red_lower = np.array([0, 100, 50])
red_upper = np.array([9, 255, 255])
orange_lower = np.array([13, 100, 50])
orange_upper = np.array([26, 255, 255])
yellow_lower = np.array([30, 50, 30])
yellow_upper = np.array([40, 255, 255])

lower_bounds = [green_lower, blue_lower, red_lower, orange_lower, yellow_lower]
upper_bounds = [green_upper, blue_upper, red_upper, orange_upper, yellow_upper]
colour = ['G', 'B', 'R', 'O', 'Y']


def update_face_state(coordinate, color):
    global cube_face
    if color != 'W':
        for coor in coordinate:
            cube_face[coor[0]][coor[1]] = color
    else:
        for i in range(3):
            for j in range(3):
                if cube_face[i][j] == 0 :
                    cube_face[i][j] = 'W'


def update_cube_state(cube_face):
    if cube_face[1][1] == "W":
        cube_state[2] = cube_face
        print(cube_state[2])
    if cube_face[1][1] == "B":
        cube_state[0] = cube_face
        print(cube_state[0])
    if cube_face[1][1] == "R":
        cube_state[1] = cube_face
        print(cube_state[1])
    if cube_face[1][1] == "Y":
        cube_state[5] = cube_face
        print(cube_state[5])
    if cube_face[1][1] == "O":
        cube_state[4] = cube_face
        print(cube_state[4])
    if cube_face[1][1] == "G":
        cube_state[3] = cube_face
        print(cube_state[3])


def detect_hex_top(imgContours, vertex_coor):
    global cube_face

    # right face
    pt1 = np.float32([[vertex_coor[12], vertex_coor[13]], [vertex_coor[10],vertex_coor[11]], [vertex_coor[6], vertex_coor[7]], [vertex_coor[8],vertex_coor[9]]])
    # Size of the Transformed Image
    pts2 = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])
    M = cv.getPerspectiveTransform(pt1, pts2)
    dst1 = cv.warpPerspective(imgContours, M, (500, 500))
    dst11 = dst1.copy()
    #cv.imshow('right face', dst1)
    for (lower, upper, colour_text) in zip(lower_bounds, upper_bounds, colour):
        coordinate = match_colour(dst1, dst11, lower, upper, colour_text)
        update_face_state(coordinate, colour_text)
    update_face_state(coordinate, "W")
    cube_face[1][1] = "R"
    update_cube_state(cube_face)
    #cv.imshow('color match of right face', dst11)
    cv.imwrite(r"./picture/cubeface1.jpg",dst11)

    cube_face = []
    for i in range(3):
        cube_face.append([])
        for j in range(3):
            cube_face[i].append(0)


    # top face
    pt3 = np.float32([[vertex_coor[0],vertex_coor[1]], [vertex_coor[10], vertex_coor[11]],[vertex_coor[2],vertex_coor[3]], [vertex_coor[12], vertex_coor[13]]])
    # Size of the Transformed Image
    pts4 = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])
    M = cv.getPerspectiveTransform(pt3, pts4)
    dst2 = cv.warpPerspective(imgContours, M, (500, 500))
    dst22 = dst2.copy()
    #cv.imshow('top face', dst22)
    for (lower, upper, colour_text) in zip(lower_bounds, upper_bounds, colour):
        coordinate = match_colour(dst2, dst22, lower, upper, colour_text)
        update_face_state(coordinate, colour_text)
    update_face_state(coordinate, "W")
    cube_face[1][1] = "B"
    update_cube_state(cube_face)
    #cv.imshow('color match of top face', dst22)
    cv.imwrite(r"./picture/cubeface0.jpg",dst22)
    cube_face = []
    for i in range(3):
        cube_face.append([])
        for j in range(3):
            cube_face[i].append(0)

    # left face (W)
    pt5 = np.float32([[vertex_coor[2],vertex_coor[3]], [vertex_coor[12], vertex_coor[13]], [vertex_coor[4], vertex_coor[5]], [vertex_coor[6], vertex_coor[7]]])
    # Size of the Transformed Image
    pts6 = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])
    M = cv.getPerspectiveTransform(pt5, pts6)
    dst3 = cv.warpPerspective(imgContours, M, (500, 500))
    dst33 = dst3.copy()
    #cv.imshow('left face', dst3)
    for (lower, upper, colour_text) in zip(lower_bounds, upper_bounds, colour):
        coordinate = match_colour(dst3, dst33, lower, upper, colour_text)
        update_face_state(coordinate, colour_text)
    update_face_state(coordinate, "W")
    cube_face[1][1] = "W"
    update_cube_state(cube_face)
    #cv.imshow('color match of left face', dst33)
    cv.imwrite(r"./picture/cubeface2.jpg",dst33)
    cube_face = []
    for i in range(3):
        cube_face.append([])
        for j in range(3):
            cube_face[i].append(0)


def detect_hex_bottom(imgContours, vertex_coor):
    global cube_face

    # right face (orange)
    pt1 = np.float32([[vertex_coor[0],vertex_coor[1]], [vertex_coor[10], vertex_coor[11]], [vertex_coor[12], vertex_coor[13]], [vertex_coor[8], vertex_coor[9]]])
    # Size of the Transformed Image
    pts2 = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])
    M = cv.getPerspectiveTransform(pt1, pts2)
    dst1 = cv.warpPerspective(imgContours, M, (500, 500))
    dst11 = dst1.copy()
    #cv.imshow('right face', dst1)
    for (lower, upper, colour_text) in zip(lower_bounds, upper_bounds, colour):
        coordinate = match_colour(dst1, dst11, lower, upper, colour_text)
        update_face_state(coordinate, colour_text)
    update_face_state(coordinate, "W")
    cube_face[1][1] = "O"
    update_cube_state(cube_face)
    #cv.imshow('color match of right face', dst11)
    cv.imwrite(r"./picture/cubeface4.jpg",dst11)

    cube_face = []
    for i in range(3):
        cube_face.append([])
        for j in range(3):
            cube_face[i].append(0)


    # bottom face (green)
    pt3 = np.float32([[vertex_coor[8],vertex_coor[9]], [vertex_coor[6], vertex_coor[7]], [vertex_coor[12], vertex_coor[13]], [vertex_coor[4],vertex_coor[5]]])
    # Size of the Transformed Image
    pts4 = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])
    M = cv.getPerspectiveTransform(pt3, pts4)
    dst2 = cv.warpPerspective(imgContours, M, (500, 500))
    dst22 = dst2.copy()
    #cv.imshow('top face', dst22)
    for (lower, upper, colour_text) in zip(lower_bounds, upper_bounds, colour):
        coordinate = match_colour(dst2, dst22, lower, upper, colour_text)
        update_face_state(coordinate, colour_text)
    update_face_state(coordinate, "W")
    cube_face[1][1] = "G"
    update_cube_state(cube_face)
    #cv.imshow('color match of top face', dst22)
    cv.imwrite(r"./picture/cubeface3.jpg",dst22)

    cube_face = []
    for i in range(3):
        cube_face.append([])
        for j in range(3):
            cube_face[i].append(0)

    # left face (yellow)
    pt5 = np.float32([[vertex_coor[2],vertex_coor[3]], [vertex_coor[0], vertex_coor[1]], [vertex_coor[4], vertex_coor[5]], [vertex_coor[12], vertex_coor[13]] ])
    # Size of the Transformed Image
    pts6 = np.float32([[0, 0], [500, 0], [0, 500], [500, 500]])
    M = cv.getPerspectiveTransform(pt5, pts6)
    dst3 = cv.warpPerspective(imgContours, M, (500, 500))
    dst33 = dst3.copy()
    #cv.imshow('left face', dst3)
    for (lower, upper, colour_text) in zip(lower_bounds, upper_bounds, colour):
        coordinate = match_colour(dst3, dst33, lower, upper, colour_text)
        update_face_state(coordinate, colour_text)
    update_face_state(coordinate, "W")
    cube_face[1][1] = "Y"
    update_cube_state(cube_face)
    #cv.imshow('color match of left face', dst33)
    cv.imwrite(r"./picture/cubeface5.jpg",dst33)
    cube_face = []
    for i in range(3):
        cube_face.append([])
        for j in range(3):
            cube_face[i].append(0)


def open_webcam():

    #capture_top = cv.VideoCapture(0)
    capvar_top = cv.imread("./picture/top.jpg")
    #capture_top.set(cv.CAP_PROP_FRAME_WIDTH, 300)
    #capture_top.set(cv.CAP_PROP_FRAME_HEIGHT, 300)
    capvar_bottom = cv.imread("./picture/bottom.jpg")
    #capture_bottom = cv.VideoCapture(1)
    #capture_bottom.set(cv.CAP_PROP_FRAME_WIDTH, 300)
    #capture_bottom.set(cv.CAP_PROP_FRAME_HEIGHT, 300)
    while True:
        #isTrue, capvar_top = capture_top.read()
        #cv.rectangle(capvar,(100,100),(450,450),(0,255,0),2)
        capvar_top = cv.resize(capvar_top, (500,500))
        pts_top, vertex_top = top_inter()
        cv.polylines(capvar_top, [pts_top], True, (0, 255, 0))
        #cv.imshow('top webcam', capvar_top)
        
        #isTrue, capvar_bottom = capture_bottom.read()
        #cv.rectangle(capvar,(100,100),(450,450),(0,255,0),2)
        capvar_bottom = cv.resize(capvar_bottom, (500, 500))
        pts_bottom, vertex_bottom = bottom_inter()
        cv.polylines(capvar_bottom, [pts_bottom], True, (0, 255, 0))
        cv.imshow('bottom webcam', capvar_bottom)
        detect_hex_top(capvar_top, vertex_top)
        detect_hex_bottom(capvar_bottom, vertex_bottom)
        break


def capture_cube():
    global cube_state
    global cube_face
    global cube_faceshow
    global coordinate
    cube_state = []

    # create a virtual cube with 3 dimensional arrays
    for i in range(6):
        cube_state.append(0)

    cube_face = []

    for i in range(3):
        cube_face.append([])
        for j in range(3):
            cube_face[i].append(0)

    open_webcam()
    print(cube_state)
    return cube_state


if __name__ ==  "__main__":
    capture_cube()
