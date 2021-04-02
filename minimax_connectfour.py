import copy
import time
import abc
from random import randint
from itertools import product
import math


class Game(object):
    """A connect four game."""
    VALID_STATES = {}

    def __init__(self, grid):
        """Instances differ by their board."""
        self.grid = copy.deepcopy(grid)  # No aliasing!

    def display(self):
        """Print the game board."""
        for row in self.grid:
            for mark in row:
                print(mark, end='')
            print()
        print()

    def possible_moves(self):
        """Return a list of possible moves given the current board."""
        # YOU FILL THIS IN
        movesGrid = copy.deepcopy(self.grid)
        moves = []
        for col in range(8):
            if movesGrid[0][col] == "-":
                moves.append(col)
        return moves

    def neighbor(self, col, color):
        """Return a Game instance like this one but with a move made into the specified column."""
        # YOU FILL THIS IN

        for row in range(7, -1, -1):
            if self.grid[row][col] == '-':
                self.grid[row][col] = color
                break

        return Game(self.grid)

    def utility(self, color):
        """Return the minimax utility value of this game"""
        # YOU FILL THIS IN
        self.color = color
        self.oppColor = {"R": "B", "B": "R"}[self.color]
        counterValue = 0
        rows, cols = len(self.grid), len(self.grid[0])
        if (rows, cols) not in Game.VALID_STATES:
            valid_states = []
            for row, col in product(reversed(range(rows)), reversed(range(cols))):
                if col + 3 < cols:  # Horizontal
                    valid_states.append(((row, col), (row, col + 1), (row, col + 2), (row, col + 3)))
                if row + 3 < rows:  # Vertical
                    valid_states.append(((row, col), (row + 1, col), (row + 2, col), (row + 3, col)))
                if col + 3 < cols and row + 3 < rows:  # Diagonal
                    valid_states.append(((row, col), (row + 1, col + 1), (row + 2, col + 2), (row + 3, col + 3)))
                if col - 3 > -1 and row + 3 < rows:  # Diagonal
                    valid_states.append(((row, col), (row + 1, col - 1), (row + 2, col - 2), (row + 3, col - 3)))
            Game.VALID_STATES[(rows, cols)] = valid_states

            rows, cols, moves_made = len(self.grid), len(self.grid[0]), 0
            for (row0, col0), (row1, col1), (row2, col2), (row3, col3) in Game.VALID_STATES[(rows, cols)]:
                if self.grid[row0][col0] == '-':
                    continue
                if self.grid[row0][col0] == self.grid[row1][col1] == self.grid[row2][col2] == self.grid[row3][col3]:
                    if self.grid[row0][col0] == self.color:
                        counterValue += 10
                    elif self.grid[row0][col0] == self.oppColor:
                        counterValue -= 12
                elif self.grid[row0][col0] == self.grid[row1][col1] == self.grid[row2][col2]:
                    if self.grid[row0][col0] == self.color:
                        counterValue += 6
                    elif self.grid[row0][col0] == self.oppColor:
                        counterValue += 8
                elif self.grid[row0][col0] == self.grid[row1][col1]:
                    if self.grid[row0][col0] == self.color:
                        counterValue += 2
                    elif self.grid[row0][col0] == self.oppColor:
                        counterValue += 3
        return counterValue

    def winning_state(self):
        """Returns float("inf") if Red wins; float("-inf") if Black wins;
           0 if board full; None if not full and no winner"""
        # YOU FILL THIS IN
        # find the consecutive moves of black and red
        rows, cols = len(self.grid), len(self.grid[0])
        if (rows, cols) not in Game.VALID_STATES:
            valid_states = []
            for row, col in product(reversed(range(rows)), reversed(range(cols))):
                if col + 3 < cols:  # Horizontal
                    valid_states.append(((row, col), (row, col + 1), (row, col + 2), (row, col + 3)))
                if row + 3 < rows:  # Vertical
                    valid_states.append(((row, col), (row + 1, col), (row + 2, col), (row + 3, col)))
                if col + 3 < cols and row + 3 < rows:  # Diagonal
                    valid_states.append(((row, col), (row + 1, col + 1), (row + 2, col + 2), (row + 3, col + 3)))
                if col - 3 > -1 and row + 3 < rows:  # Diagonal
                    valid_states.append(((row, col), (row + 1, col - 1), (row + 2, col - 2), (row + 3, col - 3)))
            Game.VALID_STATES[(rows, cols)] = valid_states

        # Check who actually won after finding consecutive moves
        rows, cols, moves_made = len(self.grid), len(self.grid[0]), 0
        for (row0, col0), (row1, col1), (row2, col2), (row3, col3) in Game.VALID_STATES[(rows, cols)]:
            if self.grid[row0][col0] == '-':
                continue
            if self.grid[row0][col0] == self.grid[row1][col1] == self.grid[row2][col2] == self.grid[row3][col3]:
                if self.grid[row0][col0] == 'R':
                    return float('inf')
                elif self.grid[row0][col0] == 'B':
                    return float('-inf')

        # to add up and check number of moves made to check for tie
        moves_made = sum(
            v != "-"
            for row in self.grid
            for v in row
        )
        return 0 if moves_made == cols * rows else None



class Agent(object):
    """Abstract class, extended by classes RandomAgent, FirstMoveAgent, MinimaxAgent.
    Do not make an instance of this class."""

    def __init__(self, color):
        """Agents use either RED or BLACK chips."""
        self.color = color

    @abc.abstractmethod
    def move(self, game):
        """Abstract. Must be implemented by a class that extends Agent."""
        pass


class RandomAgent(Agent):
    """Naive agent -- always performs a random move"""

    def move(self, game):
        """Returns a random move"""
        # YOU FILL THIS IN
        possMoves = game.possible_moves
        randCol = randint(0, len(possMoves))
        return game.neighbor(game.grid, randCol, self.color)


class FirstMoveAgent(Agent):
    """Naive agent -- always performs the first move"""

    def move(self, game):
        """Returns the first possible move"""
        # YOU FILL THIS IN
        moves = game.possible_moves(game.grid)
        return game.neighbor(game.grid, moves[0], self.color)


class MinimaxAgent(Agent):
    """Smart agent -- uses minimax to determine the best move"""

    def move(self, game):
        """Returns the best move using minimax"""
        # YOU FILL THIS IN
        # Counter is for limiting depth of recursion
        counter = 2
        self.oppColor = {"R": "B", "B": "R"}[self.color]
        value, move = self.maxValue(counter, game)
        return move


    def maxValue(self, counter, game):
        if game.winning_state() is not None or counter == 0:
            return game.utility(self.color), None
        v, move = -math.inf, None

        for a in game.possible_moves():
            v2, _ = self.minValue(counter-1, game.neighbor(a, self.color))
            if v2 > v:
                v, move = v2, a

        return v, move

    def minValue(self, counter, game):
        if game.winning_state() is not None or counter == 0:
            return game.utility(self.color), None
        v, move = math.inf, None

        for a in game.possible_moves():
            v2, _ = self.maxValue(counter-1, game.neighbor(a, self.oppColor))
            if v2 < v:
                v, move = v2, a

        return v, move

def tournament(simulations=50):
    """Simulate connect four games, of a minimax agent playing
    against a random agent"""

    redwin, blackwin, tie = 0,0,0
    for i in range(simulations):

        game = single_game(io=False)

        print(i, end=" ")
        if game.winning_state() == float("inf"):
            redwin += 1
        elif game.winning_state() == float("-inf"):
            blackwin += 1
        elif game.winning_state() == 0:
            tie += 1

    print("Red %d (%.0f%%) Black %d (%.0f%%) Tie %d" % (redwin,redwin/simulations*100,blackwin,blackwin/simulations*100,tie))

    return redwin/simulations


def single_game(io=True):
    """Create a game and have two agents play it."""

    game = Game([['-' for i in range(8)] for j in range(8)])   # 8x8 empty board
    if io:
        game.display()

    maxplayer = MinimaxAgent('R')
    minplayer = RandomAgent('B')

    while True:

        m = maxplayer.move(game)
        game = game.neighbor(m, maxplayer.color)
        if io:
            time.sleep(1)
            game.display()

        if game.winning_state() is not None:
            break

        m = minplayer.move(game)
        game = game.neighbor(m, minplayer.color)
        if io:
            time.sleep(1)
            game.display()

        if game.winning_state() is not None:
            break

    if game.winning_state() == float("inf"):
        print("RED WINS!")
    elif game.winning_state() == float("-inf"):
        print("BLACK WINS!")
    elif game.winning_state() == 0:
        print("TIE!")

    return game


if __name__ == '__main__':
    single_game(io=True)
    #tournament(simulations=50)
