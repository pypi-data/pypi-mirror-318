class AbstractGameEngine:
    @staticmethod
    def get_game_description():
        raise NotImplementedError

    @staticmethod
    def get_run_examples():
        raise NotImplementedError

    def __init__(self, *args):
        raise NotImplementedError

    def render_world(self):
        raise NotImplementedError

    def progress_game(self, user_input):
        raise NotImplementedError
