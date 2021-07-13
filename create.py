from db import db
from db.models import Character

db.drop_all()
db.create_all()

#adding sample characters to db
character1 = Character(
    race="Human",
    class="Warrior",
    blessing='Recieve the blessing of Ares - God of war: +2 Attack',
    attack=,
    defence=,
    magic=
    )

character2 = Character(
    race="Human",
    class="Warrior",
    blessing='Recieve the blessing of Athena - God of wisdom: +2 Intellect',
    attack=,
    Intellect=,
    magic=
    )

character3 = Character(
    race="Human",
    class="Warrior",
    blessing='Recieve the blessing of Artemis - God of the hunt: +2 Dexterity',
    attack=,
    defence=,
    magic=
    )

#creating lists
list = [character1]

for i in list:
    db.session.add(i)
for i in list:
    db.session.add(i)
db.session.commit()