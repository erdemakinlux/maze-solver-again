from graphics import Window
from cell import Cell
from maze import Maze


def main():
    win = Window(800, 600)

    mz =Maze(10,10,10,10,50,50,win)

    

    win.wait_for_close()


main()
