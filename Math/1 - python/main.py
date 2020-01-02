#!/usr/bin/python

import random
import sys

PENDU = ["", "", "", "", "", "", "", ""]

PENDU[0] = """









============
"""

PENDU[1] = """

   ||
   ||
   ||
   ||
   ||
   ||
  /||
 //||
============
"""

PENDU[2] = """
   ,==========Y===
   ||  /
   || /
   ||/
   ||
   ||
   ||
  /||
 //||
============
"""

PENDU[3] = """
   ,==========Y===
   ||  /      |
   || /       |
   ||/
   ||
   ||
   ||
  /||
 //||
============
"""

PENDU[4] = """
   ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||
   ||
   ||
  /||
 //||
============
"""

PENDU[5] = """
   ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||         |
   ||
   ||
  /||
 //||
============
"""

PENDU[6] = """
   ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||        /|\\
   ||
   ||
  /||
 //||
============
"""

PENDU[7] = """
   ,==========Y===
   ||  /      |
   || /       |
   ||/        O
   ||        /|\\
   ||        /|
   ||
  /||
 //||
============
"""


class Pendu(object):
    def __init__(self, word):
        self.word = word.upper().strip()
        self.tries = len(PENDU)
        self.founded = []
        self.tried = []
        self.message = ""

    def try_letter(self, letter):
        letter = letter.upper()

        if letter in self.tried:
            self.message = "Tu as déjà essayé la lettre %s debile !" % (letter)
        else:
            self.tried += letter

            if not letter in self.word:
                self.tries -= 1

    def game_continue(self):
        return not (self.won() or self.lose())

    def won(self):
        for l in self.word:
            if not l in self.tried:
                return False

        return True

    def lose(self):
        return self.tries <= 1

    def dispay(self):
        # clear the screen
        print("\x1b[2J\x1b[H")

        # Display the pendu
        print(PENDU[len(PENDU) - (self.tries)])

        for l in self.word:
            if l in self.tried:
                print(l + " ", end="")
            else:
                print("_ ", end="")

        print()
        print()

        for l in sorted(self.tried):
            if not l in self.word:
                print("\x1b[9m" + l + "\x1b[0m", end=" ")

        print()
        print()

        print(self.message)
        self.message = ""

    def play(self):
        while self.game_continue():
            self.dispay()
            letter = input("Une lettre : ")

            if (len(letter) > 0):
                self.try_letter(letter[0])

        if self.won():
            print("Bravo le mot est %s !" % (self.word))
        else:
            self.dispay()
            print("T'as perdu le mot est %s !" % (self.word))


if __name__ == "__main__":
    words = ["pomme", "poire", "prune"]
    with open("words", "r", encoding="ISO-8859-1") as f:
        words = f.readlines()

    pendu = Pendu(words[random.randint(0, len(words))])
    pendu.play()
