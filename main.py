#import tkinter
from tkinter import Tk, BOTH, Canvas
from graphics import Window, Line, Point




def main():
    win = Window(600,800)
    l = Line(Point(50, 50), Point(400, 400))
    l2 = Line(Point(400, 400), Point(600, 600))
    win.draw_line(l, "black")
    win.draw_line(l2, "red")
    win.wait_for_close()

if __name__ == "__main__":
        main()
