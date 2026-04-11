from Logic.Donor import Donor

class AllData:
    def __init__(self):
        self.donors = []
        self.items  = self.read_items()
        self.buyers = self.read_buyers()

        self.next_donor_id_num = 1
        self.next_item_id_num = 1
        self.next_buyer_id_num = 1

        self.next_donor_id = f"D{self.next_donor_id_num}"
        self.next_item_id = f"D{self.next_item_id_num}"
        self.next_buyer_id = f"D{self.next_buyer_id_num}"

    # TODO: Write function for reading list of donors and update nextDonorID
    def read_donors(self):
        pass

    # TODO: Write function for reading list of items and update nextItemID
    def read_items(self):
        pass

    # TODO: Write function for reading list of buyers and update nextBuyerID
    def read_buyers(self):
        pass

    # !! TODO: Ensure that donor ID has 'D' and three digits
    def add_donor(self, nameIn, addressIn):
        newDonor = Donor(self.next_donor_id, nameIn, addressIn)
        self.donors.append(newDonor)
        newDonor.save_donor()
        self.next_donor_id_num += 1
        self.next_donor_id = f"D{self.next_donor_id_num}"
        pass