# Python-Workshop
import time
import random
#from random_words import RandomWords

#rw = RandomWords()

name = raw_input("Hi there. Do you want to play Hangman with me? Y/N")

print "I hope you said yes because that is all I'm programmed to know how to do!"

time.sleep(1)

print "I'll pick a five-letter word... _ _ _ _ _"
time.sleep(5)

print "What is your guess?"

word_list = ["abhor","above","acids","adios","anion","annul","apply","arise","auras","await","bands","baits","babes","barns","balls","bangs","beans","blood","bored","bulls","cabal","cadet","canon","canoe","catch","chewy","claws","civil"\
,"cobra","cloak","codon","comet","curve","deism","datum","deals","deign","deeds","decaf","decry","delta","debug","denim","disco","donor","dozen","drunk","drain","dried","easel","eager","eaten","eaves","ebbed","earth","early","eagle","ed\
ema","ended","elbow","erupt","ethic","ethos","empty","fairy","falls","fangs","fard","faint","faded","fancy","farce","feral","ferns","fault","farms","fetch","feuds","feign","fears","feats","flask","gives","globe","glass","grows","guilt",\
"grant","grape","great","hands","happy","habit","hello","helps","heart","honey","hopes","horse","intro","inbox","issue","jeans","jewel","judge","juicy","kills","kinds","knees","knife","large","lamps","lines","limit","liver","lemon","mac\
ro","maple","metal","marry","miles","moist","nasal","named","newer","nexus","north","olive","older","oasis","onion","onset","orbit","oxide","piano","pills","paint","photo","plaza","posts","quest","queen","quote","rocks","raise","rally",\
"shade","shall","sheer","sauce","tempo","teeth","these","thick","third","tasty","table","union","ultra","urged","urine","usual","vague","vents","vinyl","vegan","viral","votes","wages","wagon","women","weeds","while","worse","wrist","win\
es","yacht","yards","yield","years","yummy","youth","zones"]

#word = rw.random_word(max_word_size = 5, min_word_size = 5)
word = random.choice(word_list)
guesses = ''

turns = 10

#while loop

while turns > 0:
    fails = 0
    for char in word:
        if char in guesses:
            print char,
            print "Yay, you got one!"
        else:
           # print "oops, that's not right.",
            fails += 1
    if fails == 0:
        print "Yay, you win!"

        break

    print

    #ask for a guess
    guess = raw_input("Guess a letter")

    guesses += guess

    if guess not in word:

        turns -= 1
       # print "Wrong"
        print "No pressure, you have", + turns, 'more guesses'
