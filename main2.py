from tkinter import *


class Window:
    def __init__(self,width,height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas(self.__root,bg = "white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.wm_protocol("VM_DELETE_WINDOW",self.close)

    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False


def main():
    win = Window(600,800)
    win.wait_for_close()


if __name__ == "__main__":
    main()