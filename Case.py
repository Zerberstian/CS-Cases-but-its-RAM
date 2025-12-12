class Case:
    def __init__(self, name, loot=[]):
        self.name = name
        self.loot = loot 
        self.is_open = False

    def open(self):
        self.is_open = True


class Case1(Case):
    def __init__(self, name, loot=[]):
        super().__init__(name, loot)


class Case2(Case):
    def __init__(self, name, loot=[]):
        super().__init__(name, loot)


class Case3(Case): 
    def __init__(self, name, loot=[]):
        super().__init__(name, loot) 
