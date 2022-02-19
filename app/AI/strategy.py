import random


class Strategy:
    def next_move(self, board):
        if not self.win_row_final_move(board):
            if not self.win_column(board):
                if not self.win_diagonal_right_to_left(board):
                    if not self.win_diagonal_left_to_right(board):
                        if not self.block_row_final_move(board):
                            if not self.block_column(board):
                                if not self.block_diagonal_right_to_left(board):
                                    if not self.block_diagonal_left_to_right(board):
                                        if not self.block_row_in_advanse(board):
                                            if not self.move_to_win(board):
                                                columns_indexes = [0, 1, 2, 3, 4, 5, 6]
                                                move = random.choice(columns_indexes)
                                                board.move(move, 'o')

    def block_row_final_move(self, board):
        """
        Checks if a row of 3 x's can be blocked and makes a move to block it
        :param board: the list of lists where the moves are made
        :return: True if a row was blocked and False otherwise
        """
        for row in range(0, board.rows):
            for i in range(0, board.columns - 3):

                if board.get_row(row)[i:i + 4] == ['', 'x', 'x', 'x'] and board.row_of_first_free_box(i) == row:
                    board.move(i, 'o')
                    return True

                elif board.get_row(row)[i:i + 4] == ['x', 'x', 'x', ''] and \
                        board.row_of_first_free_box(i + 3) == row:
                    board.move(i + 3, 'o')
                    return True

                elif board.get_row(row)[i:i + 4] == ['x', '', 'x', 'x'] and \
                        board.row_of_first_free_box(i + 1) == row:
                    board.move(i + 1, 'o')
                    return True

                elif board.get_row(row)[i:i + 4] == ['x', 'x', '', 'x'] and \
                        board.row_of_first_free_box(i + 2) == row:
                    board.move(i + 2, 'o')
                    return True
        return False

    def block_row_in_advanse(self, board):
        """
        Checks if a row of 2 x's can be blocked and makes a move to block it
        :param board: the list of lists where the moves are made
        :return: True if a row was blocked and False otherwise
        """
        for row in range(0, board.rows):
            for i in range(0, board.columns - 4):

                if board.get_row(row)[i:i + 5] == ['', '', 'x', 'x', ''] and \
                        board.row_of_first_free_box(i + 1) == row:
                    board.move(i + 1, 'o')
                    return True

                elif board.get_row(row)[i:i + 5] == ['', 'x', 'x', '', ''] and \
                        board.row_of_first_free_box(i + 3) == row:
                    board.move(i + 3, 'o')
                    return True

                elif board.get_row(row)[i:i + 5] == ['', 'x', '', 'x', ''] and \
                        board.row_of_first_free_box(i + 2) == row:
                    board.move(i + 2, 'o')
                    return True
        return False

    def block_column(self, board):
        """
        Checks if a column of 3 x's can be blocked and makes a move to block it
        :param board: the list of lists where the moves are made
        :return: True if a column was blocked and False otherwise
        """
        for column in range(0, board.columns):
            for i in range(0, board.rows - 2):

                if board.get_column(column)[i:i + 3] == ['x', 'x', 'x']:
                    if board.get_column(column)[i - 1] == '':
                        board.move(column, 'o')
                        return True

        return False

    def block_diagonal_right_to_left(self, board):
        """
        Checks if a column '\' of 3 x's can be blocked and makes a move to block it
        :param board: the list of lists where the moves are made
        :return: True if a column was blocked and False otherwise
        """
        column = -1
        for diagonal in board.get_diagonals_right_to_left():
            if len(diagonal) >= 4:
                column += 1
                for i in range(0, len(diagonal) - 3):
                    if diagonal[i:i + 4] == ['x', 'x', 'x', '']:
                        if column < 3 and board.row_of_first_free_box(3 - i) == column - i:
                            board.move(3 - i, 'o')
                            return True
                        elif column >= 3 and board.row_of_first_free_box(5 - column - i) == 2 - i:
                            board.move(5 - column - i, 'o')
                            return True

                    elif diagonal[i:i + 4] == ['', 'x', 'x', 'x']:
                        if column < 3 and board.row_of_first_free_box(6 - i) == column + 3 - i:
                            board.move(6 - i, 'o')
                            return True
                        elif column >= 3 and board.row_of_first_free_box(8 - column - i) == 5 - i:
                            print(board.get_diagonals_right_to_left())
                            board.move(8 - column - i, 'o')
                            return True
        return False

    def block_diagonal_left_to_right(self, board):
        """
        Checks if a column '/' of 3 x's can be blocked and makes a move to block it
        :param board: the list of lists where the moves are made
        :return: True if a column was blocked and False otherwise
        """
        column = -1
        for diagonal in board.get_diagonals_left_to_right():
            if len(diagonal) >= 4:
                column += 1
                for i in range(0, len(diagonal) - 3):
                    if diagonal[i:i + 4] == ['x', 'x', 'x', '']:
                        if column < 3 and board.row_of_first_free_box(3 + i) == column - i:
                            board.move(3 + i, 'o')
                            return True
                        elif column >= 3 and board.row_of_first_free_box(column + 1 + i) == 2 - i:
                            board.move(column + 1 + i, 'o')
                            return True

                    elif diagonal[i:i + 4] == ['', 'x', 'x', 'x']:
                        if column < 3 and board.row_of_first_free_box(i) == column + 3 - i:
                            board.move(i, 'o')
                            return True
                        elif column >= 3 and board.row_of_first_free_box(column - 2 + i) == 5 - i:
                            board.move(column - 2 + i, 'o')
                            return True

        return False

    def win_row_final_move(self, board):
        """
        Checks if there is a row of 3 o's and adds another one to win
        :param board: the list of lists where the moves are made
        :return: True if an 'o' is added and False otherwise
        """
        for row in range(0, board.rows):
            for i in range(0, board.columns - 3):

                if board.get_row(row)[i:i + 4] == ['', 'o', 'o', 'o'] and board.row_of_first_free_box(i) == row:
                    board.move(i, 'o')
                    return True

                elif board.get_row(row)[i:i + 4] == ['o', 'o', 'o', ''] and \
                        board.row_of_first_free_box(i + 3) == row:
                    board.move(i + 3, 'o')
                    return True

                elif board.get_row(row)[i:i + 4] == ['o', '', 'o', 'o'] and \
                        board.row_of_first_free_box(i + 1) == row:
                    board.move(i + 1, 'o')
                    return True

                elif board.get_row(row)[i:i + 4] == ['o', 'o', '', 'o'] and \
                        board.row_of_first_free_box(i + 2) == row:
                    board.move(i + 2, 'o')
                    return True
        return False

    def win_column(self, board):
        """
        Checks if there is a column of 3 o's and adds another one to win
        :param board: the list of lists where the moves are made
        :return: True if an 'o' is added and False otherwise
        """
        for column in range(0, board.columns):
            for i in range(0, board.rows - 2):

                if board.get_column(column)[i:i + 3] == ['o', 'o', 'o']:
                    if board.get_column(column)[i - 1] == '':
                        board.move(column, 'o')
                        return True

        return False

    def win_diagonal_right_to_left(self, board):
        """
        Checks if there is a column '\' of 3 o's and adds another one to win
        :param board: the list of lists where the moves are made
        :return: True if an 'o' is added and False otherwise
        """
        column = -1
        for diagonal in board.get_diagonals_right_to_left():
            if len(diagonal) >= 4:
                column += 1
                for i in range(0, len(diagonal) - 3):
                    if diagonal[i:i + 4] == ['o', 'o', 'o', '']:
                        if column < 3 and board.row_of_first_free_box(3 - i) == column - i:
                            board.move(3 - i, 'o')
                            return True
                        elif column >= 3 and board.row_of_first_free_box(5 - column - i) == 2 - i:
                            board.move(5 - column - i, 'o')
                            return True

                    elif diagonal[i:i + 4] == ['', 'o', 'o', 'o']:
                        if column < 3 and board.row_of_first_free_box(6 - i) == column + 3 - i:
                            board.move(6 - i, 'o')
                            return True
                        elif column >= 3 and board.row_of_first_free_box(8 - column - i) == 5 - i:
                            board.move(8 - column - i, 'o')
                            return True
        return False

    def win_diagonal_left_to_right(self, board):
        """
        Checks if there is a column '/' of 3 o's and adds another one to win
        :param board: the list of lists where the moves are made
        :return: True if an 'o' is added and False otherwise
        """
        column = -1
        for diagonal in board.get_diagonals_left_to_right():
            if len(diagonal) >= 4:
                column += 1
                for i in range(0, len(diagonal) - 3):
                    if diagonal[i:i + 4] == ['o', 'o', 'o', '']:
                        if column < 3 and board.row_of_first_free_box(3 + i) == column - i:
                            board.move(3 + i, 'o')
                            return True
                        elif column >= 3 and board.row_of_first_free_box(column + 1 + i) == 2 - i:
                            board.move(column + 1 + i, 'o')
                            return True

                    elif diagonal[i:i + 4] == ['', 'o', 'o', 'o']:
                        if column < 3 and board.row_of_first_free_box(i) == column + 3 - i:
                            board.move(i, 'o')
                            return True
                        elif column >= 3 and board.row_of_first_free_box(column - 2 + i) == 5 - i:
                            board.move(column - 2 + i, 'o')
                            return True

        return False

    def move_to_win(self, board):
        """
        Makes a move trying to win
        :param board: the list of lists where the moves are made
        :return: True if a move was made, False otherwise
        """
        for row in range(0, board.rows):
            for i in range(0, board.columns - 3):
                if board.get_row(row)[i:i+4] == ['o','o','',''] and \
                        board.row_of_first_free_box(i+2) == row:
                    board.move(i+2, 'o')
                    return True

                elif board.get_row(row)[i:i+4] == ['','o','o','']:
                    if board.row_of_first_free_box(i) == row:
                        board.move(i, 'o')
                        return True
                    elif board.row_of_first_free_box(i+3) == row:
                        board.move(i+3, 'o')
                        return True

                elif board.get_row(row)[i:i+4] == ['','','o','o'] and \
                        board.row_of_first_free_box(i+1) == row:
                    board.move(i+1, 'o')
                    return True

                elif board.get_row(row)[i:i+4] == ['o','','',''] and\
                        board.row_of_first_free_box(i+1) == row:
                    board.move(i+1,'o')
                    return True

                elif board.get_row(row)[i:i+4] == ['','o','','']:
                        if board.row_of_first_free_box(i) == row:
                            board.move(i,'o')
                            return True
                        elif board.row_of_first_free_box(i+2) == row:
                            board.move(i+2,'o')
                            return True

                elif board.get_row(row)[i:i+4] == ['','','o','']:
                        if board.row_of_first_free_box(i+1) == row:
                            board.move(i+1,'o')
                            return True
                        elif board.row_of_first_free_box(i+3) == row:
                            board.move(i+3,'o')
                            return True

                elif board.get_row(row)[i:i+4] == ['','','','o'] and\
                        board.row_of_first_free_box(i+2) == row:
                    board.move(i+2,'o')
                    return True

        for column in range(0, board.columns):
            for i in range(0, board.rows - 2):
                if board.get_column(column)[i:i + 3] == ['', 'o', 'o']:
                    board.move(column, 'o')
                    return True
            for i in range(0, board.rows - 1):
                if board.get_column(column)[i:i+2] == ['','o']:
                    board.move(column, 'o')
                    return True

        return False
