from tkinter import Frame, Canvas, W, Button


class MenuScreen:
    def __init__(self, window_manager):
        self.__manager = window_manager
        self.__frame = None
        self.__start_button = None

    def open(self):
        self.frame = Frame(self.manager.root)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.manager.root.title('Battle Element')
        self.manager.root.geometry("500x250")
        self.manager.root.overrideredirect(False)
        self.manager.root.resizable(False, False)
        self.frame.tkraise()
        self.create_widgets()

    def create_widgets(self):
        canvas = Canvas(self.frame, width=500, height=200, bg="white")
        canvas.grid(row=0, column=0)
        colors = ["blue", "orange", "green", "brown", "yellow"]
        title = "Battle Element"
        x, y = 114, 100
        for i, char in enumerate(title):
            color = colors[i % len(colors)]
            text_item = canvas.create_text(x, y, anchor=W, text=char, font=("Helvetica", 24, "bold"), fill=color)
            bbox = canvas.bbox(text_item)
            char_width = bbox[2] - bbox[0]
            x += char_width
        self.start_button = Button(self.frame, text="Procurar partida",
                                   command=self.manager.main.server.start_match)
        self.start_button.grid(row=1, column=0)

    @property
    def manager(self):
        return self.__manager

    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self, frame):
        self.__frame = frame

    @property
    def start_button(self):
        return self.__start_button

    @start_button.setter
    def start_button(self, start_button: Button):
        self.__start_button = start_button
