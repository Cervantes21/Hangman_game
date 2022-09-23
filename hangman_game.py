import random
import os

draw = ['''
        
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''

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
  /|\  |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

def random_word():
    word = []
    with open("./archivos/data.txt", "r") as f:
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
    print("""
                                                
                 _.u[[/;:,.         .odMMMMMM'
              .o888UU[[[/;:-.  .o@P^    MMM^    
             oN88888UU[[[/;::-.        dP^
            dNMMNN888UU[[[/;:--.   .o@P^
           ,MMMMMMN888UU[[/;::-. o@^        
           NNMMMNN888UU[[[/~.o@P^    ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
           888888888UU[[[/o@^-..     ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
          oI8888UU[[[/o@P^:--..      ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
       .@^  YUU[[[/o@^;::---..       ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
     oMP     ^/o@P^;:::---..         ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
  .dMMM    .o@^ ^;::---...           ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
 dMMMMMMM@^`       `^^^^                            ~ PRESS ENTER TO CONTINUE ~
 YMMMUP^                                                                             By: Cervantes21~
$
                                                       
          """)
    input()
    os.system("clear")
    word, unknown_word = saved_word()
    fails = 0
    print(draw[fails])
    while unknown_word != word and fails <= 5:
        print("Palabra: " + unknown_word)
        guess = input("Ingresa una letra: ")
        os.system("clear")
        if guess in word:
            unknown_word = replace_letters(word, unknown_word, guess)
            print(draw[fails])
        else:
            fails += 1
            print(draw[fails])
            
    if unknown_word == word:
        print("         Felicidades!!!, adivinaste la palabra: " + unknown_word)
        print("""                    
    ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗██╗██╗
    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║██║██║
     ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║██║██║
      ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║╚═╝╚═╝
       ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║██╗██╗
       ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝╚═╝
                                                by: Cervantes21~
            """)
    else:
        print("""
              
                     :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
AndyDollin:!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo "*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu "**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
              """)
        print("         LO SIENTO, LA PALABRA ERA: " + word)
         

def run ():
    hangman()

if __name__ == "__main__":
    run()