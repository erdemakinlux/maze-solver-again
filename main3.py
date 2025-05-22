from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, height, width):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas(self.__root,bg="white",height=height, width=width)
        self.__canvas.pack(fill=BOTH,expand=1)
        self.__running = False
        self.__root.protocol("VM_DELETE_WINDOW", func=self.close())

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_to_close(self):
        self.__running = True
        while self.__running :
            self.redraw()

    def close(self):
        self.__running = False
    
        


def main():
    win = Window(800,600)
    win.wait_to_close()


if __name__ == "__main__":
    main()