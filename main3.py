from graphics import Window
from cell import Cell

def main():
    win = Window(600,800)
    size=100
    for x in range(0,10):
        for y in range(0,10):
            cell1 = Cell(win)
            #cell1.has_left_wall = False
            cell1.draw(100 + y*size,100 + x*size,100 + size + y*size,100 + size + x*size)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()