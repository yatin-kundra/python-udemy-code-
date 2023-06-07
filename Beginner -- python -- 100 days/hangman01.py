# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.



word = word_list[random.randint(0, 2)]
word1 = list(word.strip(" "))

print(word1)


blanks = []
for i in range(len(word)):
    blanks.append("_")
print(blanks)


user_input = input("guess a letter ").lower()


# num = 0
#
#
# for letter in word:
#     if user_input == letter:
#         blanks[num] = word[num]
#     num+=1

for position in range(len(word)):
    if user_input == word[position]:
        blanks[position] = word[position]

print(blanks)




