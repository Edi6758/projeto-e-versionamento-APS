from tkinter import Frame, Label, BOTH, X, LEFT
from PIL import Image, ImageTk
from random import randint


class BattleScreen:
    def __init__(self, manager):
        self.__manager = manager
        self.__frame = None

    def open(self):
        self.frame = Frame(self.manager.window, bg="white")
        self.manager.window.geometry('1024x832')
        self.frame.grid(sticky='nsew')
        for i in range(4):
            self.frame.grid_rowconfigure(i, weight=1)
        for i in range(5):
            self.frame.grid_columnconfigure(i, weight=1)
        self.frame.tkraise()
        self.create_screen()

    def create_screen(self):
        header_height = 64
        header = self.create_header(header_height)
        header.grid(row=0, column=0, columnspan=5)

        num_rows = 3
        num_columns = 5
        column_widths = [128, 256, 256, 256, 128]
        row_height = 256
        image_path = 'assets/legolas_teste.png'

        for r in range(1, num_rows + 1):
            for c in range(num_columns):
                random_color = f"#{randint(0, 255):02x}{randint(0, 255):02x}{randint(0, 255):02x}"
                frame = self.create_frame(width=column_widths[c], height=row_height, bg_color=random_color)
                if num_columns == 1 or num_columns == 3:
                    pass
                    self.add_png_image(frame, image_path)
                frame.grid(row=r, column=c, padx=0, pady=0)

    def create_header(self, header_height):
        header = Frame(self.frame, height=header_height, bg="gray")
        header.grid(row=0, column=0, columnspan=5, sticky='ew')

        window_width = 1024

        num_squares = window_width // header_height

        for i in range(num_squares):
            square = self.create_square(header, header_height, header_height, "red")
            square.pack(side=LEFT)

        return header

    def create_frame(self, width, height, bg_color):
        frame = Frame(self.frame, width=width, height=height, bg=bg_color, highlightthickness=0, bd=0)
        frame.grid_propagate(False)
        return frame

    def create_square(self, header_frame, width, height, bg_color):
        square = Frame(header_frame, width=width, height=height, bg=bg_color)
        square.pack_propagate(False)
        return square

    def add_png_image(self, frame, image_path):
        img = Image.open(image_path)
        img.thumbnail((256, 256), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        label = Label(frame, image=photo)
        label.image = photo
        label.pack(fill=BOTH, expand=True)

    @property
    def manager(self):
        return self.__manager

    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self, frame):
        self.__frame = frame
