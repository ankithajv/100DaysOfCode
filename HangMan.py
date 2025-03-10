# import random

# word_list = ["cream", "roller", "snack", "learn", "development"]
# word_chosen = random.choice(word_list)
# blanks = ["_"] * len(word_chosen)
# lives = len(word_chosen) + 3

# # Display the initial blanks
# for blank in blanks:
#     print(blank, end=" ")
# print()

# while lives > 0 and "_" in blanks:
#     guess_letter = input("\nGuess a letter: ").lower()

#     if guess_letter in word_chosen:
#         # Update blanks without using enumerate
#         for i in range(len(word_chosen)):
#             if word_chosen[i] == guess_letter:
#                 blanks[i] = guess_letter
        
#         # Display updated blanks
#         for blank in blanks:
#             print(blank, end=" ")
#         print("\nCorrect!")
#     else:
#         lives -= 1
#         print(f"\nIncorrect! You have {lives} lives remaining.")

#     if "_" not in blanks:
#         print("\nCongratulations! You guessed the word:", word_chosen)
#         break
# else:
#     if "_" in blanks:
#         print("\nGame Over! The word was:", word_chosen)







import random
word_list = ["cream", "roller", "snack", "learn", "development"]

choosen_word=random.choice(word_list)
print(choosen_word)

placeholder=""

word_len=len(choosen_word)

for position in range(word_len):
    print("_",end="")


display=""

for letter in choosen_word:
    guess=input("\nGuess a letter:")
    if guess in choosen_word:
        display+=letter
        print(display)
    else:
        display+="_"
        print(display)

