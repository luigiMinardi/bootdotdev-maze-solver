from typing import Self, TypedDict
from window import Window
from line import Line
from point import Point


class TWallColors(TypedDict, total = False):
    top: str
    bottom: str
    left: str
    right: str

class Cell:
    """
    window: The Window that the Cell should be draw.
    top_left_x, top_left_y, bottom_right_x, bottom_right_y: X, Y positon of the Cell.

    x=0 is the left of the screen.
    y=0 is the top of the screen.
    """
    def __init__(self, window: Window, top_left_x:int , top_left_y: int, bottom_right_x:int , bottom_right_y: int) -> None:
        self.has_left_wall = True
        self.has_right_wall = True

        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__top_left_x = top_left_x
        self.__top_left_y = top_left_y

        self.__bottom_right_x= bottom_right_x
        self.__bottom_right_y = bottom_right_y

        self.__window = window


    def draw(self, colors: TWallColors = {}) -> None:
        """
        Draw itself and its walls on the screen based on the coordinates
        set on init and its 4 "has_<positon>_wall" booleans.
        Position being top, bottom, left, right.

        colors(TWallColors): Optional dict with the <position> and <TKColor> as key values.
        """

        if self.has_top_wall:
            top_left = Point(self.__top_left_x, self.__top_left_y)
            top_right = Point(self.__bottom_right_x, self.__top_left_y)
            top_wall = Line(top_left, top_right)

            self.__window.draw_line(top_wall, colors.setdefault("top","#232136"))

        if self.has_bottom_wall:
            bottom_left = Point(self.__top_left_x, self.__bottom_right_y)
            bottom_right = Point(self.__bottom_right_x, self.__bottom_right_y)
            bottom_wall = Line(bottom_left, bottom_right)

            self.__window.draw_line(bottom_wall, colors.setdefault("bottom","#232136"))

        if self.has_left_wall:
            top_left = Point(self.__top_left_x, self.__top_left_y)
            bottom_left = Point(self.__top_left_x, self.__bottom_right_y)
            left_wall = Line(top_left, bottom_left)

            self.__window.draw_line(left_wall, colors.setdefault("left","#232136"))

        if self.has_right_wall:
            top_right = Point(self.__bottom_right_x, self.__top_left_y)
            bottom_right = Point(self.__bottom_right_x, self.__bottom_right_y)
            right_wall = Line(top_right, bottom_right)

            self.__window.draw_line(right_wall, colors.setdefault("right","#232136"))


    def get_center(self) -> tuple[float, float]:
        """
        return the (x, y) position of the center of a Cell
        """
        return ((self.__top_left_x + self.__bottom_right_x) / 2, (self.__top_left_y + self.__bottom_right_y) / 2)


    def draw_move(self, to_cell: Self, undo: bool = False) -> None:
        """
        Draw a line between the center of two Cells.
        The line is RED if doing GRAY if undoing.

        to_cell: Cell that you want to go to.
        undo: In case you're "going back" instead of "forward".
        """
        fill_color = "red"
        if undo:
            fill_color = "gray"

        my_center_x, my_center_y = self.get_center()
        to_center_x, to_center_y = to_cell.get_center()

        my_center = Point(my_center_x, my_center_y)
        to_center = Point(to_center_x, to_center_y)
        movement = Line(my_center, to_center)

        self.__window.draw_line(movement, fill_color)


