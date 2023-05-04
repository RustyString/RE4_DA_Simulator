class Action:
    def __init__(self, points):
        self.points = points


class QTEDodge(Action):
    def __init__(self):
        super().__init__(30)


class Kick(Action):
    def __init__(self):
        super().__init__(80)


class ForwardKick(Action):
    def __init__(self):
        super().__init__(110)


class Parry(Action):
    def __init__(self):
        super().__init__(150)


class GroundStab(Action):
    def __init__(self):
        super().__init__(200)


class Stab(Action):
    def __init__(self):
        super().__init__(220)


class StealthKill(Action):
    def __init__(self):
        super().__init__(250)


class Suplex(Action):
    def __init__(self):
        super().__init__(250)


class Kill(Action):
    def __init__(self):
        super().__init__(50)


class Bonus(Action):
    def __init__(self):
        super().__init__(500)
