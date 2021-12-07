from os import system
import entaties
import time
import logging
clear= lambda: system('cls')
clear()

LOG_FORM= "Created(%(created)f) path(%(pathname)s) messege: %(message)s"
logging.basicConfig(filename= r'C:\Users\elkam\Desktop\rpg nibbas\char_data.txt', level= logging.INFO, format=LOG_FORM, filemode='w')

def player_creation():
    print('welcome to rpg nibbas please type your name: ')
    name_select= input('')
    class_choice= input('select a class please (w for warrior, m for mage, r for rogue) ')
    if class_choice == 'w':
        player1= entaties.player(name_select, 'warrior')
        player1.classes()
        return
    if class_choice == 'm':
        player1= entaties.player(name_select, 'mage')
        player1.classes()
        return
    if class_choice == 'r':
        player1= entaties.player(name_select, 'rogue')
        player1.classes()
        return
    else:
        print('invalid class selection please try agian.....')
        time.sleep(1)
        clear()
        player_creation()
        return
player_creation()
from entaties import player_hp
from entaties import player_attack
from entaties import player_abillity_power
from entaties import skills
from entaties import backpack
from entaties import class_of_player
def player_id():
    global class_of_player
    match class_of_player:
        case 'warrior':
            print(f'Player HP: {player_hp} / Player ATK: {player_attack} / Player Class: {class_of_player}')
            print(backpack)
        case 'mage':
            print(f'Player HP: {player_hp} / Player ATK: {player_attack} / Player AP:{player_abillity_power} / Player Class: {class_of_player}')
            print(backpack)
        case 'rogue':
            print(f'Player HP: {player_hp} / Player ATK: {player_attack} / Player Class: {class_of_player}')
            print(backpack) 
player_id()