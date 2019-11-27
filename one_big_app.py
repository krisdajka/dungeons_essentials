from pprint import pprint as pp

races = {
    'human': ('human',),
    'elf': ('high', 'wood'),
    'dwarf': ('hill', 'mountain'),
    'halfling': ('lightfoot', 'stout')
}

dwarf = {'constitution': 2, 'speed': 25, 'age': 350, 'size': 'medium', 'darkvision': True,
         'saving_throws_advantage': 'poison', 'resistance': 'poison',
         'combat_training': ('battleaxe', 'handaxe', 'throwing hammer', 'warhammer'),
         'tool_proficiency': ('smith', 'brewer', 'mason'), 'languages': ('common', 'dwarvish'),
         'stonecunning': 'double proficiency bonus to History checks related to origin of stonework', 'sleep': 8}

mountain = {'strength': 2, 'armor_training': ('light', 'medium')}

hill = {'wisdom': 1, 'hit_points': 1}

elf = {'dexterity': 2, 'speed': 30, 'age': 750, 'size': 'medium', 'darkvision': True,
       'saving_throws_advantage': 'charmed', 'resistance': 'sleep magic', 'languages': ('common', 'elvish'),
       'keen_senses': 'proficiency in perception', 'sleep': 4}

high = {'intelligence': 1, 'combat_training': ('longsword', 'shortsword', 'longbow', 'shortbow'), 'cantrip': dict(
    spellbook='wizard',
    ability='intelligence'
), 'languages': ('choose',)}

wood = {'combat_training': ('longsword', 'shortsword', 'longbow', 'shortbow'), 'wisdom': 1, 'speed': 5,
        'mask_of_the_wild': 'hide lightly obscured'}

RACE = {'dwarf': dwarf, 'elf': elf}

SUBRACE = {'hill': hill, 'mountain': mountain, 'high': high, 'wood': wood}

klass = ('fighter', 'cleric', 'rogue', 'wizard', 'bard')

ability_scores = ('strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma')


def get_ability_scores():
    scores = {}
    for score in ability_scores:
        scores[score] = input("What's your {}\n".format(score))
    return scores


my_scores = {'strength': '18', 'dexterity': '15', 'constitution': '14', 'intelligence': '16', 'wisdom': '18', 'charisma': '20'}

print(my_scores)


def get_human_bonus():
    human_bonus = {}
    for score in ability_scores:
        human_bonus[score] = 1
    return human_bonus


def select_race():
    pick = ''
    while pick != 'y':
        for race, subraces in races.items():
            pick = input("Would you like to be {} (y/n)\n".format(race))
            if pick == 'y':
                race = race
                for subrace in subraces:
                    pick = input("Would you like to be {} (y/n)\n".format(subrace))
                    if pick == 'y':
                        subrace = subrace
                        return race, subrace


abilities = get_ability_scores()
race, subrace = select_race()

character = dict(
    race=RACE[race],
    subrace=SUBRACE[subrace],
    abilities=abilities
)

pp(character)
