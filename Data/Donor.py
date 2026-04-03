import json

class Donor:
    def __init__(self, donor_id, name, address):
        self.donor_id = donor_id
        self.name = name
        self.address = address
        self.item_ids = [] # list of item IDs (strings)

    # TODO: Implement
    def add_item(self, item):
        self.items.append(item)

    def save_donor(self):
        data = {
            "donor_id": self.donor_id,
            "name": self.name,
            "address": self.address,
            "items": self.item_ids
        }
        with open(f"{self.donor_id}.json", "w") as f:
            f.dump(data, f)