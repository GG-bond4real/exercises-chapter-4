import numpy as np
from matplotlib import pyplot
from scipy.signal import convolve2d
"""Brief description of the function."""
glider = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])

blinker = np.array([
 [0, 0, 0],
 [1, 1, 1],
 [0, 0, 0]]
)

glider_gun = np.array([
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0]
])


class Game:
    def __init__(game, Size):
        game.board = np.zeros((Size, Size))

    def play(self):
        print("Playing life. Press ctrl + c to stop.")
        pyplot.ion()
        while True:
            self.move()
            self.show()
            pyplot.pause(0.0000005)

    def move(self):
        STENCIL = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        NeighbourCount = convolve2d(self.board, STENCIL, mode='same')

        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i, j] = (
                    1 if (NeighbourCount[i, j] == 3
                          or (NeighbourCount[i, j] == 2 and self.board[i, j]))
                    else 0
                )

    def __setitem__(self, key, value):
        self.board[key] = value

    def show(self):
        pyplot.clf()
        pyplot.matshow(self.board, fignum=0, cmap='binary')
        pyplot.show()
    


class Pattern():
    def __init__(self, grid):
        Pattern.grid = grid

    def flip_vertical(self):
        fvgrid = self.grid[::1]
        return Pattern(fvgrid)
   
    def flip_horizontal(self):
        fhgrid = [row[::1] for row in self.grid]
        return Pattern(fhgrid)
 
    def flip_diag(self):
        fdgrid = [[self.grid[i][j] for
                   i in range(len(self.grid))] for 
                  j in range(len(self.matrix[0]))]
        return Pattern(fdgrid)
 
    def rotate(self, n):
        if n//4 == 1:
            f1 = flip_horizontal(self)
            f2 = flip_diag(f1)
            return f2
        if n//4 == 2:
            f3 = flip_horizontal(self)
            f4 = flip_vertical(f3)
            return f4
        if n//4 == 3:
            f5 = flip_diag(self)
            return flip_horizontal(f5)
        if n//4 == 0:
            return self