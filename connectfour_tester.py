from minimax_connectfour import *


class GameBoards():
    game1 = Game([['-' for i in range(8)] for j in range(8)])

    game2 = Game([['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', 'R', '-', '-', '-', '-', '-']])

    game3 = Game([['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', 'B', '-', '-', '-'],
                  ['-', '-', 'R', '-', 'B', '-', '-', '-'],
                  ['-', '-', 'R', '-', 'B', '-', '-', '-'],
                  ['-', '-', 'R', 'R', 'B', '-', '-', '-']])

    game4 = Game([['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['R', 'R', 'R', 'R', 'B', 'B', 'B', '-']])

    game5 = Game([['-', '-', 'R', '-', '-', '-', '-', '-'],
                  ['-', '-', 'B', '-', '-', '-', '-', '-'],
                  ['-', '-', 'R', '-', '-', '-', '-', '-'],
                  ['-', '-', 'B', '-', '-', '-', '-', '-'],
                  ['-', '-', 'R', '-', 'R', '-', '-', '-'],
                  ['-', '-', 'B', 'R', 'B', '-', '-', '-'],
                  ['-', 'B', 'R', 'B', 'B', '-', '-', '-'],
                  ['-', 'R', 'R', 'B', 'R', '-', '-', '-']])

    game6 = Game([['B', 'B', 'B', 'R', 'R', 'R', 'B', 'R'],
                  ['B', 'B', 'R', 'R', 'B', 'B', 'B', 'R'],
                  ['B', 'R', 'B', 'B', 'B', 'R', 'R', 'B'],
                  ['B', 'B', 'B', 'R', 'R', 'B', 'R', 'B'],
                  ['R', 'R', 'R', 'B', 'B', 'B', 'R', 'B'],
                  ['R', 'R', 'B', 'B', 'R', 'R', 'B', 'R'],
                  ['B', 'B', 'R', 'R', 'B', 'R', 'R', 'B'],
                  ['R', 'B', 'B', 'B', 'R', 'B', 'R', 'B']])

    game7 = Game([['R', 'B', 'B', 'R', 'R', 'R', 'B', 'R'],
                  ['B', 'B', 'R', 'R', 'B', 'B', 'B', 'R'],
                  ['B', 'R', 'B', 'B', 'B', 'R', 'R', 'B'],
                  ['B', 'B', 'B', 'R', 'R', 'B', 'R', 'B'],
                  ['R', 'R', 'R', 'B', 'B', 'B', 'R', 'B'],
                  ['R', 'R', 'B', 'B', 'R', 'R', 'B', 'R'],
                  ['B', 'B', 'R', 'R', 'B', 'R', 'R', 'B'],
                  ['R', 'B', 'B', 'B', 'R', 'B', 'R', 'B']])

    game8 = Game([['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', '-', '-', '-', '-', '-', '-'],
                  ['-', '-', 'R', 'R', '-', '-', '-', '-']])

    game9 = Game([['-', 'B', 'B', 'R', 'R', 'B', 'B', 'R'],
                  ['-', 'B', 'B', 'R', 'R', 'B', 'B', 'R'],
                  ['B', 'R', 'R', 'B', 'B', 'R', 'R', 'B'],
                  ['B', 'R', 'B', 'R', 'B', 'B', 'R', 'B'],
                  ['R', 'B', 'R', 'B', 'B', 'B', 'R', 'B'],
                  ['B', 'R', 'R', 'B', 'R', 'R', 'B', 'R'],
                  ['B', 'B', 'R', 'R', 'B', 'R', 'R', 'B'],
                  ['R', 'B', 'B', 'B', 'R', 'B', 'R', 'B']])

    game10 = Game([['-', 'B', 'B', 'R', 'R', 'B', 'B', 'R'],
                   ['B', 'B', 'B', 'R', 'R', 'B', 'B', 'R'],
                   ['B', 'R', 'R', 'B', 'B', 'R', 'R', 'B'],
                   ['B', 'R', 'B', 'R', 'B', 'B', 'R', 'B'],
                   ['R', 'B', 'R', 'B', 'B', 'B', 'R', 'B'],
                   ['B', 'R', 'R', 'B', 'R', 'R', 'B', 'R'],
                   ['B', 'B', 'R', 'R', 'B', 'R', 'R', 'B'],
                   ['R', 'B', 'B', 'B', 'R', 'B', 'R', 'B']])


def test_moves1():
    assert len(GameBoards.game1.possible_moves()) == len([0, 1, 2, 3, 4, 5, 6, 7])
    assert set(GameBoards.game1.possible_moves()) == set([0, 1, 2, 3, 4, 5, 6, 7])


def test_moves2():
    assert GameBoards.game9.possible_moves() == [0]


def test_moves3():
    assert len(GameBoards.game5.possible_moves()) == len([0, 1, 3, 4, 5, 6, 7])
    assert set(GameBoards.game5.possible_moves()) == set([0, 1, 3, 4, 5, 6, 7])


def test_neighbor1():
    game1_a = GameBoards.game1.neighbor(2, 'R')
    assert game1_a.grid == GameBoards.game2.grid


def test_neighbor2():
    game2_a = GameBoards.game2.neighbor(3, 'R')
    assert game2_a.grid == GameBoards.game8.grid


def test_neighbor3():
    game9_a = GameBoards.game9.neighbor(0, 'B')
    assert game9_a.grid == GameBoards.game10.grid


def test_winningstate1():
    assert GameBoards.game1.winning_state() is None


def test_winningstate2():
    assert GameBoards.game3.winning_state() == float("-inf")


def test_winningstate3():
    assert GameBoards.game4.winning_state() == float("inf")


def test_winningstate4():
    assert GameBoards.game5.winning_state() == float("inf")


def test_winningstate5():
    assert GameBoards.game6.winning_state() == float("-inf")


def test_winningstate6():
    assert GameBoards.game7.winning_state() == 0


# Feel free to comment out the section that does not apply to you.
# Only the 481/575 test for the section that you are enrolled in will automatically run
# whenever you commit/push.
def test_tournament481():
    assert tournament(50) >= .7  # CSC481


def test_tournament575():
    assert tournament(50) >= .85  # CSC575




