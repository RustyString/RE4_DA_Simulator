class DamageSource:
    def __init__(self, damage):
        self.damage = damage


class Grenade(DamageSource):
    def __init__(self):
        super().__init__(770)


class Tripwire(DamageSource):
    def __init__(self):
        super().__init__(1320)


class Barrel(DamageSource):
    def __init__(self):
        super().__init__(1320)


class Punch(DamageSource):
    def __init__(self):
        super().__init__(220)


class ThrownAxe(DamageSource):
    def __init__(self):
        super().__init__(330)


class CrossBow(DamageSource):
    def __init__(self):
        super().__init__(330)


class Torch(DamageSource):
    def __init__(self):
        super().__init__(550)


class Swing(DamageSource):
    def __init__(self):
        super().__init__(660)


class CleanHit(DamageSource):
    def __init__(self):
        super().__init__(770)


class ShovelBonk(DamageSource):
    def __init__(self):
        super().__init__(880)


class Grab(DamageSource):
    def __init__(self):
        super().__init__(440)


class GrabTick(DamageSource):
    def __init__(self):
        super().__init__(33)


class FireTick(DamageSource):
    def __init__(self):
        super().__init__(50)
