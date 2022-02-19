import unittest

from app.Domain.board import Board


class BoardTest(unittest.TestCase):
    def test_board(self):

        board = Board()
        number_of_columns = 7
        number_of_rows = 6

        for i in range(number_of_rows):
            for j in range(number_of_columns):
                self.assertEqual(board.get_board[i][j], '')

        row = 5
        column = 3
        board.move(column, 'x')
        self.assertEqual(board.get_board[row][column], 'x')
        try:
            board.move(column, 'p')
            assert False
        except Exception:
            assert True

        self.assertEqual(len(board.get_diagonals()), 24)

        board.move(4, 'o')
        board.move(5, 'x')
        board.move(2, 'x')
        board.move(3, 'x')
        board.move(4, 'o')
        board.move(4, 'x')
        board.move(5, 'o')
        board.move(5, 'o')
        board.move(5, 'x')
        board.move(6, 'o')
        board.move(6, 'o')
        board.move(6, 'o')
        board.move(6, 'x')
        self.assertEqual(board.check_win(), 'x')
