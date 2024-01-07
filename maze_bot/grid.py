from cell import Cell


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = [Cell(col, row) for row in range(rows) for col in range(cols)]
        self.start_index = 52
        self.cells[self.start_index].in_maze = True
        self.cells[self.start_index].is_start = True

    def get_neighbors(self, cell):
        left = (cell.col - 1, cell.row) if cell.col > 0 else None
        right = (cell.col + 1, cell.row) if cell.col < self.cols - 1 else None
        up = (cell.col, cell.row - 1) if cell.row > 0 else None
        down = (cell.col, cell.row + 1) if cell.row < self.rows - 1 else None

        cell_dict = {'left': self.cells[self.get_index(*left)] if left else None,
                     'right': self.cells[self.get_index(*right)] if right else None,
                     'up': self.cells[self.get_index(*up)] if up else None,
                     'down': self.cells[self.get_index(*down)] if down else None}
        return cell_dict

    def get_index(self, col, row):
        return col + row * self.cols
