class Table:
    _table = {}
    _invalid = "Invalid Table Object"

    def __init__(self, value):
        if value not in self._table:
            self.value = self._invalid
        elif isinstance(value, type(self)):
            self.value = value.value
        else:
            self.value = self._table[value]


class Weather(Table):
    _table = {
        0: "Void",
        1: "Sunny",
        2: "Overcast",
        3: "Rainy",
        4: "Sandstorm",
        5: "Snowy",
        6: "Acidic",
        7: "Solar Eclipse",
        8: "Glitter",
        9: "Blooddrain",
        10: "Peanuts",
        11: "Birds",
        12: "Feedback",
        13: "Reverb"
    }
    _invalid = "Invalid Weather"


class Blood(Table):
    _table = {
        0: "A",
        1: "AAA",
        2: "AA",
        3: "Acidic",
        4: "Basic",
        5: "O",
        6: "O No",
        7: "H\u2082O",
        8: "Electric",
        9: "Love",
        10: "Fire",
        11: "Psychic",
        12: "Grass"
    }
    _invalid = "Blood?"


class Coffee(Table):
    _table = {
        0: "Black",
        1: "Light & Sweet",
        2: "Macchiato",
        3: "Cream & Sugar",
        4: "Cold Brew",
        5: "Flat White",
        6: "Americano",
        7: "Coffee?",  # Note: Should be "Expresso", but bugged in site code
        8: "Heavy Foam",
        9: "Latte",
        10: "Decaf",
        11: "Milk Substitute",
        12: "Plenty of Sugar",
        13: "Anything"
    }
    _invalid = "Coffee?"


class Item:
    _items = {
        "GUNBLADE_A": ("The Dial Tone", None),
        "GUNBLADE_B": ("Vibe Check", None),
        "ARM_CANNON": ("Literal Arm Cannon", None),
        "ENGLAND_MEMORABILIA": ("Bangers & Smash", None),
        "MUSHROOM": ("Mushroom", None),
        "GRAPPLING_HOOK": ("Grappling Hook", None),
        "FIREPROOF": ("Fireproof Jacket", "FIREPROOF"),
        "HEADPHONES": ("Noise-Cancelling Headphones", "SOUNDPROOF"),
        "SHRINK_RAY": ("Shrink Ray", None),
        "GRAVITY_BOOTS": ("Gravity Boots", None),
        "BIRDSONG": ("Birdsong", None),
        "NIGHT_VISION_GOGGLES": ("Night Vision Goggles", None)
    }

    def __init__(self, value):
        if value == None:
            self.value = "None?"
            self.attr = None
        elif value not in self._items:
            self.value = "None"
            self.attr = None
        elif isinstance(value, Item):
            self.value = value.value
            self.attr = value.attr
        else:
            self.value = self._items[value][0]
            self.attr = Attribute(self._items[value][1])


class Attribute:
    _attrs = {
        "EXTRA_STRIKE": ("The Fourth Strike", "Those with the Fourth Strike will get an extra strike in each at bat."),
        "SHAME_PIT": ("Targeted Shame", "Teams with Targeted Shame will star with negative runs the game after being shamed."),
        "HOME_FIELD": ("Home Field Advantage", "Teams with Home Field Advantage will start each home game with one run."),
        "FIREPROOF": ("Fireproof", "A Fireproof player can not be incinerated."),
        "ALTERNATE": ("Alternate", "This player is an Alternate..."),
        "SOUNDPROOF": ("Soundproof", "A Soundproof player can not be caught in Feedback's reality flickers."),
        "SHELLED": ("Shelled", "A Shelled player is trapped in a big Peanut is unable to bat or pitch."),
        "REVERBERATING": ("Reverberating", "A Reverberating player has a small chance of batting again after each of their At-Bats end."),
        "BLOOD_DONOR": ("Blood Donor", "In the Blood Bath each season, this team will donate Stars to a division opponent that finished behind them in the standings."),
        "BLOOD_THIEF": ("Blood Thief", "In the Blood Bath each season, this team will steal Stars from a division opponent that finished ahead of them in the standings."),
        "BLOOD_PITY": ("Blood Pity", "In the Blood Bath each season, this team must give Stars to the team that finished last in their division."),
        "BLOOD_WINNER": ("Blood Winner", "In the Blood Bath each season, this team must give Stars to the team that finished first in their division."),
        "BLOOD_FAITH": ("Blood Faith", "In the Blood Bath each season, this player will receive a small boost to a random stat."),
        "BLOOD_LAW": ("Blood Law", "In the Blood Bath each season, this team will gain or lose Stars depending on how low or high they finish in their division."),
        "BLOOD_CHAOS": ("Blood Chaos", "In the Blood Bath each season, each player on this team will gain or lose a random amount of Stars."),
        "RETURNED": ("Returned", "This player has Returned from the void."),
        "INWARD": ("Inward", "This player has turned Inward."),
        "MARKED": ("Unstable", "This player is Unstable."),
        "PARTY_TIME": ("Party Time", "This team is mathematically eliminated from the Postseason, and will occasionally receive permanent stats boost in their games."),
        "LIFE_OF_PARTY": ("Life of the Party", "This team gets 10% more from their Party Time stat boosts."),
        "DEBT": ("Debted", "This player must fulfill a Debt."),
        "SPICY": ("Spicy", "Spicy players can catch fire.")
    }

    def __init__(self, value):
        if value not in self._attrs:
            self.title = "Invalid Attribute"
            self.description = "Invalid Attribute"
        elif isinstance(value, Attribute):
            self.title = value.title
            self.description = value.description
        else:
            val = self._attrs[value]
            self.title = val[0]
            self.description = val[1]
