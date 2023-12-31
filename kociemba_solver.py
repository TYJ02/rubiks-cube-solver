from vision import capture_cube 
from cubestate_conversion import cvt2kociemba
import kociemba


def kociemba_solve():
    global solution
    cube = cvt2kociemba(cube_state)
    solution = str(kociemba.solve(cube))
    print(kociemba.solve(cube))
    #solution1 = steps_converter(solution)
    #print(solution1)
    #display(solution1)
    return solution

def steps_converter(raw_solution):
    set = str.split(raw_solution)
    for step in set:
        if step == "F2":
            i =set.index(step)
            set = set[:i] + ["F", "F"] + set[i+1:]
        if step == "U2":
            i =set.index(step)
            set = set[:i] + ["U", "U"] + set[i+1:]
        if step == "R2":
            i =set.index(step)
            set = set[:i] + ["R", "R"] + set[i+1:]
        if step == "Q2":
            i =set.index(step)
            set = set[:i] + ["Q", "Q"] + set[i+1:]
        if step == "D2":
            i = set.index(step)
            set = set[:i] + ["D", "D"] + set[i + 1:]
        if step == "B2":
            i = set.index(step)
            set = set[:i] + ["B", "B"] + set[i + 1:]
        if step == "F'2":
            i =set.index(step)
            set = set[:i] + ["F'", "F'"] + set[i+1:]
        if step == "U'2":
            i =set.index(step)
            set = set[:i] + ["U'", "U'"] + set[i+1:]
        if step == "R'2":
            i =set.index(step)
            set = set[:i] + ["R'", "R'"] + set[i+1:]
        if step == "Q'2":
            i =set.index(step)
            set = set[:i] + ["Q'", "Q'"] + set[i+1:]
        if step == "D'2":
            i = set.index(step)
            set = set[:i] + ["D'", "D'"] + set[i + 1:]
        if step == "B'2":
            i = set.index(step)
            set = set[:i] + ["B'", "B'"] + set[i + 1:]
        #print(set)
    return set

def Kociemba_solver():
    global solution
    global cube_state
    while True:
        try:
            global solution
            cube_state = capture_cube()
            #cube_state = [
            #[['Y', 'W', 'G'], ['R', 'B', 'G'], ['R', 'W', 'R']], 
            #[['W', 'O', 'G'], ['B', 'W', 'B'], ['W', 'Y', 'R']],
            #[['Y', 'W', 'O'], ['Y', 'R', 'O'], ['G', 'W', 'G']],
            #[['Y', 'R', 'B'], ['B', 'Y', 'Y'], ['O', 'Y', 'Y']],
            #[['R', 'G', 'B'], ['G', 'O', 'R'], ['B', 'O', 'B']],
            #[['O', 'O', 'W'], ['G', 'G', 'B'], ['O', 'R', 'W']]]
            cube = cvt2kociemba(cube_state)
            solution = str(kociemba.solve(cube))
            print(solution)
            solution = solution.replace('L', 'Q')
            set = steps_converter(solution)
            #print(set)

            print('done')
            break
            
        except ValueError:
            print('hey')
            continue
        
    return set

