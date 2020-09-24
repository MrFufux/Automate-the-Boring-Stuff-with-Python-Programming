#Ejercicio 1:
import random

print('Dude, What is your name?')
name = input()

print('Hey, I have a game just for you, '+ name +'. I am thinking of a number between 50 and 100.')
secretNumber = random.randint (50, 100)

for guessestaken in range (1, 10):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too High.')
    else:
        break

if guess == secretNumber:
    print ('That is right mate! That is the number I was looking for, ' + name +'!'' You guess my number in ' + str(guessestaken) + ' guesses!')
else:
    print('Nope dude. The number I was thinking of was ' + str(secretNumber))

    

#Ejercicio 2:
import random

print ('Hello Fella. I want to know your name.')
print('Please type your name below.')

nombre = input()

print('Oh! Hello there '+ nombre +'. Nice to meet you fam.')
print('I am thinking of a number dude. This number is between 5 and 20.')

Thenumber = random.randint (5,20)

for intentos in range (1, 5):
    print('Try please.')
    again = int(input())
    
    if again < Thenumber:
        print('Wrong dude. This number is too low.')
    elif again > Thenumber:
        print('Wrong dude. This number is too high, mate.')
    else:
        break

if again == Thenumber:
    print ('Oh my god mate. That is the correct answer! You are a cool person ' + nombre + '. You guess the number in ' + str(intentos) + ' guesses.')
else:
    print ('You lose' + nombre +'. The number that I was looking for was' + str(Thenumber))


#Ejercicio 3:

import random

print('This program is for find a number that this machine is thinking of')
print('PLEASE TYPE A NUMBER BETWEEN 10 and 20.')

numero = random.randint (10,20)

for intentados in range (1,5):
    print('Please type a number')
    x = int(input())

    if x < numero:
        print('This is not the number. Is low.')
    elif x > numero:
        print('This is not the number. Is high.')
    else:
        break

if x == numero:
    print('This is the number that this machine was thinking for. CONGRATULATIONS HUMAN!')
    print('You guess this number in '+ str(intentados) + 'guesses')
else:
    print('Bad Luck Human. You did not guess the number.')
    print('The number I was thinking of is '+ str(numero))
    print('I AM SORRY. NOW YOU HAVE TO DIE WEAK HUMAN!')


 









































