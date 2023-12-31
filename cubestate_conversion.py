import copy

import numpy as np


# from cube_reconigtion import detect_cube
# import kociemba

def cvt2kociemba(cubestate):
    try:
        cubestring = ''
        for i in range(6):
            for j in range(3):
                for k in range(3):
                    cubestring = cubestring + cubestate[i][j][k]
            #print(cubestring)
    except TypeError:
        pass

    cubestring = cubestring.replace('B', 'U')
    cubestring = cubestring.replace('W', 'F')
    cubestring = cubestring.replace('G', 'D')
    cubestring = cubestring.replace('O', 'L')
    cubestring = cubestring.replace('Y', 'B')

    return cubestring


def cvt2env(cubestate):
    global cube
    cube = np.array(np.zeros(54)).reshape(6, 3, 3)
    corner_comb = [['B', 'O', 'W'], ['B', 'R', 'W'], ['G', 'O', 'W'], ['G', 'R', 'W'], ['B', 'R', 'Y'], ['B', 'O', 'Y'],
                   ['G', 'R', 'Y'], ['G', 'O', 'Y']]
    color_index = [[6, 38, 9], [8, 18, 11], [45, 44, 15], [47, 24, 17], [2, 20, 27], [0, 36, 29], [53, 26, 33],
                   [51, 42, 35]]

    if cubestate[0][1][1] == 'B':
        cube[0][1][1] = 4
    if cubestate[1][1][1] == 'W':
        cube[1][1][1] = 13
    if cubestate[2][1][1] == 'R':
        cube[2][1][1] = 22
    if cubestate[3][1][1] == 'Y':
        cube[3][1][1] = 31
    if cubestate[4][1][1] == 'O':
        cube[4][1][1] = 40
    if cubestate[5][1][1] == 'G':
        cube[5][1][1] = 49
    cucbe100 = [cubestate[0][2][0], cubestate[1][0][0], cubestate[4][0][2]]
    if cube100.sort() == None:
        print('no sorting needed')
    else:
        cube100 = cube100.sort()
    print(cube100)
    if cube100 in corner_comb:
        index = corner_comb.index(cube100)
        cur_corner = corner_comb[index]
        cur_color_index = color_index[index]
        cube[1][0][0] = cur_color_index[cur_corner.index(cubestate[1][0][0])]
        cube[0][2][0] = cur_color_index[cur_corner.index(cubestate[0][2][0])]
        cube[4][0][2] = cur_color_index[cur_corner.index(cubestate[4][0][2])]

    cube102 = [cubestate[0][2][2], cubestate[1][0][2], cubestate[2][0][0]]
    if cube102.sort() == None:
        print('no sorting needed')
    else:
        cube102 = cube102.sort()
    print(cube102)
    if cube102 in corner_comb:
        index = corner_comb.index(cube102)
        cur_corner = corner_comb[index]
        cur_color_index = color_index[index]
        cube[0][2][2] = cur_color_index[cur_corner.index(cubestate[0][2][2])]
        cube[1][0][2] = cur_color_index[cur_corner.index(cubestate[1][0][2])]
        cube[2][0][0] = cur_color_index[cur_corner.index(cubestate[2][0][0])]

    cube120 = [cubestate[1][2][0], cubestate[4][2][2], cubestate[5][0][0]]
    if cube120.sort() == None:
        print('no sorting needed')
    else:
        cube120 = cube120.sort()
    print(cube120)
    if cube120 in corner_comb:
        index = corner_comb.index(cube120)
        cur_corner = corner_comb[index]
        cur_color_index = color_index[index]
        cube[1][2][0] = cur_color_index[cur_corner.index(cubestate[1][2][0])]
        cube[4][2][2] = cur_color_index[cur_corner.index(cubestate[4][2][2])]
        cube[5][0][0] = cur_color_index[cur_corner.index(cubestate[5][0][0])]

    cube122 = [cubestate[1][2][2], cubestate[2][2][0], cubestate[5][0][2]]
    if cube122.sort() == None:
        print('no sorting needed')
    else:
        cube122 = cube122.sort()
    print(cube122)
    if cube122 in corner_comb:
        index = corner_comb.index(cube122)
        cur_corner = corner_comb[index]
        cur_color_index = color_index[index]
        cube[1][2][2] = cur_color_index[cur_corner.index(cubestate[1][2][2])]
        cube[2][2][0] = cur_color_index[cur_corner.index(cubestate[2][2][0])]
        cube[5][0][2] = cur_color_index[cur_corner.index(cubestate[5][0][2])]

    cube300 = [cubestate[0][0][2], cubestate[2][0][2], cubestate[3][0][0]]
    if cube300.sort() == None:
        print('no sorting needed')
    else:
        cube300 = cube300.sort()
    print(cube300)
    if cube300 in corner_comb:
        index = corner_comb.index(cube300)
        cur_corner = corner_comb[index]
        cur_color_index = color_index[index]
        cube[0][0][2] = cur_color_index[cur_corner.index(cubestate[0][0][2])]
        cube[2][0][2] = cur_color_index[cur_corner.index(cubestate[2][0][2])]
        cube[3][0][0] = cur_color_index[cur_corner.index(cubestate[3][0][0])]

    cube302 = [cubestate[0][0][0], cubestate[4][0][0], cubestate[3][0][2]]
    if cube302.sort() == None:
        print('no sorting needed')
    else:
        cube302 = cube302.sort()
    print(cube302)
    if cube302 in corner_comb:
        index = corner_comb.index(cube302)
        cur_corner = corner_comb[index]
        cur_color_index = color_index[index]
        cube[0][0][0] = cur_color_index[cur_corner.index(cubestate[0][0][0])]
        cube[4][0][0] = cur_color_index[cur_corner.index(cubestate[4][0][0])]
        cube[3][0][2] = cur_color_index[cur_corner.index(cubestate[3][0][2])]
    cube320 = [cubestate[2][2][2], cubestate[3][2][0], cubestate[5][2][2]]
    if cube320.sort() == None:
        print('no sorting needed')
    else:
        cube320 = cube320.sort()
    if cube320 in corner_comb:
        index = corner_comb.index(cube320)
        cur_corner = corner_comb[index]
        cur_color_index = color_index[index]
        cube[2][2][2] = cur_color_index[cur_corner.index(cubestate[2][2][2])]
        cube[3][2][0] = cur_color_index[cur_corner.index(cubestate[3][2][0])]
        cube[5][2][2] = cur_color_index[cur_corner.index(cubestate[5][2][2])]

    cube322 = [cubestate[3][2][2], cubestate[4][2][0], cubestate[5][2][0]]
    if cube322.sort() == None:
        print('no sorting needed')
    else:
        cube322 = cube322.sort()
    print(cube322)
    if cube322 in corner_comb:
        index = corner_comb.index(cube322)
        cur_corner = corner_comb[index]
        cur_color_index = color_index[index]
        cube[3][2][2] = cur_color_index[cur_corner.index(cubestate[3][2][2])]
        cube[4][2][0] = cur_color_index[cur_corner.index(cubestate[4][2][0])]
        cube[5][2][0] = cur_color_index[cur_corner.index(cubestate[5][2][0])]

    edge_comb = [['B', 'Y'], ['B', 'R'], ['B', 'W'], ['B', 'O'], ['O', 'W'], ['O', 'Y'], ['R', 'Y'], ['R', 'W'],
                 ['G', 'W'], ['G', 'O'], ['G', 'Y'], ['G', 'R']]
    colore_index = [[1, 28], [5, 19], [7, 10], [3, 37], [41, 12], [39, 32], [23, 30], [21, 14], [46, 16], [48, 43],
                    [52, 34], [50, 25]]

    edge001 = [cubestate[0][0][1], cubestate[3][0][1]]
    if edge001.sort() == None:
        print('no sorting needed')
    else:
        edge001 = edge001.sort()
    print(edge001)
    if edge001 in edge_comb:
        index = edge_comb.index(edge001)
        cur_edge = edge_comb[index]
        cur_colore_index = colore_index[index]
        cube[0][0][1] = cur_colore_index[cur_edge.index(cubestate[0][0][1])]
        cube[3][0][1] = cur_colore_index[cur_edge.index(cubestate[3][0][1])]

    edge010 = [cubestate[0][1][0], cubestate[4][0][1]]
    if edge010.sort() == None:
        print('no sorting needed')
    else:
        edge010 = edge010.sort()
    print(edge010)
    if edge010 in edge_comb:
        index = edge_comb.index(edge010)
        cur_edge = edge_comb[index]
        cur_colore_index = colore_index[index]
        cube[0][1][0] = cur_colore_index[cur_edge.index(cubestate[0][1][0])]
        cube[4][0][1] = cur_colore_index[cur_edge.index(cubestate[4][0][1])]

    edge021 = [cubestate[0][2][1], cubestate[1][0][1]]
    if edge021.sort() == None:
        print('no sorting needed')
    else:
        edge021 = edge021.sort()
    print(edge021)
    if edge021 in edge_comb:
        index = edge_comb.index(edge021)
        cur_edge = edge_comb[index]
        cur_colore_index = colore_index[index]
        cube[0][2][1] = cur_colore_index[cur_edge.index(cubestate[0][2][1])]
        cube[1][0][1] = cur_colore_index[cur_edge.index(cubestate[1][0][1])]

    edge012 = [cubestate[0][1][2], cubestate[2][0][1]]
    if edge012.sort() == None:
        print('no sorting needed')
    else:
        edge012 = edge012.sort()
    print(edge012)
    if edge012 in edge_comb:
        index = edge_comb.index(edge012)
        cur_edge = edge_comb[index]
        cur_colore_index = colore_index[index]
        cube[0][1][2] = cur_colore_index[cur_edge.index(cubestate[0][1][2])]
        cube[2][0][1] = cur_colore_index[cur_edge.index(cubestate[2][0][1])]

    edge110 = [cubestate[1][1][0], cubestate[4][1][2]]
    if edge110.sort() == None:
        print('no sorting needed')
    else:
        edge110 = edge110.sort()
    print(edge110)
    if edge110 in edge_comb:
        index = edge_comb.index(edge110)
        cur_edge = edge_comb[index]
        cur_colore_index = colore_index[index]
        cube[1][1][0] = cur_colore_index[cur_edge.index(cubestate[1][1][0])]
        cube[4][1][2] = cur_colore_index[cur_edge.index(cubestate[4][1][2])]

    edge312 = [cubestate[3][1][2], cubestate[4][1][0]]
    if edge312.sort() == None:
        print('no sorting needed')
    else:
        edge312 = edge312.sort()
    print(edge312)
    if edge312 in edge_comb:
        index = edge_comb.index(edge312)
        cur_edge = edge_comb[index]
        cur_colore_index = colore_index[index]
        cube[3][1][2] = cur_colore_index[cur_edge.index(cubestate[3][1][2])]
        cube[4][1][0] = cur_colore_index[cur_edge.index(cubestate[4][1][0])]

    edge310 = [cubestate[3][1][0], cubestate[2][1][2]]
    if edge310.sort() == None:
        print('no sorting needed')
    else:
        edge310 = edge310.sort()
    print(edge310)
    if edge310 in edge_comb:
        index = edge_comb.index(edge310)
        cur_edge = edge_comb[index]
        cur_colore_index = colore_index[index]
        cube[3][1][0] = cur_colore_index[cur_edge.index(cubestate[3][1][0])]
        cube[2][1][2] = cur_colore_index[cur_edge.index(cubestate[2][1][2])]

    edge112 = [cubestate[1][1][2], cubestate[2][1][0]]
    if edge112.sort() == None:
        print('no sorting needed')
    else:
        edge112 = edge112.sort()
    print(edge112)
    if edge112 in edge_comb:
        index = edge_comb.index(edge112)
        cur_edge = edge_comb[index]
        cur_colore_index = colore_index[index]
        cube[1][1][2] = cur_colore_index[cur_edge.index(cubestate[1][1][2])]
        cube[2][1][0] = cur_colore_index[cur_edge.index(cubestate[2][1][0])]

    edge121 = [cubestate[1][2][1], cubestate[5][0][1]]
    if edge121.sort() == None:
        print('no sorting needed')
    else:
        edge121 = edge121.sort()
    print(edge121)
    if edge121 in edge_comb:
        index = edge_comb.index(edge121)
        cur_edge = edge_comb[index]
        cur_colore_index = colore_index[index]
        cube[1][2][1] = cur_colore_index[cur_edge.index(cubestate[1][2][1])]
        cube[5][0][1] = cur_colore_index[cur_edge.index(cubestate[5][0][1])]

    edge421 = [cubestate[4][2][1], cubestate[5][1][0]]
    if edge421.sort() == None:
        print('no sorting needed')
    else:
        edge421 = edge421.sort()
    print(edge421)
    if edge421 in edge_comb:
        index = edge_comb.index(edge421)
        cur_edge = edge_comb[index]
        cur_colore_index = colore_index[index]
        cube[4][2][1] = cur_colore_index[cur_edge.index(cubestate[4][2][1])]
        cube[5][1][0] = cur_colore_index[cur_edge.index(cubestate[5][1][0])]

    edge321 = [cubestate[3][2][1], cubestate[5][2][1]]
    if edge321.sort() == None:
        print('no sorting needed')
    else:
        edge321 = edge321.sort()
        print(edge321)
    if edge321 in edge_comb:
        index = edge_comb.index(edge321)
        cur_edge = edge_comb[index]
        cur_colore_index = colore_index[index]
        cube[3][2][1] = cur_colore_index[cur_edge.index(cubestate[3][2][1])]
        cube[5][2][1] = cur_colore_index[cur_edge.index(cubestate[5][2][1])]

    edge221 = [cubestate[2][2][1], cubestate[5][1][2]]
    if edge221.sort() == None:
        print('no sorting needed')
    else:
        edge221 = edge221.sort()
    print(edge221)
    if edge221 in edge_comb:
        index = edge_comb.index(edge221)
        cur_edge = edge_comb[index]
        cur_colore_index = colore_index[index]
        cube[2][2][1] = cur_colore_index[cur_edge.index(cubestate[2][2][1])]
        cube[5][1][2] = cur_colore_index[cur_edge.index(cubestate[5][1][2])]
    return copy.deepcopy(cube)


'''
cube_state = []

for i in range(6):
    cube_state.append(0)

cube_face = []

for i in range(3):
    cube_face.append([])
    for j in range(3):
        cube_face[i].append(0)

def main():
    cube_state = detect_cube()
    
    print(cube)
    return cube 


#cube = main()
#print(kociemba.solve(cube))
cube = np.array(np.zeros(54)).reshape(6,3,3)
cube_test= [[['B','B','B'],['B','B','B'],['B','B','B']],[['W','W','W'],['W','W','W'],['W','W','W']],[['R','R','R'],['R','R','R'],['R','R','R']],[['Y','Y','Y'],['Y','Y','Y'],['Y','Y','Y']],[['O','O','O'],['O','O','O'],['O','O','O']],[['G','G','G'],['G','G','G'],['G','G','G']]]
cvt2env(cube_test)'''
cubestate = [[['O', 'W', 'G'], ['G', 'R', 'R'], ['O', 'Y', 'G']],
[['W', 'R', 'R'], ['O', 'B', 'W'], ['B', 'G', 'W']],
[['G', 'G', 'Y'], ['O', 'W', 'Y'], ['O', 'G', 'W']],
[['R', 'B', 'Y'], ['B', 'Y', 'O'], ['R', 'R', 'B']],
[['B', 'B', 'Y'], ['R', 'G', 'Y'], ['G', 'O', 'W']],
[['B', 'W', 'O'], ['Y', 'O', 'B'], ['R', 'W', 'Y']]]
cube_state=[[['R', 'W', 'W'], ['R', 'B', 'G'], ['W', 'O', 'B']],
[['G', 'G', 'Y'], ['O', 'W', 'Y'], ['O', 'G', 'W']],
[['O', 'W', 'G'], ['G', 'R', 'R'], ['O', 'Y', 'G']],
[['R', 'B', 'Y'], ['B', 'Y', 'O'], ['R', 'R', 'B']],
[['B', 'W', 'O'], ['Y', 'O', 'B'], ['R', 'W', 'Y']],
[['B', 'B', 'Y'], ['R', 'G', 'Y'], ['G', 'O', 'W']]]
#cvt2kociemba(cube_state)
