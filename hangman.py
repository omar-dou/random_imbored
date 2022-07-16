import json
import random
import sys
f = open("words.json")

words = json.load(f)
def split(a):
    return [char for char in a]
a = random.choice(words)
print(a)
win = False
body = 0
b = split("-----")
s5="""---------|\n\t 0\n\t-|-\n\t ^ """
s4="""---------|\n\t 0\n\t-|- """
s3="""---------|\n\t 0\n\t-| """
s2="""---------|\n\t 0\n\t | """
s1="""---------|\n\t 0"""
s0="""---------|"""
parts = [s0,s1,s2,s3,s4,s5]
while win == False:
    ask = input("Type in a letter or guess the word. ")
    bad = 0
    for index, letter in enumerate(a):
        if letter == ask:
            b[index] = ask
        if letter != ask:
            bad += 1
    if ask == a:
        print("you win")
        win = True
    if bad == 5:
        body += 1
    if win == False:
        print(parts[body])
    if int(body) == 5:
        print("You Lost")
        print("The word was", a)
        sys.exit()
    h = ''.join(b)
    if win == False:
        print(h)
    if h == a:
        print("you win")
        win = True

    
    
