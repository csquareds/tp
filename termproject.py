# CATHERINE CAI 15-112 TERM PROJECT
# SPRING 2021

# Based on the board game, Betrayal at House on the Hill, published by Avalon 
# Hill in 2004. 

# Players all begin as allies exploring a haunted house filled 
# with dangers, traps, items, and omens. As players journey to new parts of the 
# mansion, room tiles are chosen at random and placed on the game board; this 
# means that the game is different each session. Eventually the "haunt" begins,
# with the nature and plot of this session's ghost story revealed; one player 
# usually "betrays" the others and takes the side of the ghosts, monsters, or 
# other enemies, while the remaining players collaborate to defeat them.

# Helpful links
# https://en.wikipedia.org/wiki/Betrayal_at_House_on_the_Hill
# https://media.wizards.com/2018/downloads/rules/betrayal_rules.pdf
# https://startyourmeeples.com/2018/09/28/betrayal-at-house-on-the-hill-characters-a-closer-inspection/
# https://startyourmeeples.com/2019/07/09/betrayal-at-house-on-the-hill-rooms-a-strategy-in-9-graphs/

# Images
# https://i0.wp.com/fantasy-hive.co.uk/wp-content/uploads/2018/06/betrayal-house-cover-image.jpg?fit=620%2C420&ssl=1

from cmu_112_graphics import *
import random, string, math, time
from dataclasses import make_dataclass
#import tpclasses import *

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
        self.role = True # explorer/hero, not traitor
    
    # example: traitValue = self.might, trait = 'might'
    def changeTrait(self, traitValue, trait, change):
        index = self.traitIndex[trait]
        index += change
        if not app.haunt:
            if 0 <= index <= 8:
                self.traitIndex[trait] += change
                traitValue = traitList[self.traitIndex[trait]]
            else:
                index -= change
        else:
            if index <= 0:
                self.status = False
            elif index <= 8:
                self.traitIndex[trait] += change
                traitValue = traitList[self.traitIndex[trait]]
            else:
                index -= change

    def attemptRole(self, trait):
        if trait == "might":
            dice = self.might

# PLAYERS, note 0 is death
def setPlayers(app):
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
# Player template
#Player = Player('name', {mightList, speedList, knowledgeList, sanityList}, {mightIndex, speedIndex, knowledgeIndex, sanityIndex}, color, age, birthday, hobbies)

class Floor(object):
    def __init__(self,name):
        self.name = name
        self.rooms = []

# FLOORS
Ground = Floor('Ground Level')
Basement = Floor('Basement')
Upper = Floor('Upper Level')

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

# ROOMS, omen event item
Abandoned = Room('Abandoned Room', [Ground, Basement], True, False, False)
Attic = Room('Attic', [Upper], False, True, False)
Balcony = Room('Balcony', [Ground], True, False, False)
Ballroom = Room('Ballroom', [Ground], False, True, False)
Creaky = Room('Creaky Hallway', [Upper, Ground, Basement], False, False, False)
Crypt = Room('Crypt', [Basement], False, True, False)
Bloody = Room('Bloody Room', [Upper, Ground], False, False, True)
Chapel = Room('Chapel', [Upper, Ground], False, True, False)
Vault = Room('Vault', [Upper, Basement], False, False, True)
Collapsed = Room('Collapsed Room', [Upper, Ground], False, False, False)
Dining = Room('Dining Room', [Ground], True, False, False)
Furnace = Room('Furnace Room', [Basement], True, False, False)
Graveyard = Room('Graveyard', [Ground], False, True, False)
Gym = Room('Gymnasium', [Upper, Basement], True, False, False)
Operating = Room('Operating Laboratory', [Upper, Basement], False, False, False)
Organ = Room('Organ Room', [Upper, Ground, Basement], False, True, False)
Store = Room('Storeroom', [Upper, Basement], False, False, True)
Tower = Room('Tower', [Upper], False, True, False)
Catacombs = Room('Catacombs', [Basement], True, False, False)
Dusty = Room('Dusty Hallway', [Upper, Ground, Basement], False, False, False)
Kitchen = Room('Kitchen', [Ground, Basement], True, False, False)
Junk = Room('Junk', [Upper, Ground, Basement], True, False, False)
Larder = Room('Larder', [Basement], False, False, True)
Patio = Room('Patio', [Ground], False, True, False)
Pentagram = Room('Pentagram Chamber', [Basement], True, False, False)
Research = Room('Research Laboratory', [Upper, Basement], False, True, False)
Underground = Room('Underground Lake', [Basement], False, True, False)
Vault = Room('Vault', [Upper, Basement], False, False, True) # two items
Chasm = Room('Chasm', [Basement], False, False, False)
Coal = Room('Coal Chute', [Ground], False, False, False)
Collapsed = Room('Collapsed Room', [Upper, Ground], False, False, False)
Charred = Room('Charred Room', [Upper, Ground], True, False, False)
Conservatory = Room('Conservatory', [Upper, Ground], False, True, False)
Gallery = Room('Gallery', [Upper], True, False, False)
Game = Room('Game Room', [Upper, Ground, Basement], False, True, False)
Gardens = Room('Gardens', [Ground], False, True, False)
Library = Room('Library', [Upper, Ground], False, True, False)
Master = Room('Master Bedroom', [Upper], True, False, False)
Mystic = Room('Mystic Elevator', [Upper, Ground, Basement], False, False, False)
Servant = Room("Servants' Quarters", [Upper, Basement], True, False, False)
StairsBasement = Room('Stairs from Basement', [Basement], False, False, False)
Statuary = Room('Statuary Corridor', [Upper, Ground, Basement], False, True, False)
Wine = Room('Wine Cellar', [Basement], False, False, True)
Bedroom = Room('Bedroom', [Upper], False, True, False)
Empty = Room('Undiscovered', [Upper, Ground, Basement], False, False, False)


# OMENS
Skull = Omen('Skull', 'A skull cracked, and missing teeth')
Bite = Omen('Bite', 'A growl, the scent of death. Pain. Darkness. Gone.')
Book = Omen('Book', 'A diary or lab notes? Ancient script or modern ravings?')
Crystal = Omen('Crystal Ball', 'Hazy images appear in the glass.')
Dog = Omen('Dog', 'COMPANION This mangy dog seems friendly. At least you hope it is.')
Girl = Omen('Girl', 'COMPANION A girl. Trapped. Alone. You free her!')
Holy = Omen('Holy Symbol', 'A symbol of calm in an unsettling world.')
Madman = Omen('Madman', 'COMPANION A raving, frothing madman.')
Mask = Omen('Mask', 'A somber mask to hide your intentions.')
Medallion = Omen('Medallion', 'A medallion inscribed with a pentagram.')
Ring = Omen('Ring', 'A battered ring with an incomprehensible inscription.')
Spear = Omen('Spear', 'WEAPON A weapon pulsing with power.')
Spirit = Omen('Spirit Board', 'A board with letters and numbers to call the dead.')

# EVENTS
Whoops = Event("Whoops!", "You feel a body under your foot. Before you can leap away from it, you've knocked over. A giggling voice runs away from you.")
What = Event("What the...?", "As you look back the way you came, you see... nothing. Just empty and mist where a room used to be.")
Webs = Event("Webs", "Casually, you reach up to brush some webs aside... but they won't brush away. They cling.")
Walls = Event("Walls", "This room is warm. Flesh-like walls pulse with a steady heartbeat. Your own heart beats with the rhythm of the house. You are drawn into the walls... and emerge somewhere else.")
Voice = Event("The Voice", '"I am under the floor, buried under the floor..." The voice whispers once, then is gone.')
Lost = Event("The Lost One", "A woman wearing a Civil War dress beckons to you. You fall into a trance.")
Beckoning = Event("The Beckoning", "Outside. You must get outside. Fly to freedom!")
Spider = Event("Spider", "A spider the size of a fist lands on your shoulder... and crawls into your hair.")
Slimy = Event("Something Slimy", "What's around your ankle? A bug? A tentacle? A dead hand clawing?")
Hidden = Event("Something Hidden", "There's something odd about this room, but what? It's tickling the back of your mind.")
Smoke = Event("Smoke", "Smoke billows around you. You cough, wiping away tears.")
Skeletons = Event("Skeletons", "Mother and child, still embracing.")
Silence = Event("Silence", "Underground, everything goes silent. Even the sound of breathing is gone.")
Wind = Event("Shrieking Wind", "The wind picks up, a slow crescendo to a screeching howl.")
Stairs = Event("Secret Stairs", "A horrible creaking sound echoes around you. You've discovered a secret stairwell.")
Passage = Event("Secret Passage", "A section of the wall slides away. Behind it, a moldy tunnel awaits.")
Rotten = Event("Rotten", "The smell in this room, it's horrible. Smells like death, like blood. A slaughterhouse smell.")
Wall = Event("Revolving Wall", "The wall spins to another place.")
Possession = Event("Possession", "A shadow separates from the wall. As you stand in shock, and shadow surrounds you and chills you to the core.")
Phone = Event("Phone Call", "A phone rings in the room. You feel compelled to answer it.")
Night = Event("Night View", "You see a vision of a ghostly couple walking the grounds, silently strolling in their wedding best.")
Mystic = Event("Mystic Slide", "The floor falls from under you.")
Mists = Event("Mists from the Walls", "Mists pour out from the walls. There are faces in the mist, human and... inhuman.")
Safe = Event("Locked Safe", "Behind a portrait is a wall safe. It is trapped, of course.")
Lights = Event("Lights Out", "Your flashlight goes out. Don't worry, someone else has batteries.")
Jonah = Event("Jonah's Turn", "Two boys are playing with a wooden top.") # not finished
Meant = Event("It is Meant to Be", "You collapse to the floor, visions of future events pouring through your head.")
Mirror = Event("Image in the Mirror", "There is an old mirror in this room") # not finished?
OtherMirror = Event("Image in the Mirror", "You then hand an item through the mirror.") # not finished too, duality
Shriek = Event("Hideous Shriek", "It starts like a whisper, but ends in a soul-rending shriek.")
Hanged = Event("Hanged Men", "A breeze chills the room. Before you, three men hang from frayed ropes. They stare at you with cold, dead eyes. The trio swing silently, then fade into dust that falls to the ground. You start to choke.")
Groundskeeper = Event("Groundskeeper", "You turn to see a man in groundskeeper clothing. He raises his shovel and charges. Inches from your face, he disappears, leaving muddy footprints, and nothing more.")
Grave = Event("Grave Dirt", "This room is covered in a thick layer of dirt. You cough as it gets on your skin and in your lungs.")
Funeral = Event("Funeral", "You see an open coffin. You're inside it.")
Footsteps = Event("Footsteps", "The floorboards slowly creak. Dust rises. Footprints appear on the dirty floor. And then, as they reach you, they are gone.")
Drip = Event("Drip... Drip... Drip...", "A rhythmic sound that needles at your brain.")
Sounds = Event("Disquieting Sounds", "A baby's cry, lost and abandoned. A scream. The crack of breaking glass. Then silence.")
Debris = Event("Debris", "Plaster falls from the walls and ceiling.")
Puppet = Event("Creepy Puppet", "You see one of those dolls that give you the willies. It jumps at you with a tiny spear.")
Crawlies = Event("Creepy Crawlies", "A thousand bugs spill out on your skin, under your clothes, and in your hair.")
Closet = Event("Closet Door", "That closet door is open... just a crack. There must be something inside.")
Burning = Event("Burning Man", "A man on fire runs through the room. His skin bubbles and cracks, falling away from him and leaving a fiery skull that clatters to the ground, bounces, rolls, and disappears.")
Vision = Event("Bloody Vision", "The walls of this room are damp with blood. The blood drips from the ceiling, down the walls, over the furniture, and onto your shoes. In a blink, it is gone.")
Angry = Event("Angry Being", "It emerges from the slime on the wall next to you.")
Hope = Event("A Moment of Hope", "Something feels strangely right about this room. Something is resisting the evil of the house.")

# ITEMS
Revolver = Item("Revolver", "WEAPON An old potent looking weapon.")
Salts = Item("Smelling Salts", "Whew, that's a lungful.")
Sacrificial_Dagger = Item("Sacrificial Dagger", "WEAPON A twisted shard of iron covered in mysterious symbols and stained with blood.")
Rabbit = Item("Rabbit's Foot", "Not so lucky for the rabbit.")
Puzzle = Item("Puzzle Box", "There must be a way to open it.")
Gloves = Item("Pickpoket's Gloves", "Helping yourself has never seemed so easy.")
Music = Item("Music Box", "A hand-crafted antique. It plays a haunting melody that gets stuck in your head.")
Medical = Item("Medical Kit", "A doctor's bag, depleted in some critical resources.")
Lucky = Item("Lucky Stone", "A smooth, ordinary-looking rock. You sense it will bring you good fortune.")
Idol = Item("Idol", "Perhaps it's chosen you for some greater purpose. Like human sacrifice.")
Healing = Item("Healing Salve", "A sticky paste in a shallow bowl.")
Dynamite = Item("Dynamite", "The fuse isn't lit... yet")
Dice = Item("Dark Dice", "Are you feeling lucky?")
Candle = Item("Candle", "It makes the shadows move— at least, you hope it's doing that.")
Bottle = Item("Bottle", "An opaque vial containing a black liquid.")
Blood_Dagger = Item("Blood Dagger", "WEAPON A nasty weapon. Needles and tubes extend from the handle... and plunge right into your veins.")
Bell = Item("Bell", "A brass bell that makes a resonant clang.")
Axe = Item("Axe", "WEAPON Very sharp.")
Armor = Item("Armor", "It's just prop armor from a Renaissance fair, but it's still metal.")
Angel = Item("Angel Feather", "A perfect feather fluttering in your hand.")
Amulet = Item("Amulet of the Ages", "Ancient silver and inlaid gems, inscribed with blessings.")
Adrenaline = Item("Adrenaline Shot", "A syringe containing a strange fluorescent liquid.")

def appStarted(app):
    app.mode = 'start'
    app.image = app.loadImage('bahoth.jpeg') # start screen image
    app.haunt = 0 # haunt count
    app.hauntDie = [0, 0, 1, 1, 2, 2] # 8 dice
    setPlayers(app)
    setCharacters(app)
    setCharacter(app)
    app.haunt = False # haunt phase
    app.rooms = [Abandoned, Attic, Balcony, Ballroom, Bedroom, Bloody, Catacombs, 
        Chapel, Charred, Chasm, Coal, Collapsed, Conservatory, Creaky, Crypt, 
        Dining, Dusty, Furnace, Gallery, Game, Gardens, Graveyard, Gym, Junk, 
        Kitchen, Larder, Library, Master, Mystic, Operating, Organ, Patio, 
        Pentagram, Research, Servant, StairsBasement, Statuary, Store, Tower, 
            Underground, Vault, Wine]
    setGround(app)
    setBasement(app)
    setUpper(app)
    app.omens = [Skull, Bite, Book, Crystal, Dog, Girl, Holy, 
                Madman, Mask, Medallion, Ring, Spear, Spirit]
    app.events = [Whoops, What, Webs, Walls, Voice, Lost, Beckoning, Spider, 
            Slimy, Hidden, Smoke, Skeletons, Silence, Wind, Stairs, Passage, 
            Rotten, Wall, Possession, Phone, Night, Mystic, Mists, Safe, Lights, 
            Jonah, Meant, Mirror, OtherMirror, Shriek, Hanged, Groundskeeper, 
            Grave, Funeral, Footsteps, Drip, Sounds, Debris, Puppet, Crawlies, 
                Closet, Burning, Vision, Angry, Hope]
    app.items = [Revolver, Salts, Sacrificial_Dagger, Rabbit, Puzzle, Gloves, 
                Music, Medical, Lucky, Idol, Healing, Dynamite, Dice, Candle, 
            Bottle, Blood_Dagger, Bell, Axe, Armor, Angel, Amulet, Adrenaline]
    app.gameOver = False

def setCharacters(app):
    app.message = None
    app.players = 0 # total number of players
    app.player1 = {'number': 1, 'character': None}
    app.player2 = {'number': 2, 'character': None}
    app.player3 = {'number': 3, 'character': None}
    app.player4 = {'number': 4, 'character': None}
    app.player5 = {'number': 5, 'character': None}
    app.player6 = {'number': 6, 'character': None}
    #print(app.player1['number'])
    app.playerList = [app.player1, app.player2, app.player3, app.player4, app.player5, app.player6]
    #app.playerListCopy = [app.player1, app.player2, app.player3, app.player4, app.player5, app.player6]
    app.index = 0
    app.currentPlayer = app.playerList[app.index]

def setCharacter(app):
    app.characterRows = 3
    app.characterCols = 4
    app.marginX = 50
    app.marginY = 200
    app.characters = [ [app.Brandon, app.Flash, app.Heather, app.Jenny], [app.Longfellow, app.Missy, app.Ox, app.Peter], [app.Rhinehardt, app.Vivian, app.Zoe, app.Zostra] ] # 4 by 3
    #app.characters = [ [Brandon, Flash, Heather], [Jenny, Longfellow, Missy], [Ox, Peter, Rhinehardt], [Vivian, Zoe, Zostra] ] # 3 by 4
    #app.characterList = [Zoe, Zostra, Longfellow, Flash, Jenny, Brandon, Ox, Vivian, Missy, Rhinehardt, Vivian, Heather, Peter]
    app.characterSelection = (-1,-1) # row and col of character grid
    app.characterSelected = None # actual character/player instance

def setGround(app):
    app.groundRows = 5
    app.groundCols = 8
    app.groundX = 100 # ground marginX
    app.groundY = 50 # ground marginY
    app.groundList = [ [Empty.name]*app.groundCols for row in range(app.groundRows)]
    app.groundList[2][0] = 'Entrance Hall'
    app.groundList[2][1] = 'Foyer'
    app.groundList[2][2] = 'Grand Staircase'
    app.player1position = (0,0)
    app.player2position = (0,0)
    app.player3position = (0,0)
    app.player4position = (0,0)
    app.player5position = (0,0)
    app.player6position = (0,0)

    #print(app.groundList)

def setBasement(app):
    app.basementRows = 5
    app.basementCols = 8
    app.basementX = 100 # basement marginX
    app.basementY = 50 # basement marginY
    app.basementList = [ [Empty.name]*app.basementCols for row in range(app.basementRows)]
    app.basementList[2][3] = 'Basement Landing'
    #print(app.basementList)

def setUpper(app):
    app.upperRows = 5
    app.upperCols = 8
    app.upperX = 100 # upper marginX
    app.upperY = 50 # upper marginY
    app.upperList = [ [Empty.name]*app.upperCols for row in range(app.upperRows)]
    app.upperList[2][4] = 'Upper Landing'
    #print(app.upperList)

def currentPlayer(app):
    total = app.players
    current = app.index
    nextPlayer = current + 1

    if nextPlayer < total:
        app.index = nextPlayer
    else:
        app.index = 0
    return app.playerList[app.index]

def rollDice(app, player, trait):
    attempt = player.trait
    result = 0
    #dice = app.hauntDie * attempt
    for i in range(attempt):
        result += app.hauntDie[random.randint(0,5)]
    return result

# START SCREEN FUNCTIONS
def start_redrawAll(app, canvas):
    font = 'Arial 20 bold'
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    canvas.create_text(app.width//2, app.height-100, text='Click the screen to begin or click any key to begin playing', font=font,fill='white')
    canvas.create_text(app.width//2, app.height-50, text='Click "r" at any time to restart game',font=font,fill='white')
    canvas.create_image(app.width//2,app.height//2, image=ImageTk.PhotoImage(app.image))
    canvas.create_text(app.width//2, 150, text='Betrayal at House on the Hill', font='Sign\Painter 45',fill='white')

def start_keyPressed(app, event):
    #print(event.key)
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)
    else:
        app.mode = 'set'

def start_mousePressed(app, event):
    app.mode = 'set'

# PLAYERS SET FUNCTIONS
def set_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    color = 'white'
    numbers = '2        3        4        5        6'
    #players = string.digits, string.digits[2:8]
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    canvas.create_text(app.width//2, 150, text='HOW MANY PLAYERS?', font='Arial 45 bold', fill=color)
    canvas.create_text(app.width//2, 250, text='Please enter a number:', font=font, fill=color)
    canvas.create_text(app.width//2, app.height-200, text=app.message, font=font, fill='red')
    canvas.create_text(app.width//2, app.height-100, text=numbers, font=font, fill=color)

def set_keyPressed(app,event):
    #newList = []
    #for player in app.playerList:
    #    newList += player
    #print(event.key)
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)
    if event.key == '2':
        app.mode = 'characters'
        app.players = 2
    elif event.key == '3':
        app.mode = 'characters'
        app.players = 3
    elif event.key == '4':
        app.mode = 'characters'
        app.players = 4
    elif event.key == '5':
        app.mode = 'characters'
        app.players = 5
    elif event.key == '6':
        app.mode = 'characters'
        app.players = 6
    elif event.key not in string.digits:
        app.message = 'Not valid input'
    else:
        app.message = 'Not valid number of players, please choose again.'
    
    #if app.players != 0:
    #    app.playerList = app.playerList[0:app.players]
    #    print(app.playerList)

# CHARACTER SELECTION FUNCTION
def characters_redrawAll(app, canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    canvas.create_text(app.width//2, 40, text='C H O O S E    Y O U R    C H A R A C T E R', font='Arial 30 bold', fill='white')
    canvas.create_text(app.width//2, 70, text='Click cell to view player traits and info', font='Arial 20 bold', fill='white')
    canvas.create_text(20, app.height-25, text='Use the left or down arrow keys to go back (reset number of players).', font='Arial 15 bold',fill='white',anchor='w')
    canvas.create_text(app.width//2, app.height-75, text=f"Current Player: Player {app.currentPlayer['number']}               Players: {app.players}", font='Arial 25 bold',fill='white')
    drawCharacterGrid(app,canvas)

def characters_keyPressed(app,event):
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)
    elif event.key == 'Down' or event.key == 'Left':
        app.mode = 'set' # back to set number of players screen
        setCharacters(app)

def characters_mousePressed(app,event):
    rows = app.characterRows
    cols = app.characterCols
    (row, col) = getCell(app, event.x, event.y, rows, cols, app.marginX, app.marginY)
    if app.characterSelection == (row,col):
        app.characterSelection = (-1,-1)
        app.characterSelected = None
    else:
        app.characterSelection = (row,col)
        if app.characterSelection == (-1,-1): # avoid indexing issues,
            app.characterSelected = None # since it would be set to last value, Zostra
        else:
            app.characterSelected = app.characters[row][col]
            #print(app.selected.name)
            app.mode = 'character'

# CHARACTER FUNCTIONS
def character_redrawAll(app,canvas):
    font = 'Arial 26 bold'
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    # TRAITS
    color = 'white'
    canvas.create_text(app.width//2, 50, text=app.characterSelected.name, fill=app.characterSelected.color,font=font)
    canvas.create_text(app.width//10, 100, text=f'Might: {app.characterSelected.might}', font=font, fill=color,anchor='w')
    canvas.create_text(app.width//10, 140, text=f'Speed: {app.characterSelected.speed}', font=font, fill=color,anchor='w')
    canvas.create_text(app.width//10, 180, text=f'Knowledge: {app.characterSelected.knowledge}', font=font, fill=color,anchor='w')
    canvas.create_text(app.width//10, 220, text=f'Sanity: {app.characterSelected.sanity}', font=font, fill=color,anchor='w')

    canvas.create_text(9*app.width//10, app.height-100, text='To confirm selection, press "Y"', font=font, fill=color, anchor='e')
    canvas.create_text(20, app.height-25, text=f"CURRENT PLAYER: {app.currentPlayer['number']}", font=font, fill=color, anchor='w')
    canvas.create_text(app.width//2, app.height-25, text='Use the left or down arrow keys to go back.', font='Arial 20 bold',fill=color)

def character_keyPressed(app, event):
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)
    elif event.key == 'Down' or event.key == 'Left':
        app.mode = 'characters' # back to characters grid
        app.characterSelection = (-1,-1) # reset selected row, col
        app.characterSelected = None # and selected character
    elif event.key == 'Right': # to debug rn
        app.mode = 'ground'
    elif event.key == 'y':
        if app.currentPlayer['number'] < app.players:
            #print(app.currentPlayer['number'], app.currentPlayer['character'].name)
            #print(app.currentPlayer['character'].name)
            #print(app.currentPlayer['number'], app.currentPlayer['character'].name)
            app.mode = 'characters'
        else:
            app.mode = 'ground'
        app.currentPlayer['character'] = app.characterSelected
        app.currentPlayer = currentPlayer(app)

def character_mousePressed(app, event):
    pass

# GROUND FLOOR BOARD FUNCTIONS
def ground_redrawAll(app,canvas):
    drawGround(app,canvas)

def ground_keyPressed(app,event):
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)
    elif event.key == 'Right':
        app.mode = 'upper'
    elif event.key == 'Left':
        app.mode = 'basement'

def ground_mousePressed(app,event):
    pass

#def ground_mouseReleased(app, event):
#    print(f'mouseReleased at {(event.x, event.y)}')

#def ground_mouseMoved(app, event):
#    print(f'mouseMoved at {(event.x, event.y)}')

#def ground_mouseDragged(app, event):
#    print(f'mouseDragged at {(event.x, event.y)}')

# BASEMENT FLOOR FUNCTIONS
def basement_redrawAll(app,canvas):
    drawBasement(app,canvas)

def basement_keyPressed(app,event):
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)

def basement_mousePressed(app,event):
    print(f'mousePressed at {(event,x, event.y)}')

def basement_mouseReleased(app,event):
    print(f'mouseReleased at {(event.x, event.y)}')

def basement_mouseMoved(app,event):
    print(f'mouseMoved at {(event.x, event.y)}')

def basement_mouseDragged(app,event):
    print(f'mouseDragged at {(event.x, event.y)}')

# UPPER FLOOR FUNCTIONS
def upper_redrawAll(app,canvas):
    drawUpper(app,canvas)

def upper_keyPressed(app,event):
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)

# cell bounds for grids
def getCellBounds(app, row, col, rows, cols, marginX, marginY):
    width = app.width - (2 * marginX)
    height = app.height - (2 * marginY)
    cellWidth = width//cols
    cellHeight = height//rows
    x0 = cellWidth * col + marginX
    y0 = cellHeight * row + marginY
    x1 = cellWidth * (col+1) + marginX
    y1 = cellHeight * (row+1) + marginY
    return x0, y0, x1, y1

def getCell(app,x,y,rows,cols,marginX,marginY): # modeled after grid cell click, https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
    if not inGrid(app, x, y, app.marginX, app.marginY):
        return (-1, -1)
    
    gridWidth = app.width - 2*marginX
    gridHeight = app.height - 2*marginY
    cellWidth = gridWidth/cols
    cellHeight = gridHeight/rows

    row = int((y - marginY)/ cellHeight)
    col = int((x - marginX)/ cellWidth)

    return (row, col)

def inGrid(app, x, y, marginX, marginY):
    return (marginX <= x <= app.width-marginX and 
                marginY <= y <= app.height - marginY)

# characters grid
def drawCharacterGrid(app,canvas):
    rows = app.characterRows
    cols = app.characterCols
    for row in range(rows):
        for col in range(cols):
            x0,y0,x1,y1 = getCellBounds(app, row, col, rows, cols, app.marginX, app.marginY)
            cellWidth = x1-x0
            cellHeight = y1-y0
            canvas.create_rectangle(x0, y0, x1, y1, fill='dodger blue') # gray25
            canvas.create_text(x0+cellWidth//2,y0+cellHeight//2,text=app.characters[row][col].name, fill='white')

# ground floor board
def drawGround(app,canvas):
    rows = app.groundRows
    cols = app.groundCols
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    for row in range(rows):
        for col in range(cols):
            x0,y0,x1,y1 = getCellBounds(app, row, col, rows, cols, app.groundX, app.groundY)
            roomWidth = x1-x0
            roomHeight = y1-y0
            canvas.create_rectangle(x0, y0, x1, y1, fill='saddle brown')
            canvas.create_text(x0+roomWidth//2,y0+roomHeight//2,text=app.groundList[row][col], fill='white')

# basement floor board
def drawBasement(app,canvas):
    rows = app.basementRows
    cols = app.basementCols
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    for row in range(rows):
        for col in range(cols):
            x0,y0,x1,y1 = getCellBounds(app, row, col, rows, cols, app.basementX, app.basementY)
            roomWidth = x1-x0
            roomHeight = y1-y0
            canvas.create_rectangle(x0, y0, x1, y1)
            canvas.create_text(x0+roomWidth//2,y0+roomHeight//2,text=app.basementList[row][col])

# upper floor board
def drawUpper(app,canvas):
    rows = app.upperRows
    cols = app.upperCols
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    for row in range(rows):
        for col in range(cols):
            x0,y0,x1,y1 = getCellBounds(app, row, col, rows, cols, app.upperX, app.upperY)
            roomWidth = x1-x0
            roomHeight = y1-y0
            canvas.create_rectangle(x0, y0, x1, y1)
            canvas.create_text(x0+roomWidth//2,y0+roomHeight//2,text=app.upperList[row][col])

runApp(width=1440, height=775)