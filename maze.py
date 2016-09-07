#!/usr/bin/python
# Maze generator in Python
# Joe Wingbermuehle
# 2010-10-06
# not the original
import sys
import random

class MazeException(Exception):
    pass

def isodd(*n):
    return all(i % 2 != 0 for i in n)

class Maze(object):

    DIRMAP = {0: ( 1,  0),
              1: ( 0,  1),
              2: (-1,  0),
              3: ( 0, -1)}

    def __init__(self, width=39, height=23):

        if not isodd(width, height):
            raise MazeException('Width and height must be odd.')

        self.width = width
        self.height = height
        self.maze = { x:{y:True for y in xrange(height)} for x in xrange(width) }

    def display(self):
        for y in xrange(self.height):
            for x in xrange(self.width):
                if self.maze[x][y]:
                    sys.stdout.write("[]")
                else:
                    sys.stdout.write("  ")
            sys.stdout.write("\n")

    def carve(self, x, y):
        maze, width, height = self.maze, self.width, self.height
        dir = random.randint(0, 3)
        for _ in xrange(4):
            dx, dy = self.DIRMAP[dir]
            x1, y1 = x + dx, y + dy
            x2, y2  = x1 + dx, y1 + dy
            if (width > x2 > 0 and height > y2 > 0
                and maze[x1][y1] and maze[x2][y2]):

                maze[x1][y1] = False
                maze[x2][y2] = False
                self.carve(x2, y2)

            dir = (dir + 1) % 4

    def generate(self):
        #random.seed(1)
        self.maze[1][1] = False
        self.carve(1, 1)
        self.maze[1][0] = False
        self.maze[self.width - 2][self.height - 1] = False

def main():
    maze = Maze()
    maze.generate()
    maze.display()

if __name__ == '__main__':
    main()
