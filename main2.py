from graphics2 import Window,Line,Point

def main():
    win = Window(600,800)
    p1 = Point(0,0)
    p2 = Point(100,100)
    p3 = Point(0,200)
    line1 = Line(p1,p2)
    line2 = Line(p2,p3)
    win.draw_line(line1)
    win.draw_line(line2)
    win.wait_for_close()


if __name__ == "__main__":
    main()
