"""
Playing engine for WARRIORS, ROBBERS AND WIZARDS GAME
"""

from models import Player, Enemy
from exceptions import EnemyDown, GameOver
import settings


def get_player_name():
    """Getting player name from terminal"""
    player_name = ""
    while not player_name:
        player_name = input("ENTER YOUR NAME: ").strip()
    return player_name


def add_score(points):
    """Adding extra scores"""
    points += settings.EXTRA_SCORE_POINTS_ADD
    return points


def play():
    """Playing engine"""
    player_name = get_player_name()
    player = Player(player_name)
    enemy = Enemy()

    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown:
            player.score_points = add_score(player.score_points)
            enemy = Enemy(enemy.level + 1)
        except GameOver:
            break
        except KeyboardInterrupt:
            raise GameOver(player, "KeyboardInterrupt")


if __name__ == '__main__':
    play()
