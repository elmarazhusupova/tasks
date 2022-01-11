import random
 
class Soldiers():
    id_ = 1
    def __init__(self):      
        self.id_ = Soldiers.id_ 
        Soldiers.id_ += 1
 
    def go_hero(self,hero):
        print(f'солдат с id {self.id_} следует за героем {hero.id_}')
        
    def __str__(self):
        return f'{self.id_}'
    
class Heroes(Soldiers):
    
    def __init__(self, team):
        Soldiers.__init__(self)
        self.team = team
        self.level = 0
 
    def level_up(self):
        self.level += 1
        print(f'герой с id {self.id_} достиг {self.level} уровня')
    
heroes = Heroes('red')
heroes_2 = Heroes('blue')
list_heroes = []
list_heroes_2 = []
for _ in range(50):
    if random.choice(['red', 'blue']) == 'red':
        list_heroes.append(Soldiers())
    else:
        list_heroes_2.append(Soldiers())
        
len_heroes = len( list_heroes)
len_heroes_2 = len( list_heroes_2) 
print(f'солдат у героя heroes - {len_heroes}')
print(f'солдат у героя heroes_2 - {len_heroes_2}')
if len_heroes > len_heroes_2:
    heroes.level_up()
else:
    heroes_2.level_up()
 
random.choice(list_heroes).go_hero(heroes)
