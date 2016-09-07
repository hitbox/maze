import curses

class Interface(object):

    def __init__(self, maze=None):
        self.screen = None
        self.maze = maze

    def start(self):
        if self.maze is None:
            raise RuntimeError('Set maze attribute first.')

        return curses.wrapper(self._start)

    def _start(self, screen):
        self.screen = screen
        self.screen.addstr(str(self.maze))
        self.screen.getch()
