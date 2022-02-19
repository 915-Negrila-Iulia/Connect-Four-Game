
class GameException(Exception):
    pass


class MoveValidator:
    @staticmethod
    def validate_move(column):
        if not (0 <= column <= 6):
            raise GameException("Columns are between 0 and 6")
