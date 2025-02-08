import unittest

from maze import Maze

class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        """
        Check if maze is propperly creating cells
        """

        num_cols = 12
        num_rows = 10
        cell_size_x = 10
        cell_size_y = 10
        m1 = Maze(num_rows, num_cols, 0, 0, cell_size_x, cell_size_y)
        num_cols_2 = 17
        num_rows_2 = 5
        cell_size_x_2 = 23
        cell_size_y_2 = 47
        m2 = Maze(num_rows_2, num_cols_2, 0, 0, cell_size_x_2, cell_size_y_2)
        print(m1._cells[0][0])
        print(m1._cells[1][0])
        print(m2._cells[0][0])
        print(m2._cells[1][0])
        # Assert colums are being created correctly
        self.assertEqual(len(m1._cells),num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

        self.assertEqual(len(m2._cells),num_cols_2)
        self.assertEqual(len(m2._cells[0]), num_rows_2)

        # Assert cells placement are correct
        self.assertEqual(m2._cells[0][0]._top_left_y + cell_size_y_2, m2._cells[1][0]._top_left_y)
        self.assertEqual(m2._cells[0][0]._bottom_right_y + cell_size_y_2, m2._cells[1][0]._bottom_right_y)

if __name__ == "__main__":
    unittest.main()
