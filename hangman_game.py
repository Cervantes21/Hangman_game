import random

def random_word():
    word = []
    with open("/home/andydollin21/Documentos/hangman_game/archivos/data.txt", "r") as f:
        for line in f:
            word.append(line.rstrip())
    return random.choice(word)

def saved_word():
    word = random_word()
    unknown_word = "_"*len(word)
    return word, unknown_word

def replace_letters(word, unknown_word, letter):
    number_of_letters = word.count(letter)
    beginning = 0
    for i in range(number_of_letters):
        position = word.find(letter, beginning)
        unknown_word = unknown_word[:position] + letter + unknown_word[position + 1:]
        beginning = position + 1
    return unknown_word

def hangman():
    word, unknown_word = saved_word()
    fails = 0
    while unknown_word != word and fails <= 10:
        print("Palabra: " + unknown_word)
        guess = input("Ingresa una letra: ")
        if guess in word:
            unknown_word = replace_letters(word, unknown_word, guess)
        else:
            fails += 1
    if unknown_word == word:
        print("Adivinaste la palabra " + unknown_word)
    else:
        print("Lo siento, la palabra era " + word)
         

def run ():
    hangman()

if __name__ == "__main__":
    run()