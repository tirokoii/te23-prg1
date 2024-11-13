
from random import randint
import random, time
from colorama import init
init()
from colorama import Fore

stop = Fore.WHITE

game = True

while game == True:

    gameRound = 0
    playGame = "yes"
    roles = ["knight", "priest", "bandit", "k", "p", "b"]
    randomWeapon = ["sword", "gummy duck", "axe", "bone", "Spear", "cat", "lollipop", "shield", "pistol", "hammer", "scythe", "bow"]
    weapon = random.choice(randomWeapon)
    yesNo = ["yes", "no"]

    playerLife = 10
    roleChoice = 0
    playerCharges = 10

    print(Fore.WHITE +"\nHello and welcome to the amazing brawl dice game!")
    print("SARCASIM")
    print("In this game you'll get to choose a class and name for your character and then fight against an opponent \003")
    time.sleep (5)

    print(Fore.WHITE + "Please choose an name: ")
    playerName = input(Fore.CYAN + "")
    playerName = Fore.CYAN + playerName + stop

