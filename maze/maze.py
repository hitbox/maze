#!/usr/bin/python
from itertools import imap
import random

range = xrange

class Maze(object):

    # The size of the maze (must be odd).
    WIDTH = 39
    HEIGHT = 23

    def __init__(self, width=None, height=None):
        self.width = self.WIDTH if width is None else width
        self.height = self.HEIGHT if height is None else height

        self.maze = { x:{ y:True for y in range(self.height) } for x in range(self.width) }

    def carve(self, x, y):
        dir = random.randint(0, 3)
        count = 0
        while count < 4:
            dx = 0
            dy = 0
            if   dir == 0:
                dx = 1
            elif dir == 1:
                dy = 1
            elif dir == 2:
                dx = -1
            else:
                dy = -1
            x1 = x + dx
            y1 = y + dy
            x2 = x1 + dx
            y2 = y1 + dy
            if x2 > 0 and x2 < self.width and y2 > 0 and y2 < self.height:
                if self.maze[x1][y1] and self.maze[x2][y2]:
                    self.maze[x1][y1] = None
                    self.maze[x2][y2] = None
                    self.carve(x2, y2)
            count = count + 1
            dir = (dir + 1) % 4

    def generate(self):
        random.seed(1)
        self.maze[1][1] = None
        self.carve(1, 1)
        self.maze[1][0] = None
        self.maze[self.width - 2][self.height - 1] = None

    def char(self, x, y):
        m = { True: '[]', None: '  ' }
        s = m[self.maze[x][y]]
        if x == self.width - 1:
            s += '\n'
        return s

    def make_string(self):
        return ''.join(self.char(x,y) for y in range(self.height) for x in range(self.width))

    def __str__(self):
        return self.make_string()
