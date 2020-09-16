#Global and Local Scopes


spam = 42      #Global Variable       

def eggs():
    spam = 8  #Local Variable
    print(spam)

eggs()
print(spam)
print('Some more code.')


#Reasons why Scopes are important

# 1 Local variables cannot be used in the global scope.



# 4 You can use the same name for different variables if they are in different scopes.


def s():
    eggs = 99   #Esta variable eggs es diferente a la de abajo
    bacon()
    print(eggs)

def bacon():     #Al retornar el local scope bacon() se destruye. 
    ham = 101
    eggs = 0    #Esta variable eggs es diferente al a de arriba

s()


# 2 Global variables can be read from a local scope.
# Code in a local scope can access global variables.



def p():
    print(eggs) #es ejecutado como una global variable

eggs = 42
p()
 
def x():
    eggs = 'Hello'
    print(eggs) #es ejecutado como una local variable

eggs = 42
x()
print(eggs)


#Global Statements

def y():
    global eggs  #esta variable es global por haberla demarcado con el statement global
    eggs = 'Hello'
    print (eggs)

eggs = 42
y()
print(eggs)



















