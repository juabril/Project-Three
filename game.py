from phrase import Phrase
import random


class Game:
    missed = 0
    phrases = []
    active_phrase = None
    guesses = []
    proceed_answer = 'y'

    def __init__(self):
        self.guesses = [" "]
        self.phrases = [Phrase('Bananas are yellow'), Phrase('I Like to Run'), Phrase('The Pandemic needs to End'),
                        Phrase('Tonight there is a full Moon'), Phrase('I CANNOT wait to eat Donuts')]
        self.active_phrase = self.get_random_phrase()

    def get_random_phrase(self):
        self.pointer = random.randint(0, 4)
        self.selected_phrase = self.phrases[self.pointer]
        return self.selected_phrase

    def welcome(self):
        print("""
            \n**************************************
            \n****Welcome to Phrase Hunters !!******
            \n**************************************
            """)

    def start(self):
        while self.proceed_answer.lower() == 'y':
            self.welcome()
            while self.missed < 5 and self.active_phrase.check_complete(self.guesses) is False:
                print("\nNumber missed: {}".format(self.missed))
                self.active_phrase.display(self.guesses)
                user_guess = self.get_guess()
                self.guesses.append(user_guess)
                if not self.active_phrase.check_guess(user_guess):
                    self.missed += 1
            self.active_phrase.display(self.guesses)
            self.game_over()
            self.proceed_answer = input("Would you like to play again (y/n): ")
            if self.proceed_answer == 'y':
                self.game_reset()
            else: 
                print("Thanks for playing ! come back soon !")    

    def get_guess(self):
        self.prompt = input("\nPlease enter a letter : ")
        while len(self.prompt) > 1 or self.prompt in self.guesses or self.prompt.isalpha() == False:
            if len(self.prompt) > 1:
                print("\nPlease enter only one letter at a time")
                print("This attempt will not count towards your missed letters count")
            elif self.prompt in self.guesses:
                print("\nYou already entered that letter, please try again")
                print("This repeated letter attempt will not count towards your missed letters count")
            elif self.prompt.isalpha() == False:
                print("Please do not enter characters other than letters from a to z")
                print("This attempt will not count towards your missed letters count")
            self.prompt = input("Please enter a letter : ")
        return self.prompt

    def game_over(self):
        if self.missed == 5:
            print("\nYou reached the maximum number of missed letters")
            print("Your game is over !")
        else:
            print("\nCongratulations, you won!!")

    def game_reset(self):
        self.missed = 0
        self.guesses = [" "]
        self.active_phrase = self.get_random_phrase()

