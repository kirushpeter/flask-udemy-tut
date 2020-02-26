"""
#numbers
print("hello world")

print(1/2)

print(2**7)

my_dogs = 2

a = 10
print(a)

a = a + a

print(a)

puppies = 6

weight = 2

total = puppies * weight

print(total)

#strings

print(len("hello"))

#indexing

mystring = "abcdefghij"
print(mystring[-1])

print(mystring[0:7:2])#start is included  start stop and step 
print(mystring[::3])

"""
"""
mystring = "hello world"

print(mystring.split())
"""
"""
username = "sammy"

color = "blue"

print("the {} favourite is {}".format(username,color))

print(f"The {username} chose {color}" )

#lists
#they ordered sequences that can hold a number of objects

myList = [1,2,3]
print(len(myList))

mylist = ['w','e','f','g']

mylist.append('k')

print(mylist)

#dictionaries

d = {'key1':'value1','key2':'value2'}

print(d)

print(d['key1'])

salaries = {'john':20,'sally':30,'sammy':15}
print(salaries['sally'])

#tuples - immutable (1,2,3)

t = (1,2,3)
print(t[0])
#sets -unordered collections of unique elements

x = set()

print(x)

x.add(1)
x.add(8)

print(x)

s = "flask"
print(s[0])
print(s[2:])
print(s[1:4])
print(s[-1])
print(s[::-1])


l = [3,7,[1,4,'hello']]

l[2][2] = "goodbye"

print(l)

mylistt = [1,1,1,1,1,2,2,2,2,3,3,3,3] 

print(set(mylistt))

age = 4

name = "sammy"

print(f"hello my dog's name is {name} and he is {age} years old")


"""
"""
#logical comparisons
username = "admin"

check = "admin"

if username == check and 1==1:
    print(access granted) 
else:
    print("all above conditions were not true")
"""
"""
username = "dhdjjd"

permission = False

if username == "admin" and permission:

    print("full access granted")

elif username == "admin" and permission == False:

    print("admin access only,no full permission")

else:
    print("no access")

"""
#loops
"""
my_iterable = [1,2,3,3,4,5,6]

for items in my_iterable:

    print(items ** 3)
"""
"""
salaries = {"john": 50,"kamau":60,"peter": 80}
for employee in salaries:

    print(employee)
    print("has salary of: ")
    print(salaries[employee])
    print(' ')
"""
"""
mypairs = [('a',1),('b',3),('c',4)]

for (item1,item2) in mypairs:

    print(item1)
    print(item2)
"""

i = 1
while i < 5:

    print(f"i is currently : {i}")

    i = i + 1

for x in range (0,11,2):

    print(x)
#functions
def report_person(name):

    print("reporting person " + name)

report_person("cindy")


def add_num(num1,num2):

    return num1 + num2

result = add_num(2,4)

print(result)

