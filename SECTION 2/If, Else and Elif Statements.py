
#If Statement

name = 'Alice'
if name == 'Alice': #Block donde If evalua a True por lo que la línea de abajo aparece.
   print ('Hi Alice')
print ('Done')   


name = 'Bob'         #Para empezar un nuevo block se debe copiar el :
if name == 'Andres': #Block donde If evalúa a False por lo que la línea de abajo no aparece.
    print('Hi Andres') 
print ('Done')

# else Statement

password = 'swordfish'
if password == 'swordfish': #Evalua a True por lo que aparece en pantalla
    print ('Access Granted.')
else: 
    print ('Wrong password.')


password = 'maluta'       
if password == 'swordfish':  # Lo evalua como False por lo que se salta esta línea y siue con el block de else

    print ('Access Granted.')
else:                           
    print ('Wrong Password.')

#Elif Statement

name = 'Bob'
age = 3000
if name == 'Alice':                         #Evalua a False por lo que lo salta
    print ('Hi Alice')
elif age < 12:                              #Evalua a False por lo que lo salta
    print ('You are not Alice, kiddo.')
elif age > 2000:                            #Evalua a True, por lo que aparece
       print ('Unlike you, Alice is not an undead, inmortal vampire')
elif age > 100:                             #Evalua a False, por lo que lo salta
    print ('You are not Alice, grannie')

name = 'Bob'
age = 3000
if name == 'Bob':                      #Evalua a True, por lo que aparece
    print('Hello Bob')
elif age < 12:                         #Evalua a False por lo que lo salta         
    print ('You are not Alice, kiddo.')
elif age > 2000:                       #Evalua a False por lo que lo salta        
       print ('Unlike you, Alice is not an undead, inmortal vampire')
elif age > 100:                        #Evalua a False por lo que lo salta        
    print ('You are not Alice, grannie')



#Last thing of Flow control Statements

print('ENTER A NAME.')
name = input ()                     #Shortcut (Atajo)
if name:
    print('Thank You for entering your name.')
else:
    print('You did not enter a name.')


                     #haciendolo más explícito...

print('ENTER A NAME.')
name = input ()         
if name != '':               #Utilizamos el no es igual (!=)
    print('Thank You for entering your name.')
else:
    print('You did not enter a name.')


#EJERCICIOS

print('Enter the Password.')
password = input ()
if password == 'swordfish': 
    print ('Access Granted.')
else: 
    print ('Wrong password.')



print ('What is your age?')
age = input()
if int(age) == 17:
    print ('Nice')
elif int(age) < 16:
    print ('Younger than my bitch')
elif int(age) > 18:
    print ('Older than my second bitch')





