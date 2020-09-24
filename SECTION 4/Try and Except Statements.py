#Try and Except Ejemplos

#Ejemplo 1:

def x(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:       #El error de dividir entre cero se llama ZeroDivisionError.
        print('Error: You tried to divide by zero')   #Al colocar el except evita el error de dividir entre cero imprimiendo el texto bajo la funcion print.

print(x (2))
print(x (12))
print(x (0))           #Con Try and Except se evita este error de division entre cero.
print(x (1))

#Ejemplo 2:

def y(divideBy):
    try:
        return 42 / divideBy
    except:       #Al colocar solo el statement except toma encuenta todos los errores.
        print('Error: Your tried to divide by zero')   #Al colocar el except evita el error de dividir entre cero imprimiendo el texto bajo la funcion print.

print(y (2))
print(y (12))
print(y (0))           #Con Try and Except se evita este error de division entre cero.
print(y (1))


#Input Validation
#Ejemplo 3

print('How many cats do you have?')
numCats = input()
if int(numCats) >= 4:
    print('That is a lot of cats.')
else:
    print('That is not that many cats.')
#En el ejemplo 3 si me da por colocar el numero con letras me aparece error porque pide es un int.

#Ejemplo 4
#Para evitar el error de colocar el numero con letras...

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats.')
except ValueError:                 #Colocamos esta excepcion para que al colocar texto nos aparezca lo de la funcion print.
    print('You did not enter a number')


##Ejemplo 5
#Para evitar que tome en cuenta los numeros negativos y que al darle cero me diga que adopte...

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    if int(numCats) == 0:
        print('Adopt a Cat.')

    elif int(numCats) < 4 and int(numCats) >= 1:    
        print("That's not that many cats.")
    elif int(numCats) < 0:
        print('Input cant be negative fool.')
except ValueError:                
    print('You did not enter a number.')

