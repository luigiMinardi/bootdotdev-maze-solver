import time
from cell import Cell
from window import Window


class Maze:
    """
    num_rows, num_cols (int): Number of rows and collumns on the Maze Matrix representation
    padding_x, padding_y (int): Distance in pixels that the Maze has from the Window
    cell_size_x, cell_size_y (int): Size that one Cell will have in pixels
        so if a Cell has 10 of size it means that it will have
        padding_x + cell_size_x then padding_y + cell_size_y.
    window (Window | None): Window in which the maze should be draw

    1st Cell top_left_x, top_left_y are the padding_x and padding_y then
    cell_size_<x/y> is the equivalent of bottom_right_x, bottom_right_y Cell position
    next Cell calculate its position based on the previous one.
    """
    def __init__(
            self,
            num_rows: int,
            num_cols: int,
            padding_x: int,
            padding_y: int,
            cell_size_x: int,
            cell_size_y: int,
            window: Window | None = None,
        ) -> None:
        self.window = window

        self.num_rows = num_rows
        self.num_cols = num_cols

        self.padding_x = padding_x
        self.padding_y = padding_y

        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y

        self._create_cells()


    def _create_cells(self) -> None:
        """
        Create a matrix with Cells to draw the maze

        with the maze Maze(Window, 3, 3, 10, 10, 10,10) you get the Matrix:
        [
         [(Cell at 10 10 to 20 20), (Cell at 20 10 to 30 20), (Cell at 30 10 to 40 20)],
         [(Cell at 10 20 to 20 30), (Cell at 20 20 to 30 30), (Cell at 30 20 to 40 30)],
         [(Cell at 10 30 to 20 40), (Cell at 20 30 to 30 40), (Cell at 30 30 to 40 40)]
        ]
        """
        # TODO: Refactor this method to be more easy to understand
        # if possible faster too.

        self._cells: list[list[Cell]] = []

        first_row = True
        for row in range(self.num_cols):
            self._cells.append([])

            first_col = True
            for col in range(self.num_rows):
                if first_row == True:
                    first_row = False
                    first_col = False
                    self._cells[row].append(Cell(
                        self.padding_x,
                        self.padding_y,
                        self.padding_x + self.cell_size_x,
                        self.padding_y + self.cell_size_y,
                        self.window
                    ))
                    continue

                if first_col == True:
                    first_col = False
                    self._cells[row].append(Cell(
                        self.padding_x,
                        self._cells[row-1][0]._top_left_y + self.cell_size_y,
                        self.padding_x + self.cell_size_x,
                        self._cells[row-1][0]._bottom_right_y + self.cell_size_y,
                        self.window
                    ))
                    continue

                self._cells[row].append(Cell(
                    self._cells[row][col-1]._top_left_x + self.cell_size_x,
                    self._cells[row][col-1]._top_left_y,
                    self._cells[row][col-1]._bottom_right_x + self.cell_size_x,
                    self._cells[row][col-1]._bottom_right_y,
                    self.window
                ))
        if self.window:
            self._draw_cell()


    def _draw_cell(self) -> None:
        for row in self._cells:
            for cell in row:
                cell.draw()
                self._animate()
    
    def _animate(self) -> None:
        if self.window:
            self.window.redraw()
        self.animation_delay: float = 0.01
        time.sleep(self.animation_delay)
