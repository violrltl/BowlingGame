from dataclasses import dataclass
from typing import Optional


@dataclass
class Roll:
    pins: int


class Frame:
    def __init__(self, next_frame=None):
        self.rolls: list[Roll] = []
        self.next_frame: Frame = next_frame

    def score(self) -> int:
        pass


class TenthFrame(Frame):
    def __init__(self):
        super().__init__()
        self.extra_roll: Optional[Roll] = None


class Game:
    def __init__(self):
        self.frames: list[Frame] = []
        self._initialize_frames()

    def _initialize_frames(self):
        for i in range(9):
            previous_frame = Frame()
            self.frames.append(Frame())
        self.frames.append(TenthFrame())

    def roll(self, pins: int):
        pass

    def score(self) -> int:
        pass

