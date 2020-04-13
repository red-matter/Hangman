from threading import Timer
import random

num_rounds = 3
max_tries = 10
rounds = 1
final_score = 0

print("Welcome to my really useless hangman game!")
print("Maximum", max_tries, "tries", sep=" ")
print("This game goes to", num_rounds, "rounds")
print("Remember to type in 'used letters' to see the letters you've already guessed!")
print("Type 'guess word' if you want to guess the entire word at once, you can risk getting a better score but if you "
      "get it wrong, you get a score of 0")
print("Type 'hint' if you're stuck to get a clue, however, it would reduce your score")
input("hit ENTER to start the game")
answers = (
    "CHRISTOPHER", "RYAN", "FELICIANO", "REUBEN", "FISH", "MAGNETISM", "ELECTRICITY", "ENGINEERING", "COLUMBIA",
    "COLLINS", "DANIEL", "EHIMEN", "JACKBOX", "HUMAN", "DESTINY", "CELEBRATION", "PILLOW", "PIANO", "DELIVERABLE",
    "WARLORD", "BALENCI", "ETERNAL", "MECHANICAL", "PROCRASTINATION")

while rounds <= num_rounds:  # allows user to play game for a set number of rounds
    answer = list(random.choice(answers))  # picks a random word from the list
    used_letter_string = ""  # keeps track of the letters that the user has already guessed
    dashed_line = ""
    count = 0
    wrong_counter = 0
    num_tries = 0
    hints_used = 0

    for letter in answer:  # counts the number of letters in the answer
        count += 1
    counter = count
    while count > 0:
        dashed_line += "-"
        count -= 1
    count = 0
    guessed_answer = [None] * counter
    while count < counter:
        guessed_answer[count] = "-"
        count += 1
    count = counter
    print("round", rounds)
    print(dashed_line)

    while guessed_answer != answer:  # while loop that evaluates guess
        print("\n")
        guess = input("Enter your guess: ")  # asks user for guess
        num = 0
        index = 0
        ans = 0
        guessed_word = ""
        word = 1
        used_letter_string = list(used_letter_string)

        indexes = random.randrange(counter-1)

        if guess == "hint":
            while indexes < counter:
                if guessed_answer[indexes] == '-':
                    guessed_answer[indexes] = answer[indexes]
                    break
                else:
                    indexes += 1
                if indexes == counter:
                    indexes = 0
            guessed_answer = ''.join(guessed_answer)
            print(guessed_answer)
            guessed_answer = list(guessed_answer)
            num_tries += 1
            hints_used += 1
            if guessed_answer == answer:  # checks if the letters correctly guessed complete the predetermined answer
                print("")
                print("Congratulations!You got the answer!")
                break
            else:
                continue

        answer = ''.join(answer)

        if guess == "guess word":  # evaluates if the guessed word is the answer or not
            guessed_word = input("What is your guess for the word? (you lose the round if you get a score of 0): ")
            guessed_word = guessed_word.upper()
            if guessed_word != answer:
                print("You got it wrong :(")
                print("The answer was: ", answer)
                word = False
                break
            else:
                print("You got it right!")
                score = round(len(answer) * (200 / num_tries) * (1 - hints_used / len(answer)))
                break

        answer = list(answer)

        used_letter_string = list(dict.fromkeys(used_letter_string))  # removes duplicates in used letter string
        if guess == "used letters":  # gives the user the list of the letters that they've already guessed
            print(used_letter_string)
            guessed_answer = ''.join(guessed_answer)
            print(guessed_answer)
            guessed_answer = list(guessed_answer)
            continue
        used_letter_string = "".join(used_letter_string)

        guess = guess.upper()  # converts guess to the upper case
        used_letter_string = used_letter_string.upper()

        used_letter_string = list(used_letter_string)
        while index < len(used_letter_string):  # tells the user if they've already guessed the letter before
            if guess == used_letter_string[index]:
                print("You've already guessed that letter")
                guessed_answer = ''.join(guessed_answer)
                print(guessed_answer)
                guessed_answer = list(guessed_answer)
                ans = True
                num_tries += 1
                break
            index += 1
        if ans:  # resets the loop if user entered already used letter
            continue

        used_letter_string = "".join(used_letter_string)
        used_letter_string += guess  # adds the guessed letter to the used letters string
        index = 0

        while index < counter:  # this verifies if the letter guessed is in the answer or not
            if guess != answer[index]:
                num = False
            else:
                num = True
                break
            index += 1
        if not num:  # if the guess does not appear anywhere, wrong letter message is shown
            print("Wrong letter")
            wrong_counter += 1
            i = 0
            while i < wrong_counter:  # prints the number of X's representing the amount of times you got it wrong
                print("X ", end="")
                i += 1
            print("\n")
            guessed_answer = ''.join(guessed_answer)
            print(guessed_answer)
            guessed_answer = list(guessed_answer)
        else:  # forms new word with the correctly guessed letter
            index = 0
            while index < count:
                if answer[index] == guess:
                    print(answer[index], end="")
                    guessed_answer[index] = answer[index]
                elif guessed_answer[index] == "-":
                    print("-", end="")
                else:
                    print(guessed_answer[index], end="")
                index += 1
        num_tries += 1
        guessed_answer = ''.join(guessed_answer)
        answer = ''.join(answer)
        if guessed_answer == answer:  # checks if the letters correctly guessed complete the predetermined answer
            print("")
            print("Congratulations!You got the answer!")
            break
        guessed_answer = list(guessed_answer)

        if wrong_counter == max_tries:  # if wrong counter reaches max count, break from loop and player fails game
            print("Maximum wrong answers reached, you've failed :(")
            print("The answer was: ", answer)
            break
        answer = list(answer)

    if not word:
        score = 0
    else:
        score = round(len(answer) * (200 / num_tries) * (1 - hints_used / len(answer)))
    final_score += score
    rounds += 1
    print("score:", score)

print("final score:", final_score)
print("Game finished")

# try researching on GUI's and learn how to make a graphic display of hangman
# incorporate different word categories and answer lists based on the word categories. category is told before each word
# find a way to make guessing line more spaced out without messing up code
# find a way to put a timer for the amount of time they have to complete every round (maybe 20 seconds per round)
# a way to let the code not include letters from non key phrases in the input to the guessed_answer array, and display
# a message telling them to either input a letter or a key phrase
