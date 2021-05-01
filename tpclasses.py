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

        # TRAITS
        #self.traits = traits
        #self.mightList = self.traits['mightList'] # list of trait values
        #self.mightIndex = self.traits['mightIndex'] # index number of list
        #self.might = self.mightList[self.mightIndex] # actual value
        #self.speedList = self.traits['speedList']
        #self.speedIndex = self.traits['speedIndex']
        #self.speed = self.speedList[self.speedIndex]
        #self.knowledgeList = self.traits['knowledgeList']
        #self.knowledgeIndex = self.traits['knowledgeIndex']
        #self.knowledge = self.knowledgeList[self.knowledgeIndex]
        #self.sanityList = self.traits['sanityList']
        #self.sanityIndex = self.traits['sanityIndex']
        #self.sanity = self.sanityList[self.sanityIndex]

        # INFO/CHARACTERISTICS
        self.name = name
        self.color = color
        self.age = age
        self.birthday = birthday
        self.hobbies = hobbies
        self.status = True # alive, not dead
        self.role = True # explorer/hero, not traitor
    
    def changeTrait(self, traitValue, trait, change, haunt):
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

class Floor(object):
    def __init__(self,name,floor):
        self.name = name
        self.floor = floor
        self.rooms = []

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

# 'name', mightlist, mightIndex, speedlist, speedIndex, knowledgelist, knowledgeIndex, sanitylist, sanityIndex, color, age, birthday, hobbies
#traits = {'mightList': [0,2,2,3,3,4,4,6,7], 'mightIndex': 4, 'speedList': [0,4,4,4,4,5,6,8,8], 'speedIndex': '4', 'knowledgeList': [0,1,2,3,4,4,5,5,5], 'knowledgeIndex': 3, 'sanityList': [0,3,4,5,5,6,6,7,8], 'sanityIndex': 3}
# def __init__(self, name, traitList, traitIndex, color, age, birthday, hobbies):

'''
app.Zoe = Player('Zoe Ingstrom', {'might': [0,2,2,3,3,4,4,6,7], 'speed': [0,4,4,4,4,5,6,8,8], 'knowledge': [0,1,2,3,4,4,5,5,5], 'sanity': [0,3,4,5,5,6,6,7,8]}, {'might': 4, 'speed': 4, 'knowledge': 3, 'sanity': 3}, 'yellow', 8, 'November 5th', 'Dolls, Music')
app.Zostra = Player('Madame Zostra', {'might': [0,2,3,3,4,5,5,5,6], 'speed': [0,2,3,3,5,5,6,6,7], 'knowledge': [0,1,3,4,4,4,5,6,6], 'sanity': [0,4,4,4,5,6,7,8,8]}, {'might': 4, 'speed': 3, 'knowledge': 4, 'sanity': 3}, 'deep sky blue', 37, 'December 10th', 'Astrology, Cooking, Baseball')
app.Longfellow = Player('Professor Longfellow', {'might': [0,1,2,3,4,5,5,6,6], 'speed': [0,2,2,4,4,5,5,6,6], 'knowledge': [0,4,5,5,5,5,6,7,8], 'sanity': [0,1,3,3,4,5,5,6,7]}, {'might': 3, 'speed': 4, 'knowledge': 5, 'sanity': 3}, 'white', 57, 'July 27th', 'Gaelic Music, Drama, Fine Wines')
app.Flash = Player('Darrin "Flash" Williams', {'might': [0,2,3,3,4,5,6,6,7], 'speed': [0,4,4,4,5,6,7,7,8], 'knowledge': [0,2,3,3,4,5,5,5,7], 'sanity': [0,1,2,3,4,5,5,5,7]}, {'might': 3, 'speed': 5, 'knowledge': 3, 'sanity': 3}, 'red', 20, 'June 6th', 'Track, Music, Shakespearean Literature')
app.Jenny = Player('Jenny LeClerc', {'might': [0,3,4,4,4,4,5,6,8], 'speed': [0,2,3,4,4,4,5,6,8], 'knowledge': [0,2,3,3,4,4,5,6,8], 'sanity': [0,1,1,2,4,4,4,5,6]}, {'might': 3, 'speed': 4, 'knowledge': 3, 'sanity': 5}, 'purple1', 21, 'March 4th', 'Reading, Soccer')
app.Brandon = Player('Brandon Jaspers', {'might': [0,2,3,3,4,5,6,6,7], 'speed': [0,3,4,4,4,5,6,7,8], 'knowledge': [0,1,3,3,5,5,6,6,7], 'sanity': [0,3,3,3,4,5,6,7,8]}, {'might': 4, 'speed': 3, 'knowledge': 3, 'sanity': 4}, 'green2', 12, 'May 21st', 'Computers, Camping, Hockey')
app.Vivian = Player('Vivian Lopez', {'might': [0,2,2,2,4,4,5,6,6], 'speed': [0,3,4,4,4,4,6,7,8], 'knowledge': [0,4,5,5,5,5,6,6,7], 'sanity': [0,4,4,4,5,6,7,8,8]}, {'might': 3, 'speed': 4,  'knowledge': 4,  'sanity': 3}, 'deep sky blue', 42, 'January 11th', 'Old Movies, Horses')
app.Missy = Player('Missy Dubourde', {'might': [0,2,3,3,3,4,5,6,7], 'speed': [0,3,4,5,6,6,6,7,7], 'knowledge': [0,2,3,4,4,5,6,6,6], 'sanity': [0,1,2,3,4,5,5,6,7]}, {'might': 4, 'speed': 3, 'knowledge': 4,  'sanity': 3}, 'yellow', 9, 'February 14th', 'Swimming, Medicine')
app.Rhinehardt = Player('Father Rhinehardt', {'might': [0,1,2,2,4,4,5,5,7], 'speed': [0,2,3,3,4,5,6,7,7], 'knowledge': [0,1,3,3,4,5,6,6,8], 'sanity': [0,3,4,5,5,6,7,7,8]}, {'might': 3, 'speed': 3, 'knowledge': 4, 'sanity': 5}, 'white', 62, 'April 29th', 'Fencing, Gardening')
app.Heather = Player('Heather Granville', {'might': [0,3,3,3,4,5,6,7,8], 'speed': [0,3,3,4,5,6,6,7,8], 'knowledge': [0,2,3,3,4,5,6,7,8], 'sanity': [0,3,3,3,4,5,6,6,6]}, {'might': 3, 'speed': 3, 'knowledge': 5, 'sanity': 3}, 'purple1', 18, 'August 2nd', 'Television, Shopping')
app.Peter = Player('Peter Akimoto', {'might': [0,2,3,3,4,5,5,6,8], 'speed': [0,3,3,3,4,6,6,7,7], 'knowledge': [0,3,4,4,5,6,7,7,8], 'sanity': [0,3,4,4,4,5,6,6,7]}, {'might': 3, 'speed': 4,  'knowledge': 3, 'sanity': 4}, 'green2', 13, 'September 3rd', 'Bugs, Basketball')
app.Ox = Player('Ox Bellows', {'might': [0,4,5,5,6,6,7,8,8], 'speed': [0,2,2,2,3,4,5,5,6], 'knowledge': [0,2,2,3,3,5,5,6,6], 'sanity': [0,2,2,3,4,5,5,6,7]}, {'might': 3,  'speed': 5,  'knowledge': 3, 'sanity': 3}, 'red', 23, 'October 18th', 'Football, Shiny Objects')
'''
#Zoe = Player('Zoe Ingstrom', {'mightList': [0,2,2,3,3,4,4,6,7], 'mightIndex': 4, 'speedList': [0,4,4,4,4,5,6,8,8], 'speedIndex': 4, 'knowledgeList': [0,1,2,3,4,4,5,5,5], 'knowledgeIndex': 3, 'sanityList': [0,3,4,5,5,6,6,7,8], 'sanityIndex': 3}, 'yellow', 8, 'November 5th', 'Dolls, Music')