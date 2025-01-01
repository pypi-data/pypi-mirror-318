import os

from bink.story import Story, story_from_file

from abstract_game_engine import AbstractGameEngine
from utils import get_text_after_prompt, GameArgumentError

PROMPT = ">"
DEFAULT_STORY = "unitea/games/ink/example/intercept.ink.json"


class InkGameEngine(AbstractGameEngine):
    @staticmethod
    def get_game_description():
        return "Play an Ink story."

    @staticmethod
    def get_run_examples():
        return [
            ["", "Play the Intercept story"],
            ["MYSTORY.json", "use this story"],
        ]

    def __init__(self, *args):
        if len(args) > 1:
            raise GameArgumentError

        story_file = args[0] if len(args) else DEFAULT_STORY
        assert os.path.isfile(story_file) and os.access(story_file, os.R_OK), f"Could not open file: {story_file}"
        self.story = story_from_file(story_file)
        self.cached_world_render = None

        assert self.story.can_continue()

    def render_world(self):
        if self.cached_world_render == None:
            res = ""

            # render story
            while self.story.can_continue():
                line = self.story.cont()
                res += line

            # render user choices
            choices = self.story.get_current_choices()
            if choices:
                indent = ""
                res += f"\n"
                res += f"{indent}.{'-' * 50}\n"
                res += f"{indent}| Choices:\n"
                res += f"{indent}|{'-' * 50}\n"
                for i, text in enumerate(choices):
                    res += f"{indent}| {i + 1}) {text}\n"
                res += f"{indent}`{'-' * 50}\n"

            self.cached_world_render = res.strip()

        return self.cached_world_render + (
            f"\n\n{PROMPT} " if not self._has_game_ended() else "\n<Game over>"
        )

    def progress_game(self, user_input):
        user_input = get_text_after_prompt(user_input, PROMPT)

        if user_input != None:
            choices = self.story.get_current_choices()

            try:
                choice_idx = int(user_input) - 1
            except ValueError:
                # TODO: RENDER ON TEXT EDITOR THIS CHOICE
                print(f"Bad choice [{user_input}] (select number 1-{len(choices)})")
                return

            if choice_idx in range(len(choices)):
                self.story.choose_choice_index(choice_idx)
                self.cached_world_render = None
            else:
                # TODO: RENDER ON TEXT EDITOR THIS CHOICE
                print(f"Bad choice [{choice_idx}] (select number 1-{len(choices)})")
                return

    def _has_game_ended(self):
        return not self.story.get_current_choices()
