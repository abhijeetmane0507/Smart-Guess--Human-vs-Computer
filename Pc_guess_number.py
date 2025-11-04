import random
import time
def guess(x):

    random_number= random.randint(1,x)
    guess=0


    print("🎯 Welcome to the Number Guessing Game!")
    time.sleep(1)
    print(f"🔢 I'm thinking of a number between 1 and {x}...")
    time.sleep(1)

    while guess!= random_number:
         try:

            guess=int(input(f' Guess the number between 1 to {x} :'))

            if guess < random_number:
              print("Your guess is too low😑")
              time.sleep(0.8)
            elif guess > random_number:
               print("Your guess is too high😆")
               time.sleep(0.8)
         except ValueError:
            print("⚠️ Invalid input! Please enter a number only 😅")
            time.sleep(0.5)

    print("Congratulations🏆! you guessed the number🤩")
    time.sleep(0.5)


def computer_guess(x):
    low= 1
    high= x
    feedback=''
    while feedback != 'c' and  low != high:
          if low !=high:
            guess=random.randint(low,high)
          else:
            guess=low # could also be high b/c= low=high
          feedback= input(f' Is {guess} too high (h) or too low(l) or Correct (c)? h').lower()

          if feedback =='h':
            high= guess-1
          elif feedback =='l':
             low= guess+1

    print(f' yay..!!, Computer guessed number {guess},correctly!!')

computer_guess(20)