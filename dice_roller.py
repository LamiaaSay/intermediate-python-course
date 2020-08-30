import random


def main():
    
    dice_sum=0
    num_players=int(input('How many players?'))
    
    for j in range(0, num_players):
        print(f'------Player number {j+1}, it is your turn!------'+'\n')
        dice_rolls=int(input('How many dices would you like to roll?'))
        dice_size=int(input('How many sides are in the dice?'))     
        for i in range(0, dice_rolls):
            roll=random.randint(1,dice_size)
            if roll==1:
                print(f'You rolled a {roll}! Critical Fail')
            elif roll==dice_size:
                print(f'You rolled a {roll}! Critical Success')
            else:
                print(f'You rolled a {roll}')
            dice_sum +=roll
        print(f'You have rolled a total of {dice_sum}'+'\n')

if __name__== "__main__":
  main()