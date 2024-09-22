class Address:
    def __init__(self, index, town, street, house, flat):
        self.index = index
        self.town = town
        self.street = street
        self.house = house
        self.flat = flat

    def getAddress(self):
        return f'{self.index}, {self.town}, {self.street}, {self.house}-{self.flat}'
