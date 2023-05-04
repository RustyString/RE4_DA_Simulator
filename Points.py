from Action import Action
from DamageSource import DamageSource
from Item import Item

MAX_AP = 5000
MIN_AP = -5000
INITIAL_AP = 5000


class Points:
    def __init__(self, item_points):
        self.action_points = INITIAL_AP
        self.item_points = item_points

    def pick_item(self, item: Item):
        self.item_points += item.points

    def lose_item(self, item: Item):
        self.item_points -= item.points

    def perform_action(self, action: Action):
        self.action_points += action.points
        if self.action_points > MAX_AP:
            self.action_points = MAX_AP

    def get_multiplier(self):
        total_points = self.action_points + self.item_points
        multiplier = 0.1 * int(total_points // 1000) + 0.6
        return multiplier

    def apply_damage_source(self, damage_source: DamageSource):
        multiplier = self.get_multiplier()
        self.action_points -= multiplier * damage_source.damage
        if self.action_points < MIN_AP:
            self.action_points = MIN_AP
