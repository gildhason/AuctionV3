from enum import Enum
import json
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path

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

    def create_object(self, entity_type, **kwargs):
        cls = self.class_list[entity_type.value]
        params = {key: kwargs[key] for key in cls.REQUIRED}
        object = cls(**params)
        # print(vars(object))
        self.object_list[entity_type.value][kwargs["id"]] = object
        self.set_next_id(entity_type.value, int(object.id))
        object.save()
        return object

    def edit_object(self, entity_type, **kwargs):
        object = self.object_list[entity_type.value][kwargs["id"]]
        object.edit(kwargs)
        object.save()
        pass

    def delete_object(self, entity_type, idIn):
        object = self.object_list[entity_type.value][idIn]
        object.delete()
        del self.object_list[entity_type.value][idIn]

    def read_objects(self):
        pass

    def set_next_id(self, index, num):
        print(f"num: {num} | curr next id: {self.next_ids[index]}")
        if num >= self.next_ids[index]:
            self.next_ids[index] = num + 1

    def load_object_files_on_init(self):
        dir_list = [donors_dir, items_dir, buyers_dir]
        for dir in dir_list:
            for file in Path(dir).glob("*.json"):
                with open(file) as f:
                    object_json = json.load(f)
                    object = None
                    if object_json["class"] == "Donor":
                        object = Donor(
                            object_json["id"],
                            object_json["name"],
                            object_json["address"],
                            object_json["items"],
                        )
                        self.object_list[0][object_json["id"]] = object
                        self.set_next_id(0, int(object_json["id"]))
                    elif object_json["class"] == "Item":
                        object = Item(
                            object_json["id"],
                            object_json["name"],
                            object_json["donor"],
                            object_json["starting_price"],
                            object_json["buyer"],
                            object_json["ending_price"],
                        )
                        self.object_list[1][object_json["id"]] = object
                        self.set_next_id(1, int(object_json["id"]))
                    elif object_json["class"] == "Buyer":
                        object = Buyer(
                            object_json["id"],
                            object_json["name"],
                            object_json["address"],
                            object_json["items"],
                        )
                        self.object_list[2][object_json["id"]] = object
                        self.set_next_id(2, int(object_json["id"]))
                    
        for i in range(0, 3):
            self.object_list[i] = {
                k: v
                for k, v in sorted(self.object_list[i].items(), key=lambda item: int(item[0]))
            }

