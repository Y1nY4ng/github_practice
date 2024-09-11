import random
constant = 0
def twist():
  while constant < 1:
    z = random.randint(0,7) 
    if z == 0:
      print("player 2 MIGHT throw a rock here")
      break
    if z == 1:
      print("player 1 should DEFINITELY throw a paper")
      break
    if z == 2:
      print("player 2 ABSOLUTELY should throw a rock")
      break
    if z == 3:
      print("this counts as a twist, it throws off the players thinking (probably)")
      break
    if z == 4:
      print("player 1 QUITE POSSIBLY could throw a paper next")
      break
    if z == 5:
      print("player 2 could PERCHANCE throw a scissors")
      break
    if z == 6:
      print("if player 1 WANTED to win, they'd throw a rock")
      break
def playGame(plr1,plr2):
  p1 = 0
  p2 = 0 
  while p1 < 2 or p2 < 2:
    if plr1 == "scissors" and plr2 == "paper" or plr1 == "paper" and plr2 == "rock" or plr1 == "rock" and plr2 == "scissors":
      print("player 1 Wins!")
      p1 += 1
      print(p1)
    elif plr2 == "scissors" and plr1 == "paper" or plr2 == "paper" and plr1 == "rock" or plr2 == "rock" and plr1 == "scissors":
      print("player 2 Wins!")
      p2 += 1
    else:
      print("sorry, you lose! try again")
    loop = input("keep going? (yes or no) ")
    if loop == "yes":
      twist()
      plr1 = input("player 1, rock, paper, or scissors? ") 
      plr2 = input("player 2, rock, paper. or scissors? ")
    else:
      break
    if p1 == 2:
      print("player 1 wins the game!")
      break
    if p2 == 2:
      print("player 1 wins the game!")
      break
playGame(input("player 1, pick rock, paper, or scissors: "),input("player 2, pick rock, paper, or scissors: "))