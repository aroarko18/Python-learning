import random


def choose_word():
    words = ["python", "java", "javascript", "computer", "science"]
    return random.choice(words)


def play_hangman():
    word = choose_word()
    word_letters = set(word)
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    used_letters = set()
    tries = 6

    print("Hangman")
    while len(word_letters) > 0 and tries > 0:
        print("You have", tries, "tries left.")
        print("Used letters:", " ".join(used_letters))
        print("Word:", " ".join([letter if letter in used_letters else "_" for letter in word]))

        guess = input("Enter a letter: ").lower()
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                tries -= 1
        else:
            print("You already used that letter.")

    if len(word_letters) == 0:
        print("You won!")
    else:
        print("You lost.")
        print("The word was", word)


play_hangman()
