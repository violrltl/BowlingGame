from customtkinter import set_appearance_mode

from bowlinggame.ui.tkinter_ui import BowlingApp

if __name__ == "__main__":
    set_appearance_mode("light")
    app = BowlingApp()
    app.mainloop()