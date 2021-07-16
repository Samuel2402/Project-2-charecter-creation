print('= import-for-create ==============================================')

from app import db
from flask import Flask
from app import Character

db.drop_all()
db.create_all()

print('= add-characters-to-db ==============================================')

# adding sample characters to db
character1 = Character(
    race="Human",
    character_class="Warrior",
    blessing='Recieve the blessing of Ares: +2 Attack',
    stats=("Attack: " + "5") + ("Intelligence:" + "3") + ("Dexterity:" + "3"),
    points=5
    )

character2 = Character(
    race="Elf",
    character_class="Mage",
    blessing='Recieve the blessing of Athena: +2 Intellect',
    stats=("Attack: " + "3") + ("Intelligence:" + "5") + ("Dexterity:" + "3"),
    points=6
    )

character3 = Character(
    race="Orc",
    character_class="Ranger",
    blessing='Recieve the blessing of Artemis: +2 Dexterity',
    stats=("Attack: " + "3") + ("Intelligence:" + "3") + ("Dexterity:" + "5"), 
    points=4
    )

# creating lists
character_list = [character1, character2, character3]

# adding characters to db
for i in character_list:
    db.session.add(i)
for i in character_list:
    db.session.add(i)
db.session.commit()

print('= added-characters-to-db ==============================================')