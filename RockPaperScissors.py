player = int(input("LET'S PLAY ROCK PAPER SCISSORS:\npress:>\n'1' for rock\n'2' for paper\n'3' for Scissors: "))
import random
play = random.randint(a=1,b=3)
#PLAYER
if(play==1):
    print("Computer choose rock")
elif(play==2):
    print("Computer choose paper")
else:
    print("Computer choose scissors")


if(player==1):
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif(player==2):
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
#COMPUTER
if(play==1):
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif(play==2):
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if(play==player):
    print("It's Draw")
elif(play==1,2,3 and player==2,3,1):
    print("You Win")
else:
    print("You lost")