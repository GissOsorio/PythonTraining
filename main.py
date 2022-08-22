from naughtyNice import *
from doppelgangerEnigma import *
from reversingWords import *
from exceptionHandling import *

print("**Naughty Nice**")
bad_actions = ['broke someone\'s window', 'fought over a toaster', 'killed a bug']
print("Bad actions: " + my_function(bad_actions))
good_actions = ['got someone a new car', 'saved a man from drowning', 'never got into a fight']
print("Good actions: " + my_function(good_actions))
actions = ['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']
print("Actions: " + my_function(actions))

print("**Doppelganger Enigma**")
print(doppelgangerEnigma())

print("**Reversing Words in a String**")
print(reverse('Hi    There.'))
print(reverse('Hello World'))

print("**ExceptionHandling**")
print(index_of(4,[1,2,3]))