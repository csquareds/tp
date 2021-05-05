# CATHERINE CAI 15-112 TERM PROJECT
# SPRING 2021

# Helpful links
# https://en.wikipedia.org/wiki/Betrayal_at_House_on_the_Hill
# https://media.wizards.com/2018/downloads/rules/betrayal_rules.pdf
# https://startyourmeeples.com/2018/09/28/betrayal-at-house-on-the-hill-characters-a-closer-inspection/
# https://startyourmeeples.com/2019/07/09/betrayal-at-house-on-the-hill-rooms-a-strategy-in-9-graphs/

# Images
# https://i0.wp.com/fantasy-hive.co.uk/wp-content/uploads/2018/06/betrayal-house-cover-image.jpg?fit=620%2C420&ssl=1

from cmu_112_graphics import *
import random, string
from tpclasses import *
from hauntinfo import *

# PLAYERS, note 0 is death
def setPlayers(app):
    app.Zoe = Player('Zoe Ingstrom', {'might': [0,2,2,3,3,4,4,6,7], 'speed': [0,4,4,4,4,5,6,8,8], 'knowledge': [0,1,2,3,4,4,5,5,5], 'sanity': [0,3,4,5,5,6,6,7,8]}, {'might': 4, 'speed': 4, 'knowledge': 3, 'sanity': 3}, 'yellow', 8, 'November 5th', 'Dolls, Music')
    app.Zostra = Player('Madame Zostra', {'might': [0,2,3,3,4,5,5,5,6], 'speed': [0,2,3,3,5,5,6,6,7], 'knowledge': [0,1,3,4,4,4,5,6,6], 'sanity': [0,4,4,4,5,6,7,8,8]}, {'might': 4, 'speed': 3, 'knowledge': 4, 'sanity': 3}, 'deep sky blue', 37, 'December 10th', 'Astrology, Cooking, Baseball')
    app.Longfellow = Player('Professor Longfellow', {'might': [0,1,2,3,4,5,5,6,6], 'speed': [0,2,2,4,4,5,5,6,6], 'knowledge': [0,4,5,5,5,5,6,7,8], 'sanity': [0,1,3,3,4,5,5,6,7]}, {'might': 3, 'speed': 4, 'knowledge': 5, 'sanity': 3}, 'white', 57, 'July 27th', 'Gaelic Music, Drama, Fine Wines')
    app.Flash = Player('Darrin "Flash" Williams', {'might': [0,2,3,3,4,5,6,6,7], 'speed': [0,4,4,4,5,6,7,7,8], 'knowledge': [0,2,3,3,4,5,5,5,7], 'sanity': [0,1,2,3,4,5,5,5,7]}, {'might': 3, 'speed': 5, 'knowledge': 3, 'sanity': 3}, 'indian red', 20, 'June 6th', 'Track, Music, Shakespearean Literature')
    app.Jenny = Player('Jenny LeClerc', {'might': [0,3,4,4,4,4,5,6,8], 'speed': [0,2,3,4,4,4,5,6,8], 'knowledge': [0,2,3,3,4,4,5,6,8], 'sanity': [0,1,1,2,4,4,4,5,6]}, {'might': 3, 'speed': 4, 'knowledge': 3, 'sanity': 5}, 'purple1', 21, 'March 4th', 'Reading, Soccer')
    app.Brandon = Player('Brandon Jaspers', {'might': [0,2,3,3,4,5,6,6,7], 'speed': [0,3,4,4,4,5,6,7,8], 'knowledge': [0,1,3,3,5,5,6,6,7], 'sanity': [0,3,3,3,4,5,6,7,8]}, {'might': 4, 'speed': 3, 'knowledge': 3, 'sanity': 4}, 'green2', 12, 'May 21st', 'Computers, Camping, Hockey')
    app.Vivian = Player('Vivian Lopez', {'might': [0,2,2,2,4,4,5,6,6], 'speed': [0,3,4,4,4,4,6,7,8], 'knowledge': [0,4,5,5,5,5,6,6,7], 'sanity': [0,4,4,4,5,6,7,8,8]}, {'might': 3, 'speed': 4,  'knowledge': 4,  'sanity': 3}, 'deep sky blue', 42, 'January 11th', 'Old Movies, Horses')
    app.Missy = Player('Missy Dubourde', {'might': [0,2,3,3,3,4,5,6,7], 'speed': [0,3,4,5,6,6,6,7,7], 'knowledge': [0,2,3,4,4,5,6,6,6], 'sanity': [0,1,2,3,4,5,5,6,7]}, {'might': 4, 'speed': 3, 'knowledge': 4,  'sanity': 3}, 'yellow', 9, 'February 14th', 'Swimming, Medicine')
    app.Rhinehardt = Player('Father Rhinehardt', {'might': [0,1,2,2,4,4,5,5,7], 'speed': [0,2,3,3,4,5,6,7,7], 'knowledge': [0,1,3,3,4,5,6,6,8], 'sanity': [0,3,4,5,5,6,7,7,8]}, {'might': 3, 'speed': 3, 'knowledge': 4, 'sanity': 5}, 'white', 62, 'April 29th', 'Fencing, Gardening')
    app.Heather = Player('Heather Granville', {'might': [0,3,3,3,4,5,6,7,8], 'speed': [0,3,3,4,5,6,6,7,8], 'knowledge': [0,2,3,3,4,5,6,7,8], 'sanity': [0,3,3,3,4,5,6,6,6]}, {'might': 3, 'speed': 3, 'knowledge': 5, 'sanity': 3}, 'purple1', 18, 'August 2nd', 'Television, Shopping')
    app.Peter = Player('Peter Akimoto', {'might': [0,2,3,3,4,5,5,6,8], 'speed': [0,3,3,3,4,6,6,7,7], 'knowledge': [0,3,4,4,5,6,7,7,8], 'sanity': [0,3,4,4,4,5,6,6,7]}, {'might': 3, 'speed': 4,  'knowledge': 3, 'sanity': 4}, 'green2', 13, 'September 3rd', 'Bugs, Basketball')
    app.Ox = Player('Ox Bellows', {'might': [0,4,5,5,6,6,7,8,8], 'speed': [0,2,2,2,3,4,5,5,6], 'knowledge': [0,2,2,3,3,5,5,6,6], 'sanity': [0,2,2,3,4,5,5,6,7]}, {'might': 3,  'speed': 5,  'knowledge': 3, 'sanity': 3}, 'indian red', 23, 'October 18th', 'Football, Shiny Objects')
    app.Death = Player('Death', {'might':[1,1,1,1,1,1,1,1,1], 'speed':[8,8,8,8,8,8,8,8,8],'knowledge':[0,1,2,3,4,5,6,7,8], 'sanity': [1,1,1,1,1,1,1,1,1]}, {'might': 8, 'speed': 8, 'knowledge': 8, 'sanity': 8}, 'gray25', None, 'Beginning of time', 'Chess')

# FLOORS
def setFloors(app):
    app.Ground = Floor('Ground Level','ground')
    app.Basement = Floor('Basement','basement')
    app.Upper = Floor('Upper Level','upper')

# ROOMS, does it have: omen item
def setRooms(app):
    app.Entrance = Room('Entrance Hall', [app.Ground], False, False)
    app.Foyer = Room('Foyer', [app.Ground], False, False)
    app.Grand = Room('Grand Stairs', [app.Ground], False, False)
    app.Basement_Landing = Room('Basement Landing', [app.Basement], False, False)
    app.Upper_Landing = Room('Upper Landing', [app.Upper], False, False)
    app.Abandoned = Room('Abandoned Room', [app.Ground, app.Basement], True, False)
    app.Attic = Room('Attic', [app.Upper], False, True)
    app.Balcony = Room('Balcony', [app.Ground, app.Upper], True, False)
    app.Ballroom = Room('Ballroom', [app.Ground, app.Basement], False, True)
    app.Creaky = Room('Creaky Hallway', [app.Upper, app.Ground, app.Basement], False, False)
    app.Crypt = Room('Crypt', [app.Basement, app.Ground], False, True)
    app.Bloody = Room('Bloody Room', [app.Upper, app.Ground, app.Basement], False, True)
    app.Chapel = Room('Chapel', [app.Upper, app.Ground], False, False)
    app.Vault = Room('Vault', [app.Upper, app.Basement, app.Ground], False, True)
    app.Collapsed = Room('Collapsed Room', [app.Upper, app.Ground, app.Basement], True, False)
    app.Dining = Room('Dining Room', [app.Ground], True, False)
    app.Furnace = Room('Furnace Room', [app.Basement, app.Ground], True, False)
    app.Graveyard = Room('Graveyard', [app.Ground], False, False)
    app.Gym = Room('Gymnasium', [app.Ground, app.Basement], True, False)
    app.Operating = Room('Operating Laboratory', [app.Upper, app.Basement], False, False)
    app.Organ = Room('Organ Room', [app.Upper, app.Ground, app.Basement], False, False)
    app.Store = Room('Storeroom', [app.Upper, app.Basement], False, True)
    app.Tower = Room('Tower', [app.Upper], False, False)
    app.Catacombs = Room('Catacombs', [app.Basement], True, False)
    app.Dusty = Room('Dusty Hallway', [app.Upper, app.Ground, app.Basement], False, False)
    app.Kitchen = Room('Kitchen', [app.Ground, app.Basement], True, False)
    app.Junk = Room('Junk', [app.Upper, app.Ground, app.Basement], True, False)
    app.Larder = Room('Larder', [app.Basement], False, True)
    app.Patio = Room('Patio', [app.Ground], False, False)
    app.Pentagram = Room('Pentagram Chamber', [app.Basement], True, False)
    app.Research = Room('Research Laboratory', [app.Upper, app.Basement], False, False)
    app.Underground = Room('Underground Lake', [app.Basement], False, False)
    app.Vault = Room('Vault', [app.Upper, app.Basement], False, True) 
    app.Chasm = Room('Chasm', [app.Basement], False, False)
    app.Coal = Room('Coal Chute', [app.Ground], False, False)
    app.Collapsed = Room('Collapsed Room', [app.Upper, app.Ground], False, False)
    app.Charred = Room('Charred Room', [app.Upper, app.Ground], True, False)
    app.Conservatory = Room('Conservatory', [app.Upper, app.Ground], False, False)
    app.Gallery = Room('Gallery', [app.Upper], True, False)
    app.Game = Room('Game Room', [app.Upper, app.Ground, app.Basement], False, False)
    app.Gardens = Room('Gardens', [app.Ground], False, False)
    app.Library = Room('Library', [app.Upper, app.Ground], False, False)
    app.Master = Room('Master Bedroom', [app.Upper], True, False)
    app.Mystic = Room('Mystic Room', [app.Upper, app.Ground, app.Basement], False, False)
    app.Servant = Room("Servants' Quarters", [app.Upper, app.Basement], True, False)
    app.StairsBasement = Room('Stairs from Basement', [app.Basement], False, False)
    app.Statuary = Room('Statuary Corridor', [app.Upper, app.Ground, app.Basement], False, False)
    app.Wine = Room('Wine Cellar', [app.Basement], False, True)
    app.Bedroom = Room('Bedroom', [app.Upper], False, False)
    app.Bathroom = Room('Bathroom', [app.Upper, app.Ground, app.Basement], False, False)
    app.Hallway = Room('Hallway', [app.Upper, app.Ground, app.Basement], False, False)
    app.Bedroom2 = Room('Old Bedroom', [app.Upper, app.Ground, app.Basement], False, False)
    app.Movie = Room('Movie Room', [app.Upper, app.Ground, app.Basement], True, False)
    app.Empty = Room('Undiscovered', [app.Upper, app.Ground, app.Basement], False, False)

# OMENS
def setOmens(app):
    app.Skull = Omen('Skull', 'A skull cracked, and missing teeth')
    app.Bite = Omen('Bite', 'A growl, the scent of death. Pain. Darkness. Gone.')
    app.Book = Omen('Book', 'A diary or lab notes? Ancient script or modern ravings?')
    app.Crystal = Omen('Crystal Ball', 'Hazy images appear in the glass.')
    app.Dog = Omen('Dog', 'COMPANION This mangy dog seems friendly. At least you hope it is.')
    app.Girl = Omen('Girl', 'COMPANION A girl. Trapped. Alone. You free her!')
    app.Holy = Omen('Holy Symbol', 'A symbol of calm in an unsettling world.')
    app.Madman = Omen('Madman', 'COMPANION A raving, frothing madman.')
    app.Mask = Omen('Mask', 'A somber mask to hide your intentions.')
    app.Medallion = Omen('Medallion', 'A medallion inscribed with a pentagram.')
    app.Ring = Omen('Ring', 'A battered ring with an incomprehensible inscription.')
    app.Spear = Omen('Spear', 'WEAPON A weapon pulsing with power.')
    app.Spirit = Omen('Spirit Board', 'A board with letters and numbers to call the dead.')

# ITEMS
def setItems(app):
    app.Puzzle = Item("Puzzle Box", "There must be a way to open it.", "Gain 1 knowledge.")
    app.Music = Item("Music Box", "A hand-crafted antique. It plays a haunting melody that gets stuck in your head.", "Gain 1 knowledge.")
    app.Medical = Item("Medical Kit", "A doctor's bag, depleted in some critical resources.", "Gain 1 knowledge.")
    app.Idol = Item("Idol", "Perhaps it's chosen you for some greater purpose. Like human sacrifice.", "Lose 1 might.")
    app.Healing = Item("Healing Salve", "A sticky paste in a shallow bowl.", "Gain 1 sanity.")
    app.Dynamite = Item("Dynamite", "The fuse isn't lit... yet", "Gain 1 speed.")
    app.Dice = Item("Dark Dice", "Are you feeling lucky?", "Gain 1 knowledge.")
    app.Candle = Item("Candle", "It makes the shadows move— at least, you hope it's doing that.", "Gain 1 knowledge.")
    app.Bottle = Item("Bottle", "An opaque vial containing a black liquid.", "Lose 1 sanity.")
    app.Blood_Dagger = Item("Blood Dagger", "WEAPON A nasty weapon. Needles and tubes extend from the handle... and plunge right into your veins.", "Lose 1 might.")
    app.Bell = Item("Bell", "A brass bell that makes a resonant clang.", "Gain 1 sanity.")
    app.Axe = Item("Axe", "WEAPON Very sharp.", "Gain 1 might.")
    app.Armor = Item("Armor", "It's just prop armor from a Renaissance fair, but it's still metal.", "Gain 1 might")
    app.Amulet = Item("Amulet of the Ages", "Ancient silver and inlaid gems, inscribed with blessings.", "Gain 1 for every trait.")
    app.Adrenaline = Item("Adrenaline Shot", "A syringe containing a strange fluorescent liquid.", "Gain 1 speed.")

def setUp(app): # general setup: rooms, omens, items
    app.rooms = [app.Abandoned, app.Attic, app.Balcony, app.Ballroom, app.Bedroom, app.Bloody, app.Catacombs, 
        app.Chapel, app.Charred, app.Chasm, app.Coal, app.Collapsed, app.Conservatory, app.Creaky, app.Crypt, 
        app.Dining, app.Dusty, app.Furnace, app.Gallery, app.Game, app.Gardens, app.Graveyard, app.Gym, app.Junk, 
        app.Kitchen, app.Larder, app.Library, app.Master, app.Mystic, app.Operating, app.Organ, app.Patio, 
        app.Pentagram, app.Research, app.Servant, app.StairsBasement, app.Statuary, app.Store, app.Tower, 
            app.Underground, app.Vault, app.Wine, app.Bathroom, app.Hallway, app.Bedroom2, app.Movie]
    app.omens = [app.Skull, app.Bite, app.Book, app.Crystal, app.Dog, app.Girl, app.Holy, 
                app.Madman, app.Mask, app.Medallion, app.Ring, app.Spear, app.Spirit]
    app.items = [app.Puzzle, app.Music, app.Medical, app.Idol, app.Healing, app.Dynamite, app.Dice, 
        app.Candle, app.Bottle, app.Blood_Dagger, app.Bell, app.Axe, app.Armor, app.Amulet, app.Adrenaline]

def setHaunt(app):
    app.heroText1 = heroText1
    app.heroText2 = heroText2
    app.heroText3 = heroText3
    app.heroText4 = heroText4
    app.heroText6 = heroText6

def appStarted(app):
    app.mode = 'start'
    app.image = app.loadImage('bahoth.jpeg') # start screen image
    app.hauntCount = 0 # haunt count
    app.haunt = False # NOT haunt phase
    setFloors(app)
    setRooms(app)
    setOmens(app)
    setItems(app)
    setPlayers(app)
    setCharacters(app)
    setCharacter(app)
    setUp(app)
    setGround(app)
    setBasement(app)
    setUpper(app)
    setDiceRoll(app)
    setCard(app)
    setHaunt(app)
    app.floorLists = {'ground':app.groundList, 'basement':app.basementList, 'upper':app.upperList}
    app.deathRoll = 0
    app.deathKnowledge = 9
    app.gameOver = False
    app.deathWin = False
    app.heroWin = False

def setCharacters(app):
    app.message = None
    app.players = 0 # total number of players
    app.player1 = {'number': 1, 'character': None, 'ground': (2,0), 'upper': (2,4), 'basement': (2,4), 'current': 'ground'} # starting floor positions, current floor, all start on ground floor
    app.player2 = {'number': 2, 'character': None, 'ground': (2,0), 'upper': (2,4), 'basement': (2,4), 'current': 'ground'}
    app.player3 = {'number': 3, 'character': None, 'ground': (2,0), 'upper': (2,4), 'basement': (2,4), 'current': 'ground'}
    app.player4 = {'number': 4, 'character': None, 'ground': (2,0), 'upper': (2,4), 'basement': (2,4), 'current': 'ground'}
    app.player5 = {'number': 5, 'character': None, 'ground': (2,0), 'upper': (2,4), 'basement': (2,4), 'current': 'ground'}
    app.player6 = {'number': 6, 'character': None, 'ground': (2,0), 'upper': (2,4), 'basement': (2,4), 'current': 'ground'}
    app.player7 = {'number': 7, 'character': None, 'ground': (2,0), 'upper': (2,4), 'basement': (2,4), 'current': 'ground'} # for monster/ghost/haunt
    app.playerList = [app.player1, app.player2, app.player3, app.player4, app.player5, app.player6, app.player7]
    app.index = 0
    app.currentPlayer = app.playerList[app.index]

def setCharacter(app):
    app.characterRows = 3
    app.characterCols = 4
    app.marginX = 50
    app.marginY = 150
    app.characters = [ [app.Brandon, app.Flash, app.Heather, app.Jenny], [app.Longfellow, app.Missy, app.Ox, app.Peter], [app.Rhinehardt, app.Vivian, app.Zoe, app.Zostra] ] # 4 by 3
    app.characterSelection = (-1,-1) # row and col of character grid
    app.characterSelected = None # actual character/player instance
    app.selectedCharacters = set()
    app.invalidCharacterMessage = None

def setGround(app):
    app.groundRows = 5
    app.groundCols = 8
    app.groundX = 100 # ground marginX
    app.groundY = 100 # ground marginY
    app.groundList = [ [app.Empty.name]*app.groundCols for row in range(app.groundRows)]
    app.groundList[2][0] = 'Entrance Hall'
    app.groundList[2][1] = 'Foyer'
    app.groundList[2][2] = 'Grand Staircase'
    app.groundSelection = (-1,-1) # row and col of ground grid
    app.groundSelected = None # selected room instance

def setBasement(app):
    app.basementRows = 5
    app.basementCols = 8
    app.basementX = 100 # basement marginX
    app.basementY = 100 # basement marginY
    app.basementList = [ [app.Empty.name]*app.basementCols for row in range(app.basementRows)]
    app.basementList[2][4] = 'Basement Landing'
    app.basementSelection = (-1,-1) # row and col of basement grid
    app.basementSelected = None # selected room instance

def setUpper(app):
    app.upperRows = 5
    app.upperCols = 8
    app.upperX = 100 # upper marginX
    app.upperY = 100 # upper marginY
    app.upperList = [ [app.Empty.name]*app.upperCols for row in range(app.upperRows)]
    app.upperList[2][4] = 'Upper Landing'
    app.upperSelection = (-1,-1) # row and col of upper grid
    app.upperSelected = None # selected room instance

def setDiceRoll(app):
    app.roll = None
    app.die = [0, 0, 1, 1, 2, 2] # 8 dice
    app.dice = [app.roll, app.roll, app.roll, app.roll, app.roll, app.roll, app.roll, app.roll]
    app.rollType = None
    app.result = 0
    app.target = 0

def setCard(app):
    app.type = None
    app.currentCard = None
    app.currentOmen = None
    app.currentItem = None
    app.omenSet = set()
    app.itemSet = set()

def currentPlayer(app):
    total = app.players
    current = app.index
    nextPlayer = current + 1
    count = 0 # death counter
    
    if nextPlayer < total:
        app.index = nextPlayer
    else:
        app.index = 0
    
    if app.haunt:
        for i in range(total):
            if not app.playerList[i]['character'].status: # if player is dead
                count += 1
        if count >= app.players:
            app.gameOver = True
            app.deathWin = True
            app.mode = 'gameOver'
        else:
            while not app.playerList[app.index]['character'].status: # while player not dead
                if app.index + 1 < total:
                    app.index += 1
                else:
                    app.index = 0
    return app.playerList[app.index]

def validMoveHelper(app, floor, player, rows, cols, row, col):
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    currentFloor = app.currentPlayer['current']
    currentRow,currentCol = app.currentPlayer[floor]
    totalRows,totalCols = rows,cols
    potentialRow,potentialCol = row, col
    
    if currentFloor != floor:
        return False

    for drow,dcol in directions:
        nextToRow = potentialRow + drow
        nextToCol = potentialCol + dcol
        if ((nextToRow < 0) or (nextToRow >= totalRows) or
           (nextToCol < 0) or (nextToCol >= totalCols)):
           nextToRow = potentialRow - drow
           nextToCol = potentialCol - dcol
        elif app.floorLists[floor][nextToRow][nextToCol] != 'Undiscovered': # checks if room is next to at least one already discovered/set room
            return True
    return False

def validMove(app, floor, player, rows, cols, row, col):
    currentPlayer = app.currentPlayer['character']
    moves = currentPlayer.speed
    
    currentRow,currentCol = app.currentPlayer[floor]
    totalRows,totalCols = rows,cols
    potentialRow,potentialCol = row, col
    rowDifference = abs(potentialRow - currentRow)
    colDifference = abs(potentialCol - currentCol)
    totalMoves = rowDifference + colDifference
    validMoveHelp = validMoveHelper(app, floor, player, rows, cols, row, col)
    
    if (0 <= potentialRow <= totalRows and 0 <= potentialCol <= totalCols and 
            totalMoves <= moves and validMoveHelp and app.rooms != []):
        return True
    else:
        return False

def rollDice(app, trait, target): # for example, trait = self.might
    attempt = trait
    app.result = 0

    for i in range(attempt):
        app.roll = app.die[random.randint(0,5)]
        app.dice[i] = app.roll
        app.result += app.roll
    if app.result < target:
        return False
    else:
        return True
    app.mode = app.currentPlayer['current']

def hauntRoll(app):
    app.mode = 'rollDice'
    app.result = 0
    app.target = app.hauntCount
    for i in range(6):
        app.roll = app.die[random.randint(0,5)]
        app.dice[i] = app.roll
        app.result += app.roll
    if app.result < app.hauntCount:
        app.haunt = True
        app.currentPlayer = app.playerList[0]
        app.mode = 'hauntHeroes'
    else:
        app.hauntCount += 1

def chessRoll(app):
    app.dice = [None] * 8
    app.result = 0
    app.deathRoll = 0
    roll = 0
    difference = 0
    current = app.currentPlayer['character']

    if app.deathKnowledge < 2:
        app.heroWin = True
        app.gameOver = True
        app.mode = 'gameOver'
    else:
        for i in range(app.deathKnowledge):
            roll = app.die[random.randint(0,4)]
            app.deathRoll += roll

        for i in range(current.knowledge):
            app.roll = app.die[random.randint(0,5)]
            app.dice[i] = app.roll
            app.result += app.roll
        
        difference = app.deathRoll - app.result
        if difference < 3:
            app.deathKnowledge -= 1
        else:
            current.knowledge = current.changeTrait(current.knowledge, 'knowledge',-1, app.haunt)
    
    if app.result > app.deathRoll:
        app.heroWin = True
        app.gameOver = True
        app.mode = 'gameOver'

    app.currentPlayer = currentPlayer(app)

# START SCREEN FUNCTIONS
def start_redrawAll(app, canvas):
    font = 'Arial 20 bold'
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    canvas.create_text(app.width//2, app.height-100, text='Click the screen to begin or click any key to begin playing', font=font,fill='white')
    canvas.create_text(app.width//2, app.height-50, text='Click "r" at any time to restart game',font=font,fill='white')
    canvas.create_image(app.width//2,app.height//2, image=ImageTk.PhotoImage(app.image))
    canvas.create_text(app.width//2, 140, text='Betrayal at House on the Hill', font='Sign\Painter 70',fill='white')

def start_keyPressed(app, event):
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
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    canvas.create_text(app.width//2, 150, text='HOW MANY PLAYERS?', font='Arial 45 bold', fill=color)
    canvas.create_text(app.width//2, 250, text='Please enter a number:', font=font, fill=color)
    canvas.create_text(app.width//2, app.height-200, text=app.message, font=font, fill='red')
    canvas.create_text(app.width//2, app.height-100, text=numbers, font=font, fill=color)

def set_keyPressed(app,event):
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
            app.invalidCharacterMessage = None
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
    canvas.create_text(app.width//10, 300, text=f'Might List: {app.characterSelected.traitList["might"]}', font=font, fill=color,anchor='w')
    canvas.create_text(app.width//10, 350, text=f'Speed List: {app.characterSelected.traitList["speed"]}', font=font, fill=color,anchor='w')
    canvas.create_text(app.width//10, 400, text=f'Knowledge List: {app.characterSelected.traitList["knowledge"]}', font=font, fill=color,anchor='w')
    canvas.create_text(app.width//10, 450, text=f'Sanity List: {app.characterSelected.traitList["sanity"]}', font=font, fill=color,anchor='w')
    canvas.create_text(app.width//10, 520, text=f'Age: {app.characterSelected.age}, Birthday: {app.characterSelected.birthday}, Hobbies: {app.characterSelected.hobbies}', font=font, fill=color,anchor='w')
    
    # OTHER
    canvas.create_text(app.width//2, app.height-150, text="Note: SPEED is how many floor tiles you may move.", font=font, fill=color)
    canvas.create_text(9*app.width//10, app.height-100, text='To confirm selection, press "Y"', font=font, fill=color, anchor='e')
    canvas.create_text(20, app.height-25, text=f"CURRENT PLAYER: {app.currentPlayer['number']}", font=font, fill=color, anchor='w')
    canvas.create_text(app.width//2, app.height-25, text='Use the left or down arrow keys to go back.', font='Arial 20 bold',fill=color)

    if app.invalidCharacterMessage != None:
        canvas.create_text(app.width//2, app.height-150, text=app.invalidCharacterMessage,font=font,fill='red')

def character_keyPressed(app, event):
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)
    elif event.key == 'Down' or event.key == 'Left':
        app.mode = 'characters' # back to characters grid
        app.characterSelection = (-1,-1)# reset selected row, col
        app.characterSelected = None # and selected character
    elif event.key == 'y':
        if app.characterSelected not in app.selectedCharacters:
            if app.currentPlayer['number'] < app.players:
                app.mode = 'characters'
            else:
                app.mode = 'rules'
            app.selectedCharacters.add(app.characterSelected)
            app.currentPlayer['character'] = app.characterSelected
            app.currentPlayer = currentPlayer(app)
            app.characterSelection = (-1,-1)# reset selected row, col
            app.characterSelected = None # and selected character
        else:
            app.invalidCharacterMessage = 'Character has already been chosen, please go back and choose another character.'

# RULES FUNCTIONS
def rules_redrawAll(app,canvas):
    drawRules(app,canvas)

def rules_keyPressed(app,event):
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)

def rules_mousePressed(app,event):
    app.mode = 'ground'

# GROUND FLOOR BOARD FUNCTIONS
def ground_redrawAll(app,canvas):
    drawGround(app,canvas)
    canvas.create_text(20, 25, text='GROUND FLOOR',font='Arial 20 bold',fill='white', anchor='w')
    informationText(app,canvas)
    drawGroundPositions(app,canvas)
    
def ground_keyPressed(app,event):
    rows, cols = app.groundRows, app.groundCols
    selectedRow, selectedCol = app.groundSelection

    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)
    elif event.key == 'Right':
        app.mode = 'upper'
    elif event.key == 'Left':
        app.mode = 'basement'
    elif event.key == 'h':
        app.hauntCount = 13
        hauntRoll(app)
        app.result = 0
        app.dice = [None] * 8
        app.mode = 'hauntHeroes'
    elif event.key == 'c':
        if validMove(app, 'ground', app.currentPlayer, rows, cols, selectedRow, selectedCol):
            if app.groundList[selectedRow][selectedCol] == 'Undiscovered':
                room = app.rooms[random.randrange(len(app.rooms))]
                while app.Ground not in room.floors or room in app.Ground.rooms: # checking if room is a ground floor room and if already discovered (prevent repeat rooms)
                    room = app.rooms[random.randrange(len(app.rooms))]
                app.groundList[selectedRow][selectedCol] = room.name # set new room name / discover new room!
                app.Ground.rooms.add(room)
                app.rooms.remove(room)
                cards(app,room)
            elif app.groundList[selectedRow][selectedCol] == 'Grand Staircase':
                app.currentPlayer['current'] = 'upper'
            elif app.groundList[selectedRow][selectedCol] == 'Coal Chute':
                app.currentPlayer['current'] = 'basement'
            app.currentPlayer['ground'] = (selectedRow, selectedCol) # set player's new position
            app.currentPlayer = currentPlayer(app) # next player's turn
            app.groundSelection = (-1,-1)
            app.groundSelected = None

def ground_mousePressed(app,event):
    rows, cols = app.groundRows, app.groundCols
    (row, col) = getCell(app, event.x, event.y, rows, cols, app.groundX, app.groundY)
    if app.groundSelection == (row,col):
        app.groundSelection = (-1,-1)
        app.groundSelected = None
    else:
        app.groundSelection = (row,col)
        if app.groundSelection == (-1,-1): # avoid indexing issues,
            app.groundSelected = None # since it would be set to last value
        else:
            app.groundSelected = app.groundList[row][col]

# BASEMENT FLOOR FUNCTIONS
def basement_redrawAll(app,canvas):
    drawBasement(app,canvas)
    canvas.create_text(20, 25, text='BASEMENT',font='Arial 20 bold',fill='white', anchor='w')
    informationText(app,canvas)
    drawBasementPositions(app,canvas)
    
def basement_keyPressed(app,event):
    rows, cols = app.basementRows, app.basementCols
    selectedRow, selectedCol = app.basementSelection

    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)
    elif event.key == 'Right':
        app.mode = 'ground'
    elif event.key == 'c':
        if validMove(app, 'basement', app.currentPlayer, rows, cols, selectedRow, selectedCol):
            if app.basementList[selectedRow][selectedCol] == 'Undiscovered':
                room = app.rooms[random.randrange(len(app.rooms))]
                while app.Basement not in room.floors or room in app.Basement.rooms: # checking if room is a ground floor room and if already discovered (prevent repeat rooms)
                    room = app.rooms[random.randrange(len(app.rooms))]
                app.basementList[selectedRow][selectedCol] = room.name # set new room name / discover new room!
                app.Basement.rooms.add(room)
                app.rooms.remove(room)
                cards(app,room)
            elif app.basementList[selectedRow][selectedCol] == 'Stairs from Basement':
                app.currentPlayer['current'] = 'ground'
                app.currentPlayer['ground'] = (2,1) # can use stairs go to foyer, but cannot go from foyer to basement
            app.currentPlayer['basement'] = (selectedRow, selectedCol) # set player's new position
            app.basementSelection = (-1,-1)
            app.basementSelected = None
            app.currentPlayer = currentPlayer(app) # next player's turn
            
def basement_mousePressed(app,event):
    rows, cols = app.basementRows, app.basementCols
    (row, col) = getCell(app, event.x, event.y, rows, cols, app.basementX, app.basementY)
    if app.basementSelection == (row,col):
        app.basementSelection = (-1,-1)
        app.basementSelected = None
    else:
        app.basementSelection = (row,col)
        if app.basementSelection == (-1,-1): # avoid indexing issues,
            app.basementSelected = None # since it would be set to last value
        else:
            app.basementSelected = app.basementList[row][col]

# UPPER FLOOR FUNCTIONS
def upper_redrawAll(app,canvas):
    drawUpper(app,canvas)
    canvas.create_text(20, 25, text='UPPER FLOOR',font='Arial 20 bold',fill='white',anchor='w')
    informationText(app,canvas)
    drawUpperPositions(app,canvas)

def upper_keyPressed(app,event):
    rows, cols = app.upperRows, app.upperCols
    selectedRow, selectedCol = app.upperSelection

    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)
    elif event.key == 'Left':
        app.mode = 'ground'
    elif event.key == 'c':
        if validMove(app, 'upper', app.currentPlayer, rows, cols, selectedRow, selectedCol):
            if app.upperList[selectedRow][selectedCol] == 'Undiscovered':
                room = app.rooms[random.randrange(len(app.rooms))]
                while app.Upper not in room.floors or room in app.Upper.rooms: # checking if room is a ground floor room and if already discovered (prevent repeat rooms)
                    room = app.rooms[random.randrange(len(app.rooms))]
                app.upperList[selectedRow][selectedCol] = room.name # set new room name / discover new room!
                app.Upper.rooms.add(room)
                app.rooms.remove(room)
                cards(app,room)
            elif app.upperList[selectedRow][selectedCol] == 'Upper Landing':
                app.currentPlayer['current'] = 'ground'
            app.currentPlayer['upper'] = (selectedRow, selectedCol) # set player's new position
            app.upperSelection = (-1,-1)
            app.upperSelected = None
            app.currentPlayer = currentPlayer(app) # next player's turn
            
def upper_mousePressed(app,event):
    rows, cols = app.upperRows, app.upperCols
    (row, col) = getCell(app, event.x, event.y, rows, cols, app.upperX, app.upperY)
    if app.upperSelection == (row,col):
        app.upperSelection = (-1,-1)
        app.upperSelected = None
    else:
        app.upperSelection = (row,col)
        if app.upperSelection == (-1,-1): # avoid indexing issues,
            app.upperSelected = None # since it would be set to last value
        else:
            app.upperSelected = app.upperList[row][col]

def angryBeing(currentPlayer):
    player = currentPlayer['character']
    trait = currentPlayer.speed
    target = 5
    change = 1
    return trait, 'currentPlayer.speed', target, change

# ROLL DICE FUNCTIONS
def rollDice_redrawAll(app,canvas):
    drawDice(app,canvas)

def rollDice_mousePressed(app,event):
    if app.rollType == 'omen':
        hauntRoll(app)
        app.rollType = None
    elif app.rollType == 'normal':
        if app.type == 'event':
            if app.currentItem == app.Angry:
                traitValue, trait, target, change = angryBeing(app.currentPlayer)
                if rollDice(app, trait, target): # for example, trait = self.might
                    app.currentPlayer['character'].speed = app.currentPlayer['character'].changeTrait(traitValue, trait, 1, app.haunt)
                else:
                    app.currentPlayer['character'].speed = app.currentPlayer['character'].changeTrait(traitValue, trait, -1, app.haunt)
        app.rollType = None
    else:
        app.roll = None
        app.die = [0, 0, 1, 1, 2, 2] # 8 dice
        app.dice = [app.roll, app.roll, app.roll, app.roll, app.roll, app.roll, app.roll, app.roll]
        app.rollType = None
        app.result = 0
        app.mode = app.currentPlayer['current']

def rollDice_keyPressed(app,event):
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)

# CARD FUNCTIONS - OMENS, EVENTS, ITEMS
def card_redrawAll(app,canvas):
    drawCard(app,canvas)

def card_mousePressed(app,event):
    current = app.currentPlayer['character']
    if app.type == 'omen':
        app.mode = 'rollDice'
    elif app.type == 'item':
        if app.currentItem == app.Adrenaline:
            current.speed = current.changeTrait(current.speed, 'speed',1, app.haunt)
        elif app.currentItem == app.Amulet:
            current.speed = current.changeTrait(current.speed, 'speed',1, app.haunt)
            current.might = current.changeTrait(current.might, 'might',1, app.haunt)
            current.knowledge = current.changeTrait(current.knowledge, 'knowledge',1, app.haunt)
            current.sanity = current.changeTrait(current.sanity, 'sanity',1, app.haunt)
        elif app.currentItem == app.Armor:
            current.might = current.changeTrait(current.might, 'might',1, app.haunt)
        elif app.currentItem == app.Axe:
            current.might = current.changeTrait(current.might, 'might',1, app.haunt)
        elif app.currentItem == app.Bell:
            current.sanity = current.changeTrait(current.sanity, 'sanity',1, app.haunt)
        elif app.currentItem == app.Blood_Dagger:
            current.might = current.changeTrait(current.might, 'might',-1, app.haunt)
        elif app.currentItem == app.Bottle:
            current.sanity = current.changeTrait(current.sanity, 'sanity',1, app.haunt)
        elif app.currentItem == app.Candle:
            current.knowledge = current.changeTrait(current.knowledge, 'knowledge',1, app.haunt)
        elif app.currentItem == app.Dice:
            current.knowledge = current.changeTrait(current.knowledge, 'knowledge',1, app.haunt)
        elif app.currentItem == app.Dynamite:
            current.speed = current.changeTrait(current.speed, 'speed',1, app.haunt)
        elif app.currentItem == app.Healing:
            current.sanity = current.changeTrait(current.sanity, 'sanity',1, app.haunt)
        elif app.currentItem == app.Idol:
            current.might = current.changeTrait(current.might, 'might',-1, app.haunt)
        elif app.currentItem == app.Medical:
            current.knowledge = current.changeTrait(current.knowledge, 'knowledge',1, app.haunt)
        elif app.currentItem == app.Music:
            current.knowledge = current.changeTrait(current.knowledge, 'knowledge',1, app.haunt)
        app.mode = app.currentPlayer['current']

def card_keyPressed(app,event):
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)
    else:
        app.mode = 'rollDice'

# HAUNT HEROES FUNCTIONS
def hauntHeroes_redrawAll(app,canvas):
    drawHauntHeroes(app,canvas)

def hauntHeroes_mousePressed(app,event):
    app.mode = 'chessRoll'

def hauntHeroes_keyPressed(app,event):
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)
        
# CHESS ROLL SCREEN FUNCTIONS
def chessRoll_redrawAll(app,canvas):
    drawHauntRoll(app,canvas)

def chessRoll_mousePressed(app,event):
    chessRoll(app)

def chessRoll_keyPressed(app,event):
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)

# GAME OVER FUNCTIONS
def gameOver_redrawAll(app,canvas):
    drawGameOver(app,canvas)

def gameOver_keyPressed(app,event):
    if event.key == 'r':
        app.mode = 'start'
        appStarted(app)

# omen event item helper function
def cards(app,room):
    if room.omen:
        if app.omens != []:
            if not app.haunt:
                app.rollType = 'omen' # set roll type to omen, in order for hauntroll
                app.type = 'omen'
                app.mode = 'card' # set screen to view omen information
                app.currentOmen = random.choice(app.omens)
                while app.currentOmen in app.omenSet: # until omen not in set/seen before, choose another random omen
                    app.currentOmen = random.choice(app.omens)
                app.omenSet.add(app.currentOmen) # add omen to set
                app.omens.remove(app.currentOmen) # remove from original list
                app.currentCard = app.currentOmen
            else:
                app.rollType = 'normal' # set roll type to omen, in order for hauntroll
                app.type = 'omen'
                app.mode = 'card' # set screen to view omen information
                app.currentOmen = random.choice(app.omens)
                while app.currentOmen in app.omenSet:
                    app.currentOmen = random.choice(app.omens)
                app.omenSet.add(app.currentOmen)
                app.currentCard = app.currentOmen
    elif room.item:
        if app.items != []:
            app.rollType = 'normal'
            app.type = 'item'
            app.mode = 'card' # set screen to view item information
            app.currentItem = random.choice(app.items)
            while app.currentItem in app.itemSet: # until item not in set/seen before, choose another random item
                app.currentItem = random.choice(app.items)
            app.itemSet.add(app.currentItem)
            app.currentCard = app.currentItem

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
    if not inGrid(app, x, y, marginX, marginY):
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
    rows, cols = app.characterRows, app.characterCols
    for row in range(rows):
        for col in range(cols):
            x0,y0,x1,y1 = getCellBounds(app, row, col, rows, cols, app.marginX, app.marginY)
            cellWidth = x1-x0
            cellHeight = y1-y0
            canvas.create_rectangle(x0, y0, x1, y1, fill='dodger blue') # gray25
            canvas.create_text(x0+cellWidth//2,y0+cellHeight//2,text=app.characters[row][col].name, fill='white')

# ground floor board
def drawGround(app,canvas):
    rows, cols = app.groundRows, app.groundCols
    selectedRow, selectedCol = app.groundSelection
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    for row in range(rows):
        for col in range(cols):
            x0,y0,x1,y1 = getCellBounds(app, row, col, rows, cols, app.groundX, app.groundY)
            roomWidth = x1-x0
            roomHeight = y1-y0
            room = app.groundList[row][col]
            if room == 'Undiscovered':
                color = 'white'
            else:
                color = 'black'
            
            if row == selectedRow and col == selectedCol:
                if validMove(app, 'ground', app.currentPlayer, rows, cols, selectedRow, selectedCol):
                    coloroom = 'green'
                else:
                    coloroom = 'red'
                canvas.create_rectangle(x0, y0, x1, y1, fill=coloroom)
            else:
                canvas.create_rectangle(x0, y0, x1, y1, fill='saddle brown')
            canvas.create_text(x0+roomWidth//2,y0+roomHeight//2,text=room, fill=color)

# basement floor board
def drawBasement(app,canvas):
    rows, cols = app.basementRows, app.basementCols
    selectedRow, selectedCol = app.basementSelection
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    for row in range(rows):
        for col in range(cols):
            x0,y0,x1,y1 = getCellBounds(app, row, col, rows, cols, app.basementX, app.basementY)
            roomWidth = x1-x0
            roomHeight = y1-y0
            room = app.basementList[row][col]
            if room == 'Undiscovered':
                color = 'white'
            else:
                color = 'skyblue'

            if row == selectedRow and col == selectedCol:
                if validMove(app, 'basement', app.currentPlayer, rows, cols, selectedRow, selectedCol):
                    coloroom = 'green'
                else:
                    coloroom = 'red'
                canvas.create_rectangle(x0, y0, x1, y1, fill=coloroom)
            else:
                canvas.create_rectangle(x0, y0, x1, y1, fill='gray25')
            canvas.create_text(x0+roomWidth//2,y0+roomHeight//2,text=room,fill=color)

# upper floor board
def drawUpper(app,canvas):
    rows, cols = app.upperRows, app.upperCols
    selectedRow, selectedCol = app.upperSelection
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    for row in range(rows):
        for col in range(cols):
            x0,y0,x1,y1 = getCellBounds(app, row, col, rows, cols, app.upperX, app.upperY)
            roomWidth = x1-x0
            roomHeight = y1-y0
            room = app.upperList[row][col]
            if room == 'Undiscovered':
                color = 'black'
            else:
                color = 'blue'
            if row == selectedRow and col == selectedCol:
                if validMove(app, 'upper', app.currentPlayer, rows, cols, selectedRow, selectedCol):
                    coloroom = 'green'
                else:
                    coloroom = 'red'
                canvas.create_rectangle(x0, y0, x1, y1, fill=coloroom)
            else:
                canvas.create_rectangle(x0, y0, x1, y1,fill='burlywood')
            canvas.create_text(x0+roomWidth//2,y0+roomHeight//2,text=room,fill=color)

def drawGroundPositions(app,canvas):
    rows, cols = app.groundRows, app.groundCols
    drawPlayerPositions(app,canvas,'ground',rows,cols)

def drawBasementPositions(app,canvas):
    rows, cols = app.basementRows, app.basementCols
    drawPlayerPositions(app,canvas,'basement',rows,cols)

def drawUpperPositions(app,canvas):
    rows, cols = app.upperRows, app.upperCols
    drawPlayerPositions(app,canvas,'upper',rows,cols)

def drawPlayerPositions(app,canvas,floor,rows,cols):
    pos = {0: (10,10), 1: (75,10), 2: (145,10), 3: (10,105), 4: (75,105), 5: (145,105)}
    
    for row in range(rows):
        for col in range(cols):
            x0,y0,x1,y1 = getCellBounds(app, row, col, rows, cols, app.upperX, app.upperY)
            for i in range(app.players):
                x, y = pos[i]
                positionRow, positionCol = app.playerList[i][app.playerList[i]['current']]
                if row == positionRow and col == positionCol:
                    if app.playerList[i]['character'] != None and app.playerList[i]['current'] == floor: # only draw however many players there are
                        canvas.create_text(x0+x, y0+y, text=app.playerList[i]['number'],fill=app.playerList[i]['character'].color)

def informationText(app,canvas):
    font = 'Arial 18 bold'
    color = 'white'
    canvas.create_text(app.width//2, app.height-25, text=f"CURRENT PLAYER: Player {app.currentPlayer['number']}, CHARACTER: {app.currentPlayer['character'].name}, Player SPEED: {app.currentPlayer['character'].speed}, Current FLOOR: {app.currentPlayer['current']}", 
            font=font, fill=color)
    canvas.create_text(app.width-20, 25, text='Red denotes invalid moves, while green denotes valid moves. To confirm position, press "C".',font=font, fill=color, anchor='e')
    if not app.haunt:
        canvas.create_text(app.width-20, 50, text=f'Haunt Counter: {app.hauntCount}',font=font,fill=color,anchor='e')

def drawDice(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    canvas.create_text(app.width//2, 50, text=f'Roll Total: {app.result}, Target (what you need to roll): {app.target}',font='Arial 24 bold',fill='white')
    canvas.create_text(app.width//2, app.height-75, text='Click anywhere to roll. Click again to end turn.',font='Arial 24 bold',fill='white')
    
    y0 = app.height//10
    y1 = app.height * 9//10
    lines = 4 # numbers per line
    line = 2 # how many lines

    for i in range(8): # modeled after hw4 word game
        dice = app.dice
        if i < lines:
            currentLine = 0
        else:
            currentLine = 1
        numberInLine = i % lines
        cx = (app.width//lines)*(numberInLine + 1/2)
        cy = y0 + (y1 - y0)//line * (currentLine + 1/2)

        r = 100
        canvas.create_rectangle(cx-r,cy-r,cx+r,cy+r, fill='white')
        
        if dice[i] != None:
            canvas.create_text(cx,cy,text=dice[i],font="Arial 30")

def drawCard(app,canvas): # omen, item
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    if app.type == 'omen':
        text = 'OMEN'
    elif app.type == 'item':
        text = 'ITEM'
        canvas.create_text(app.width//2, app.height-150, text=app.currentItem.change, font='Arial 20 bold', fill='white')
    canvas.create_text(app.width//2, 50, text=text,font='Arial 30 bold',fill='white')
    canvas.create_text(app.width//2, app.height//4, text=app.currentCard.name, font='Arial 26 bold', fill='white')
    canvas.create_text(app.width//2, app.height//4+100, text=app.currentCard.description, font='Arial 20 bold', fill='white')
    canvas.create_text(app.width//2, app.height-75, text='After you are finished reading, click to roll dice if applicable. Else, click to return to board.',font='Arial 24 bold',fill='white')

def drawHauntHeroes(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    canvas.create_text(app.width//2, 50, text='You are the HEROES!',font='Arial 30 bold',fill='white')
    canvas.create_text(app.width//2, 80, text='You are all trying to defeat Death at chess.', font='Arial 26 bold', fill='white')
    canvas.create_text(app.width//2, app.height-50, text="Click to begin chess game.",font='Arial 24 bold',fill='white')
    
    for i in range(len(app.heroText1)):
        canvas.create_text(40, app.height*(i+2)//35 + app.height//10, 
            text=app.heroText1[i], font="Arial 14 bold",fill='white', anchor='w')

    for i in range(len(app.heroText2)):
        canvas.create_text(40, app.height*(i+2)//35 + app.height*4//10, 
            text=app.heroText2[i], font="Arial 14 bold",fill='white', anchor='w')
    
    for i in range(len(app.heroText3)):
        canvas.create_text(40, app.height*(i+2)//35 + app.height*6//10, 
            text=app.heroText3[i], font="Arial 14 bold",fill='white', anchor='w')
    
    for i in range(len(app.heroText4)):
        canvas.create_text(app.width//2 + 60, app.height*(i+2)//35 + app.height//10, 
            text=app.heroText4[i], font="Arial 14 bold",fill='white', anchor='w')
    
    for i in range(len(app.heroText6)):
        canvas.create_text(app.width//2 + 60, app.height*(i+2)//35 + app.height*6//10, 
            text=app.heroText6[i], font="Arial 14 bold",fill='white', anchor='w')

def drawRules(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    canvas.create_text(app.width//2, 50, text='Rules',font='Arial 30 bold',fill='white')
    canvas.create_text(app.width//2, 90, text='Your character speed is how many floor tiles or blocks you may move in one turn.', font='Arial 26 bold', fill='white')
    canvas.create_text(app.width//2, 120, text='You can either choose to move to an already discovered or set room or discover a new room.', font='Arial 26 bold', fill='white')
    canvas.create_text(app.width//2, 150, text='Left arrow key to go from ground floor to basement and right arrow key to go from ground to upper floor. You can', font='Arial 26 bold', fill='white')
    canvas.create_text(app.width//2, 180, text='only move on your current designated floor unless you move to the grand staircase or coal chute room.', font='Arial 26 bold', fill='white')
    canvas.create_text(app.width//2, 210, text='There will be numbers that correspond to player number in the floor tiles that designate which room you are in.', font='Arial 26 bold', fill='white')
    canvas.create_text(app.width//2, 240, text='When discovering new rooms, there may be omens or items.', font='Arial 26 bold', fill='white')
    canvas.create_text(app.width//2, 270, text='Everytime an omen appears, you must attempt a haunt roll. If the roll is less than the haunt count,', font='Arial 26 bold', fill='white')
    canvas.create_text(app.width//2, 300, text='the haunt phase begins. All players will then try to beat Death.', font='Arial 26 bold', fill='white')
    canvas.create_text(app.width//2, 330, text='More information about the haunt will appear when it is triggered.', font='Arial 26 bold', fill='white')
    canvas.create_text(app.width//2, app.height-50, text="Click to begin game!",font='Arial 24 bold',fill='white')

def drawHauntRoll(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    canvas.create_text(app.width//2, 50, text='A Game of Chess with Death',font='Arial 30 bold',fill='white')
    canvas.create_text(app.width//2, 80, text=f'Roll Total: {app.result}, Death Roll: {app.deathRoll}',font='Arial 24 bold',fill='white')
    canvas.create_text(app.width//2, app.height-75, text='Click anywhere to roll.',font='Arial 24 bold',fill='white')
    canvas.create_text(app.width//2, app.height-25, text=f"CURRENT PLAYER: Player {app.currentPlayer['number']}, CHARACTER: {app.currentPlayer['character'].name}, Player KNOWLEDGE: {app.currentPlayer['character'].knowledge}", 
            font='Arial 26 bold', fill='white')
        
    y0 = app.height//10
    y1 = app.height * 9//10
    lines = 4 # numbers per line
    line = 2 # how many lines

    for i in range(8):
        dice = app.dice
        if i < lines:
            currentLine = 0
        else:
            currentLine = 1
        numberInLine = i % lines
        cx = (app.width//lines)*(numberInLine + 1/2)
        cy = y0 + (y1 - y0)//line * (currentLine + 1/2)

        r = 100
        canvas.create_rectangle(cx-r,cy-r,cx+r,cy+r, fill='white')
        
        if dice[i] != None:
            canvas.create_text(cx,cy,text=dice[i],font="Arial 30")

def drawGameOver(app,canvas):
    canvas.create_rectangle(0,0,app.width,app.height,fill='black')
    canvas.create_text(app.width//2, 70, text='GAME OVER!',font='Arial 40 bold',fill='white')
    canvas.create_text(app.width//2, 100, text=f'Roll Total: {app.result}, Death Roll: {app.deathRoll}',font='Arial 24 bold',fill='white')
    if app.deathWin:
        canvas.create_text(app.width//2, 150, text='Death has won, try again next time!',font='Arial 30 bold',fill='white')
    elif app.heroWin:
        canvas.create_text(app.width//2, 150, text='Your team, the heroes, have won!',font='Arial 30 bold',fill='white')
    canvas.create_text(app.width//2, app.height-50, text='Click "r" to play again!',font='Arial 30 bold',fill='white')
    
runApp(width=1440, height=775)