from toetactic.tictactoe import TicTacToe

from abstract_game_engine import AbstractGameEngine
from utils import get_text_after_prompt, GameArgumentError


PROMPT = "Enter 'X' on the tile of your choice:\n\n"


class TictactoeGameEngine(AbstractGameEngine):
    @staticmethod
    def get_game_description():
        return "The classic Tic-Tac-Toe game."

    @staticmethod
    def get_run_examples():
        return [
            ["", "play versus computer. You start first."],
        ]

    def __init__(self, *args):
        if len(args) != 0:
            raise GameArgumentError

        self._reset()

    def _reset(self):
        self.game = TicTacToe()

    def render_world(self):
        board = self.game.get_board()
        res = PROMPT
        for row in board:
            res += "|" + "|".join(row) + "|\n"

        if self.game.is_over():
            winner = self.game.get_winner()
            if winner:
                res += f"\n{'User' if winner == 'X' else 'Computer'} wins!"
            else:
                res += f"\nIt's a draw!"

        return res

    def progress_game(self, user_input):
        prev_board = "".join(f"{x}" for row in self.game.get_board() for x in row)
        cur_board = "".join(get_text_after_prompt(user_input, PROMPT).strip().split("\n")).replace("|", "")

        if cur_board == "restart":
            self._reset()

        # user maybe added or deleted more characters than she should
        if len(prev_board) != 9 or len(cur_board) != 9:
            return

        # if user only changed a single cell which was previously empty
        # (we don't care what character was entered in that cell)
        diffs = [i for i in range(len(cur_board)) if prev_board[i] != cur_board[i]]
        if len(diffs) == 1 and prev_board[diffs[0]] == " ":
            index = diffs[0]
            row = index // 3
            col = index % 3

            self.game.user_move(row, col)
            if not self.game.is_over():
                self.game.computer_move()
