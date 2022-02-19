
from app.AI.strategy import Strategy
from app.Domain.board import Board

class ConnectFour:
    def __init__(self):
        self._board = Board()
        self._strategy = Strategy()

    @property
    def board(self):
        return self._board

    def human_move(self, column):
        return self._board.move(column,'x')

    def computer_move(self):
        return self._strategy.next_move(self._board)

