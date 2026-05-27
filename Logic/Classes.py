
class Object:
    def __init__(self, idIn, nameIn):
        self.id = idIn
        self.name = nameIn

    def save(self, file):
        file.dumps(vars(self))

class Donor(Object):
    def __init__(self, idIn, nameIn, addressIn, itemsIn=[]):
        super().__init__(idIn, nameIn)
        self.address = addressIn
        self.items = itemsIn

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Address: {self.address}"

class Item(Object):
    def __init__(self, idIn, nameIn, donor, startingPrice, buyer, endingPrice):
        super().__init__(idIn, nameIn)
        self.donor = donor
        self.startingPrice = startingPrice
        self.buyer = buyer
        self.endingPrice = endingPrice

class Buyer(Object):
    def __init__(self, idIn, nameIn, addressIn, itemsIn=[]):
        super().__init__(idIn, nameIn)
        self.address = addressIn
        self.items = itemsIn

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Address: {self.address}"