# This program says hello an ask for my name and age.


print('Hello Stranger.')
print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('the length of your name is:')
print(len(myName))

print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) +1) + ' in a year.')

