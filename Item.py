class Item:
    def __init__(self, points):
        self.points = points


class SMGAmmo(Item):
    def __init__(self):
        super().__init__(6)


class PistolAmmo(Item):
    def __init__(self):
        super().__init__(12)


class Bolt(Item):
    def __init__(self):
        super().__init__(15)


class SniperAmmo(Item):
    def __init__(self):
        super().__init__(36)


class KitchenKnife(Item):
    def __init__(self):
        super().__init__(40)


class ShotgunAmmo(Item):
    def __init__(self):
        super().__init__(50)


class BootKnife(Item):
    def __init__(self):
        super().__init__(60)


class MineRound(Item):
    def __init__(self):
        super().__init__(65)


class Grenade(Item):
    def __init__(self):
        super().__init__(70)


class HeavyGrenade(Item):
    def __init__(self):
        super().__init__(80)


class FlashGrenade(Item):
    def __init__(self):
        super().__init__(80)


class CombatKnife(Item):
    def __init__(self):
        super().__init__(250)


class GreenHerb(Item):
    def __init__(self):
        super().__init__(50)


class RedHerb(Item):
    def __init__(self):
        super().__init__(100)


class Resource(Item):
    def __init__(self):
        super().__init__(50)


class Gunpowder(Item):
    def __init__(self):
        super().__init__(5)
