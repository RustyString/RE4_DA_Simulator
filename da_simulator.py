from Scenario import Scenario, ItemLose, ItemPick, PerformAction, GetDamage
import Item
import DamageSource
import Action


def simulate(starting_item_points, events):
    scenario = Scenario(starting_item_points, events)
    scenario.run_scenario()


if __name__ == '__main__':
    meta_events = [GetDamage(DamageSource.Grab()),
                   GetDamage(DamageSource.GrabTick()),
                   GetDamage(DamageSource.GrabTick()),
                   PerformAction(Action.Bonus()),
                   PerformAction(Action.Kill()),
                   PerformAction(Action.Kill())]
    starting_ip = 1400
    simulate(starting_ip, meta_events)
