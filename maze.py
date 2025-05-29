

from cell import Cell
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win,
            ):
        self._x1=x1
        self._y1=y1
        self._num_rows=num_rows
        self._num_cols=num_cols
        self._cell_size_x=cell_size_x
        self._cell_size_y=cell_size_y
        self._win=win
        rows, cols = (self._cell_size_x,  self._cell_size_y)
        self.__cells = [[0]*cols]*rows
        self.__create_cells()

    
    def __create_cells(self):
        for x in range(0,self._num_rows):
            for y in range(0,self._num_cols):
                self.__cells[x][y]=Cell(self._win)
                self.__draw_cell(x,y)
                print(f"{x}{y} was created.")

    
    def __draw_cell(self, i , j):
        x1 = self._x1  + self._cell_size_x * i
        y1 = self._y1 + self._cell_size_y * j
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self.__cells[i][j].draw(x1,y1,x2,y2)
        self.animate()

    def animate(self):
        self._win.redraw()
        time.sleep(0.05)