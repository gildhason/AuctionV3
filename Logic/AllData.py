from enum import Enum
import json
import os
from os import listdir
from os.path import isfile, join

from Logic.Classes import *

class ObjectData:
    def __init__(self, folder):
        self.folder = folder
        self.objects = []

class AllData:
    def __init__(self):
        self.class_list = [Donor, Item, Buyer]
        self.object_list = [{}, {}, {}]
        self.next_ids = [1, 1, 1]

    def convert_id_to_file_id(self, idIn, int_to_str):
        if int_to_str:
            id_str = str(idIn)
            while len(id_str) < 3:
                id_str = "".join(["0", id_str])
            return id_str
        else:
            id_int = int(idIn)
            return id_int

    def create_object(self, entity_type, **kwargs):
        cls = self.class_list[entity_type.value]
        object = cls(**kwargs)
        # print(vars(object))
        self.object_list[entity_type.value][kwargs["idIn"]] = object
        if int(object.id) >= self.next_ids[entity_type.value]:
            self.next_ids[entity_type.value] = int(object.id) + 1
        object = cls(**kwargs)
        object.save()
        return object

    def delete_object(self, entity_type, idIn):
        del self.object_list[entity_type.value][idIn]

    def read_objects(self):
        pass

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
