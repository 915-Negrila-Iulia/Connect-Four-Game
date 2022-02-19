
from app.Domain.validator import MoveValidator
from app.Game.game import ConnectFour

class Console:
    def __init__(self):
        self._game = ConnectFour()
        self._validator = MoveValidator()

    def read_human_move(self):
        column = int(input('Choose column: '))
        self._validator.validate_move(column)
        self._game.human_move(column)

    def start(self):
        stop = False
        human_turn = True

        while not stop:
            try:
                if(human_turn):
                    print("my turn (x):")
                else:
                    print("computer's turn (o):")
                print(self._game.board)
                if human_turn:
                    self.read_human_move()
                    if self._game.board.check_win() == 'x':
                        print("Congrats, you won!")
                        print(self._game.board)
                        stop=True
                else:
                    self._game.computer_move()
                    if self._game.board.check_win() == 'o':
                        print("Sorry, you lost!")
                        print(self._game.board)
                        stop=True
                human_turn = not human_turn
            except Exception as exception:
                print(str(exception))