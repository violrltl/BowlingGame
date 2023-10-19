class BowlingError(Exception):
    pass


class FramePinsExceededError(BowlingError):
    """
    Raised when the number of pins in a frame exceeds 10
    """
    pass