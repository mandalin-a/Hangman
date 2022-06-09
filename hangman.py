import random
import string

print("H A N G M A N")
win_count = 0
lose_count = 0


def spell_check(user_input):
    if (len(user_input) != 1) or (user_input == ''):
        return print("Please, input a single letter.")
    elif user_input not in english_lowercase:
        return print("Please, enter a lowercase letter from the English alphabet.")
    else:
        return False


while True:
    menu_input = input(f'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if menu_input == "play":
        word_list = ["python", "java", "swift", "javascript"]
        word = random.choice(word_list)
        hyphens = list(len(word) * "-")
        counter = 8
        english_alphabet = list(string.ascii_letters)
        english_lowercase = list(string.ascii_lowercase)
        already_guessed = []
        while counter > 0:
            if "".join(hyphens) == word:
                win_count += 1
                print(f'You guessed the word {word}!\nYou survived!')
                break
            print("")
            print("".join(hyphens))
            user_guess = input("Input a letter: ")
            if (spell_check(user_guess) is False) and (user_guess not in word):
                if user_guess in already_guessed:
                    print("You've already guessed this letter.")
                else:
                    print("That letter doesn't appear in the word.")
                    counter -= 1
            elif (user_guess in word) and (user_guess not in hyphens):
                for i in range(len(word)):
                    if user_guess == word[i]:
                        hyphens[i] = user_guess
            elif (user_guess in word) and (spell_check(user_guess) is False):
                print("You've already guessed this letter.")
            already_guessed.append(user_guess)

        if ("".join(hyphens) == word) and counter == 0:
            win_count += 1
            print(f'You guessed the word {word}!\nYou survived!')
        elif "".join(hyphens) != word:
            lose_count += 1
            print("\nYou lost!")
    elif menu_input == "results":
        print(f'You won: {win_count} times.\nYou lost: {lose_count} times.')
    else:
        break
