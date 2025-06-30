from PIL.ImageFile import ImageFile
from pydantic import BaseModel


class Item(BaseModel):
    name:str
    dlc:str
    image:str|None = None

class Character(Item):
    ...
    #gender:str
    #personality:str

class Snack(Item):
    ...
    #character_like:str
    #personality_like:str
    #effect:str

class Food(Item):
    ...
    #character_like:str
    #personality_like:str
    #effect:str