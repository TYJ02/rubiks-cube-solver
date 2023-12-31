import kociemba
import tkinter as tk
import numpy as np
from kociemba_solver import cvt2kociemba, steps_converter
from Arduino_communication import arduino_com
from vision import capture_cube
from PIL import Image, ImageTk
import serial
import os

class App:
    def __init__(self, master):

        self.width = 60  # width of a facelet in pixels
        self.facelet_id = [[[0 for col in range(3)] for row in range(3)] for face in range(6)]
        self.colorpick_id = [0 for i in range(6)]
        self.curcol = None
        self.t = ("U", "R", "F", "D", "L", "B")
        self.color = ("B", "R", "W", "G", "O", "Y")
        self.cols = ("blue", "red", "white", "green", "orange", "yellow")
        self.cubestring = ""

        self.master = master
        self.master.geometry("800x800")

        # Create a NumPy array
        self.array = np.zeros((6, 3, 3))

        # Create a Tkinter canvas to display the array
        self.canvas = tk.Canvas(master, width = 18*self.width + 20 * 10*6, height= 9*self.width + 20)
        self.canvas.pack()


        #self.display = tk.Text(height=7, width=39)
        #self.text_window = self.canvas.create_window(10 + 6.5 * self.width, 10 + .5 * self.width, anchor=tk.NW, window=self.display)

        # Draw the array on the canvas
        self.create_facelet_rect(self.width)
        self.create_colorpicker_rect(self.width)
        self.text = tk.Text(width = 50, height = 5, font=("Arial",20))
        #self.text['state'] = "disabled"
        self.display = self.canvas.create_window(12*self.width, 8*self.width, window = self.text)
        self.text.insert("end", "hello")

        # bind <Return> key to entry widjet
        self.canvas.bind("<Button-1>", self.click)

        # Create a Tkinter button to allow the user to update the array with the new value
        self.button = tk.Button(master, text="click me", command=self.print_test)
        self.button.pack()
        self.webcam_button = tk.Button(master, text="webcam", command = self.webcam)
        self.webcam_button.pack()
        self.update_button = tk.Button(master, text="update cubestring", command = self.update_cubestring)
        self.update_button.pack()
        self.solve_button = tk.Button(master, text="solve the cube", command = self.solve)
        self.solve_button.pack()

        # establish arduino connection
        self.arduino = serial.Serial(port='COM4',baudrate=9600, timeout=1)
        #self.arduino = serial.Serial(port='/dev/cu.usbmodem1101',baudrate=9600, timeout=1)
        #self.arduino = serial.Serial(port='/dev/cu.usbserial-130',baudrate=19200, timeout=1)
        #self.arduino.close()
        #self.arduino.open()


    def print_test(self):
        self.text.delete(1.0, "end")
        self.text.insert(1.0, "clicked")
        print('clicked')
        set = steps_converter("F B L R U D")
        arduino_com(set, self.arduino)
        #test_serial(self.arduino)

    def webcam(self):
        self.text.delete(1.0, "end")
        self.text.insert(1.0, "taking screenshot of the cube ...")
        #TODO import data from kociemba_solver.py (kociemba notation)
        cube_state = capture_cube()
        self.cubestring = cvt2kociemba(cube_state)
        self.text.delete(1.0, "end")
        self.text.insert(1.0, f"cubestring is {self.cubestring}")
        #self.cubestring = cvt2kociemba([
        #    [['Y', 'W', 'G'], ['R', 'B', 'G'], ['R', 'W', 'R']], 
        #    [['W', 'O', 'G'], ['B', 'W', 'B'], ['W', 'Y', 'R']],
        #    [['Y', 'W', 'O'], ['Y', 'R', 'O'], ['G', 'W', 'G']],
        #    [['Y', 'R', 'B'], ['B', 'Y', 'Y'], ['O', 'Y', 'Y']],
        #    [['R', 'G', 'B'], ['G', 'O', 'R'], ['B', 'O', 'B']],
        #    [['O', 'O', 'W'], ['G', 'G', 'B'], ['O', 'R', 'W']]])
        print(self.cubestring)
        #TODO update the colors to the app
        n = 0
        for f in range(6):
            for row in range(3):
                for col in range(3):
                    self.canvas.itemconfig(self.facelet_id[f][row][col], fill=self.cols[self.color.index(cube_state[f][row][col])])
                    n += 1

        self.cube_image()
        self.text.delete(1.0, "end")
        self.text.insert(1.0, "done ...")

    def solve(self):
        try: 
            solution = kociemba.solve(self.cubestring)
            self.text.delete(1.0, "end")
            self.text.insert("end", f"solution found ... steps are {solution}")
            set = steps_converter(solution)
            arduino_com(set, self.arduino)
            self.text.insert("end", "solving ...")

        except ValueError:
            print("no solution found: invalid cubestring")
            self.text.delete(1.0,"end")
            self.text.insert("end", "invalid cubestring ... no solution found")

    def create_facelet_rect(self, a):
        offset = ((1, 0), (2, 1), (1, 1), (1, 2), (0, 1), (3, 1))
        for f in range(6):
            if f == 0: 
                gap = 0 
            else:
                gap =10
            for row in range(3):
                y = 20 + a * row 
                for col in range(3):
                    x =20 + a * col + f * 3 * a + f* gap
                    self.facelet_id[f][row][col] = self.canvas.create_rectangle(x, y, x + a, y + a, fill="grey")

        for f in range(6):
            self.canvas.itemconfig(self.facelet_id[f][1][1], fill = self.cols[f])

    def create_colorpicker_rect(self, width):
        """Initialize the "paintbox" on the canvas."""
        for i in range(6):
            x = (i % 3)*(width+5) + width
            y = (i // 3)*(width+5) + 7*width
            self.colorpick_id[i] = self.canvas.create_rectangle(x, y, x + width, y + width, fill=self.cols[i])
            self.canvas.itemconfig(self.colorpick_id[0], width=4)
            self.curcol = self.cols[0]


    def cube_image(self):
        for i in range(6):
            directory_path =f"./picture/cubeface{i}.jpg"
            raw_string = repr(directory_path)[1:-1]
            print(raw_string)
            image = Image.open(raw_string)
            image = image.resize((180, 180))
            test = ImageTk.PhotoImage(image)
            label = tk.Label(image = test)
            label.image = test
            label.place(x =20 + i*180 + i*10, y =220)

    def click(self, unused):
        idlist = self.canvas.find_withtag("current")
        if len(idlist) > 0:
            if idlist[0] in self.colorpick_id:
                self.curcol = self.canvas.itemcget("current", "fill")
                for i in range(6):
                    self.canvas.itemconfig(self.colorpick_id[i],width =1)
                self.canvas.itemconfig(idlist[0],width =5)
            else:
                self.canvas.itemconfig("current",fill=self.curcol)


    def update_cubestring(self):
        try: 
            color_to_facelet = {}
            for i in range(6):
                color_to_facelet.update({self.canvas.itemcget(self.facelet_id[i][1][1], "fill"): self.t[i]})
            s = ''
            for f in range(6):
                for row in range(3):
                    for col in range(3):
                        s += color_to_facelet[self.canvas.itemcget(self.facelet_id[f][row][col], "fill")]
            self.cubestring = s
            print(s)
            self.text.delete(1.0,"end")
            self.text.insert("end", self.cubestring)
        except KeyError:
            self.text.delete(1.0,"end")
            self.text.insert("end", "missing colour in some of the facelets ...")



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

