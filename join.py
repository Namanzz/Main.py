print("Bollywood Guesser!!")
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["cocktail","race","agneepath","swades","bodyguard","bombay","raees","dhoom","brahmastra"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


lives = 6



display = []
for letter in range(word_length):
    display.append("_")

print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
        
    
    if guess not in chosen_word:
      lives-=1
      if lives==0:
        end_of_game=True
        print("You Lose")
    
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")
    
      

    
    print(stages[lives])