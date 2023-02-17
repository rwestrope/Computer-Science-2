import random

possible_scores = {
    
}

def list_to_string(num_list, str_list):
    #str_list = []
    for item in num_list:
        str_list.append(str(item))
    return str_list

class Dice:
    def __init__(self):
        self.faces = [1, 2, 3, 4, 5, 6]

    def roll(self):
        result = random.choice(self.faces)
        return result

die1 = Dice()
die2 = Dice()
die3 = Dice()
die4 = Dice()
die5 = Dice()
die6 = Dice()
class Cup:
    def __init__(self):
        self.cup = []
        self.count = []
        self.add_dice()

    def add_dice(self):
        self.cup.append(die1)
        self.cup.append(die2)
        self.cup.append(die3)
        self.cup.append(die4)
        self.cup.append(die5)
        self.cup.append(die6)

    def roll(self):
        roll_result = []
        for die in self.cup:
            roll_result.append(die.roll())
        return roll_result

    def get_dice_count(self, roll):    
        global count
        count = [0, 0, 0, 0, 0, 0]
        for die in roll:
            if (die == 1):
                count[0] += 1
            elif (die == 2):
                count[1] += 1
            elif (die == 3):
                count[2] += 1
            elif (die == 4):
                count[3] += 1
            elif (die == 5):
                count[4] += 1
            elif (die == 6):
                count[5] += 1
        return count
        
    def score_check(self, count):
        
        farkle = False

        #check for ones
        if count[0] <= 2 and count[0] != 0:
            print(f"You can take the {str(count[0])} 1's for {str(count[0]*100)} points.")

        #check for fives
        if count[4] <= 2 and count[4] != 0:
            print(f"You can take the {str(count[4])} fives for {str(count[4]*50)} points.")

        #check for straight
        if count == [1, 1, 1, 1, 1, 1]:
            print(f"You can take all the dice for 3000 points.")
        






game_cup = Cup()
class Player:
    def __init__(self, number, name):
        self.name = name
        self.number = number
        self.score = 0

    def get_score_as_str(self):
        return str(self.score)

    def get_name(self):
        return self.name

    def turn(self):
        print(f"{self.name}, it is your turn")
        print(f"Your score is {self.score}")
        decision = input("Would you like to roll or pass?")
        if decision == "roll":
            #printing the dice for this turn's roll
            print("You rolled the following numbers:")
            turn_roll = game_cup.roll()
            str_turn_roll = []
            str_turn_roll = list_to_string(turn_roll, str_turn_roll)
            for die in str_turn_roll:
                print(die)

            #checking how many of each dice there are in the roll
            dice_count = game_cup.get_dice_count(turn_roll)
            str_dice_count = []
            str_dice_count = list_to_string(dice_count, str_dice_count)
            print(str_dice_count)

            #checking for combinations of dice that can score
            game_cup.score_check(dice_count)
            
            



def start_game():
    play = True
    num_of_players = int(input("How many players are playing today?\n:"))
    player_list = []
    for num in range(1,num_of_players +1):
        name = input(f"What is player {num}'s name?\n:")
        player = Player(num, name)
        player_list.append(player)

    while play:
        for player in player_list:
            player.turn()

    
if __name__ == "__main__":
    start_game()