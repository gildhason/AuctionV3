from enum import Enum

class ObjectType(Enum):
    DONOR   = 0
    ITEM    = 1
    BUYER   = 2

donors_dir = "Data/Donors/"
items_dir = "Data/Items/"
buyers_dir = "Data/Buyers/"