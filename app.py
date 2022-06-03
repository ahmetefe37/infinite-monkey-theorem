# infinite monkey theorem 

from random import randint
from re import S

# 3 function > generator - scorer - controller

def generator(sentence):
    letters = []
    for i in range(97,123): # letters created - 26 characters
        letters.append(chr(i)) 

    guess_len = len(sentence)
    guess_str = ""
    
    for j in range(0,guess_len): # string is generated
        random_chr = letters[randint(0,25)]
        guess_str += random_chr

    return guess_str# exports to scorer function as result

def scorer(generator,sentence):
    guess_str = generator(sentence)
    sentence = sentence
    matched_letters = 0
    
    if(guess_str == sentence):
        return True

    

def controller(scorer,sentence,loop_count):
    loop_counter = 0
    matching_counter = 0
    # while loop for each word to reach the sentece
    while True:
        if(scorer(generator,sentence) == True):
            matching_counter += 1
            print("-------------------------------- Matched ---------------------------------")
            break

        loop_counter += 1
        if(loop_counter == loop_count):
            break
    print("Posibility ratio: {:.4f}%".format((matching_counter/loop_counter)*100)," in {} loops".format(loop_counter))
    # controlling to generating process and scoring process with if statements


controller(scorer,"ahmetefe",10000000)