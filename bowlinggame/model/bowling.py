from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from bowlinggame.model.bowling_errors import FramePinsExceededError


@dataclass
class Roll:
    pins: int


class Frame(ABC):

    def __init__(self):
        self.rolls: list[Roll] = []
        self._next_frame: Optional[Frame] = None

    @property
    def next_frame(self):
        return self._next_frame

    @next_frame.setter
    def next_frame(self, value):
        self._next_frame = value

    @property
    def total_pins(self) -> int:
        return sum(roll.pins for roll in self.rolls)

    def is_strike(self):
        return len(self.rolls) > 0 and self.rolls[0].pins == 10

    def is_spare(self):
        return len(self.rolls) == 2 and self.rolls[0].pins + self.rolls[1].pins == 10

    @abstractmethod
    def add_roll(self, pins: int):
        raise NotImplementedError

    @abstractmethod
    def score(self) -> int:
        raise NotImplementedError

    def __str__(self) -> str:
        if len(self.rolls) == 0:
            return ""
        elif len(self.rolls) == 1:
            if self.is_strike():
                return "X"
            else:
                return f"{self.rolls[0].pins} | "
        elif len(self.rolls) == 2:
            if self.is_spare():
                return f"{self.rolls[0].pins} | /"
            else:
                return f"{self.rolls[0].pins} | {self.rolls[1].pins}"

class NormalFrame(Frame):
    def __init__(self):
        super().__init__()

    def add_roll(self, pins: int):
        if pins + self.total_pins > 10:
            raise FramePinsExceededError("A frame's rolls cannot exceed 10 pins")

        if len(self.rolls) < 2:
            self.rolls.append(Roll(pins))

    def score(self) -> int:
        points = self.total_pins
        if self.is_strike():
            if len(self.next_frame.rolls) == 2:
                points += self.next_frame.total_pins
            elif len(self.next_frame.rolls) == 1:
                points += self.next_frame.rolls[0].pins
                if len(self.next_frame.next_frame.rolls) > 0:
                    points += self.next_frame.next_frame.rolls[0].pins
        elif self.is_spare():
            if len(self.next_frame.rolls) > 0:
                points += self.next_frame.rolls[0].pins

        return points


class TenthFrame(Frame):
    def __init__(self):
        super().__init__()
        self.extra_roll: Optional[Roll] = None

    def add_roll(self, pins: int):
        if len(self.rolls) < 2:
            self.rolls.append(Roll(pins))
        elif len(self.rolls) == 2 and self.extra_roll is None:
            if self.is_strike() or self.is_spare():
                self.extra_roll = Roll(pins)
            else:
                raise IndexError("Can't throw bonus roll with an open tenth frame")
        else:
            raise IndexError("Can't add more than three rolls to the tenth frame")

    def score(self) -> int:
        points = self.total_pins
        if self.is_strike() or self.is_spare():
            return points + self.extra_roll.pins
        return points


class Game:

    MAX_FRAMES = 10

    def __init__(self):
        self.frames: list[Frame] = []
        self._init_frames()
        self.roll_count: int = 0

    @property
    def current_frame_index(self) -> int:
        if self.roll_count < (Game.MAX_FRAMES * 2):
            return self.roll_count // 2
        else:
            return Game.MAX_FRAMES - 1

    @property
    def current_frame(self) -> Frame:
        return self.frames[self.current_frame_index]

    def _init_frames(self):
        frame = NormalFrame()

        for i in range(9):
            if i < 8:
                next_frame = NormalFrame()
            else:
                next_frame = TenthFrame()
            frame.next_frame = next_frame
            self.frames.append(frame)
            frame = next_frame

        self.frames.append(frame)

    def roll(self, pins: int):
        self.frames[self.current_frame_index].add_roll(pins)
        if self.frames[self.current_frame_index].is_strike():
            self.roll_count += 2
        else:
            self.roll_count += 1

    def score(self) -> int:
        if self.current_frame_index < Game.MAX_FRAMES - 1:
            raise IndexError("There are not enough frames to calculate score")

        return sum(frame.score() for frame in self.frames)
