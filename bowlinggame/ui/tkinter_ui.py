from tkinter import Tk, Frame, Label, Entry
from tkinter.constants import TOP, X, SOLID, W, LEFT
from tkinter.ttk import Button
from customtkinter import CTk, set_appearance_mode


class BowlingFrame(Frame):
    def __init__(self, master=None, number=0, is_total=False, **kwargs):
        super().__init__(master, **kwargs)
        self.config(borderwidth=1, relief=SOLID)
        self.config(padx=0, pady=0)
        self.config(bg="white")

        if is_total:
            bg = "darkblue"
            fg = "white"
        else:
            bg = "white"
            fg = "black"

        self.frame_label = Label(self, text=str(number))
        self.frame_label.pack(side=TOP, fill=X)
        self.frame_label.config(borderwidth=1, relief=SOLID, width=5, height=1, bg=bg, fg=fg)
        self.frame_rolls = Label(self, text="")
        self.frame_rolls.pack(side=TOP, fill=X)
        self.frame_rolls.config(borderwidth=1, relief=SOLID, bg=bg, fg=fg)
        self.frame_score = Label(self, text="")
        self.frame_score.pack(side=TOP, fill=X)
        self.frame_score.config(borderwidth=1, relief=SOLID, bg=bg, fg=fg)

    def update_rolls(self, rolls):
        self.frame_rolls.config(text=str(rolls))

    def update_score(self, score):
        self.frame_score.config(text=str(score))


class BowlingApp(CTk):
    def __init__(self):
        super().__init__()
        self.add_roll_entry = None
        self.title("Bowling Score Manager")
        self.geometry("475x120")
        self.config(padx=10, pady=10)
        self.resizable(False, False)
        self.frames = []
        self.create_frames()
        self.create_action_panel()

    def create_frames(self):

        l_frame = Label(self, text="Frame:", width=7)
        l_frame.grid(row=0, column=0, padx=1)
        l_frame.config(foreground="blue")
        l_frame.config(anchor=W, justify=LEFT)

        l_roll = Label(self, text="Rolls:", width=7)
        l_roll.grid(row=1, column=0, padx=1)
        l_roll.config(foreground="blue")
        l_roll.config(anchor=W, justify=LEFT)

        l_score = Label(self, text="Score:", width=7)
        l_score.grid(row=2, column=0, padx=1)
        l_score.config(foreground="blue")
        l_score.config(anchor=W, justify=LEFT)

        for i in range(1, 13):
            if i < 11:
                frame = BowlingFrame(self, number=i)
            elif i == 11:
                frame = BowlingFrame(self, number="Extra")
            else:
                frame = BowlingFrame(self, number="Total", is_total=True)

            frame.grid(row=0, column=i, rowspan=3, padx=1)
            self.frames.append(frame)

    def create_action_panel(self):
        l_add_roll = Label(self, text="Add roll", width=7)
        l_add_roll.grid(row=3, column=0, padx=1, pady=30)
        l_add_roll.config(fg="blue")
        l_add_roll.config(anchor=W, justify=LEFT)

        self.add_roll_entry = Entry(self, width=13, justify=LEFT)
        self.add_roll_entry.grid(row=3, column=1, columnspan=2, pady=30)

        # add button next to entry
        add_roll_button = Button(self, text="Add", width=5, command=self.add_roll)
        add_roll_button.grid(row=3, column=3, pady=30)

        # load from file button
        load_button = Button(self, text="Load from file", width=20, command=self.load_from_file)
        load_button.grid(row=3, column=8, columnspan=3, pady=30)

        # reset button next to load button
        reset_button = Button(self, text="Reset", command=self.reset)
        reset_button.grid(row=3, column=11, columnspan=2, pady=30)

    def reset(self):
        pass

    def add_roll(self):
        pass

    def load_from_file(self):
        pass

    def update_frames(self, frames):
        for i, frame in enumerate(frames):
            self.frames[i].update_rolls(frame.rolls)
            self.frames[i].update_score(frame.score())


if __name__ == "__main__":
    set_appearance_mode("light")
    app = BowlingApp()
    app.mainloop()