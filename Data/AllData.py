from Data.Donor import Donor

class AllData:
    def __init__(self):
        self.donors = self.readDonors()
        self.items  = self.readItems()
        self.buyers = self.readBuyers()

        self.nextDonorID = 1
        self.nextItemID = 1
        self.nextBuyerID = 1
        
    # TODO: Write function for reading list of donors and update nextDonorID
    def readDonors(self):
        pass

    # TODO: Write function for reading list of items and update nextItemID
    def readItems(self):
        pass

    # TODO: Write function for reading list of buyers and update nextBuyerID
    def readBuyers(self):
        pass

    # TODO: Write function for adding a donor
    def addDonor(self, nameIn, addressIn, itemsIn):
        self.donors
        pass