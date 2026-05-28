import json
import os

from globals import donors_dir, items_dir, buyers_dir

class Object:
    def __init__(self, idIn, nameIn):
        self.id = idIn
        self.name = nameIn

    def to_dict(self):
        return {
            "class": self.__class__.__name__,
            "id": self.id,
            "name": self.name,
        }

    def convert_id_to_file_id(self, idIn, int_to_str):
        if int_to_str:
            id_str = str(idIn)
            while len(id_str) < 3:
                id_str = "".join(["0", id_str])
            return id_str
        else:
            id_int = int(idIn)
            return id_int

    def save(self):
        directory = None
        if isinstance(self, Donor):
            directory = donors_dir
        elif isinstance(self, Item):
            directory = items_dir
        elif isinstance(self, Buyer):
            directory = buyers_dir
        else:
            print("Unrecognized object trying to save")
        
        filename = f"{directory}{self.convert_id_to_file_id(self.id, True)}.json"
        try:
            os.remove(filename)
        except OSError:
            pass

        with open(filename, mode="x") as f:
            json.dump(self.to_dict(), f, indent=4)

class Donor(Object):
    def __init__(self, idIn, nameIn, addressIn, itemsIn=[]):
        super().__init__(idIn, nameIn)
        self.address = addressIn
        self.items = itemsIn

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Address: {self.address}"

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "address": self.address,
            "items": self.items
        })
        return data

    def from_dict(self, data):
        return Donor(data["id"], data["name"], data["address"], data["items"])


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

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "address": self.address,
            "items": self.items
        })
        return data

    def from_dict(self, data):
        return Donor(data["id"], data["name"], data["address"], data["items"])
