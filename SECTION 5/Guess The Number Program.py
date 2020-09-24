#Guess the number Program.

import random   #Como necesitamos un numero random importamos este modulo

print('Hello. What is your name?')
name = input()

print('Well, '+ name +', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1,20)      #Esta funcion retorna integers
#el + name + es porque name regresa str por lo que se puede concatenar.

for guessesTaken in range (1, 7):
    print('Take a guess.')
    #Input retorna un string pero necesito un integer
    guess = int(input())  #Para que me de un integer de pasar por la funcion int
    
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break      #Esta condicion es para el guess correcto!
                   #Aqui termina el loop de manera prematura cuando adivina el numero.

if guess == secretNumber:
    print('Good Job, ' + name + '! You guess my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

#Se llama la funcion str al secretNumber
#hay que hacer concatenacion de strings porque secretNumber devuelve un int





