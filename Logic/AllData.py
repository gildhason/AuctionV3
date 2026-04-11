import json
from os import listdir
from os.path import isfile, join

from Logic.Donor import Donor

class AllData:
    def __init__(self):
        self.next_donor_id_num = 1
        self.next_item_id_num = 1
        self.next_buyer_id_num = 1

        self.donors = self.read_donors()
        self.items  = self.read_items()
        self.buyers = self.read_buyers()

        self.next_donor_id = f"D{self.next_donor_id_num:03}"
        self.next_item_id = f"D{self.next_item_id_num}"
        self.next_buyer_id = f"D{self.next_buyer_id_num}"

    # TODO: Write function for reading list of donors and update nextDonorID
    def read_donors(self):
        donor_list = [f for f in listdir("Data/Donors/") if isfile(join("Data/Donors/", f))]
        donor_dict = {}
        for file in donor_list:
            with open(f"Data/Donors/{file}") as f:
                donor_json = json.load(f)
                donor_dict[donor_json["donor_id"]] = donor_json
                if int(donor_json["donor_id"][1:]) >= self.next_donor_id_num:
                    self.next_donor_id_num = int(donor_json["donor_id"][1:]) + 1
                print(donor_dict)
        return donor_dict

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
        self.next_donor_id = f"D{self.next_donor_id_num:03}"
        pass