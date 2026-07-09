from decimal import Decimal
from enum import Enum, auto
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

    class ObjectOpRet(Enum):
        OP_SUCCESS                          = auto()
        ID_MISSING                          = auto() 
        NAME_MISSING                        = auto()
        TRIED_ADDING_EXISTING_BUYER         = auto()
        TRIED_EDITING_ID_TO_EXISTING_BUYER  = auto()
        ID_INVALID                          = auto()
        STARTING_PRICE_INVALID              = auto()
        ENDING_PRICE_INVALID                = auto()
        DONATION_INVALID                    = auto()
        BUYER_DOES_NOT_EXIST                = auto()
        
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

    def eval_all_params(self, entity_type, action, **kwargs):
        def dollar_is_valid(dec_str):
            try:
                price_dec = Decimal(dec_str)
                if price_dec < 0:
                    raise Exception
                # if price_dec.as_tuple.exponent <= 2:
                #     raise Exception
                # print("Decimal place passed")
                return True
            except:
                return False
                
        retvals = []
        if kwargs["id"] == "":
            retvals.append(self.ObjectOpRet.ID_MISSING)
        try:
            id_int = int(kwargs["id"])
            if id_int < 1:
                raise Exception # Will this work? 
        except:
            retvals.append(self.ObjectOpRet.ID_INVALID)
        if kwargs["name"] == "":
            retvals.append(self.ObjectOpRet.NAME_MISSING)
        if entity_type == ObjectType.ITEM:
            if kwargs["starting_price"] != "":
                if not dollar_is_valid(kwargs["starting_price"]): 
                    retvals.append(self.ObjectOpRet.STARTING_PRICE_INVALID)
            if kwargs["ending_price"] != "":
                if not dollar_is_valid(kwargs["ending_price"]):
                    retvals.append(self.ObjectOpRet.ENDING_PRICE_INVALID)
            if kwargs["buyer"] != "" and kwargs["buyer"] not in self.object_list[ObjectType.BUYER.value]:
                retvals.append(self.ObjectOpRet.BUYER_DOES_NOT_EXIST)
        if entity_type == ObjectType.BUYER:
            if self.ObjectOpRet.ID_INVALID not in retvals and kwargs["id"] in self.object_list[ObjectType.BUYER.value] and action == "CREATE":
                retvals.append(self.ObjectOpRet.TRIED_ADDING_EXISTING_BUYER)
            if kwargs["donation"] != "":
                if not dollar_is_valid(kwargs["donation"]): 
                    retvals.append(self.ObjectOpRet.DONATION_INVALID)
        if action == "EDIT":
            pass

        return retvals

    def create_object(self, entity_type, **kwargs):
        retvals = self.eval_all_params(entity_type, "CREATE", **kwargs)
        print(f"Type: {entity_type} | {retvals}")
        if retvals:
            return retvals

        cls = self.class_list[entity_type.value]
        params = {key: kwargs[key] for key in cls.REQUIRED}
        object = cls(**params)
        self.object_list[entity_type.value][kwargs["id"]] = object
        self.set_next_id(entity_type, int(object.id))
        object.save()
        if entity_type == ObjectType.ITEM:
            self.update_people(object)
        if entity_type == ObjectType.BUYER:
            self.object_list[ObjectType.BUYER.value] = {
                k: v
                for k, v in sorted(self.object_list[ObjectType.BUYER.value].items(), key=lambda item: int(item[0]))
            }
        return [self.ObjectOpRet.OP_SUCCESS]

    def edit_object(self, entity_type, edit_buyer_id=False, **kwargs):
        retvals = self.eval_all_params(entity_type, "EDIT", **kwargs)
        if retvals:
            return retvals

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
        return [self.ObjectOpRet.OP_SUCCESS]

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
        if entity_type == ObjectType.BUYER:
            self.set_next_id(entity_type, 0)

    def set_next_id(self, object_type, num):
        if object_type == ObjectType.BUYER:
            next_id = 1
            while str(next_id) in self.object_list[ObjectType.BUYER.value]:
                next_id += 1
            self.next_ids[object_type.value] = next_id
        else: 
            if num >= self.next_ids[object_type.value]:
                self.next_ids[object_type.value] = num + 1

    def get_amount_owed(self, buyer):
        items_bought = buyer.items
        amt = 0
        for item_id in items_bought:
            price = self.object_list[ObjectType.ITEM.value][item_id].ending_price
            if price == "":
                continue
            else:
                amt += int(price)
        if buyer.donation != "":
            amt += int(buyer.donation)
        return amt

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
                                        ending_price=get_field_from_json(object_json, "ending_price"),
                                        donation=get_field_from_json(object_json, "donation")
                                        )

        for i in range(0, 3):
            self.object_list[i] = {
                k: v
                for k, v in sorted(self.object_list[i].items(), key=lambda item: int(item[0]))
            }

