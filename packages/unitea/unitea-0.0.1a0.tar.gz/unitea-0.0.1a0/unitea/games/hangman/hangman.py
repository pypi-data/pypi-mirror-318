from hangman.model import Hangman
from hangman.utils import GameLost, GameWon

from abstract_game_engine import AbstractGameEngine
from utils import get_text_after_prompt, GameArgumentError

PROMPT = "Your letter:"


class HangmanGameEngine(AbstractGameEngine):
    @staticmethod
    def get_game_description():
        return "Can you guess the hidden word in less than 7 tries?"

    @staticmethod
    def get_run_examples():
        return [
            ["", "use random word"],
            ["MYWORD", "use the word MYWORD"],
        ]

    def __init__(self, *args):
        if len(args) > 1:
            raise GameArgumentError

        self._reset(args[0] if len(args) else None)

    def _reset(self, word):
        self.game = Hangman(answer=word)
        self.game.MAX_TURNS = 7
        self.player_won = None

    def render_world(self):
        bachslash = "\\"
        wrong_guesses = self.game.MAX_TURNS - self.game.remaining_turns
        show_if = lambda char, num: char if wrong_guesses >= num else ""
        res = f"""
   +------
   |    {show_if('|', 1)}
   |    {show_if('O', 2)}
   |   {show_if('/', 3)}{show_if('|', 4)}{show_if(bachslash, 5)}
   |   {show_if('/', 6)} {show_if(bachslash, 7)}
   |
   |
=========

"""
        res += f"Status:     {' '.join(self.game.status)}\n"
        res += f"Misses:     {', '.join(self.game.misses)}\n"
        res += f"Tries left: {self.game.remaining_turns}"
        if self.player_won == True:
            res += f"\n\nYou won!"
        elif self.player_won == False:
            res += f"\n\nGame over!\nThe word was: {self.game.answer}."
        else:
            res += f"\n\n{PROMPT} "

        return res

    def progress_game(self, user_input):
        user_input = get_text_after_prompt(user_input, PROMPT)

        if len(user_input.split()) == 2 and user_input.split()[0] == "restart":
            self._reset(user_input.split()[1])
            return

        try:
            self.game.guess(user_input)
        except ValueError:
            pass
        except GameLost:
            self.player_won = False
        except GameWon:
            self.player_won = True
