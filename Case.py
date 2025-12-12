class Case:
    def __init__(self, name, loot=None):
        self.name = name
        self.loot = loot if loot is not None else []
        self.is_open = False

    def open(self):
        self.is_open = True


class DDR3(Case):
    DEFAULT_LOOT = ["DDR3 8 GB", "DDR3 16 GB", "DDR3 32 GB"]

    def __init__(self, name):
        super().__init__(name, loot=list(self.DEFAULT_LOOT))


class DDR4(Case):
    DEFAULT_LOOT = ["DDR4 8 GB", "DDR4 16 GB", "DDR4 32 GB"]

    def __init__(self, name):
        super().__init__(name, loot=list(self.DEFAULT_LOOT))


class DDR5(Case):
    DEFAULT_LOOT = ["DDR5 8 GB", "DDR5 16 GB", "DDR5 32 GB"]

    def __init__(self, name):
        super().__init__(name, loot=list(self.DEFAULT_LOOT))

class Mixed(Case):
     DEFAULT_LOOT = ["DDR5 8 GB", "DDR5 16 GB", "DDR5 32 GB"]

    def __init__(self, name):
        super().__init__(name, loot=list(self.DEFAULT_LOOT))
