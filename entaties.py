import random
player_hp=0
player_abillity_power= 0
player_attack=0
skills= set()
backpack=[]
class_of_player=''
class player:
    global player_hp
    global player_attack
    global skills
    global backpack
    global player_abillity_power
    global class_of_player
    def __init__(self, name_player, player_class):
        self.name_player= name_player
        self.player_class= player_class
    def classes(self):
        global player_hp
        global player_attack
        global skills
        global backpack
        global player_abillity_power
        global class_of_player
        if self.player_class== 'warrior':
            class_of_player= 'warrior'
            player_hp=100
            player_abillity_power=0 
            skills= ['Slam, Heroic Shout!, Strong Attack']
            weapons_list_war=['axe', 'sword', '2h sword']
            weapon= random.choice(weapons_list_war)
            match weapon:
                case 'sword':
                    backpack.append('sword')
                    player_attack= 8
                case '2h sword':
                    backpack.append('2h sword')
                    player_attack= 13
                case 'axe':
                    backpack.append('axe')
                    player_attack= 10
        if self.player_class== 'mage':
            class_of_player= 'mage'
            player_hp= 60
            player_attack= 0
            skills= ['fireball', 'conjure weak hp potion', 'ice spikes']
            weapons_list_mage=['scroll of minor wisdom', 'book of basic arcane', 'apprentice robe']
            weapon= random.choice(weapons_list_mage)
            match weapon:
                case 'scroll of minor wisdom':
                    backpack.append('scroll of minor wisdom')
                    player_abillity_power= 20
                case 'book of basic arcane':
                    backpack.append('book of basic arcane')
                    player_abillity_power= 35
                case 'apprentice robe':
                    backpack.append('apprentice robe')
                    player_abillity_power= 40
