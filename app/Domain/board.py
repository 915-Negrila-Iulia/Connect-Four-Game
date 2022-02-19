"""

Plan:
    1. Draw an empty _board
    2. Alternate moves (computer moves)
    3. Console, win/lose condition
Classes:
    Board
        - internal state of the _board
        - move
            -> make a move on the _board with X or O
            -> return True if at least 1 valid move remaining
    Strategy
        - computer "AI"
        - next_move(_board) => return computer's next move
    Game
        - has a Board instance
        - human player move
        - computer move
            -> call a strategy for the computer player
    Console
        - has a Game instance
        - has a Strategy instance
        - alternate play between human and computer
"""

from texttable import Texttable


class Board:

    def __init__(self):
        """
        Creates a list of lists which represents the _board of the game
        """
        self._rows = 6
        self._columns = 7
        self._board = [['' for i in range(self._columns)] for j in range(self._rows)]

    @property
    def get_board(self):
        return self._board

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    def get_column(self, column_index):
        """
        Creates an empty list and appends elements to it from the column
        :param column_index: index of the column which elements will be in the new list
        :return: the list of elements representing a column
        """
        column_list = []
        for row_index in range(self._rows):
            column_list.append(self._board[row_index][column_index])

        return column_list

    def get_row(self, row_index):
        return self._board[row_index]

    def get_diagonals_left_to_right(self):
        """
        Creates a list having all the diagonals '/' from the board
        :return: list of diagonals '/'
        """
        diagonals_list = []
        for i in range(0, self._rows + self._columns - 1):
            diagonal = []
            row_index = min(i, self._rows - 1)

            if i < self._rows:
                column_index = 0
            else:
                column_index = i - (self._rows - 1)

            while column_index != min(i + 1, self._columns):
                diagonal.append(self.get_board[row_index][column_index])
                row_index -= 1
                column_index += 1
            diagonals_list.append(diagonal)

        return diagonals_list

    def get_diagonals_right_to_left(self):
        """
        Creates a list having all the diagonals '\' from the board
        :return: list of diagonals '\'
        """
        diagonals_list = []
        for i in range(0, self._rows + self._columns - 1):
            diagonal = []
            row_index = min(i, self._rows - 1)

            if i < self._rows:
                column_index = 6
            else:
                column_index = 11 - i

            while column_index != max(-1, self._columns - i - 2):
                diagonal.append(self.get_board[row_index][column_index])
                row_index -= 1
                column_index -= 1
            diagonals_list.append(diagonal)

        return diagonals_list

    def get_diagonals(self):
        """
        Creates a list having all the diagonals from the board
        :return: list of diagonals
        """
        diagonals_list = []

        right_to_left = self.get_diagonals_right_to_left()
        left_to_right = self.get_diagonals_left_to_right()

        diagonals_list.extend(right_to_left)
        diagonals_list.extend(left_to_right)

        return diagonals_list

    def move(self, column, symbol):
        """
        Makes a move
        Adds a symbol ( only x or o ) to the list of lists (which represents the board)
        :param column: index where to add the symbol in the list
        :param symbol: symbol to be add
        :return:
        """
        if symbol not in ['x', 'o']:
            raise Exception("Symbol is not ok")

        if '' not in self.get_column(column):
            raise Exception("Can't make any moves on this column")

        row = 0
        while row < self._rows and self._board[row][column] == '':
            row += 1

        self._board[row - 1][column] = symbol

    def row_of_first_free_box(self, column):
        """
        Checks the first free box of a column from bottom to top
        :param column: column to be checked
        :return: the row of the first free box
        """
        row = 0
        while row < self._rows and self._board[row][column] == '':
            row += 1
        return row-1

    def __str__(self):
        t = Texttable()
        for row in range(0, 6):
            row_data = []

            for index in self._board[row]:
                if index == '':
                    row_data.append(' ')
                elif index == 'x' or index == 'o':
                    row_data.append(index)
            t.add_row(row_data)

        return t.draw()

    def check_win(self):
        """
        Checks if there is a winner
        :return: the symbol of the winner
        """

        x_list = ['x', 'x', 'x', 'x']
        o_list = ['o', 'o', 'o', 'o']

        for row in range(0, self._rows):
            for i in range(0, self._columns - 3):
                if self.get_row(row)[i:i + 4] == x_list:
                    return 'x'
                elif self.get_row(row)[i:i + 4] == o_list:
                    return 'o'

        for column in range(0, self._columns):
            for i in range(0, self._rows - 3):
                if self.get_column(column)[i:i + 4] == x_list:
                    return 'x'
                elif self.get_column(column)[i:i + 4] == o_list:
                    return 'o'

        for diagonal in self.get_diagonals():
            if len(diagonal) >= 4:
                for i in range(0, len(diagonal) - 3):
                    if diagonal[i:i + 4] == x_list:
                        return 'x'
                    elif diagonal[i:i + 4] == o_list:
                        return 'o'
