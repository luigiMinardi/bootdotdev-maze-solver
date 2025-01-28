from window import Window
from line import Line
from point import Point

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

    def draw(self) -> None:
        """
        Draw itself and its walls on the screen based on the coordinates
        set on init and its 4 "has_<positon>_wall" booleans,
        position being top, bottom, left, right.
        """

        if self.has_top_wall:
            top_left = Point(self.__top_left_x, self.__top_left_y)
            top_right = Point(self.__bottom_right_x, self.__top_left_y)
            top_wall = Line(top_left, top_right)

            self.__window.draw_line(top_wall)

        if self.has_bottom_wall:
            bottom_left = Point(self.__bottom_right_x, self.__top_left_y)
            bottom_right = Point(self.__bottom_right_x, self.__bottom_right_y)
            bottom_wall = Line(bottom_left, bottom_right)

            self.__window.draw_line(bottom_wall)

        if self.has_left_wall:
            left_top = Point(self.__top_left_x, self.__top_left_y)
            left_bottom = Point(self.__top_left_x, self.__bottom_right_y)
            left_wall = Line(left_top, left_bottom)

            self.__window.draw_line(left_wall)

        if self.has_right_wall:
            right_top = Point(self.__bottom_right_x, self.__top_left_x)
            right_bottom = Point(self.__bottom_right_x, self.__bottom_right_y)
            right_wall = Line(right_top, right_bottom)

            self.__window.draw_line(right_wall)


