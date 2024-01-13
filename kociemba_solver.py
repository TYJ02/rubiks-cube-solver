import kociemba

def steps_converter(raw_solution):
    setup_D = ["R","L","F2","B2","R'","L'"]
    set = str.split(raw_solution)
    for step in set:
        if step == "U":
            i = set.index(step)
            set = set[:i] + setup_D + ["D"] + setup_D +set[i+1:]
        if step == "U2":
            i = set.index(step)
            set = set[:i] + setup_D + ["D2"] + setup_D +set[i+1:]
        if step == "U'":
            i = set.index(step)
            set = set[:i] + setup_D + ["D'"] + setup_D +set[i+1:]
        if step == "U'2":
            i = set.index(step)
            set = set[:i] + setup_D + ["D'2"] + setup_D +set[i+1:]

    return set

def arduino_command(set):
    print("done")
    arduino_string = ""
    for step in set:
        if step == "F":
            arduino_string += "A"
        if step == "F2":
            arduino_string += "B"
        if step == "F'":
            arduino_string += "C"
        if step == "F'2":
            arduino_string += "D"
        if step == "R":
            arduino_string += "E"
        if step == "R2":
            arduino_string += "F"
        if step == "R'":
            arduino_string += "G"
        if step == "R'2":
            arduino_string += "H"
        if step == "B":
            arduino_string += "I"
        if step == "B2":
            arduino_string += "J"
        if step == "B'":
            arduino_string += "K"
        if step == "B'2":
            arduino_string += "L"
        if step == "L":
            arduino_string += "M"
        if step == "L2":
            arduino_string += "N"
        if step == "L'":
            arduino_string += "O"
        if step == "L'2":
            arduino_string += "P"
        if step == "D":
            arduino_string += "Q"
        if step == "D2":
            arduino_string += "R"
        if step == "D'":
            arduino_string += "S"
        if step == "D'2":
            arduino_string += "T"
    return arduino_string
    

solution = "R2 D U F"
set = steps_converter(solution)
print(set)
string = arduino_command(set)
print(string)
