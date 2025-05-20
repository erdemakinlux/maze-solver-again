#import tkinter
from tkinter import Tk, BOTH, Canvas


class Window():
        def __init__(self,width,height):
                self.__width = width
                self.__height = height
                self.__root = Tk()
                self.__root.title = ("Maze Solver")
                self.__root.protocol("WM_DELETE_WINDOW", self.close)
                self.__canvas = Canvas()
                self.__canvas.pack()
                self.__is_window_running = False
        
        def redraw(self):
                self.__root.update()
                
        def wait_for_close(self):
                self.__is_window_running = True
                while self.__is_window_running:
                        self.redraw()
        
        def close(self):
                self.__is_window_running = False
        


def main():
        main_window = Window(100,100)
        main_window.wait_for_close()

if __name__ == "__main__":
        main()
