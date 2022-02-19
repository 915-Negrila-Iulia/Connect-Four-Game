import unittest

from app.AI.strategy import Strategy
from app.Domain.board import Board


class AiTest(unittest.TestCase):
    def test_ai(self):
        strategy = Strategy()

        block_row = Board()
        for i in range(1,4):
            block_row.move(i,'x')
        self.assertEqual(strategy.block_row_final_move(block_row), True)

        block_column = Board()
        for i in range(0,3):
            block_column.move(1,'x')
        self.assertEqual(strategy.block_column(block_column), True)
        self.assertEqual(strategy.block_column(block_row), False)

        empty_board = Board()
        self.assertEqual(strategy.block_diagonal_right_to_left(empty_board), False)
        self.assertEqual(strategy.block_diagonal_left_to_right(empty_board), False)

        win_row = Board()
        for i in range(0,3):
            win_row.move(i,'o')
        self.assertEqual(strategy.win_row_final_move(win_row), True)

        win_column = Board()
        for i in range(0,3):
            win_column.move(1,'o')
        self.assertEqual(strategy.win_column(win_column), True)

        block_diagonal = Board()
        for i in range(0,2):
            block_diagonal.move(i,'o')
        for i in range(2,4):
            block_diagonal.move(i,'x')
        for i in range(0,2):
            block_diagonal.move(i,'o')
        for i in range(0,3):
            block_diagonal.move(i,'x')
        self.assertEqual(strategy.block_diagonal_right_to_left(block_diagonal), True)