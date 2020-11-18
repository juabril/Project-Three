import random

class Phrase:

    def __init__(self, phrase):
       self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            if letter == " ":
                print(f" ", end=" ")
            else:
                i = 0
                for any_guess in guesses:
                    if any_guess == letter:
                        print(f"{letter}", end=" ")
                        i += 1
                if i == 0:
                    print(f"_", end=" ")

    def check_guess(self, guess):
        if guess in self.phrase:
            return True
        else:
            return False

    def check_complete(self, guesses):
        for any_letter in self.phrase:
            if any_letter not in guesses:
                return False
        return True
