from model.player_interface import PlayerInterface


if __name__ == '__main__':
    game = PlayerInterface()
    game.initialize()
    game.window.root.mainloop()
