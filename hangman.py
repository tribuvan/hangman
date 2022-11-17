import random
import string
from words import words

def valid(words):
	word = random.choice(words)
	while '-' in word or ' ' in word:
		word = random.choice(words)
	return word.upper()

def hangman():
	word = valid(words)
	letters = set(word)
	alphabet = set(string.ascii_uppercase)
	used_alphabet = set()
	lives = 7

	while len(letters) > 0 and lives > 0 :
		print("you have",lives,"lives left and you have used the alphabets:",' '.join(used_alphabet))
		your_word = [letter if letter in used_alphabet and letter in word else '-' for letter in word]
		print("current word: ",' '.join(your_word))
		
		user = input("Enter your alphabet: ").upper()
		if user in alphabet - used_alphabet:
			used_alphabet.add(user)
			if user in letters:
				letters.remove(user)
				print('')
			else:
				lives = lives-1
				print('\nYour letter,', user, 'is not in the word.')
		elif user in used_alphabet:
			print('\nYou have already used that letter. Guess another letter.')
		else:
			print('\nThat is not a valid letter.')

	if lives == 0:
		print('You died, sorry. The word was', word)
	else:
		print('YAY! You guessed the word', word, '!!')


hangman()

			
