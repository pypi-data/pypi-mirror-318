from minesweeper import core

from abstract_game_engine import AbstractGameEngine
from utils import GameArgumentError
from utils import get_text_after_prompt


PROMPT = "Use 'X' to mark a mine, 'O' to open a tile:\n\n"
DIFFICULTIES = {
    #          rows cols mines
    'easy':   (  9,   9,   10),
    'medium': ( 16,  16,   40),
    'hard':   ( 16,  30,   99),
}


class MinesweeperGameEngine(AbstractGameEngine):
    @staticmethod
    def get_game_description():
        return "Minesweeper game!"

    @staticmethod
    def get_run_examples():
        return [
            ["", "play game with default settings."],
            ["DIFFICULTY", f"play game with given difficulty ({', '.join(DIFFICULTIES.keys())})."],
        ]

    def __init__(self, *args):
        if len(args) > 1 or (len(args) == 1 and args[0] not in DIFFICULTIES):
            raise GameArgumentError

        difficulty = args[0] if len(args) else list(DIFFICULTIES.keys())[0]
        rows, cols, mines = DIFFICULTIES[difficulty]
        self.board = core.Board(rows=rows, cols=cols, mines=mines)
        self.mines_marked = [""] * self.board.rows * self.board.cols

        self.tile_map = {
            "t": " ",  # unopened tile
            "x": "@",  # mine
            "0": "-",
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
        }

    def _mark_tile_as_mine(self, i, j):
        self.mines_marked[i * self.board.cols + j] = "X"

    def _get_tile(self, i, j):
        return "X" if self.mines_marked[i][j] and cur_board[i][j] == " " else cur_board[i][j]

    def _get_existing_board(self):
        # 1D: [self.tile_map[t] for t in str(self.board).split()]
        # 2D: [[self.tile_map[t] for t in row.split()] for row in str(self.board).split("\n")]
        cur_board = [self.tile_map[t] for t in str(self.board).split()]
        return [
            "X" if self.mines_marked[i] and cur_board[i] == " " else cur_board[i]
            for i in range(len(cur_board))
        ]

    def render_world(self):
        res = PROMPT
        cur_board = self._get_existing_board()
        for i in range(self.board.rows):
            res += "|" + "|".join(
                cur_board[i * self.board.cols + j] for j in range(self.board.cols)
            ) + "|\n"

        if self.board.is_game_over:
            res += "\nYou lost!"
        elif self.board.is_game_finished:
            res += "\nYou won!"

        return res

    def progress_game(self, user_input):
        if not self.board.is_game_over and not self.board.is_game_finished:
            prev_board = "".join(self._get_existing_board())
            cur_board = "".join(get_text_after_prompt(user_input, PROMPT).strip().split("\n")).replace("|", "")

            # print(f"prev   [{prev_board}]")
            # print(f"cur:   [{cur_board}]")
            # print(f"mines: [" + "".join(f"{x:1}" for x in self.mines_marked) + "]")

            if len(prev_board) != self.board.rows * self.board.cols or \
                len(cur_board) != self.board.rows * self.board.cols:
                return

            # if user changed cell which was previously unopened
            indices_of_diffs = [i for i in range(len(cur_board)) if prev_board[i] != cur_board[i]]
            for index in (i for i in indices_of_diffs if prev_board[i] == " "):
                row = index // self.board.rows
                col = index % self.board.cols
                print(f"user entered {cur_board[index].upper()} in [{row}, {col}]")

                if cur_board[index].upper() == "O":
                    self.board.tile_open(row, col)
                elif cur_board[index].upper() == "X":
                    self._mark_tile_as_mine(row, col)

                if self.board.is_game_over or self.board.is_game_finished:
                    break
