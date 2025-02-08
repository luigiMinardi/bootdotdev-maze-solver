from typing import Literal, Self, TypedDict
from utils import BACKGROUND_COLOR, LINE_COLOR
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
    top_left_x, top_left_y, bottom_right_x, bottom_right_y (int): X, Y positon of the Cell.
    window (Window | None): The Window that the Cell should be draw.

    x=0 is the left of the screen.
    y=0 is the top of the screen.
    """
    def __init__(
            self,
            top_left_x:int,
            top_left_y: int,
            bottom_right_x:int,
            bottom_right_y: int,
            window: Window | None
        ) -> None:
        self.has_left_wall = True
        self.has_right_wall = True

        self.has_top_wall = True
        self.has_bottom_wall = True

        self._top_left_x = top_left_x
        self._top_left_y = top_left_y

        self._bottom_right_x= bottom_right_x
        self._bottom_right_y = bottom_right_y

        self.__window = window

        self.visited = False


    def draw(self, colors: TWallColors | None = None) -> tuple[None, TWallColors]:
        """
        Draw itself and its walls on the screen based on the coordinates
        set on init and its 4 "has_<positon>_wall" booleans.
        Position being top, bottom, left, right.

        colors(TWallColors): Optional dict with the <position> and <TKColor> as key values.
        """

        draw_colors: TWallColors = colors if colors else {}
        if self.has_top_wall:
            draw_colors["top"] = draw_colors.setdefault("top", LINE_COLOR)
        else:
            draw_colors["top"] = draw_colors.setdefault("top", BACKGROUND_COLOR)

        if self.has_bottom_wall:
            draw_colors["bottom"] = draw_colors.setdefault("bottom",LINE_COLOR)
        else:
            draw_colors["bottom"] = draw_colors.setdefault("bottom",BACKGROUND_COLOR)

        if self.has_left_wall:
            draw_colors["left"] = draw_colors.setdefault("left",LINE_COLOR)
        else:
            draw_colors["left"] = draw_colors.setdefault("left",BACKGROUND_COLOR)

        if self.has_right_wall:
            draw_colors["right"] = draw_colors.setdefault("right",LINE_COLOR)
        else:
            draw_colors["right"] = draw_colors.setdefault("right", BACKGROUND_COLOR)

        if self.__window:
            top_left = Point(self._top_left_x, self._top_left_y)
            top_right = Point(self._bottom_right_x, self._top_left_y)
            top_wall = Line(top_left, top_right)

            self.__window.draw_line(top_wall, draw_colors["top"])

            bottom_left = Point(self._top_left_x, self._bottom_right_y)
            bottom_right = Point(self._bottom_right_x, self._bottom_right_y)
            bottom_wall = Line(bottom_left, bottom_right)

            self.__window.draw_line(bottom_wall, draw_colors["bottom"])

            top_left = Point(self._top_left_x, self._top_left_y)
            bottom_left = Point(self._top_left_x, self._bottom_right_y)
            left_wall = Line(top_left, bottom_left)

            self.__window.draw_line(left_wall, draw_colors["left"])

            top_right = Point(self._bottom_right_x, self._top_left_y)
            bottom_right = Point(self._bottom_right_x, self._bottom_right_y)
            right_wall = Line(top_right, bottom_right)

            self.__window.draw_line(right_wall, draw_colors["right"])

        return None, draw_colors


    def get_center(self) -> tuple[float, float]:
        """
        return the (x, y) position of the center of a Cell
        """
        return ((self._top_left_x + self._bottom_right_x) / 2, (self._top_left_y + self._bottom_right_y) / 2)


    def draw_move(self, to_cell: Self, undo: bool = False) -> tuple[Line, Literal['gray', 'red'], bool] | None:
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

        if not self.__window:
            return movement, fill_color, undo
        self.__window.draw_line(movement, fill_color)


    def __repr__(self) -> str:
        return f"Cell({self._top_left_x}, {self._top_left_y}, {self._bottom_right_x}, {self._bottom_right_y}, {repr(self.__window)})"

    def __str__(self) -> str:
        #return f"(Cell at {self._top_left_x} {self._top_left_y} to {self._bottom_right_x} {self._bottom_right_y})"
        return f"Cell FROM {self._top_left_x}, {self._top_left_y} TO {self._bottom_right_x}, {self._bottom_right_y} WITH top {self.has_top_wall}, bottom {self.has_bottom_wall}, left {self.has_left_wall}, right {self.has_right_wall}"
