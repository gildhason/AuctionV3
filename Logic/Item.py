class Item:
    def __init__(self, name, startingPrice, donor):
        self.id = None
        self.name = name
        self.startingPrice = startingPrice
        self.donor = donor
        self.buyer = None
        self.endingPrice = None

    def setID(self, idIn):
        self.id = idIn