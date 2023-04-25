from tkinter import Canvas, W, Button, Frame


class MainMenuScreen:
    def __init__(self, manager):
        self.__manager = manager
        self.__frame = Frame(self.manager.window)

    def open(self):
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.manager.window.title('Battle Element')
        self.manager.window.geometry("500x250")
        self.manager.window.overrideredirect(False)
        self.manager.window.resizable(False, False)
        self.frame.tkraise()
        self.title()
        self.button()

    def button(self):
        # Create a centralized button
        button = Button(self.frame, text="Procurar partida", command=self.swap_to_hero_creation)
        button.grid(row=1, column=0)

    def swap_to_hero_creation(self):
        self.frame.grid_remove()
        self.manager.hero_creator.open()

    def title(self):
        # Create a canvas to draw the title
        canvas = Canvas(self.frame, width=500, height=200, bg="white")
        canvas.grid(row=0, column=0)

        # Draw the title
        colors = ["blue", "orange", "green", "brown", "yellow"]
        title = "Battle Element"
        x, y = 114, 100  # Center coordinates

        for i, char in enumerate(title):
            color = colors[i % len(colors)]
            text_item = canvas.create_text(x, y, anchor=W, text=char, font=("Helvetica", 24, "bold"), fill=color)
            bbox = canvas.bbox(text_item)
            char_width = bbox[2] - bbox[0]
            x += char_width  # Move x coordinate to the right for the next character

    @property
    def manager(self):
        return self.__manager

    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self, frame):
        self.__frame = frame
