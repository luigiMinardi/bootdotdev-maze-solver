from line import Line
from point import Point
from window import Window


def main():
    win = Window(800, 600, "Beautiful window")
    point_A = Point(10,100)
    point_B = Point(100,10)
    line = Line(point_A, point_B)
    point_C = Point(10,10)
    point_D = Point(100,100)
    line2 = Line(point_C, point_D)
    win.draw_line(line, "#232136")
    win.draw_line(line2, "#232136")
    win.wait_for_close()


if __name__ == "__main__":
    main()
