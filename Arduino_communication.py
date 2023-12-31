# #use pyserial to communicate with arduino UNO
import serial
import time
#replace L with Q , dk why list is not comparing the alphabet L only , other alphabets work just fine.


# all fundamental movement of the robot : each of this is a defined function in the arduino environment

def transition(solution,i): #take in previous step in solution list to determine clockwise or anticlockwise turn
    global disengage
    global engage
    global rotate
    global arotate
    global orientation
    global arduino_command
    if i == 0:
        if solution[i] == ("Q" or "Q'"):
            arduino_command.append(rotate)
            arduino_command.append(rotate)
            arduino_command.append(engage)
            orientation = "Q"
        if solution[i] == ("Q'"):
            arduino_command.append(rotate)
            arduino_command.append(rotate)
            arduino_command.append(engage)
            orientation = "Q"
        if solution[i] == ("U'"):
            arduino_command.append(rotate)
            arduino_command.append(engage)
            orientation = "U"
        if solution[i] == ("U'"):
            arduino_command.append(rotate)
            arduino_command.append(engage)
            orientation = "U"
        if solution[i] == ("D'"):
            arduino_command.append(arotate)
            arduino_command.append(engage)
            orientation = "D"
        if solution[i] == ("D'"):
            arduino_command.append(arotate)
            arduino_command.append(engage)
            orientation = "D"
        if solution[i] == ("R"):
            arduino_command.append(engage)
        if solution[i] == ("R'"):
            arduino_command.append(engage)
        if solution[i] == ("B'"):
            arduino_command.append(engage)
        if solution[i] == ("B'"):
            arduino_command.append(engage)
        if solution[i] == ("F"):
            arduino_command.append(engage)
        if solution[i] == ("F'"):
            arduino_command.append(engage)

    else:
        if ((orientation == ("U" or "U'") ) and (solution[i] == ("R" or "R'"))):
            if solution[i] == ("R" or "R'"):
                arduino_command.append(disengage)
                arduino_command.append(arotate)
                arduino_command.append(engage)
                orientation = "R"
            else:
                arduino_command.append(disengage)
                arduino_command.append(rotate)
                arduino_command.append(engage)
                orientation = "Q"
        if ((orientation == ("U" or "U'")) and (solution[i] == ("Q" or "Q'"))):
            print('heelo')
            arduino_command.append(disengage)
            arduino_command.append(arotate)
            arduino_command.append(engage)
            orientation = "Q"
        if ((orientation == ("U" or "U'")) and (solution[i] == ("D" or "D'"))):
            arduino_command.append(disengage)
            arduino_command.append(rotate)
            arduino_command.append(rotate)
            arduino_command.append(engage)
            orientation = "D"
        if ((orientation == ("R" or "R'")) and (solution[i] == ("U" or "U'" or "D" or "D'"))):
            if solution[i] == ("U" or "U'"):
                arduino_command.append(disengage)
                arduino_command.append(rotate)
                arduino_command.append(engage)
                orientation = "U"
            else:
                arduino_command.append(disengage)
                arduino_command.append(arotate)
                arduino_command.append(engage)
                orientation = "D"
        if ((orientation == ("R" or "R'")) and (solution[i] == ("Q" or "Q'"))):
            arduino_command.append(disengage)
            arduino_command.append(rotate)
            arduino_command.append(rotate)
            arduino_command.append(engage)
            orientation = "Q"
        if((orientation == ("D" or "D'")) and (solution[i] == ("R" or "R'"))):
            print('heelo')
            if solution[i] == ("Q" or "Q'"):
                arduino_command.append(disengage)
                arduino_command.append(arotate)
                arduino_command.append(engage)
                orientation = "Q"
            else:
                print('heelo')
                arduino_command.append(disengage)
                arduino_command.append(rotate)
                arduino_command.append(engage)
                orientation = "R"
        # created a seperate logic for Q because there is also error where the code cant detect Q and update orientation Q
        if ((orientation == ("D" or "D'")) and (solution[i] == ("Q" or "Q'"))):
            print('heelo')
            arduino_command.append(disengage)
            arduino_command.append(arotate)
            arduino_command.append(engage)
            orientation = "Q"
        if ((orientation == ("D" or "D'")) and (solution[i] == ("U" or "U'"))):
            arduino_command.append(disengage)
            arduino_command.append(rotate)
            arduino_command.append(rotate)
            arduino_command.append(engage)
            orientation = "U"
        if ((orientation == ("Q" or "Q'")) and (solution[i] == ("U" or "U'" or "D" or "D'"))):
            if solution[i] == ("U" or "U'"):
                arduino_command.append(disengage)
                arduino_command.append(arotate)
                arduino_command.append(engage)
                orientation = "U"
            else:
                arduino_command.append(disengage)
                arduino_command.append(rotate)
                arduino_command.append(engage)
                orientation = "D"
        if ((orientation == ("Q" or "Q'")) and (solution[i] == ("R" or "R'"))):
            arduino_command.append(disengage)
            arduino_command.append(rotate)
            arduino_command.append(rotate)
            arduino_command.append(engage)
            orientation = "R"

# write  the sequence of function as a list

def arduino_converter(solution):

    global arduino_command
    print(solution)
    # initial engage
    for i in range(len(solution)):  #can to for i in len() because we want to call the next step
        #print(arduino_command)
        transition(solution, i)
        #print(i)
        #print ('orientation is '+orientation)
        #print(arduino_command)
        if i == 0:
            if solution[i] == 'F':
                arduino_command.append(front)
            if solution[i] == "F'":
                arduino_command.append(afront)
            if solution[i] == 'B':
                arduino_command.append(back)
            if solution[i] == "B'":
                arduino_command.append(aback)
            if solution[i] == "R":
                arduino_command.append(sv1)
            if solution[i] == "R'":
                arduino_command.append(asv1)
            if solution[i] == "U":
                arduino_command.append(sv1)
            if solution[i] == "U'":
                arduino_command.append(asv1)
            if solution[i] == "Q":
                arduino_command.append(sv1)
            if solution[i] == "Q'":
                arduino_command.append(asv1)
            if solution[i] == "D":
                arduino_command.append(sv1)
            if solution[i] == "D'":
                arduino_command.append(asv1)
        else:
            if solution[i] == 'F':
                arduino_command.append(front)
            if solution[i] == "F'":
                arduino_command.append(afront)
            if solution[i] == 'B':
                arduino_command.append(back)
            if solution[i] == "B'":
                arduino_command.append(aback)
            if solution[i] == "R":
                arduino_command.append(sv1)
            if solution[i] == "R'":
                arduino_command.append(asv1)
            if solution[i] == "U":
                arduino_command.append(sv1)
            if solution[i] == "U'":
                arduino_command.append(asv1)
            if solution[i] == "Q":
                arduino_command.append(sv1)
            if solution[i] == "Q'":
                arduino_command.append(asv1)
            if solution[i] == "D":
                arduino_command.append(sv1)
            if solution[i] == "D'":
                arduino_command.append(asv1)


# solve rotation on first rotation
def write_read(arduino, x):
    arduino.write(bytes(x, 'utf-8'))
    print(f"wrote {x}")
    time.sleep(1)
    print('reading ...')
    data = arduino.readline().decode("utf-8")
    print(f'read {data}')
    return data


def arduino_com(solutions, arduino):

    global arduino_command
    global orientation
    global front 
    global afront
    global back
    global aback
    global disengage
    global engage
    global rotate
    global arotate
    global sv1
    global asv1 

    arduino_command = []
    orientation = "R"

    front = 'A'
    afront = 'B'
    back = 'C'
    aback = 'D'
    disengage = 'E'
    engage = 'F'
    rotate = 'G'
    arotate = 'H'
    sv1 = 'I'
    asv1 = 'J'

    solution = solutions
    print(len(solution))

    arduino_converter(solution)
    print(arduino_command)
    sent_command = '2'+  ''.join(arduino_command) + '2'
    print(sent_command)
    expected_return = list(sent_command[1:-1])
    #arduino=serial.Serial(port='COM4',baudrate=19200, timeout=1)
    #arduino = serial.Serial(port='/dev/cu.usbmodem11101', baudrate=115200, timeout=.1)
    #arduino = serial.Serial(port='/dev/cu.usbmodem11301', baudrate=19200,timeout=1) 
    while True:
        print('helo')
        data = write_read(arduino, sent_command)
        print('hey')
        data_list = list(data[:-2])
        print(data_list)
        if len(data) > 0:
            #print(data[0])
            #print(data[-3])
            if data_list == expected_return:
                print(data)
                print('done')
                break
            else: 
                print('not correct')
        else:
            print('nothing received')
            continue
    #Listen(arduino, expected_return) 

'''
front = 'A'
afront = 'B'
back = 'C'
aback = 'D'
disengage = 'E'
engage = 'F'
rotate = 'G'
arotate = 'H'
sv1 = 'I'
asv1 = 'J'

arduino_command = []
orientation = "R"
'''
