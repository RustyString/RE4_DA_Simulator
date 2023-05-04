from Points import Points


class Event:
    def __init__(self, event_description):
        self.event_description = event_description


class ItemPick(Event):
    def __init__(self, item):
        super().__init__(item)


class ItemLose(Event):
    def __init__(self, item):
        super().__init__(item)


class PerformAction(Event):
    def __init__(self, action):
        super().__init__(action)


class GetDamage(Event):
    def __init__(self, damage_source):
        super().__init__(damage_source)


class Scenario:
    def __init__(self, starting_item_points, events):
        self.events = events
        self.points = Points(starting_item_points)
        self.event_number = 0

    def run_scenario(self):
        self.log_event(None)
        for event in self.events:
            self.event_number += 1
            self.simulate_event(event)
            self.log_event(event)

    def simulate_event(self, event: Event):
        actions = {ItemPick: self.points.pick_item, ItemLose: self.points.lose_item,
                   PerformAction: self.points.perform_action, GetDamage: self.points.apply_damage_source}
        actions[type(event)](event.event_description)

    def log_event(self, event):
        event_name = str(type(event).__name__) + '_' + str(type(event.event_description).__name__) if event else 'Start'
        print(
            f'{self.event_number}. {event_name}, AP: {self.points.action_points}, IP: {self.points.item_points}, Total: {self.points.action_points + self.points.item_points},  multiplier: {self.points.get_multiplier()}')
