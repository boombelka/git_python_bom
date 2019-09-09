class Inventory():
    def __init__(self, size=1, hitpoint=1, weight=1):
        self.size = size
        self.hitpoint = hitpoint
        self.weight = weight

class Coin(Inventory):
    def __init__(self, size=0, hitpoint=0, weight=1):
        Inventory.__init__(self, size=1, hitpoint=1, weight=1)
        self.size = size
        self.hitpoint = hitpoint
        self.weight = weight

    def __str__(self):
        return 'Монета'


class Rubin(Inventory):
    def __init__(self, size=0, hitpoint=0, weight=1):
        Inventory.__init__(self, size=1, hitpoint=1, weight=1)
        self.size = size
        self.hitpoint = hitpoint
        self.weight = weight

    def __str__(self):
        return 'Рубин'


class Might(Inventory):
    def __init__(self, size=0, hitpoint=0, weight=1):
        Inventory.__init__(self, size=1, hitpoint=1, weight=1)
        self.size = size
        self.hitpoint = hitpoint
        self.weight = weight

    def __str__(self):
        return 'Меч-кладенец'