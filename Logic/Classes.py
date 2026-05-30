import json
import os
import traceback

from globals import donors_dir, items_dir, buyers_dir

class Object:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            "class": self.__class__.__name__,
            "id": self.id,
            "name": self.name,
        }

    def convert_id_to_file_id(self, id, int_to_str):
        if int_to_str:
            id_str = str(id)
            while len(id_str) < 3:
                id_str = "".join(["0", id_str])
            return id_str
        else:
            id_int = int(id)
            return id_int

    def save(self):
        directory = self.get_dir()
        
        filename = f"{directory}{self.convert_id_to_file_id(self.id, True)}.json"
        try:
            os.remove(filename)
        except OSError:
            pass

        with open(filename, mode="x") as f:
            json.dump(self.to_dict(), f, indent=4)
    
    def edit(self, kwargs):
        for key in self.REQUIRED:
            if key in kwargs:
                setattr(self, key, kwargs[key])

    def delete(self):
        directory = self.get_dir()
        filename = f"{directory}{self.convert_id_to_file_id(self.id, True)}.json"
        os.remove(filename)

    def get_dir(self):
        if isinstance(self, Donor):
            return donors_dir
        elif isinstance(self, Item):
            return items_dir
        elif isinstance(self, Buyer):
            return buyers_dir
        else:
            print("Unrecognized object trying to save")
            return None

class Donor(Object):
    REQUIRED = ["id", "name", "address"]

    def __init__(self, id, name, address, items=[]):
        super().__init__(id, name)
        self.address = address
        self.items = items

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
    REQUIRED = ["id", "name", "donor", "starting_price", "buyer", "ending_price"]

    def __init__(self, id, name, donor, starting_price, buyer, ending_price):
        super().__init__(id, name)
        self.donor = donor
        self.starting_price = starting_price
        self.buyer = buyer
        self.ending_price = ending_price

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Donor: {self.donor}, Starting Price: {self.starting_price}, Buyer: {self.buyer}, Ending Price: {self.ending_price}"

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "donor": self.donor,
            "starting_price": self.starting_price,
            "buyer": self.buyer,
            "ending_price": self.ending_price
        })
        return data

    def from_dict(self, data):
        return Donor(data["id"], data["name"], data["address"], data["items"])

class Buyer(Object):
    REQUIRED = ["id", "name", "address"]

    def __init__(self, id, name, address, items=[]):
        super().__init__(id, name)
        self.address = address
        self.items = items

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
