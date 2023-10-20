import pytest



from bowlinggame.model.bowling import Game


@pytest.fixture
def game():
    """ Return a new Game """
    return Game()


def roll_many(game, n, pins):
    """
    Simulates several roll in a game
    :param game: the game object
    :param n: the number of rolls
    :param pins: the number of pins knocked down in every roll
    """
    for _ in range(n):
        game.roll(pins)


def roll_spare(game):
    """
    Simulates rolling a spare
    :param game: the game object
    """
    game.roll(5)
    game.roll(5)


def roll_strike(game):
    """
    Simulates rolling a strike
    :param game: the game object
    """
    game.roll(10)


def test_awful_game(game):
    """ Test a game where no pins where knocked down """
    roll_many(game, 20, 0)
    assert game.score() == 0


def test_all_ones_game(game):
    """ test a game where one pin was knocked down in all rolls """
    roll_many(game, 20, 1)
    assert game.score() == 20


def test_one_spare(game):
    """ Test a game with one spare """
    roll_spare(game)
    game.roll(3)
    roll_many(game, 17, 0)
    assert game.score() == 16


def test_one_strike(game):
    """ Test a game with one strike """
    roll_strike(game)
    game.roll(3)
    game.roll(4)
    roll_many(game, 16, 0)
    assert game.score() == 24


def test_perfect_game(game):
    """ Test a game with all strikes """
    roll_many(game, 12, 10)
    assert game.score() == 300


def test_raise_exception_when_frame_rolls_exceed_10_pins(game):
    with pytest.raises(ValueError, match="A frame's rolls cannot exceed 10 pins"):
        game.roll(5)
        game.roll(7)


def test_raise_exception_when_bonus_roll_with_open_tenth_frame(game):
    roll_many(game, 18, 0)
    with pytest.raises(IndexError, match="Can't throw bonus roll with an open tenth frame"):
        game.roll(5)
        game.roll(2)
        game.roll(5)


def test_raise_exception_when_tenth_frame_with_more_than_3_rolls(game):
    roll_many(game, 12, 10)
    with pytest.raises(IndexError, match="Can't add more than three rolls to the tenth frame"):
        game.roll(5)


def test_raise_exception_when_calculate_score_without_game_end(game):
    roll_many(game, 10, 2)
    with pytest.raises(IndexError, match="There are not enough frames to calculate score"):
        game.score()
