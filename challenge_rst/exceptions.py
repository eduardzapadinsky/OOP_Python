"""
Exceptions for WARRIORS, ROBBERS AND WIZARDS GAME
"""


class EnemyDown(Exception):
    """Raised when enemy is defeated"""

    def __init__(self, level):
        super().__init__()
        self.level = level
        print(f"Enemy level {self.level} is defeated")

    def __dir__(self):
        return "EnemyDown Exception"


class GameOver(Exception):
    """Raised when player is defeated"""

    def __init__(self, player, *args):
        super().__init__()
        self.name = player.name
        self.points = player.score_points
        print(f"\n{self.name} is defeated \n"
              f"SCORE POINTS: {self.points}")
        if not args:
            print("GOOD BYE!")
