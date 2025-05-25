from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, height, width):
        self._root = Tk()
        self._root.title = "Maze Solver"
        self._canvas = Canvas(self._root, bg="white", height=height, width=width)
        self._canvas.pack(fill=BOTH, expand=1)
        self._running=False
        self._root.protocol("VM_DELETE_WINDOW",self.close)
        
    def draw(self):
        self._root.update()
        self._root.update_idletasks()

    def wait_for_close(self):
        self._running=True
        while self._running:
            self.draw()

    def draw_line(self,line):
        line.draw(self._canvas)


    def close(self):
        self._running=False

class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Line():
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2
 

    def draw(self,canvas):
        canvas.create_line(self.p1.x,self.p1.y,self.p2.x,self.p2.y,fill="green",width=5)