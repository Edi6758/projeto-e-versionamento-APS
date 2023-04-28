from tkinter import Frame, Label, BOTH, X, LEFT
from PIL import Image, ImageTk
from random import randint


class BattleScreen:
    def __init__(self, manager):
        self.__manager = manager
        self.__frame = Frame(self.manager.window, bg="white")

    def open(self):
        self.manager.window.geometry('1100x950')
        self.frame.grid(sticky='nsew')
        self.frame.tkraise()
        self.create_screen()

    def create_screen(self):

        header_height = 50
        header = self.create_header(header_height)
        header.grid(row=0, column=0, columnspan=5)

        # Cria a matriz [3, 5] dentro do frame principal
        num_rows = 3
        num_columns = 5
        column_widths = [100, 300, 300, 300, 100]
        row_height = 300

        # Substitua 'image.png' pelo caminho da sua imagem PNG
        image_path = 'assets/legolas_teste.png'

        for r in range(1, num_rows + 1):
            for c in range(num_columns):
                random_color = f"#{randint(0, 255):02x}{randint(0, 255):02x}{randint(0, 255):02x}"
                frame = self.create_frame(width=column_widths[c], height=row_height, bg_color=random_color)
                if num_columns == 1 or num_columns == 3:
                    self.add_png_image(frame, image_path)
                frame.grid(row=r, column=c, padx=1, pady=1)

    def create_header(self, header_height):
        header = Frame(self.frame, height=header_height, bg="gray")
        header.pack(fill=X)

        # Calcule a largura da janela
        window_width = self.frame.winfo_screenwidth()

        # Calcule a quantidade de quadrados que podem caber no cabeçalho
        num_squares = window_width // header_height

        # Crie e adicione os quadrados ao cabeçalho
        for i in range(num_squares):
            square = self.create_square(header, header_height, header_height, "red")
            square.pack(side=LEFT)

        return header

    # Função para criar um frame com cor de fundo e tamanho específico
    def create_frame(self, width, height, bg_color):
        frame = Frame(self.frame, width=width, height=height, bg=bg_color)
        frame.grid_propagate(False)  # Impede que o frame redimensione com base no conteúdo
        return frame

    def create_square(self, header_frame, width, height, bg_color):
        square = Frame(header_frame, width=width, height=height, bg=bg_color)
        square.pack_propagate(False)
        return square

    # Função para adicionar uma imagem PNG a um frame
    def add_png_image(self, frame, image_path):
        img = Image.open(image_path)
        img.thumbnail((300, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        label = Label(frame, image=photo)
        label.image = photo  # Guarde uma referência à imagem para evitar que seja coletada como lixo
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
