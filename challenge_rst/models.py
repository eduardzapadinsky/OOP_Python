"""
Behavior description for WARRIORS, ROBBERS AND WIZARDS GAME
"""

from random import randint

import settings
from exceptions import EnemyDown, GameOver


class Enemy:
    """Create game enemy"""

    def __init__(self, level: int = 1):
        self.health = level
        self.level = level

    @staticmethod
    def fight_choice_select():
        """Select person choice for enemy"""
        random_person = str(randint(1, 3))
        return random_person

    def decrease_health(self, score_down):
        """Decrease enemy health"""
        self.health -= score_down
        if self.health > 0:
            return self.health
        else:
            raise EnemyDown(self.level)

    def select_attack(self):
        """Select person choice for attack"""
        attack_choice = self.fight_choice_select()
        return attack_choice

    def select_defence(self):
        """Select person choice for defence"""
        defence_choice = self.fight_choice_select()
        return defence_choice


class Player:
    """Create game player"""

    def __init__(self, name: str):
        self.name = name
        self.health_points = settings.INITIAL_PLAYER_HEALTH
        self.score_points = 0

    def __repr__(self):
        return f"Player - {self.name}"

    def write_to_file(self):
        """Write game results to the file"""
        data = f"Name - {self.name}, score points: {self.score_points}\n"
        with open("scores.txt", "a") as file:
            file.write(data)

    @staticmethod
    def fight_choice_select():
        """Select person choice for player"""

        fight_choice = ''
        while fight_choice not in ["1", "2", "3"]:
            fight_choice = input(
                "MAKE A FIGHT CHOICE FROM (WARRIOR - 1, ROBBER - 2, WIZARD - 3): "
            )
        return fight_choice

    def decrease_health(self, score_down):
        """Decrease player health"""

        self.health_points -= score_down
        if self.health_points > 0:
            return self.health_points
        else:
            self.write_to_file()
            raise GameOver(self)

    def select_attack(self):
        """Select person choice for attack manually"""

        attack_choice = self.fight_choice_select()
        return attack_choice

    def select_defence(self):
        """Select person choice for defence manually"""

        defence_choice = self.fight_choice_select()
        return defence_choice

    @staticmethod
    def fight(attack_choice, defence_choice):
        """Fight results determination"""
        if [attack_choice, defence_choice] in [
            ["1", "2"],
            ["2", "3"],
            ["3", "1"]
        ]:
            return 'win'
        elif attack_choice == defence_choice:
            return 'draw'
        else:
            return 'loss'

    def attack(self, enemy: Enemy):
        """Attack an enemy"""
        attack_choice = self.select_attack()
        defence_choice = enemy.select_defence()
        fight_result = self.fight(attack_choice, defence_choice)
        if fight_result == 'win':
            try:
                print('YOUR ATTACK IS SUCCESSFUL!')
                self.score_points += settings.SCORE_PLAYER_ADD
                enemy.decrease_health(settings.SCORE_ENEMY_DOWN)
            except EnemyDown:
                raise
        elif fight_result == 'loss':
            print('YOUR ATTACK IS FAILED!')
        elif fight_result == 'draw':
            print("IT'S A DRAW!")

    def defence(self, enemy: Enemy):
        """Defence from an enemy"""

        defence_choice = self.select_attack()
        attack_choice = enemy.select_defence()
        fight_result = self.fight(attack_choice, defence_choice)
        if fight_result == 'win':
            try:
                print('YOUR DEFENCE IS FAILED!')
                self.decrease_health(settings.SCORE_PLAYER_DOWN)
            except GameOver:
                raise
        elif fight_result == 'loss':
            print('YOUR DEFENCE IS SUCCESSFUL!')

        elif fight_result == 'draw':
            print("IT'S A DRAW!")
