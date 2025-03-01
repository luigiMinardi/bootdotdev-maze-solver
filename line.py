from tkinter import Canvas
from point import Point
from utils import LINE_COLOR


class Line:
    """
    Receive two Point classes to draw a line between them.
    """
    def __init__(self, point_A: Point, point_B: Point) -> None:
        self.point_A = point_A
        self.point_B = point_B

    def draw(self, canvas: Canvas, fill_color: str = LINE_COLOR) -> None:
        """
        Draw a line between two Point's in a Canvas.

        canvas: TK Canvas
        fill_color: TK Color (name of the color or HEX #rrggbb value)
        """
        canvas.create_line(
            self.point_A.x,
            self.point_A.y,
            self.point_B.x,
            self.point_B.y,
            fill=fill_color,
            width=2
        )

    def __repr__(self) -> str:
        return f"Line({repr(self.point_A)}, {repr(self.point_B)})"

    def __str__(self) -> str:
        return f"Line between: ({str(self.point_A)}) and ({str(self.point_B)})"
