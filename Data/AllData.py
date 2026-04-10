from Data.Donor import Donor

class AllData:
    def __init__(self):
        self.donors = []
        self.items  = self.read_items()
        self.buyers = self.read_buyers()

        self.next_donor_id = 1
        self.next_item_id = 1
        self.next_buyer_id = 1

    # TODO: Write function for reading list of donors and update nextDonorID
    def read_donors(self):
        pass

    # TODO: Write function for reading list of items and update nextItemID
    def read_items(self):
        pass

    # TODO: Write function for reading list of buyers and update nextBuyerID
    def read_buyers(self):
        pass

    # TODO: Write function for adding a donor
    def add_donor(self, nameIn, addressIn):
        self.donors.append(Donor(self.next_donor_id, nameIn, addressIn))
        self.next_donor_id += 1
        pass