from enum import Enum
import json
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path

from Logic.Classes import *
from globals import ObjectType

class ObjectData:
    def __init__(self, folder):
        self.folder = folder
        self.objects = []

class AllData:
    def __init__(self):
        self.class_list = [Donor, Item, Buyer]
        self.object_list = [{}, {}, {}]
        self.next_ids = [1, 1, 1]
        self.load_object_files_on_init()

    def convert_id_to_file_id(self, idIn, int_to_str):
        if int_to_str:
            id_str = str(idIn)
            while len(id_str) < 3:
                id_str = "".join(["0", id_str])
            return id_str
        else:
            id_int = int(idIn)
            return id_int

    def update_people(self, item, old_donor_id = "", old_buyer_id = ""):
        item_id = item.id
        donor_id = item.donor
        buyer_id = item.buyer
        if old_donor_id != "" and old_donor_id != donor_id:
            self.object_list[ObjectType.DONOR.value][old_donor_id].remove_item(item_id)
        if old_buyer_id != "" and old_buyer_id != buyer_id:
            self.object_list[ObjectType.BUYER.value][old_buyer_id].remove_item(item_id)
        if donor_id != "" and item_id not in self.object_list[ObjectType.DONOR.value][donor_id].items:
            self.object_list[ObjectType.DONOR.value][donor_id].add_item(item_id)
            self.object_list[ObjectType.DONOR.value][donor_id].save()
        if buyer_id != "" and item_id not in self.object_list[ObjectType.BUYER.value][buyer_id].items:
            self.object_list[ObjectType.BUYER.value][buyer_id].add_item(item_id)
            self.object_list[ObjectType.BUYER.value][buyer_id].save()

    def create_object(self, entity_type, **kwargs):
        cls = self.class_list[entity_type.value]
        params = {key: kwargs[key] for key in cls.REQUIRED}
        object = cls(**params)
        self.object_list[entity_type.value][kwargs["id"]] = object
        self.set_next_id(entity_type.value, int(object.id))
        object.save()
        if entity_type == ObjectType.ITEM:
            self.update_people(object)
        return object

    def edit_object(self, entity_type, **kwargs):
        old_donor_id = None
        old_buyer_id = None
        if entity_type == ObjectType.ITEM:
            old_donor_id = self.object_list[entity_type.value][kwargs["id"]].donor
            old_buyer_id = self.object_list[entity_type.value][kwargs["id"]].buyer
        object = self.object_list[entity_type.value][kwargs["id"]]
        object.edit(kwargs)
        object.save()
        if entity_type == ObjectType.ITEM:
            self.update_people(object, old_donor_id, old_buyer_id)

    def delete_object(self, entity_type, idIn):
        object = self.object_list[entity_type.value][idIn]
        if entity_type == ObjectType.DONOR:
            items = object.items
            for item_id in items:
                self.object_list[ObjectType.ITEM.value][item_id].remove_person(ObjectType.DONOR, idIn)
        elif entity_type == ObjectType.ITEM:
            donor_id = object.donor
            buyer_id = object.buyer
            if donor_id != "":
                self.object_list[ObjectType.DONOR.value][donor_id].remove_item(idIn)
            if buyer_id != "":
                self.object_list[ObjectType.BUYER.value][buyer_id].remove_item(idIn)
        elif entity_type == ObjectType.BUYER:
            items = object.items
            for item_id in items:
                self.object_list[ObjectType.ITEM.value][item_id].remove_person(ObjectType.BUYER, idIn)
        object.delete()
        del self.object_list[entity_type.value][idIn]

    def set_next_id(self, index, num):
        if num >= self.next_ids[index]:
            self.next_ids[index] = num + 1

    def load_object_files_on_init(self):
        def get_field_from_json(json, key):
            return json[key] if key in json else ""

        dir_list = [donors_dir, buyers_dir, items_dir]
        object_str_to_class = {
            "Donor":    ObjectType.DONOR,
            "Item":     ObjectType.ITEM,
            "Buyer":    ObjectType.BUYER
        }
        for dir in dir_list:
            for file in Path(dir).glob("*.json"):
                with open(file) as f:
                    object_json = json.load(f)
                    object_type = object_str_to_class[object_json["class"]]
                    self.create_object(object_type,
                                        id=get_field_from_json(object_json, "id"),
                                        name=get_field_from_json(object_json, "name"),
                                        address=get_field_from_json(object_json, "address"),
                                        donor=get_field_from_json(object_json, "donor"),
                                        starting_price=get_field_from_json(object_json, "starting_price"),
                                        buyer=get_field_from_json(object_json, "buyer"),
                                        ending_price=get_field_from_json(object_json, "ending_price")
                                        )

        for i in range(0, 3):
            self.object_list[i] = {
                k: v
                for k, v in sorted(self.object_list[i].items(), key=lambda item: int(item[0]))
            }

