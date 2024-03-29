class MagicCard:
    cardBack = "cardBack.png"

    '''
    The plan is to have the program pass in set+name, a dictionary/fast data
    structure is used to find the card in the given set, then it is passed 
    to a getter that returns all of the other data.
    '''
    def __init__(self, name="None", set="None"):
        self.name = name
        self.set = set

        # TODO: Implement and return card getter/setter for following vars
        self.manaCost = ""
        self.type = ""
        self.powerToughness = ()
        self.rarity = ""
        self.oracleText = ""
        self.keywords = []


        self.tapped = False

        # Is it safe to assume that all cards instantiated are in the library?
        self.zone = 0
        # 0 = library
        # 1 = hand
        # 2 = stack
        # 3 = battlefield
        # 4 = graveyard
        # 5 = exile
        # 6 = command

    def getManaValue(self):
        # self.manaCost should always be formatted as "X{C}" where "X" is the 
        # total generic mana cost and "{C}" is each color in the mana cost.
        return int(self.manaCost[0]) + len(self.manaCost[:1])

    # TODO: Finish method, incl planeswalker attacking 
    def attack(self, attackableObject):
        print("TODO: Define MagicCard.attack() method.")
        pass