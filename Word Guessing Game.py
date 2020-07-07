#Word 1######################################################################
import random
player1word1 = input('ROUND 1- Player 1 write a word for Player 2 to guess')
player2word1 = input('ROUND 1- Player 2 write a word for Player 1 to guess')
mylist1 = list(player1word1)
mylist2 = list(player2word1)
random.shuffle(mylist1)
random.shuffle(mylist2)


#Word 1_Player 2 Guess
print(mylist1)
player2point = 0
player2guess= input('Player 2 Guess the word')
if player2guess == player1word1:
    player2point +=1
    print('Player 2: You guessed correct')
    print("Player 2 has points= " + str(player2point))
else:
    print('Player 2 guessed wrong')
    print("Player 2 has points= " + str(player2point))

#Word 1_Player 1 Guess
print(mylist2)
player1point = 0
player1guess= input('Player 1 Guess the word')
if player1guess == player2word1:
    player1point +=1
    print('Player 1: You guessed correct')
    print("Player 1 has points= " + str(player1point))
else:
    print('Player 1 guessed wrong')
    print("Player 1 has points= " + str(player1point))


#Word 2######################################################################
import random
player1word2 = input('ROUND 2- Player 1 write a word for Player 2 to guess')
player2word2 = input('ROUND 2- Player 2 write a word for Player 1 to guess')
mylist1_2 = list(player1word2)
mylist2_2 = list(player2word2)
random.shuffle(mylist1_2)
random.shuffle(mylist2_2)

#Word 2_Player 2 Guess
print(mylist1_2)
player2guess_2= input('Player 2 Guess the word')
if player2guess_2 == player1word2:
    player2point +=1
    print('Player 2: You guessed correct')
    print("Player 2 has points= " + str(player2point))
else:
    print('Player 2 guessed wrong')
    print("Player 2 has points= " + str(player2point))

#Word 2_Player 1 Guess
print(mylist2_2)
player1guess_2= input('Player 1 Guess the word')
if player1guess_2 == player2word2:
    player1point +=1
    print('Player 1: You guessed correct')
    print("Player 1 has points= " + str(player1point))
else:
    print('Player 1 guessed wrong')
    print("Player 1 has points= " + str(player1point))



#Word 3######################################################################
import random
player1word3 = input('ROUND 3- Player 1 write a word for Player 2 to guess')
player2word3 = input('ROUND 3- Player 2 write a word for Player 1 to guess')
mylist1_3 = list(player1word3)
mylist2_3 = list(player2word3)
random.shuffle(mylist1_3)
random.shuffle(mylist2_3)

#Word 3_Player 2 Guess
print(mylist1_3)
player2guess_3= input('Player 2 Guess the word')
if player2guess_3 == player1word3:
    player2point +=1
    print('Player 2: You guessed correct')
    print("Player 2 has points= " + str(player2point))
else:
    print('Player 2 guessed wrong')
    print("Player 2 has points= " + str(player2point))

#Word 3_Player 1 Guess
print(mylist2_3)
player1guess_3= input('Player 1 Guess the word')
if player1guess_3 == player2word3:
    player1point +=1
    print('Player 1: You guessed correct')
    print("Player 1 has points= " + str(player1point))
else:
    print('Player 1 guessed wrong')
    print("Player 1 has points= " + str(player1point))






#Word 4######################################################################
import random
player1word4 = input('ROUND 4- Player 1 write a word for Player 2 to guess')
player2word4 = input('ROUND 4- Player 2 write a word for Player 1 to guess')
mylist1_4 = list(player1word4)
mylist2_4 = list(player2word4)
random.shuffle(mylist1_4)
random.shuffle(mylist2_4)

#Word 4_Player 2 Guess
print(mylist1_4)
player2guess_4= input('Player 2 Guess the word')
if player2guess_4 == player1word4:
    player2point +=1
    print('Player 2: You guessed correct')
    print("Player 2 has points= " + str(player2point))
else:
    print('Player 2 guessed wrong')
    print("Player 2 has points= " + str(player2point))

#Word 4_Player 1 Guess
print(mylist2_4)
player1guess_4= input('Player 1 Guess the word')
if player1guess_4 == player2word4:
    player1point +=1
    print('Player 1: You guessed correct')
    print("Player 1 has points= " + str(player1point))
else:
    print('Player 1 guessed wrong')
    print("Player 1 has points= " + str(player1point))




#Word 5######################################################################
import random
player1word5 = input('ROUND 5- Player 1 write a word for Player 2 to guess')
player2word5 = input('ROUND 5- Player 2 write a word for Player 1 to guess')
mylist1_5 = list(player1word5)
mylist2_5 = list(player2word5)
random.shuffle(mylist1_5)
random.shuffle(mylist2_5)

#Word 5_Player 2 Guess
print(mylist1_5)
player2guess_5= input('Player 2 Guess the word')
if player2guess_5 == player1word5:
    player2point +=1
    print('Player 2: You guessed correct')
    print("Player 2 has points= " + str(player2point))
else:
    print('Player 2 guessed wrong')
    print("Player 2 has points= " + str(player2point))

#Word 5_Player 1 Guess
print(mylist2_5)
player1guess_5= input('Player 1 Guess the word')
if player1guess_5 == player2word5:
    player1point +=1
    print('Player 1: You guessed correct')
    print("Player 1 has points= " + str(player1point))
else:
    print('Player 1 guessed wrong')
    print("Player 1 has points= " + str(player1point))



if player2point < player1point:
    print('player 1 wins')
elif player1point < player2point:
    print('player 2 wins')
else:
    print('Draw!')






