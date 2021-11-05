import random
import math
#imports

randomiser=0
fraction=0
health=0
role=0
attackM = 0
attackR = 0
defenceM = 0
defenceR = 0
speed = 0
P1_amount = 0
P2_amount = 0
#integers
bot_string = "How many players would you like the bot to generate?"
player2_string = "How many players would player 2 like to generate?"
#strings
P1_fighter_stats=[]
P2_fighter_stats=[]
Stats =["Fraction","Role","Health","Melee Attack","Melee Defence","Ranged Attack","Ranged Defence","Speed"]
#lists

#fix start
def single_player_or_multiplayer(bot_string,player2_string):
    bot_valid = str(input("Would you like to play multiplayer or single player?"))
    while bot_valid != True and bot_valid != False:
        if bot_valid.lower() == "single player":
            string = bot_string
            bot_valid = True
        elif bot_valid.lower() == "multiplayer":
            string = player2_string
            bot_valid = False
        else:
            bot_valid = str(input("Sorry, I didn't understand that. Please input either multiplayer or single player"))
    return string,bot_valid
    #asks if user wants to play multiplayer or single player
#fix end


def ask_character_amount(P1,P2,string):
    P1=str(input("How many characters would player 1 like to generate?"))
    while P1.isnumeric() == False or int(P1) >3 or int(P1)<1:
        try:
            int(P1)
        except:
            print("Please make sure your answer is numerical.")
        P1=str(input("Enter a value between 1 and 3"))
    P2=str(input(string))
    #asks either for player 2 or the bot's amount of characters depending on what gamemode was chosen
    while P2.isnumeric() == False or int(P2) >3 or int(P2)<1:
        try:
            int(P2)
        except:
            print("Please make sure your answer is numerical.")
        P2=str(input("Enter a value between 1 and 3"))
    return P1,P2
    #asks for how many characters to generate for each player

def generate_fraction(fraction):
    fraction = random.randint(1, 3)
    if fraction == 1:
        fraction=("Energy")
    elif fraction == 2:
        fraction=("Aqua")
    else:
        fraction=("Earth")
    return fraction
    #randomly generates an elemental fraction.

def generate_role(role):
    role = random.randint(1, 5)
    if role == 1:
        role="TankM"
    elif role == 2:
        role="AttackerR"
    elif role == 3:
        role="AttackerM"
    elif role == 4:
        role="TankR"
    else:
        role="Speedster"
    return role
    #randomly generates a character role.

def generate_health(role,health):
    if role[0] =="T":
        randomiser = random.randint(1, 4)
        if randomiser == 4:
            health = random.randint(171, 200)
        else:
            health = random.randint(120, 170)
    else:
        health = random.randint(70, 119)
    return health
    #randomly generates character's health

def generate_defenceM(role,defenceM):
    if role == "TankM":
        randomiser = random.randint(1,8)
        if randomiser == 6:
            defenceM = random.randint(150, 180)
        elif randomiser == 4 or randomiser == 5:
            defenceM = random.randint(130, 149)
        else: defenceM = random.randint(100,129)
    elif role == "TankR":
        defenceM = random.randint(50,80)
    else: defenceM = random.randint(65,90)
    return defenceM
    #generates defenceM

def generate_attackM(role,attackM):
    if role == "AttackerM":
        randomiser = random.randint(1,5)
        if randomiser == 5:
            attackM = random.randint(150,160)
        elif randomiser == 4:
            attackM = random.randint(130,149)
        else:
            attackM = random.randint(110,149)
    elif role == "AttackerR":
        attackM = random.randint(50, 70)
    elif role == "Speedster":
        attackM = random.randint(100, 110)
    else:
        attackM = random.randint(70,100)
    return attackM
    #generates attackM

def generate_defenceR(role,defenceR):
    if role == "TankR":
        randomiser = random.randint(1,8)
        if randomiser == 6:
            defenceR = random.randint(150, 180)
        elif randomiser == 4 or randomiser == 5:
            defenceR = random.randint(130, 149)
        else: defenceR = random.randint(100,129)
    elif role == "TankM":
        defenceR = random.randint(50,80)
    else: defenceR = random.randint(65,90)
    return defenceR
    #generates defenceR

def generate_attackR(role,attackR):
    if role == "AttackerR":
        randomiser = random.randint(1,5)
        if randomiser == 5:
            attackR = random.randint(150,160)
        elif randomiser == 4:
            attackR = random.randint(130,149)
        else:
            attackR = random.randint(110,149)
    elif role == "AttackerM":
        attackR = random.randint(50, 70)
    elif role == "Speedster":
        attackR = random.randint(100, 110)
    else:
        attackR = random.randint(70,100)
    return attackR
        #generates attackR

def generate_speed(role,speed):
    if role == "Speedster":
        speed = random.randint(120,180)
    elif role[0] == "A":
        speed = random.randint(60,130)
    else:
        speed = random.randint(30,90)
    return speed
    #generates speed
def add_character_stats_to_list(amount,fraction,role,health,defenceM,attackM,defenceR,attackR,speed):
    stats =[]
    chars=[]
    for value in range(0,int(amount)):
        fraction = generate_fraction(fraction)
        role = generate_role(role)
        health = generate_health(role,health)
        defenceM = generate_defenceM(role,defenceM)
        attackM = generate_attackM(role,attackM)
        defenceR = generate_defenceR(role,defenceR)
        attackR = generate_attackR(role,attackR)
        speed = generate_speed(role,speed)
        stats.append(fraction)
        stats.append(role)
        stats.append(health)
        stats.append(attackM)
        stats.append(defenceM)
        stats.append(attackR)
        stats.append(defenceR)
        stats.append(speed)
        chars.append(stats)
        stats = []
    #Adds stats to list
    return chars

def print_fighter_stats(P1,P2,Stats):
    print ("\n\nPlayer 1:\n")
    for i in P1:
        print("Fighter #No: ",str(P1.index(i)+1))
        for r in i:
            print(Stats[i.index(r)]+":",r)
        print("\n")

    print ("Player 2:\n")
    for i in P2:
        print("Fighter #No: ",str(P2.index(i)+1))
        for r in i:
            print(Stats[i.index(r)]+":",r)
        print("\n")
    #prints stats

chosen_string,bot_valid = single_player_or_multiplayer(bot_string,player2_string)
P1_amount,P2_amount = ask_character_amount(P1_amount,P2_amount,chosen_string)
P1_fighter_stats =add_character_stats_to_list(P1_amount,fraction,role,health,defenceM,attackM,defenceR,attackR,speed)
P2_fighter_stats =add_character_stats_to_list(P2_amount,fraction,role,health,defenceM,attackM,defenceR,attackR,speed)
#functions that store to a variable

print_fighter_stats(P1_fighter_stats,P2_fighter_stats,Stats)
#output functions
