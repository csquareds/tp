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

class Player(object):
    def __init__(self, name, mightList, mightIndex, speedList, speedIndex, 
                    knowledgeList, knowledgeIndex, sanityList, sanityIndex, 
                        color, age, birthday, hobbies):
        # TRAITS
        self.mightList = mightList # list of trait values
        self.mightIndex = mightIndex # index number of list
        self.might = self.mightList[self.mightIndex] # actual value
        self.speedList = speedList
        self.speedIndex = speedIndex
        self.speed = self.speedList[self.speedIndex]
        self.knowledgeList = knowledgeList
        self.knowledgeIndex = knowledgeIndex
        self.knowledge = self.knowledgeList[self.knowledgeIndex]
        self.sanityList = sanityList
        self.sanityIndex = sanityIndex
        self.sanity = self.sanityList[self.sanityIndex]

        # INFO/CHARACTERISTICS
        self.name = name
        self.color = color
        self.age = age
        self.birthday = birthday
        self.hobbies = hobbies
        self.status = True # alive, not dead
        self.role = True # explorer/hero, not traitor
    
    def changeTrait(self, trait, change):
        if trait == "might":
            index = self.mightIndex
            index += change
            if not app.haunt:
                if 0 <= index <= 8:
                    self.mightIndex += change
                    self.might = self.mightList[self.mightIndex]
                else:
                    index -= change
            else:
                if index <= 0:
                    self.status = False
                elif index <= 8:
                    self.mightIndex += change
                    self.might = self.mightList[self.mightIndex]
                else:
                    index -= change

        elif trait == "speed":
            index = self.speedIndex
            index += change
            if not app.haunt:
                if 0 <= index <= 8:
                    self.speedIndex += change
                    self.speed = self.speedList[self.speedIndex]
                else:
                    index -= change
            else:
                if index <= 0:
                    self.status = False
                elif index <= 8:
                    self.speedIndex += change
                    self.speed = self.speedList[self.speedIndex]
                else:
                    index -= change

        elif trait == "knowledge":
            index = self.knowledgeIndex
            index += change
            if not app.haunt:
                if 0 <= index <= 8:
                    self.knowledgeIndex += change
                    self.knowledge = self.knowledgeList[self.knowledgeIndex]
                else:
                    index -= change
            else:
                if index <= 0:
                    self.status = False
                elif index <= 8:
                    self.knowledgeIndex += change
                    self.knowledge = self.knowledgeList[self.knowledgeIndex]
                else:
                    index -= change

        elif trait == "sanity":
            index = self.sanityIndex
            index += change
            if not app.haunt:
                if 0 <= index <= 8:
                    self.sanityIndex += change
                    self.sanity = self.sanityList[self.sanityIndex]
                else:
                    index -= change
            else:
                if index <= 0:
                    self.status = False
                elif index <= 8:
                    self.sanityIndex += change
                    self.sanity = self.sanityList[self.sanityIndex]
                else:
                    index -= change
        else:
            return None

    def attemptRole(self, trait):
        if trait == "might":
            dice = self.might

# PLAYERS, note 0 is death
Zoe = Player('Zoe Ingstrom', [0,2,2,3,3,4,4,6,7], 4, [0,4,4,4,4,5,6,8,8], 4,
            [0,1,2,3,4,4,5,5,5], 3, [0,3,4,5,5,6,6,7,8], 3, 'yellow', 8, 
            'November 5th', 'Dolls, Music')
Zostra = Player('Madame Zostra', [0,2,3,3,4,5,5,5,6], 4, [0,2,3,3,5,5,6,6,7], 
            3, [0,1,3,4,4,4,5,6,6], 4, [0,4,4,4,5,6,7,8,8], 3, 'blue', 37, 
            'December 10th', 'Astrology, Cooking, Baseball')
Longfellow = Player('Professor Longfellow', [0,1,2,3,4,5,5,6,6], 3, 
            [0,2,2,4,4,5,5,6,6], 4, [0,4,5,5,5,5,6,7,8], 5, [0,1,3,3,4,5,5,6,7], 
            3, 'white', 57, 'July 27th', 'Gaelic Music, Drama, Fine Wines')
Flash = Player('Darrin "Flash" Williams', [0,2,3,3,4,5,6,6,7], 3, 
            [0,4,4,4,5,6,7,7,8], 5, [0,2,3,3,4,5,5,5,7], 3, [0,1,2,3,4,5,5,5,7],
            3, 'red', 20, 'June 6th', 'Track, Music, Shakespearean Literature')
Jenny = Player('Jenny LeClerc', [0,3,4,4,4,4,5,6,8], 3, [0,2,3,4,4,4,5,6,8], 
            4, [0,2,3,3,4,4,5,6,8], 3, [0,1,1,2,4,4,4,5,6], 5, 'purple', 21, 
                'March 4th', 'Reading, Soccer')
Brandon = Player('Brandon Jaspers', [0,2,3,3,4,5,6,6,7], 4, [0,3,4,4,4,5,6,7,8], 
            3, [0,1,3,3,5,5,6,6,7], 3, [0,3,3,3,4,5,6,7,8], 4, 'green', 12, 
                'May 21st', 'Computers, Camping, Hockey')
Vivian = Player('Vivian Lopez', [0,2,2,2,4,4,5,6,6], 3, [0,3,4,4,4,4,6,7,8], 
            4, [0,4,5,5,5,5,6,6,7], 4, [0,4,4,4,5,6,7,8,8], 3, 'blue', 42, 
                'January 11th', 'Old Movies, Horses')
Missy = Player('Missy Dubourde', [0,2,3,3,3,4,5,6,7], 4, [0,3,4,5,6,6,6,7,7], 
            3, [0,2,3,4,4,5,6,6,6], 4, [0,1,2,3,4,5,5,6,7], 3, 'yellow', 9, 
                'February 14th', 'Swimming, Medicine')
Rhinehardt = Player('Father Rhinehardt', [0,1,2,2,4,4,5,5,7], 3, 
            [0,2,3,3,4,5,6,7,7], 3, [0,1,3,3,4,5,6,6,8], 4, [0,3,4,5,5,6,7,7,8], 
                5, 'white', 62, 'April 29th', 'Fencing, Gardening')
Heather = Player('Heather Granville', [0,3,3,3,4,5,6,7,8], 3, 
            [0,3,3,4,5,6,6,7,8], 3, [0,2,3,3,4,5,6,7,8], 5, [0,3,3,3,4,5,6,6,6], 
                3, 'purple', 18, 'August 2nd', 'Television, Shopping')
Peter = Player('Peter Akimoto', [0,2,3,3,4,5,5,6,8], 3, [0,3,3,3,4,6,6,7,7], 
            4, [0,3,4,4,5,6,7,7,8], 3, [0,3,4,4,4,5,6,6,7], 4, 'green', 13, 
                'September 3rd', 'Bugs, Basketball')
Ox = Player('Ox Bellows', [0,4,5,5,6,6,7,8,8], 3, [0,2,2,2,3,4,5,5,6], 
            5, [0,2,2,3,3,5,5,6,6], 3, [0,2,2,3,4,5,5,6,7], 3, 'red', 23, 
                'October 18th', 'Football, Shiny Objects')

# Player template
#Player = Player('name', mightlist, mightIndex, speedlist, speedIndex, knowledgelist, knowledgeIndex, sanitylist, sanityIndex, color, age, birthday, hobbies)

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
    app.rows = 4
    app.cols = 3
    app.message = None
    app.margin = 50
    app.players = 0
    app.selection = (-1,-1) # row and col of character grid
    app.selected = None # actual character/player instance
    app.player1 = None
    app.player2 = None
    app.player3 = None
    app.player4 = None
    app.player5 = None
    app.player6 = None
    app.characters = [ [Brandon, Flash, Heather, Jenny], [Longfellow, Missy, Ox, Peter], [Rhinehardt, Vivian, Zoe, Zostra] ]
    app.haunt = False
    app.rooms = [Abandoned, Attic, Balcony, Ballroom, Bedroom, Bloody, Catacombs, 
        Chapel, Charred, Chasm, Coal, Collapsed, Conservatory, Creaky, Crypt, 
        Dining, Dusty, Furnace, Gallery, Game, Gardens, Graveyard, Gym, Junk, 
        Kitchen, Larder, Library, Master, Mystic, Operating, Organ, Patio, 
        Pentagram, Research, Servant, StairsBasement, Statuary, Store, Tower, 
            Underground, Vault, Wine]
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
    #app.players = [Zoe, Zostra, Longfellow, Flash, Jenny, Brandon, Ox,
    #                Vivian, Missy, Rhinehardt, Vivian, Heather, Peter]
    app.gameOver = False

def getCell(app,x,y): # modeled after grid cell click, https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
    if not inGrid(app, x, y):
        return (-1, -1)
    
    gridWidth = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    cellWidth = gridWidth/app.cols
    cellHeight = gridHeight/app.rows

    row = int((y - app.margin)/ cellHeight)
    col = int((x - app.margin)/ cellWidth)

    return (row, col)

def inGrid(app, x, y):
    return (app.margin <= x <= app.width-app.margin and 
                app.margin <= y <= app.height - app.margin)

def board_mousePressed(app,event):
    print(f'mousePressed at {(event,x, event.y)}')

def board_mouseReleased(app, event):
    print(f'mouseReleased at {(event.x, event.y)}')

def board_mouseMoved(app, event):
    print(f'mouseMoved at {(event.x, event.y)}')

def board_mouseDragged(app, event):
    print(f'mouseDragged at {(event.x, event.y)}')

def set_keyPressed(app,event):
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
    #elif (event.key == '1' or event.key == '7' or event.key == '8' 
    #    or event.key == '9' or event.key == '0'):
        app.message = 'Not valid number of players, please choose again.'

#def timerFired(app):
#    pass

def rollDice(app, player, trait):
    attempt = player.trait
    result = 0
    #dice = app.hauntDie * attempt
    for i in range(attempt):
        result += app.hauntDie[random.randint(0,5)]
    return result

def start_redrawAll(app, canvas):
    font = 'Helvetica 26 bold'
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    canvas.create_text(app.width//2, app.height-100, text='Click the screen to begin or click any key to begin playing', font=font,fill='white')
    canvas.create_text(app.width//2, app.height-50, text='Click "r" at any time to restart game',font=font,fill='white')
    canvas.create_image(app.width//2,app.height//2, image=ImageTk.PhotoImage(app.image))
    canvas.create_text(app.width//2, 150, text='Betrayal at House on the Hill', font='Sign\Painter 45',fill='white')

def set_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    #players = string.digits, string.digits[2:8]
    canvas.create_text(app.width//2, 150, text='How many players?', font=font)
    canvas.create_text(app.width//2, 200, text='Enter number:', font=font)
    canvas.create_text(app.width//2, app.height-200, text=app.message, font=font)
    canvas.create_text(app.width//2, app.height-100, text='2   3   4   5   6', font=font)

def board_redrawAll(app,canvas):
    drawGrid(app,canvas)

def characters_redrawAll(app, canvas):
    font = 'Arial 26 bold'
    canvas.create_text(app.width//2, 25, text='C H O O S E   Y O U R   C H A R A C T E R', font=font)
    canvas.create_text(app.width//2, app.height-25, text=f'Players: {app.players}', font=font)
    drawGrid(app,canvas)

def characters_keyPressed(app,event):
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)
    elif event.key == 'Down' or event.key == 'Left':
        app.message = None
        app.mode = 'set' # back to set number of players screen
        app.players = 0 # reset number of players

def characters_mousePressed(app,event):
    (row, col) = getCell(app, event.x, event.y)
    if app.selection == (row,col):
        app.selection = (-1,-1)
    app.selection = (row,col)

    app.selected = app.characters[row][col]
    #print(app.selected.name)
    app.mode = 'character'

def character_redrawAll(app,canvas):
    font = 'Arial 26 bold'
    canvas.create_text(app.width//2, 50, text=app.selected.name, font=font)
    canvas.create_text(app.width//10, 100, text=f'Might: {app.selected.might}', font=font, anchor='w')
    canvas.create_text(app.width//10, 130, text=f'Speed: {app.selected.speed}', font=font, anchor='w')
    canvas.create_text(app.width//10, 160, text=f'Knowledge: {app.selected.knowledge}', font=font, anchor='w')
    canvas.create_text(app.width//10, 190, text=f'Sanity: {app.selected.sanity}', font=font, anchor='w')

def character_keyPressed(app, event):
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)
    elif event.key == 'Down' or event.key == 'Left':
        app.mode = 'characters' # back to characters grid
        app.selected = None # reset selected character

def character_mousePressed(app, event):
    pass

def start_keyPressed(app, event):
    print(event.key)
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)
    else:
        app.mode = 'set'

def start_mousePressed(app, event):
    app.mode = 'set'

def getCellBounds(app,row,col):
    width = app.width - (2 * app.margin)
    height = app.height - (2 * app.margin)
    cellWidth = width//app.cols
    cellHeight = height//app.rows
    x0 = cellWidth * col + app.margin
    y0 = cellHeight * row + app.margin
    x1 = cellWidth * (col+1) + app.margin
    y1 = cellHeight * (row+1) + app.margin
    return x0, y0, x1, y1

# characters grid
def drawGrid(app,canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            x0,y0,x1,y1 = getCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1)

def drawRoom(app,canvas):
    x0,y0,x1,y1 = 1,2,3,4
    canvas.create_rectangle(x0,y0,x1,y1,fill='black')

runApp(width=1440, height=775)