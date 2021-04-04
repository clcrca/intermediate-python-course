import random

def main():
  dice_rolls = int(input("how many round do you want roll?"))
  dice_side = int(input("how many side does dice has?"))
  dice_sum = 0
  for i in range(1, dice_rolls):
    roll = random.randint(1,dice_side)
    if roll == 1:
      print(f"you rolled {roll} cirtical fail")
    elif roll == 6:
      print(f"you rolled {roll}! cirtical sucess")
    else:
      print(f'You rolled a die {roll}')
    dice_sum += roll
  print(f'total dice_sum {dice_sum}')
if __name__== "__main__":
  main()