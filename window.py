from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int, height: int, title: str) -> None:
        """
        width and height are the size of the new window in pixels.
        title is the self.__root title.
        """
        self.__root = Tk()
        self.__root.title(title)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, bg="#403d52", width=width, height=height)
        self.__canvas.pack()

        self.__is_window_running = False


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
        self.__is_window_running = True
        while self.__is_window_running is True:
            self.redraw()


    def close(self):
        self.__is_window_running = False


