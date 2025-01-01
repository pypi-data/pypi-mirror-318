import logging
import random

from abstract_game_engine import AbstractGameEngine
from utils import get_text_after_prompt, GameArgumentError

PROMPT = "Your guess: "
MAX_NUM = 1000
MAX_TRIES = 10

class NumberguessGameEngine(AbstractGameEngine):
    @staticmethod
    def get_game_description():
        return "Guess the number in less than 10 tries!"

    @staticmethod
    def get_run_examples():
        return [
            ["", f"use a random number in [1, {MAX_NUM}]."],
            ["MYNUMBER", "use this number"],
        ]

    def __init__(self, *args):
        if len(args) > 1 or (len(args) == 1 and int(args[0]) not in range(1, MAX_NUM + 1)):
            raise GameArgumentError

        self.number = random.randint(1, MAX_NUM) if len(args) == 0 else int(args[0])
        logging.debug(f"Number: {self.number}")
        self.tries_left = MAX_TRIES
        self.last_guess = None

    def render_world(self):
        res = ""
        if self.last_guess != None:
            if self.last_guess == self.number:
                res += "You found it!"
            else:
                if self.last_guess > self.number:
                    res += "Very large!\n"
                elif self.last_guess < self.number:
                    res += "Very small!\n"
                res += "Tries left: {}\n".format(self.tries_left)
                res += "\n" + PROMPT
        else:
            res += PROMPT

        return res

    def progress_game(self, user_input):
        if self.tries_left > 0 and self.last_guess != self.number:
            user_input = get_text_after_prompt(user_input, PROMPT).strip()
            if user_input:
                try:
                    guess = int(user_input)
                    if guess:
                        self.last_guess = guess
                        self.tries_left -= 1
                except ValueError:
                    pass
