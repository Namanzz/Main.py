rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice=int(input("What do you want to chose?\nType 0 for rock, 1 for paper and 2 for scissors!!\n"))

game=[rock, paper, scissors]
game=game[choice]
print(game)

import random
com_choice=random.randint(0,2)
com_game=[rock,paper,scissors]
print(com_game[com_choice])

if com_choice==choice:
  print("The match is a draw. Try again!")
elif com_choice==0 and choice==1:
  print("You win!")
elif com_choice==1 and choice==2:
  print("You win!")
elif com_choice==2 and choice==0:
  print("You win!")  
else:
  print("You lose.. Better luck next time!")  