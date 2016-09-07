from maze import Maze
from interface import Interface

def main():
    maze = Maze()
    maze.generate()

    #print maze

    interface = Interface()
    interface.maze = maze
    interface.start()

    #screen = Screen()
    #screen._screen.
