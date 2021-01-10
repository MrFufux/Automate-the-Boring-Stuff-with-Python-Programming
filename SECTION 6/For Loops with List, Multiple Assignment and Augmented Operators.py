#for Loops with Lists, Multiple Assignment, and Augmented Operators LESSON.

for i in range (4):
    print(i)

print('/////////////////////////////////////////////////////////////')
#----------------------RANGE OBJECTS AND LISTS-LIKE VALUES------------------------

#-------------------------The list and range  function------------------------------------------
#list() range()

print(list(range(4)))

print(list(range(0, 100, 2)))

x = list(range(0, 100, 2))
print(x)

#----------------------------for a in range(len(someList)):---------------
print('///////////////////////////////////////////////////////////////////////')

#Ejemplo 1
supplies = ['pens', 'staplers', 'flames', 'binders']
for a in range(len(supplies)):
    print('Index ' + str(a)+ ' in supplies is:' + supplies[a])

print('///////////////////////////////////////////////////////////////////////')

#Ejemplo 2. La lista puede ser de cualquier longitud y aun funciona el for a in range(len(someList))

y = ['flames','flames','flames','flames','flames','flames', 'flames','flames','flames','flames','flames','flames','flames','flames','flames','flames',]
for u in range(len(y)):
    print('Index ' + str(u)+ ' in y is:' + y[u])

#------------------------Multiple Assigment-----------------------------------------------------------------------------------------------------------------
print('///////////////////////////////////////////////////////////////////////')

#ejemplo 1
cat = ['fat','orange','loud']
size, color, disposition = cat #se puede definir varias variables.
print(size, color, disposition)

print('///////////////////////////////////////////////////////////////////////')

#ejemplo 2
tamano, colour, conducta = 'skinny', 'black', 'quiet' #se puede definir cada cosa a cada variable.
print(tamano, colour, conducta)

#-------------------------Swapping Variables--------------------------------------------------------
print('///////////////////////////////////////////////////////////////////////')

e = 'AAA'
c = 'BBB'
print(e)
print(c)
e, c = c, e          #Se intercambian el valor de las variables
print(e, c)

#-----------------------Augmented Assignment Operators--------------------------------------------------
print('///////////////////////////////////////////////////////////////////////')

spam = 42
spam += 1                 #Shortcut
print (spam)

#Tabla de augmented assignment operators

#spam += 1 ------------> spam = spam + 1
#spam -= 1 ------------> spam = spam - 1
#spam *= 1 ------------> spam = spam * 1
#spam /= 1 ------------> spam = spam / 1
#spam %= 1 ------------> spam = spam % 1










