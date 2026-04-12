import json

class Donor:
    def __init__(self, idIn, name, address):
        self.id = idIn
        self.name = name
        self.address = address
        self.item_ids = [] # list of item IDs (strings)

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Address: {self.address}"

    # TODO: Implement
    def add_item(self, item):
        self.items.append(item)

    def save_donor(self):
        data = {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "items": self.item_ids
        }
        with open(f"Data/Donors/{self.donor_id}.json", "w") as f:
            json.dump(data, f)