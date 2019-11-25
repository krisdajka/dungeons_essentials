race = {
    'human': (),
    'elf': ('high elf', 'wood elf'),
    'dwarf': ('hill dwarf', 'mountain dwarf'),
    'halfling': ('lightfoot', 'stout')
}

klass = ('fighter', 'cleric', 'rogue', 'wizard', 'bard')

abililty_scores = ('strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma')


def get_ability_scores():
    scores = {}
    for score in abililty_scores:
        scores[score] = input("What's your {}\n".format(score))

    return scores


my_scores = {'strength': '18', 'dexterity': '15', 'constitution': '14', 'intelligence': '16', 'wisdom': '18', 'charisma': '20'}

print(my_scores)


def get_human_bonus():
    human_bonus = {}
    for score in abililty_scores:
        human_bonus[score] = 1

    return human_bonus


def get_dwarf_bonus():
    dwarf_bonus = {}
    for score in abililty_scores:
        dwarf_bonus[score] = 2 if score == 'constitution' else 0

    return dwarf_bonus


print(get_human_bonus())
print(get_dwarf_bonus())
