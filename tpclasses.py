# CATHERINE CAI 15-112 TERM PROJECT
# SPRING 2021

# CLASS HELPER FILE

from dataclasses import make_dataclass

class Player(object):
    def __init__(self, name, traitList, traitIndex, color, age, birthday, hobbies):
        # TRAITS
        self.traitList = traitList # dictionary of trait lists
        self.traitIndex = traitIndex # dictionary of trait indexes
        self.might = traitList['might'][traitIndex['might']] # actual values
        self.speed = traitList['speed'][traitIndex['speed']]
        self.knowledge = traitList['knowledge'][traitIndex['knowledge']]
        self.sanity = traitList['sanity'][traitIndex['sanity']]

        # INFO/CHARACTERISTICS
        self.name = name
        self.color = color
        self.age = age
        self.birthday = birthday
        self.hobbies = hobbies
        self.status = True # alive, not dead
    
    def changeTrait(self, traitValue, trait, change, haunt): # traitValue self.trait, trait = 'trait'
        index = self.traitIndex[trait]
        index += change
        if not haunt:
            if 1 <= index <= 8:
                self.traitIndex[trait] += change
                traitValue = self.traitList[trait][self.traitIndex[trait]]
            else:
                index -= change
        else:
            if index <= 0:
                self.status = False
            elif index <= 8:
                self.traitIndex[trait] += change
                traitValue = self.traitList[trait][self.traitIndex[trait]]
            else:
                index -= change
        return traitValue

class Floor(object):
    def __init__(self,name,floor):
        self.name = name
        self.floor = floor
        self.rooms = set()

class Omen(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Event(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Room(object):
    def __init__(self, name, floors, omen, event, item):
        self.name = name
        self.floors = floors # eligible floors to place, list
        self.omen = omen # does it have omen? boolean
        self.event = event # does it have event? boolean
        self.item = item # does it have item? boolean