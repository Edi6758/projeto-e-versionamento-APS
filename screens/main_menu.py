from tkinter import Canvas, W, Button, Frame


class MainMenuScreen:
    def __init__(self, manager):
        self.__manager = manager
        self.__frame = None

    def open(self):
        self.frame = Frame(self.manager.window)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.manager.window.title('Battle Element')
        self.manager.window.geometry("500x250")
        self.manager.window.overrideredirect(False)
        self.manager.window.resizable(False, False)
        self.frame.tkraise()
        self.create_widgets()

    def create_widgets(self):
        self.title()
        self.button()

    def button(self):
        button = Button(self.frame, text="Procurar partida",
                        command=self.manager.player_interface.server_manager.start_match)
        button.grid(row=1, column=0)

    def title(self):
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

    @property
    def manager(self):
        return self.__manager

    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self, frame):
        self.__frame = frame
