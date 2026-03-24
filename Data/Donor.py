class Donor:
    def __init__(self, donorID, name, address):
        self.donorID = donorID
        self.name = name
        self.address = address
        self.items = []

    def addItem(self, item):
        self.items.append(item)