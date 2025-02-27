# Making a function

def my_function():
    print("Well hello")
#Calling the function
my_function()
    

# Scope 

def func():
    # local scope
    s="Me too!(on local scope)"   
    print(s)
#Global scope
s="I love python!(on global scope)"
print(s)

#Integer

pi=3.14
pi2= int(pi)
print(pi)
print(pi2)

# float
pi3="3.14"
print(type(pi3))
pi4= float(pi3)
print(type(pi4))

# Boolean
print(0<1)
print(1>0)
bool(0)
bool(1)
bool("Hello there!")

X= None
print(X)    


print("Hello!!")
print("this is the first script")
a= "the latin letters in english"
print(a)

#string function
print(len(a))
print(a.upper())
print(a.lower())
print(a.count("i"))
print(a.find("d"))
print(a.split())

#String concatenation
b="hello"
c="Hello"
d=b+"!!"+c+"??"
print(d)

#String replication
print("alice"*5)

#string Formatting
name="Minjur"
print(f"hello{name}")
print("Greeting to you,{}".format(name))
Number=2
print("there are %d %s in the class"%(Number,name))


# List
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
print(thislist.index("banana"))
thislist.remove("banana")
thislist.insert(1, "strawberry")
print(thislist)

# Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))

# Set
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
print(len(thisset))
print(thisset)

# Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])


import random
a = 10
b = random.randint(0,20)
c = 100
print("a is", a, "and", "b is", b)
print("The answer to a + b is", a + b)
print("a < b is", a < b)
print("a == b is", a == b)
print("a + b is", a + b)
print("a * b is", a * b)
print("a to the power of b is", a ** b)
# If-Else Statement in While Loop
while(c != b):
    c = int(input("Enter Guess! "))
    if (c == b):
        print("You won!")
        break
    else:
        print("Wrong Answer, Try Again!")