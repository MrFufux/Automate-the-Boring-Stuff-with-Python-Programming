#WHILE LOOPS

#Ejemplo 1

spam = 0
while spam < 5:        #Este while loop itera a 5.
    print ('Hello World')
    spam = spam + 1     # En cada iteración la variable spam incrementó en 1.



#Ejemplo 2
#La condicion es True y hay loop, cuando se tipea Andres es falsa e sale del loop. 

name = ''
while name != 'Andres':
        print ('Please type your name.')
        name = input ()
print ('Thank you')



#Break Statement

#Ejemplo 3 
#El break statement hace que salte el loop.

name = ''
while True:                              #Esta linea siempre hace que evalue a True.
    print ('Please type your name')
    name = input()
    if name == 'your name':
        break
print ('Thank You')


#Continue Statement

#Ejemplo 4 
#Salta inmediatamente al inicio del loop y reevalua las condiciones dadas del loop.

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print ('spam is ' + str(spam))















