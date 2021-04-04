import random

def main():
  dice_rolls = 3
  dice_sum = 0
  for i in range(1, dice_rolls):
    roll = random.randint(1,6)
    dice_sum += roll
    print(f'You rolled a die {roll}')
  print(f'total dice_sum {dice_sum}')
if __name__== "__main__":
  main()