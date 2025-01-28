from tkinter import Tk, BOTH, Canvas
from typing import TypedDict


class Data(TypedDict):
    root: Tk
    canvas: Canvas
    is_window_running: bool


class Window:
    def __init__(self, width: int, height: int, title: str) -> None:
        """
        width and height are the size of the new window in pixels.
        title is the self.__root title.
        """
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.title(title)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas()
        self.canvas.pack()

        self.data: Data = {
            "root": self.__root,
            "canvas": self.canvas,
            "is_window_running": False
        }


    def redraw(self):
        """
        call self.__root.update_idletasks() and self.__root.update()
        to redraw the screen.
        """
        self.__root.update_idletasks()
        self.__root.update()
    

    def wait_for_close(self):
        """
        set self.data["is_window_running"] to True
        call self.redraw() until "is_window_running" is False
        """
        self.data["is_window_running"] = True
        while self.data["is_window_running"] is True:
            self.redraw()


    def close(self):
        self.data["is_window_running"] = False


