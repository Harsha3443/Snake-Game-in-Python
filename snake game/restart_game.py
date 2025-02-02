from scoreboard import Scoreboard
scoreboard=Scoreboard()
class RestartGame:
    def __init__(self, game_screen, game_function):
        print('Click "r" to restart')
        self.game_screen = game_screen
        self.game_function = game_function
        self.game_screen.listen()
        self.game_screen.onkey(self.restart_game, "r")

    def restart_game(self):
        print("Game is restarting...")
        self.game_screen.reset()
        self.game_function()
        scoreboard.reset_score()