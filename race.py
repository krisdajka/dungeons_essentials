from pprint import pprint as pp

ABILITIES = (
    'strength',
    'dexterity',
    'constitution',
    'intelligence',
    'wisdom',
    'charisma'
)

"""
Races
"""
dwarf = {'constitution': 2}
elf = {'dexterity': 2}
halfling = {'dexterity': 2}
human = {'strength': 1, 'dexterity': 1, 'constitution': 1,
         'intelligence': 1, 'wisdom': 1, 'charisma': 1}
half_orc = {'strength': 2, 'constitution': 1}
tiefling = {'intelligence': 1, 'charisma': 2}

"""
Subraces
"""
mountain_dwarf = {'strength': 2, 'race': dwarf}
hill_dwarf = {'wisdom': 1, 'hit_points': 1, 'race': dwarf}
high_elf = {'intelligence': 1, 'race': elf}
wood_elf = {'race': elf, 'wisdom': 1}
dark_elf = {'race': elf, 'charisma': 1}
lightfoot_halfling = {'race': halfling, 'charisma': 1}
stout_halfling = {'race': halfling, 'constitution': 1}
human = {'race': human}
half_orc = {'race': half_orc}
tiefling = {'race': tiefling}


class SelectRace(object):
    def __init__(self, subrace):
        self.subrace = subrace
        self.race = subrace['race']
        self.ability_scores = self.get_ability_scores()
        self.adjusted_scores = self.get_adjusted_scores()

    def get_ability_bonus(self):
        ability_bonus = {}

        for field in self.race:
            if field in ABILITIES:
                ability_bonus[field] = self.race[field]

        for field in self.subrace:
            if field in ABILITIES:
                try:
                    ability_bonus[field] += self.subrace[field]
                except KeyError:
                    ability_bonus[field] = self.subrace[field]

        return ability_bonus

    def get_ability_scores(self):
        ability_scores = {}
        for ability in ABILITIES:
            ability_scores[ability] = int(input("What's your {}\n".format(ability)))
        return ability_scores

    def get_adjusted_scores(self):
        adjusted_scores = self.ability_scores
        ability_bonus = self.get_ability_bonus()
        for ability in ability_bonus:
            adjusted_scores[ability] += ability_bonus[ability]

        return adjusted_scores


tiefling = SelectRace(subrace=tiefling)
pp(tiefling.adjusted_scores)

