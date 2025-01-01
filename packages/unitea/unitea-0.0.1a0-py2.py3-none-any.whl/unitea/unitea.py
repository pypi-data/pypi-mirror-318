import argparse
import fcntl
import logging
import os
import sys

from utils import monitor_file_for_external_modification
from utils import import_optional_module
from utils import get_text_after_prompt
from utils import GameArgumentError

Global_last_internal_modification_time = None
BASE_GAME_DIR = os.path.join("unitea", "games")


def capitalize_first_letter(s):
    if not s:
        return s
    return s[0].upper() + s[1:]


def get_file_modification_time(filename):
    # TODO: dedup
    return os.stat(filename).st_mtime


def save_file(filename, file_contents):
    logging.debug("save_file")

    global Global_last_internal_modification_time
    # TODO: dedup with save_file()
    try:
        with open(filename, "w") as file:
            fcntl.flock(file, fcntl.LOCK_EX)
            file.write(file_contents)
            Global_last_internal_modification_time = get_file_modification_time(filename)
            fcntl.flock(file, fcntl.LOCK_UN)
    except Exception as e:
        logging.error(f"Failed to save file {filename}: {e}")


def load_file(filename):
    logging.debug("load_file")

    # TODO: dedup with load_file()
    try:
        with open(filename, "r") as file:
            fcntl.flock(file, fcntl.LOCK_SH)
            file_content = file.read()
            Global_last_internal_modification_time = get_file_modification_time(filename)
            fcntl.flock(file, fcntl.LOCK_UN)

            return file_content
    except Exception as e:
        logging.error(f"Failed to load file {filename}: {e}")


def get_game_class(game):
    game_module = f"games.{game}.{game}"
    game_class = f"{game.title()}GameEngine"
    return getattr(import_optional_module(game_module), game_class)


def is_installed(game):
    try:
        get_game_class(game)
        return True
    except ModuleNotFoundError:
        return False


def get_description(game):
    return get_game_class(game).get_game_description() if is_installed(game) else ""


def get_run_examples(game):
    if is_installed(game):
        return (
            "\n       [" + f"{' '.join([game] + args[:-1]).strip()}]: {capitalize_first_letter(args[-1]).rstrip('.')}."
            for args in get_game_class(game).get_run_examples()
        )
    else:
        return ""


def get_install_command(game):
    return "pip install -r " + os.path.join(BASE_GAME_DIR, game, "requirements.txt")


PROMPT = "Your game choice (enter choice and save file):"


def welcome_message(available_games, available_commands):
    games_details = (
        (
            game,
            is_installed(game),
            get_description(game),
            get_run_examples(game),
        )
        for game in available_games
    )
    # move installed games first
    games_details = sorted(games_details, key=lambda x: (x[1] == False, x[0]))

    available_games_str = "\n".join(
        f" - {game}" + ("  (not installed)" if not installed else f": {descr}") + "\n"
        + ("     Install with: [" + get_install_command(game) + "]\n" if not installed else "")
        + ("     Run with:" + "".join(run_examples) + "\n" if run_examples else "")
        for game, installed, descr, run_examples in games_details
    )

    available_commands_str = "\n".join(
        f" - [{cmd}]: {desc}" for cmd, (desc, _) in available_commands.items()
    )

    return f"""Welcome to UniTEA!

Available games:
{available_games_str}
Available commands (replace file contents with a command and save file):
{available_commands_str}

{PROMPT}
"""


def select_game(game_info, game_name, game_args):
    game_info["selected_game"] = game_name
    game_info["game_args"] = game_args


def unselect_game(game_info):
    game_info.pop("selected_game", None)
    game_info.pop("game_args", None)


def goto_main_menu(game_info):
    game_info.pop("game", None)
    unselect_game(game_info)


def replay_game(game_info):
    game_info.pop("game", None)


def game_step(game_info):
    logging.debug(f"game_step()")

    user_input = load_file(game_info["state_file"])
    text = ""

    available_commands = {
        "menu": ("go to main menu", goto_main_menu),
        "replay": ("replay current game with same arguments", replay_game),
    }

    user_input = user_input.strip()
    if user_input in available_commands:
        _, callback = available_commands[user_input]
        callback(game_info)

    # game has not been initialize yet
    if "game" not in game_info:
        # user has not selected a game yet
        if "selected_game" not in game_info:
            user_input = get_text_after_prompt(user_input, PROMPT)
            logging.debug(f"user_input = [{user_input}]")
            user_input_tokens = user_input.split()
            if len(user_input_tokens) and user_input_tokens[0] in game_info["available_games"]:
                # user just selected a game
                select_game(game_info, user_input_tokens[0], user_input_tokens[1:])

                return game_step(game_info)
            else:
                text = welcome_message(game_info["available_games"], available_commands)
        # user has selected a game -> initialize game
        else:
            selected_game = game_info["selected_game"]
            try:
                game_info["game"] = get_game_class(selected_game)(*game_info["game_args"])
                text = game_info["game"].render_world()
            except ModuleNotFoundError:
                text = f"{selected_game} is not installed. You may install it with:\n"
                text += get_install_command(selected_game)
                unselect_game(game_info)
            except GameArgumentError:
                text = f"Wrong arguments. Run with: {''.join(get_run_examples(selected_game))}"
                unselect_game(game_info)
    # game initialized -> progress game based on user input
    else:
        game_info["game"].progress_game(user_input)
        text = game_info["game"].render_world()

    save_file(game_info["state_file"], text)


def create_game(gamename):
    gamename = gamename.replace("_", "").replace("-", "").lower()
    dirname = os.path.join(BASE_GAME_DIR, gamename)
    os.mkdir(dirname)
    filepath = os.path.join(dirname, f"{gamename}.py")
    save_file(
        filepath,
        f"""from abstract_game_engine import AbstractGameEngine


{open(os.path.join('unitea', 'abstract_game_engine.py')).read()}
""".replace(
            "class AbstractGameEngine", f"class {gamename.title()}GameEngine(AbstractGameEngine)"
        ),
    )
    logging.info(f"File {filepath} created.")


def play_game(filename):
    games = [
        dir
        for dir in (entry.name for entry in os.scandir(BASE_GAME_DIR) if entry.is_dir())
        if os.path.isfile(os.path.join(BASE_GAME_DIR, dir, f"{dir}.py"))
    ]

    game_info = {
        "available_games": games,
        "state_file": filename,
    }

    # empty file contents
    save_file(game_info["state_file"], "")

    # run game step once
    game_step(game_info)
    # run game step each time the disk file is modified
    monitor_file_for_external_modification(
        game_info["state_file"],
        lambda: Global_last_internal_modification_time,
        lambda: game_step(game_info),
    )


def main():
    logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] [%(levelname)s] %(message)s")

    parser = argparse.ArgumentParser(description="UniTEA - play games on your text editor.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--create", metavar="GAMENAME", help="Create a new game file with the specified name."
    )
    group.add_argument("--play", metavar="FILENAME", help="Play a game from the specified file.")

    args = parser.parse_args()

    if args.create:
        create_game(args.create)
    elif args.play:
        play_game(args.play)


if __name__ == "__main__":
    main()
