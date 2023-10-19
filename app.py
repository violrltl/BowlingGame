from customtkinter import set_appearance_mode

from bowlinggame.model.bowling import Game
from bowlinggame.ui.tkinter_ui import BowlingApp

if __name__ == "__main__":
    set_appearance_mode("light")
    game: Game = Game()
    app = BowlingApp(game)
    app.mainloop()