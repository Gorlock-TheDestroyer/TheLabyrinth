import random
import math

class Race():
    def __init__(self, r, arch, arm, melee, lock, sneak, speech, dest, alt, rest, hprgn, poires, mgres, frires, shttimered, unarm, frores, hp, st, mg):
        self.racen = r
        self.archery = arch
        self.armorRat = arm
        self.melee = melee
        self.lockpicking = lock
        self.sneak = sneak
        self.speech = speech
        self.destruction = dest
        self.alteration = alt
        self.restoration = rest
        self.healthRegen = hprgn
        self.poisonRes = poires
        self.magicRes = mgres
        self.fireRes = frires
        self.shoutTimeRed = shttimered
        self.unarmed = unarm
        self.frostRes = frores
        self.health = hp
        self.healthMax = hp
        self.stamina = st
        self.staminaMax = st
        self.magicka = mg
        self.magickaMax = mg

class Item:
    def __init__(self, name, weight, isConsumable):
        self.name = name
        self.weight = weight
        self.isConsumable = isConsumable

    def __str__(self):
        return self.name

class Book(Item):
    def __init__(self, name, weight, isConsumable, spell):
        super().__init__(name,weight,isConsumable)
        self.spell = spell

class Weapon(Item):
    def __init__(self, name, weight, isConsumable, damage):
        super().__init__(name, weight, isConsumable)
        self.damage = damage

class Sword(Weapon):
    def __init__(self, name, weight, isConsumable, damage):
        super().__init__(name, weight, isConsumable, damage)

class Bow(Weapon):
    def __init__(self, name, weight, isConsumable, damage):
        super().__init__(name, weight, isConsumable, damage)

class Armor(Item):
    def __init__(self, name, weight, isConsumable, armorRating):
        super().__init__(name, weight, isConsumable)
        self.armorRating = armorRating

class Shield(Armor):
    def __init__(self, name, weight, isConsumable, armorRating):
        super().__init__(name, weight, isConsumable, armorRating)

class Spell:
    def __init__(self, name, magickaCost):
        self.name = name
        self.magickaCost = magickaCost

class Destruction(Spell):
    def __init__(self, name, magickaCost, damage):
        super().__init__(name, magickaCost)
        self.damage = damage

class Restoration(Spell):
    def __init__(self, name, magickaCost, healing):
        super().__init__(name, magickaCost)
        self.healing = healing

class Alteration(Spell):
    def __init__(self, name, magickaCost, alterationEffect):
        super().__init__(name, magickaCost)
        self.alterationEffect = alterationEffect

#Name, weight, consumable, damage
iron_sword = Sword('Iron Sword', 10, False, 7)
steel_sword = Sword('Steel Sword', 12, False, 10)
dwarven_sword = Sword('Dwarven Sword', 14, False, 13)
ebony_sword = Sword('Ebony Sword', 16, False, 16)
deadric_sword = Sword('Deadric Sword', 17, False, 20)

hide_armor = Armor('Hide Armor', 5, False, 30)
steel_armor = Armor('Steel Armor', 25, False, 45)
dwarven_armor = Armor('Dwarven Armor', 40, False, 60)
ebony_armor = Armor('Ebony Armor', 38, False, 80)
deadric_armor = Armor('Deadric Armor', 48, False, 100)

#name, cost, damage
flames = Destruction('Flames', 16, 8)
firebolt = Destruction('Firebolt', 25, 15)
fireball = Destruction('Fireball', 40, 30)

firestorm = Destruction('Fire Storm', 100, 100)

flames_book = Book('Tome of Flames', 1, True, flames)
firebolt_book = Book('Tome of Fire Bolt', 1, True, firebolt)
fireball_book = Book('Tome of Fire Ball', 1, True, fireball)

firestorm_book = Book('Tome of Fire Storm', 1, True, firestorm)




healing = Restoration('Healing', 22, 20)
fast_healing = Restoration('Fast Healing', 30, 35)

healing_book = Book('Tome of Healing', 1, True, healing)
fast_healing_book = Book('Tome of Fast Healing', 1, True, fast_healing)

oakflesh = Alteration('Oakflesh', 80, 20) #Armor rating increases by 20 for 5 clock turns
stoneflesh = Alteration('Stoneflesh', 90, 30)

ebonyflesh = Alteration('Ebonyflesh', 110, 50)

oakflesh_book = Book('Tome of Oakflesh', 1, True, oakflesh)
stoneflesh_book = Book('Tome of Stoneflesh', 1, True, stoneflesh)
ebonyflesh_book = Book('Tome of Ebonyflesh', 1, True, ebonyflesh)


long_bow = Bow('Long Bow', 10, False, 7)
hunting_bow = Bow('Hunting Bow', 12, False, 10)
dwarven_bow = Bow('Dwarven Bow', 14, False, 13)
ebony_bow = Bow('Ebony Bow', 16, False, 16)
deadric_bow = Bow('Deadric Bow', 17, False, 20)

level1List = [iron_sword, hide_armor, long_bow, oakflesh_book, flames_book, healing_book]
level2List = [steel_sword, steel_armor, hunting_bow, stoneflesh_book, firebolt_book, fast_healing_book]
level3List = [dwarven_sword, dwarven_armor, dwarven_bow, fireball_book]
level4List = [ebony_sword,ebony_armor,ebony_bow,ebonyflesh_book]
level5List = [deadric_sword,deadric_armor,deadric_bow,firestorm_book]
itemList = ['',level1List, level2List, level3List, level4List, level5List]

class Player(Race):
    def __init__(self, name, race_obj):
        super().__init__(race_obj.racen, race_obj.archery, race_obj.armorRat, race_obj.melee,
                         race_obj.lockpicking, race_obj.sneak, race_obj.speech,
                         race_obj.destruction, race_obj.alteration, race_obj.restoration,
                         race_obj.healthRegen, race_obj.poisonRes, race_obj.magicRes,
                         race_obj.fireRes, race_obj.shoutTimeRed, race_obj.unarmed,
                         race_obj.frostRes, race_obj.health, race_obj.stamina, race_obj.magicka)
        self.name = name
        self.weapon = iron_sword
        self.armor = hide_armor
        self.shield = ''
        self.inventory = []
        self.spellbook = [flames, healing]
        self.spell = flames
        self.level = 1
        self.location = [9, 4]
        self.row = 9
        self.col = 4
        self.clock = 0
        self.isDetected = True
        self.itemList = itemList
        self.altEffect = False
        self.currentEffect = 0
        self.clock2 = 0
    def __str__(self):
        return self.name

kriisfahliil = Race('Kriisfahliil', 15, 15, 15, 15, 15, 15, 25, 20, 20, 0, 0, 0, 0, 0, 0, 0, 100, 100, 120)
siigoniis = Race('Siigoniis',15,20,15,25,15,15,15,20,15,3,0,0,0,0,0,0,100,100,100)
feyfahliil = Race('Feyfahliil',25,15,15,20,20,15,15,15,15,0,0.50,0,0,0,0,0,100,100,100)
munfahliil = Race('Munfahliil',15,15,15,15,15,15,20,25,20,0,0,0.25,0,0,0,0,100,100,100)
vulfahliil = Race('Vulfahliil',15,15,15,15,15,15,25,20,20,0,0,0,0.50,0,0,0,100,100,100)
lokolteiren = Race('Lokolteiren',15,20,15,15,15,20,15,15,25,0,0,0,0,0.20,0,0,100,100,100)
kaaz = Race('Kaaz',20,15,20,15,25,15,15,15,15,0,0,0,0,0,5,0,100,100,100)
bron = Race('Bron',15,20,25,15,15,20,15,15,15,0,0,0,0,0,0,0.50,100,100,100)
ogiim = Race('Ogiim',15,25,25,15,15,15,15,15,15,0,0,0,0,0,0,0,120,100,100)
sahqomun = Race('Sahqomun',20,15,25,15,15,15,15,20,15,0,0,0,0,0,0,0,100,120,100)
listOfRaces = [kriisfahliil, siigoniis, feyfahliil, munfahliil, vulfahliil, lokolteiren, kaaz, bron, ogiim, sahqomun]
raceDict = {"kriisfahliil" : kriisfahliil, "siigoniis" : siigoniis, "feyfahliil" : feyfahliil, "munfahliil" : munfahliil, "vulfahliil" : vulfahliil, 'lokolteiren' : lokolteiren, "kaaz" : kaaz, "bron" : bron, "ogiim" : ogiim, "sahqomun" : sahqomun}

print("Drem yol lok, wunduniik. Greetings, traveler. Tell me your name.")
name = input()
print(f"{name}, which mortal race are you?")

print("- KRIISFAHLIIL : Altmer, +10 Destruction, +5 Alteration, +5 Restoration, +20 magicka")
print("- SIIGONIIS : Argonian, +10 Lockpicking, +5 Armor, +5 Alteration, +3 health regeneration")
print("- FEYFAHLIIL : Bosmer, +10 Archery, +5 Lockpicking, +5 Sneak, +50% resist poison")
print("- MUNFAHLIIL : Breton, +10 Alteration, +5 Destruction, +5 Restoration, +25% resist magic")
print("- VULFAHLIIL : Dunmer, +10 Destruction, +5 Alteration, +5 Restoration, +50% resist fire")
print("- LOKOLTEIREN : Imperial, +10 Restoration, +5 Armor, +5 Speech, 20% reduced Shout time")
print("- KAAZ : Khajiit, +10 Sneak, +5 Archery, +5 Melee, +5 unarmed attack damage")
print("- BRON : Nord, +10 Melee, +5 Armor, +5 Speech, +50% resist frost")
print("- OGIIM : Orc, +10 Melee, +10 Armor, +20 health")
print("- SAHQOMUN : Redguard, +10 Melee, +5 Archery, +5 Alteration, +20 stamina")

while True:
    race = input()
    race = race.lower()
    if race in raceDict:
        p1 = Player(name, raceDict[race])
        break
    else:
        print(f"I do not recognize that name. Which mortal race are you, {name}?")

print(f'\n{p1}, {p1.racen}, you have followed myth and legend to a place called Labyrinthian. Within lie the')
print('tombs of the ancient Dragon Priests. The most vile of all is Bahlok, an ancient enemy to')
print('the nords.')

print('\nYou have tracked him here to this place. He awaits deep within the Labyrinth. With not but')
print('a sword and a spell in hand, do you have the strength to defeat him? How far can your')
print('courage take you?\n')

playerX = 9 # player row
playerY = 4 # player column
playerLocation = [playerX, playerY]

exitRoomRow = random.randint(1,3)
exitRoomCol = random.randint(3,6)

gameBoardFloor = [[[], [], [], [], [], [], [], [], [], []],[[], [], [], [], [], [], [], [], [], []],[[], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], []],[[], [], [], [], [], [], [], [], [], []],[[], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], []],[[], [], [], [], [], [], [], [], [], []],[[], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], []]]

gameBoardFloor[exitRoomRow][exitRoomCol] = 'X'
#move north
def brom(p1, board, num):

    if p1.row - 1 > - 1:   
        p1.clock += 1
        p1.row -= 1
        p1.location = [p1.row, p1.col]
        
        printMap(board, p1.location)

        if board[p1.row][p1.col] == 'X':
            bossFight(p1, board)

        if random.randrange(0, 4) == 0:
            items(p1, board)

        if random.randint(0, 1) == 1:
            fight(p1,board)

        elif random.randint(1, 10) == 10:
            randomEvent(p1, board)
    
    return board, p1

#move south
def sedin(p1, board, num):

    if p1.row + 1 < len(board):
        p1.clock += 1
        p1.row += 1
        p1.location = [p1.row, p1.col]
        
        
        printMap(board, p1.location)

        if board[p1.row][p1.col] == 'X':
            bossFight(p1, board)

        if random.randrange(0, 4) == 0:
            items(p1, board)

        if random.randint(0, 1) == 1:
            fight(p1,board)

    return board, p1

#move west
def welkand(p1, board, num):

    if p1.col - 1 > - 1:
        p1.clock += 1
        p1.col -= 1
        p1.location = [p1.row, p1.col]
        
        printMap(board, p1.location)

        if board[p1.row][p1.col] == 'X':
            bossFight(p1, board)

        if random.randrange(0, 4) == 0:
            items(p1, board)

        if random.randint(0, 1) == 1:
            fight(p1,board)

    return board,p1

#move east
def jer(p1, board, num):

    if p1.col + 1 < len(board[p1.row]):
        p1.clock += 1
        p1.col += 1
        p1.location = [p1.row, p1.col]

        printMap(board, p1.location)

        if board[p1.row][p1.col] == 'X':
            bossFight(p1, board)

        if random.randrange(0, 4) == 0:
            items(p1, board)

        if random.randint(0, 1) == 1:
            fight(p1,board)

    return board,p1

#Look at inv
def vuuk(p1, board, num):
    inv = p1.inventory

    if(len(inv) == 0):
        print("Your inventory is empty.")
    else:
        print('You are carrying:\n')

        for i in range(len(inv)):
            if isinstance(inv[i], Weapon):
                print(f'{i + 1} : {inv[i].name}, {inv[i].damage}/{inv[i].weight}')
            elif isinstance(inv[i], Armor):
                print(f'{i + 1} : {inv[i].name}, {inv[i].armorRating}/{inv[i].weight}')
            elif isinstance(inv[i], Book):
                print(f'{i + 1} : {inv[i].name}, {inv[i].weight}')

    print()
    print("Commands:\n")
    print("KOD # : equip")
    print("VOKOD # : unequip, 1 - Weapon, 2 - Shield, 3 - Armor")
    print("GOVEY # : drop")
    print("DREH # : use")

#Show spells
def luh(p1, board, num):
    print("You know the following spells:\n")
    for i in range(len(p1.spellbook)):
        if isinstance(p1.spellbook[i], Destruction):
            print(f'{i + 1}. {p1.spellbook[i].name}, {p1.spellbook[i].damage}/{p1.spellbook[i].magickaCost}')
        elif isinstance(p1.spellbook[i], Restoration):
            print(f'{i + 1}. {p1.spellbook[i].name}, {p1.spellbook[i].healing}/{p1.spellbook[i].magickaCost}')
        elif isinstance(p1.spellbook[i], Alteration):
            print(f'{i + 1}. {p1.spellbook[i].name}, {p1.spellbook[i].alterationEffect}')
    # Add print statement and function allowing the user to switch spells
    print('Commands:\n')
    print('STAV # : equip spell')

def stav(p1, board, num):
    p1.spell = p1.spellbook[num - 1]
    return p1

#Search room
def tovit(p1, board, num):
    cell = board[p1.row][p1.col]
    if cell != 'X':
        if len(cell) > 0:
            print('You find the following items:\n')
            for i in range(len(cell)):
                if cell[i].isConsumable:
                    if isinstance(cell[i],Book):
                        print(f'{i + 1} : {cell[i].name}, {cell[i].weight}')
                else:
                    if isinstance(cell[i], Armor):
                        print(f'{i + 1} : {cell[i].name}, {cell[i].armorRating}/{cell[i].weight}')
                    else:
                        print(f'{i + 1} : {cell[i].name}, {cell[i].damage}/{cell[i].weight}')
            print('\nCommands:\n\nKUN # : take')
        else:
            print('Nope, sorry, nothing.')
    else:
        pass

#Pick up item
def kun(p1, board, num):
    cell = board[p1.row][p1.col]
    if len(cell) > 0:
        if num > 0 and num <= len(cell):
            print(f'You take the {cell[num-1]}.')
            p1.inventory.append(cell[num-1])
            cell.pop(num-1)
        else:
            print('I do not recognize that item.')
    
        board[p1.row][p1.col] = cell
        tovit(p1, board, num)
    else:
        print('There is nothing to take.')

    board[p1.row][p1.col] = cell
    return board, p1

#Rest
def praan(p1,board,num):
    #hp [1][0]...
    p1.clock += 5
    p1.health = p1.healthMax
    p1.stamina = p1.staminaMax
    p1.magicka = p1.magickaMax

    printHealth(p1)
    printStamina(p1)
    printMagicka(p1)

    return p1

#prints commands
def uth(p1, board,num):

    if p1.row - 1 > - 1:
        print("- BROM : move north")
    if p1.row + 1 < len(board):
        print("- SEDIN : move south")
    if p1.col - 1 > - 1:
        print("- JER : move east")
    if p1.col + 1 < len(board[p1.row]):
        print("- WELKAND : move west")
    
    print("- VUUK : inventory")
    print("- LUH : spells")
    print("- TOVIT : search room")
    print("- PRAAN : rest")
    print("- UTH : commands")

#Equip
def kod(p1, board,num):

    if len(p1.inventory) == 0:
        print("There is nothing to equip.")
    else:
        if num > 0 and num <= len(p1.inventory): #If num is valid
            if isinstance(p1.inventory[num - 1], Weapon): #If you are trying to equip a weapon
                if p1.weapon == '': #If you dont have a weapon equipped
                    p1.weapon = p1.inventory[num - 1]
                    p1.inventory.pop(num - 1)
                else: # If you have a weapon
                    p1.inventory.append(p1.weapon)
                    p1.weapon = p1.inventory[num - 1]
                    p1.inventory.pop(num - 1)

            elif isinstance(p1.inventory[num - 1], Shield): #If you are trying to equip a shield
                if p1.shield == '': #If you dont have a shield equipped
                    p1.shield = p1.inventory[num - 1]

                    p1.armorRat += p1.shield.armorRating

                    p1.inventory.pop(num - 1)
                else: # If you have a shield
                    p1.inventory.append(p1.shield)

                    p1.armorRat -= p1.shield.armorRating

                    p1.shield = p1.inventory[num - 1]

                    p1.armorRat += p1.shield.armorRating

                    p1.inventory.pop(num - 1)

            elif isinstance(p1.inventory[num - 1], Armor): #If you are trying to equip armor
                if p1.armor == '': #If you dont have armor equipped
                    p1.armor = p1.inventory[num - 1]

                    p1.armorRat += p1.armor.armorRating    

                    p1.inventory.pop(num - 1)
                else: # If you have a weapon
                    p1.inventory.append(p1.armor)

                    p1.armorRat -= p1.armor.armorRating

                    p1.armor = p1.inventory[num - 1]

                    p1.armorRat += p1.armor.armorRating

                    p1.inventory.pop(num - 1)
        else:
            print("I do not recognize that item.")

    vuuk(p1,board,num)
    return p1

#Unequip
def vokod(p1, board,num):

    if num == 1:
        if p1.weapon != '':
            p1.inventory.append(p1.weapon)
            p1.weapon = ''
        else:
            print('There is nothing to unequip.')
    elif num == 2:
        if p1.shield != '':

            p1.armorRat -= p1.shield.armorRating

            p1.inventory.append(p1.shield)
            p1.shield = ''
        else:
            print('There is nothing to unequip.')
    elif num == 3:
        if p1.armor != '':

            p1.armorRat -= p1.armor.armorRating

            p1.inventory.append(p1.armor)
            p1.armor = ''
        else:
            print('There is nothing to unequip.')
    else:
        print("I do not recognize that item.")

    vuuk(p1,board,num)
    return p1

#Drop
def govey(p1, board, num):
        if num > 0 and num <= len(p1.inventory):
            print(f'Your {p1.inventory[num - 1].name} falls to the floor.')
            board[p1.row][p1.col].append(p1.inventory[num - 1])
            p1.inventory.pop(num - 1)
        elif(board[p1.row][p1.col] == 'X'):
            pass
        else:
            print('I do not recognize that item.')
        
        print()
        vuuk(p1,board,num)
        return p1, board

def dreh(p1,board,num):
    if p1.inventory[num - 1].isConsumable:
        if isinstance(p1.inventory[num - 1],Book):
            p1.spellbook.append(p1.inventory[num - 1].spell)
            p1.inventory.pop(num - 1)

def items(p1, board):
    print("There are items in the room...")
    numItems = random.randint(1, 5)
    for i in range(numItems):
        itemLevel = random.randint(1, math.floor(math.sqrt(p1.level)))
        itemIndex = random.randint(0, len(p1.itemList[itemLevel]) - 1)
        item = p1.itemList[itemLevel][itemIndex]
        board[p1.row][p1.col].append(item)
    return board

def calculateMeleeDamage(p1):
    if isinstance(p1.weapon,Sword):
        dmg = p1.weapon.damage + round(p1.melee / 10)
    elif isinstance(p1.weapon,Bow):
        dmg = p1.weapon.damage + round(p1.archery / 10)
    elif isinstance(p1.weapon,str):
        dmg = 5 + p1.unarmed 
    
    if not p1.isDetected:

        dmg *= 3
    
    return dmg

def enemyDeath(room, num, board):
    print("Great work Dovahkiin! You slayed a bad guy!")
    print(f"The {room[num - 1].name}'s items fall to the floor")
    for item in room[num - 1].items:
        board[p1.row][p1.col].append(item)
    room.pop(num - 1)

def fight(p1,board):

    enemyNumber = random.randint(1, 3)

    class Enemy:
        def __init__(self, name, damage, health, level, items):
            self.name = name
            self.damage = damage
            self.health = health
            self.level = level
            self.items = items

        def __str__(self):
            return f'{self.name}, {self.health} HP'
    #Level 1 enemies

    class SkeletonArcher(Enemy):
        def __init__(self):
            super().__init__("Skeleton Archer", damage=15, health=20, level=1, items=[long_bow])

    class Draugr(Enemy):
        def __init__(self):
            super().__init__("Draugr", damage=15, health=20, level=1, items=[iron_sword])

    class Ghost(Enemy):
        def __init__(self):
            super().__init__("Ghost", damage=15, health=20, level=1, items=[])
            self.items

    class Skeever(Enemy):
        def __init__(self):
            super().__init__("Skeever", damage=15, health=20, level=1, items=[])

    #Level 2 enemies

    class Bandit(Enemy):
        def __init__(self):
            super().__init__("Bandit", damage=25, health=40, level=2, items=[hunting_bow, steel_armor])

    class RestlessDraugr(Enemy):
        def __init__(self):
            super().__init__("Restless Draugr", damage=25, health=40, level=2, items=[steel_sword])

    class IceWraith(Enemy):
        def __init__(self):
            super().__init__("Ice Wraith", damage=25, health=40, level=2, items=[])
            self.items

    class Wolf(Enemy):
        def __init__(self):
            super().__init__("Wolf", damage=20, health=30, level=2, items=[])

    #Level 3 enemies

    class BanditChief(Enemy):
        def __init__(self):
            super().__init__("Bandit Chief", damage=35, health=60, level=3, items=[dwarven_bow, dwarven_armor])

    class DraugrWarlord(Enemy):
        def __init__(self):
            super().__init__("Draugr Warlord", damage=35, health=60, level=3, items=[dwarven_sword])

    class Wispmother(Enemy):
        def __init__(self):
            super().__init__("Wispmother", damage=35, health=60, level=3, items=[])
            self.items

    class Troll(Enemy):
        def __init__(self):
            super().__init__("Troll", damage=35, health=60, level=3, items=[])

    #Level 4 enemies

    class Falmer(Enemy):
        def __init__(self):
            super().__init__("Falmer", damage=35, health=60, level=4, items=[])

    class DragonPriest(Enemy):
        def __init__(self):
            super().__init__("Dragon Priest", damage=60, health=70, level=4, items=[])

    class DwarvenCenturion(Enemy):
        def __init__(self):
            super().__init__("Dwarven Centurion", damage=60, health=70, level=4, items=[dwarven_sword, dwarven_bow, dwarven_armor])
            self.items

    class EbonyWarriorSon(Enemy):
        def __init__(self):
            super().__init__("Ebony Warrior's Son", damage=100, health=100, level=4, items=[ebony_sword, ebony_bow, ebony_armor])

#LEVEL 5
    class EbonyWarrior(Enemy):
        def __init__(self):
            super().__init__("Ebony Warrior", damage=70, health=120, level=5, items=[ebony_sword, ebony_bow, ebony_armor])

    class Dragon(Enemy):
        def __init__(self):
            super().__init__("Dragon", damage=70, health=120, level=5, items=[])

    class Miraak(Enemy):
        def __init__(self):
            super().__init__("Miraak", damage=70, health=120, level=5, items=[])
            self.items

    class DremoraLord(Enemy):
        def __init__(self):
            super().__init__("Dremora Lord", damage=70, health=120, level=5, items=[deadric_armor,deadric_bow,deadric_sword])



    room = []



    for i in range(enemyNumber):
        lvl1 = (SkeletonArcher(),Draugr(),Ghost(),Skeever())
        lvl2 = (Bandit(),RestlessDraugr(),IceWraith(),Wolf())
        lvl3 = (BanditChief(),Wispmother(),Troll(),DraugrWarlord())
        lvl4 = (Falmer(),DragonPriest(),DwarvenCenturion(),EbonyWarriorSon())
        lvl5 = (EbonyWarrior(),Dragon(),Miraak(),DremoraLord())
        megaTuple = (0,lvl1,lvl2,lvl3,lvl4,lvl5)

        enemyType = random.randint(0, 3)
        enemyLevel = random.randint(1, math.floor(math.sqrt(p1.level)))
        room.append(megaTuple[enemyLevel][enemyType])

    if random.random() * 100 < p1.sneak:
        isDetected = False
    else:
        isDetected = True


    def nos(p1, room, num):
        
        if isinstance(p1.weapon,Sword):
            dmg = calculateMeleeDamage(p1)
            print(f"You strike the {room[num - 1]} for {dmg} damage!\n")
            room[num - 1].health -= dmg
        elif isinstance(p1.weapon,Bow):
            dmg = calculateMeleeDamage(p1)
            print(f"Your arrow hits {room[num - 1]} for {dmg} damage!\n")
            room[num - 1].health -= dmg
        elif isinstance(p1.weapon,str):
            dmg = calculateMeleeDamage(p1)
            print(f"Your fists strike {room[num - 1]} for {dmg} damage!\n")
            room[num - 1].health -= dmg

        p1.isDetected = True        

        if room[num - 1].health <= 0:
            enemyDeath(room, num, board)
            p1.level += 1 #Level goes up by 1
        else:
            print(f'The {room[num - 1]} attacks you for {room[num - 1].damage - (p1.armorRat // 10)} damage.')
            #Health decreases
            p1.health -= room[num - 1].damage - p1.armorRat // 10
        
        return p1,room

    def mulaag(p1, room, num):
        if p1.stamina - 20 >= 0 and not isinstance(p1.weapon, Bow):
            if isinstance(p1.weapon,Sword):
                dmg = (p1.weapon.damage + round(p1.melee / 10)) * 1.7
                dmg = round(dmg)
                print(f"You strike the {room[num - 1]} for {dmg} damage!\n")
                
            elif isinstance(p1.weapon,Bow):
                dmg = (p1.weapon.damage + round(p1.archery / 10)) * 1.7
                dmg = round(dmg)
                print(f"Your arrow hits {room[num - 1]} for {dmg} damage!\n")
                
            elif isinstance(p1.weapon,str):
                dmg = (5 + p1.unarmed) * 1.7
                dmg = round(dmg)
                print(f"Your fists strike {room[num - 1]} for {dmg} damage!\n")
                
            room[num - 1].health -= dmg
            p1.isDetected = True  

            if room[num - 1].health <= 0:
                enemyDeath(room, num, board)
                p1.level += 1 #Level goes up by 1
            else:
                print(f'The {room[num - 1]} attacks you for {room[num - 1].damage - p1.armorRat // 10} damage.')
                
                #Health decreases
                p1.health -= room[num - 1].damage - p1.armorRat // 10

            p1.stamina -= 20
        return p1,room

    def stavek(p1, room, num):

        if p1.magicka - p1.spell.magickaCost > 0 and isinstance(p1.spell,Destruction):
            dmg = p1.spell.damage + round(p1.destruction / 10)
            print(f"You cast a spell damaging {room[num - 1]} for {dmg} damage!\n")
            p1.isDetected = True  
            room[num - 1].health -= dmg
            p1.magicka -= p1.spell.magickaCost
            if room[num - 1].health <= 0:
                enemyDeath(room, num, board)
                p1.level += 1 #Level goes up by 1
            else:
                print(f'The {room[num - 1]} attacks you for {room[num - 1].damage - p1.armorRat // 10} damage')
                    
                    #Health decreases
                p1.health -= room[num - 1].damage - p1.armorRat // 10
        elif p1.magicka - p1.spell.magickaCost > 0 and isinstance(p1.spell,Restoration):
            heal = p1.spell.healing + p1.restoration // 10
            print(f'You heal yourself for {heal} health!')
            p1.health += heal 
            if p1.health > p1.healthMax:
                p1.health = p1.healthMax
        elif p1.magicka - p1.spell.magickaCost > 0 and isinstance(p1.spell,Alteration):
            arm = p1.spell.alterationEffect + p1.alteration // 10
            print(f'Your armor increases by {arm}')
            p1.altEffect = True
            p1.currentEffect = arm
            p1.armorRat += arm
            p1.clock2 = p1.clock + 5
        else:
            print("You dont have enough magicka to perform that spell.")

        return p1, room

    commandsDict = {
        'nos' : nos,
        'mulaag' : mulaag,
        'stavek' : stavek,
        'luh': luh,
        'stav': stav
    }
    #WHILE
    while len(room) > 0:

        printHealth(p1)
        printStamina(p1)
        printMagicka(p1)
        print("\nEnemies are in the room:\n")
        count = 1
        for enemies in room:
            print(f'{count} : {enemies}')
            count += 1
        
        print("\nCommands:\n")
        print("NOS # : attack")
        print("MULAAG # : power attack")
        print("STAVEK # : cast spell")
        #print("RU : flee")
        if not p1.isDetected:
            print("You are not detected. (3x damage for standard 'nos' attacks)")

        command = input("> ")
        command = command.lower()

        num = 1
        try:
            if type(int(command.strip()[-1])) == int:
                num = int(command.strip()[-1])
                command = command.strip()[:-2]
        except:
            pass
        if command in commandsDict:
            commandsDict[command](p1, room, num)

            p1.clock += 1
            if p1.clock > p1.clock2 and p1.altEffect:
                p1.armorRat -= p1.currentEffect
                p1.altEffect = False
                p1.currentEffect = 0


            p1.health += 5 + p1.healthRegen
            if p1.health > p1.healthMax:
                p1.health = p1.healthMax
            p1.stamina += 5
            if p1.stamina > p1.staminaMax:
                p1.stamina = p1.staminaMax
            p1.magicka += 5
            if p1.magicka > p1.magickaMax:
                p1.magicka = p1.magickaMax

        if p1.health <= 0:
            print("You have died.")
            break

    if p1.health > 0:
        printHealth(p1)
        printStamina(p1)
        printMagicka(p1)
        printMap(board, p1.location)

def bossFight(p1, board):
    class Dragon:
        def __init__(self):
            self.name = 'Alduin'
            self.health = 250
            self.damage = 25
            self.level = 10
    
    p1.isDetected = True
    
    alduin = Dragon()
    room = [alduin]

    def nos(p1, room, num):
        
        if isinstance(p1.weapon,Sword):
            dmg = calculateMeleeDamage(p1)
            print(f"You strike the {room[num - 1]} for {dmg} damage!\n")
            room[num - 1].health -= dmg
        elif isinstance(p1.weapon,Bow):
            dmg = calculateMeleeDamage(p1)
            print(f"Your arrow hits {room[num - 1]} for {dmg} damage!\n")
            room[num - 1].health -= dmg
        elif isinstance(p1.weapon,str):
            dmg = calculateMeleeDamage(p1)
            print(f"Your fists strike {room[num - 1]} for {dmg} damage!\n")
            room[num - 1].health -= dmg

        p1.isDetected = True        

        if room[num - 1].health <= 0:
            print("You slayed Alduin!")
            p1.level += 1 #Level goes up by 1
        else:
            print(f'The {room[num - 1]} attacks you for {room[num - 1].damage - (p1.armorRat // 10)} damage.')
            #Health decreases
            p1.health -= room[num - 1].damage - p1.armorRat // 10
        
        return p1,room

    def mulaag(p1, room, num):
        if p1.stamina - 20 >= 0 and not isinstance(p1.weapon, Bow):
            if isinstance(p1.weapon,Sword):
                dmg = (p1.weapon.damage + round(p1.melee / 10)) * 1.7
                dmg = round(dmg)
                print(f"You strike the {room[num - 1]} for {dmg} damage!\n")
                
            elif isinstance(p1.weapon,Bow):
                dmg = (p1.weapon.damage + round(p1.archery / 10)) * 1.7
                dmg = round(dmg)
                print(f"Your arrow hits {room[num - 1]} for {dmg} damage!\n")
                
            elif isinstance(p1.weapon,str):
                dmg = (5 + p1.unarmed) * 1.7
                dmg = round(dmg)
                print(f"Your fists strike {room[num - 1]} for {dmg} damage!\n")
                
            room[num - 1].health -= dmg
            p1.isDetected = True  

            if room[num - 1].health <= 0:
                print("You slayed Alduin!")
                p1.level += 1 #Level goes up by 1
            else:
                print(f'The {room[num - 1]} attacks you for {room[num - 1].damage - p1.armorRat // 10} damage.')
                
                #Health decreases
                p1.health -= room[num - 1].damage - p1.armorRat // 10

            p1.stamina -= 20
        return p1,room

    def stavek(p1, room, num):

        if p1.magicka - p1.spell.magickaCost > 0 and isinstance(p1.spell,Destruction):
            dmg = p1.spell.damage + round(p1.destruction / 10)
            print(f"You cast a spell damaging {room[num - 1]} for {dmg} damage!\n")
            p1.isDetected = True  
            room[num - 1].health -= dmg
            p1.magicka -= p1.spell.magickaCost
            if room[num - 1].health <= 0:
                print("You slayed Alduin!")
                p1.level += 1 #Level goes up by 1
            else:
                print(f'The {room[num - 1]} attacks you for {room[num - 1].damage - p1.armorRat // 10} damage')
                    
                    #Health decreases
                p1.health -= room[num - 1].damage - p1.armorRat // 10
        elif p1.magicka - p1.spell.magickaCost > 0 and isinstance(p1.spell,Restoration):
            heal = p1.spell.healing + p1.restoration // 10
            print(f'You heal yourself for {heal} health!')
            p1.health += heal 
            if p1.health > p1.healthMax:
                p1.health = p1.healthMax
        elif p1.magicka - p1.spell.magickaCost > 0 and isinstance(p1.spell,Alteration):
            arm = p1.spell.alterationEffect + p1.alteration // 10
            print(f'Your armor increases by {arm}')
            p1.altEffect = True
            p1.currentEffect = arm
            p1.armorRat += arm
            p1.clock2 = p1.clock + 5
        else:
            print("You dont have enough magicka to perform that spell.")

        return p1, room

    commandsDict = {
        'nos' : nos,
        'mulaag' : mulaag,
        'stavek' : stavek,
        'luh': luh,
        'stav': stav
    }
    #WHILE
    while len(room) > 0:

        printHealth(p1)
        printStamina(p1)
        printMagicka(p1)
        print("\nEnemies are in the room:\n")
        count = 1
        for enemies in room:
            print(f'{count} : {enemies.name}')
            count += 1
        
        print("\nCommands:\n")
        print("NOS # : attack")
        print("MULAAG # : power attack")
        print("STAVEK # : cast spell")
        #print("RU : flee")
        if not p1.isDetected:
            print("You are not detected. (3x damage for standard 'nos' attacks)")

        command = input("> ")
        command = command.lower()
        num = 1
        try:
            if type(int(command.strip()[-1])) == int:
                num = int(command.strip()[-1])
                command = command.strip()[:-2]
        except:
            pass
        if command in commandsDict:
            commandsDict[command](p1, room, num)

            p1.clock += 1
            if p1.clock > p1.clock2 and p1.altEffect:
                p1.armorRat -= p1.currentEffect
                p1.altEffect = False
                p1.currentEffect = 0


            p1.health += 5 + p1.healthRegen
            if p1.health > p1.healthMax:
                p1.health = p1.healthMax
            p1.stamina += 5
            if p1.stamina > p1.staminaMax:
                p1.stamina = p1.staminaMax
            p1.magicka += 5
            if p1.magicka > p1.magickaMax:
                p1.magicka = p1.magickaMax
        
        if len(room) == 0:
            print("You have beat the game!")
            break

        if p1.health <= 0:
            print("You have died.")
            break

    if p1.health > 0:
        printHealth(p1)
        printStamina(p1)
        printMagicka(p1)
        printMap(board, p1.location)

def sheogorathEvent(p1, board):
    print("You have stumbled upon the mad god Sheogorath\n")
    print("Sheogorath: Hello my little muffin! How sweet of you to come by...")
    if p1.speech > 15:
        print("I have decided to bless you... but on only one condition")
        print("You must strip down for me.")
    else:
        print("I will spare you if you do one thing for me.")
        print("Strip.")
    while p1.armor != '':
        num = 3
        command = input('> ')
        command = command.lower()
        try:
            if type(int(command.strip()[-1])) == int:
                num = int(command.strip()[-1])
                command = command.strip()[:-2]
        except:
            pass
        if command == 'vuuk':
            vuuk(p1,board,num)
        if command == 'vokod':
            vokod(p1,board,num)
    print("Sheogorath: Your figure looks absolutely stunning my pumpkin.")
    if p1.speech > 15:
        print("As promised, I will give you my gift :)")
        p1.inventory.append(deadric_sword)
        print("-A deadric sword has been added to your inventory")
    else:
        print("As promised I will let you go :)")

    return p1

def randomEvent(p1, board):
    sheogorathEvent(p1, board)

    return p1

def levelUp(p1):
    print("You have leveled up! Choose which skill to raise:")
    print("-Health")
    print('-Stamina')
    print('-Magicka')
    while True:
        command = input('> ')
        command = command.lower()
        if command == 'health':
            p1.healthMax += 10
            p1.health = p1.healthMax
            break
        elif command == 'stamina':
            p1.staminaMax += 10
            p1.stamina = p1.staminaMax
            break
        elif command == 'magicka':
            p1.magickaMax += 10
            p1.magicka = p1.magickaMax
            break
    printHealth(p1)
    printStamina(p1)
    printMagicka(p1)

def printHealth(p1):
    print("Health:")
    if p1.health != 0:
        print('🟥', end='')
        for i in range(1, 10):
            if p1.healthMax // 10 * i <= p1.health:
                print("🟥", end='')
            else:
                print('⬛', end='')
    else:
        print('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛', end='')
    print(' ' + str(p1.health))

def printStamina(p1):
    print("Stamina:")
    if p1.stamina != 0:
        print('🟩', end='')
        for i in range(1, 10):
            if p1.staminaMax // 10 * i <= p1.stamina:
                print("🟩", end='')
            else:
                print('⬛', end='')
    else:
        print('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛', end='')  
    print(' ' + str(p1.stamina))

def printMagicka(p1):
    print("Magicka:")
    if p1.magicka != 0:
        print('🟦', end='')
        for i in range(1, 10):
            if p1.magickaMax // 10 * i <= p1.magicka:
                print("🟦", end='')
            else:
                print('⬛', end='')
    else:
        print('⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛', end='')
    print(' ' + str(p1.magicka))

def printMap(board, loc):
    i = 0
    for row in board:
        print()
        for j in range(len(row)):
            if [i, j] == loc:
                print('🧔', end='')
            elif board[i][j] == 'X':
                print('🏰', end='')
            else:
                print('🔲', end='')
        i += 1
    print()


commandsDict = {
    "brom" : brom,
    "vuuk" : vuuk,
    'luh' : luh,
    'tovit' : tovit,
    'praan' : praan,
    'uth' : uth, #INVENTORY RELATED
    'kod' : kod,
    'vokod' : vokod,
    'govey': govey,
    'kun' : kun,
    'sedin' : sedin,
    'jer' : jer,
    'welkand' : welkand,
    'stav' : stav,
    'dreh' : dreh
    }
num = 1
printHealth(p1)
printStamina(p1)
printMagicka(p1)
printMap(gameBoardFloor, p1.location)
print(f"\n{p1}, what will you do?")
uth(p1, gameBoardFloor, num)
levelVar = 1
p1.armorRat = p1.armor.armorRating

while True:

    if math.floor(math.sqrt(p1.level)) > levelVar and levelVar < 6:
        levelUp(p1)
        levelVar += 1

    num = 1
    command = input("> ")
    command = command.lower()
    try:
        if type(int(command.strip()[-1])) == int:
            num = int(command.strip()[-1])
            command = command.strip()[:-2]
    except:
        pass
    if command in commandsDict:
        commandsDict[command](p1, gameBoardFloor,num)
        p1.health += 5 + p1.healthRegen
        if p1.health > p1.healthMax:
            p1.health = p1.healthMax
        p1.stamina += 5
        if p1.stamina > p1.staminaMax:
            p1.stamina = p1.staminaMax
        p1.magicka += 5
        if p1.magicka > p1.magickaMax:
            p1.magicka = p1.magickaMax

    if p1.health <= 0:
        break

    if gameBoardFloor[p1.row][p1.col] == 'X':
        break