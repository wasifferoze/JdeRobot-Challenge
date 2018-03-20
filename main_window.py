import tkinter as tk
from enum import Enum
from tkinter import ttk

from conway_main import Universe


class GameStatus(Enum):
    PAUSE = 0
    ONGOING = 1

class GameOfLife(tk.Frame):
    WIDTH = 803
    HEIGHT = 506

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.canvas = tk.Canvas(self, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack(side=tk.TOP)
        # self.control_info = tk.Frame(self)
        # self.control_info.pack(side=tk.TOP, fill=tk.X)
        # self.start_button = tk.Button(self.control_info, text='Start', command=self.start)
        # self.start_button.pack(side=tk.RIGHT)
        # self.pause_button = tk.Button(self.control_info, text='Pause', command=self.pause)
        # self.pause_button.pack(side=tk.RIGHT)
        # # self.reset_button = tk.Button(self.control_area, text='Random Input', command=self.reset)
        # # self.reset_button.pack(side=tk.LEFT, padx=3, pady=2)
        # self.generation_text_var = tk.StringVar()
        # self.generation_text = tk.Label(self.control_info, textvariable=self.generation_text_var)
        # self.generation_text.pack()

        self.control_area = tk.Frame(self)
        self.control_area.config(bg="#808080")
        self.control_area.pack(side=tk.BOTTOM, fill=tk.X)
        self.create_widgets()

        dim = (50, 50)
        nos = 500
        self.u = Universe(dim)
        self.nseed = nos

        self.status = GameStatus.ONGOING
        self.reset()

    def draw(self):
        if self.status == GameStatus.ONGOING:
            self.canvas.delete('all')
            h, w = self.u.dim
            ds = self.WIDTH / max(h, w)
            for i in range(h):
                for j in range(w):
                    if self.u.space[i][j] == 1:
                        self.canvas.create_rectangle(
                            j*ds, i*ds, j*ds+ds, i*ds+ds, fill="#508080")
                    else:
                        self.canvas.create_rectangle(
                            j*ds, i*ds, j*ds+ds, i*ds+ds)
            self.generation_text_var.set("Width: {}, Height: {}, Number of initial seeds: {}\nGeneration: {} ".
                                         format(self.u.dim[1], self.u.dim[0], self.nseed, self.u.generation))
            self.u.next_generation()
            self.after(1000, self.draw)

    def start(self):
        self.status = GameStatus.ONGOING
        self.draw()

    def reset(self):
        self.u.random_reset(self.nseed)
        self.status = GameStatus.ONGOING
        self.draw()
        self.status = GameStatus.PAUSE

    def pause(self):
        self.status = GameStatus.PAUSE

    def create_widgets(self):
        """all widget code is here"""
        tkvar = tk.StringVar(root)
        # Dictionary with options
        choices = ('Clear', 'Small Glider', 'Glider', 'Exploder', '10 Cell Row', 'Light Weight Spaceship', 'Tumbler',
                   'Gosper Glider Gu')
        self.combo_input = ttk.Combobox(self.control_area, width=25, values=choices, state='readonly')
        self.combo_input.pack(side=tk.LEFT)
        self.combo_input.current(0)
        self.combo_input.bind("<<ComboboxSelected>>", self.combo_callback)

        self.next = tk.Button(self.control_area, text="Next", command="")
        self.next.pack(side=tk.LEFT, padx=3, pady=2)
        self.start = tk.Button(self.control_area, text="Start", command=self.start)
        self.start.pack(side=tk.LEFT, padx=3, pady=2)

        self.stop = tk.Button(self.control_area, text="Pause", fg="red", command=self.pause)
        self.stop.pack(side=tk.LEFT, padx=3, pady=2)

        self.stop = tk.Button(self.control_area, text="Fast", fg="red", command="")
        self.stop.pack(side=tk.LEFT, padx=3, pady=2)

        self.reset_button = tk.Button(self.control_area, text='Random Input', command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=3, pady=2)

        self.generation_text_var = tk.StringVar()
        self.gen_label = tk.Label(self.control_area, textvariable=self.generation_text_var, bg="#808080")
        self.gen_label.pack(side=tk.RIGHT, padx=3, pady=2)

    def combo_callback(self, eventobj):
        """this method get combobox events"""
        # TODO implement method for initial input types other than random initailistion
        print(self.combo_input.get())  # print name
        print(self.combo_input.current())  # print index
        input_index = self.combo_input.current()
        if input_index == 0 and GameStatus.ONGOING:
            GameStatus.PAUSE
            self.canvas.delete('all')
            # TODO only clear fill rectangles
        elif input_index == 1:
            print(input_index)
        elif input_index == 2:
            print(input_index)
        elif input_index == 3:
            print(input_index)
        elif input_index == 4:
            print(input_index)
        elif input_index == 5:
            print(input_index)
        elif input_index == 6:
            print(input_index)
        else:
            print(input_index)

root = tk.Tk()
root.title("Conway's Game of Life")
root.resizable(0, 0)
app = GameOfLife(master=root)
app.mainloop()
