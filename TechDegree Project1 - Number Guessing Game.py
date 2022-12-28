import random


def start_game():
  randomNumber = random.randrange(1,50)
  count = 0
  name = input("What is your name so i can address you properly?: ")
  
  print("""Yippee!!!Thank you for joining.
Welcome to my number guessing game.
Lets see how lucky you can be!""")
  guess = int(input("""{}!,
Please guess a number between 0 and 50: """.format(name)))
  
  while guess != randomNumber:
    if guess < randomNumber:
      print("""Ooops! Sorry {},
Your guess is lower, please try again.""".format(name))
      guess = int(input("Please guess a number between 0 and 50: "))
      count += 1
      
    else:
      print("Eish {}! your guess is higher. Guess again".format(name))
      guess = int(input("Please guess a number between 0 and 50: "))
      count += 1
  print("""!!!!Got it!!!!
Welldone {} for getting it right!
It took you {} guesses in total""".format(name,count))
  print("Game is Over now")
start_game()
