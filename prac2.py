# Name : PRATHAM MODI
# ID : 20CE056
# Aim :  Study and Learn List, Tuple, Set and Dictionary
# GITHUB LINK : https://github.com/prathammodi333/python-programs



#                                    ***********Dictionary***********
# a....Python script to check whether a given key already exists in a dictionary.
d1 = {1:10, 2:20, 3:30, 4:40}
key = int(input("Enter a key : "))

if(key in d1):
    print("key is exists")
else:  
    print("key is not exists")


# b....Python script to merge two Python dictionaries.
d1 = {
    "f1" : "Mango",
    "f2" : "watermelon"
}

d2 = {
    "f3" : "Apple",
    "f4" : "Orange"
}

d1.update(d2)
print(d1)


# c....Python program to sum all the items in a dictionary.

d1 = {
    "key1" : 10,
    "key2" : 20,
    "key3" : 30
}


l1 = []
for i in d1:
    l1.append(d1[i])
ans = sum(l1)
print(ans)



# d.... Python script to add a key to a dictionary.
d1 = {
    0:10,
    1:20
}

print(d1)
d1.update({2:20})
print(d1)



# e....Python script to concatenate following dictionaries to create a new one.

# Sample Dictionary :

# dic1={1:10, 2:20}

# dic2={3:30, 4:40}

# dic3={5:50,6:60}

# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
d1 = {1:10, 2:20}

d2 = {3:30, 4:40}

d3 = {5:50,6:60}

d4 = {}

d4.update(d1)
d4.update(d2)
d4.update(d3)
print(d4)









#                                    ***********tuple***********
# a.....Python program to create a tuple with different data types.
t1 = ("Item1",12,True,12.2)
print(t1)

#b....Python program to create a tuple with numbers and print one item.
t1 = ("Item1","Item2","Item3","Item4")
print(t1[0])

# c....program to add an item in a tuple.
t1 = ("Item1","Item2","Item3","Item4")
print("Before adding Item")
print(t1)
print("After adding Item")
l1 = list(t1)
l1.append("Item5")
t1 = tuple(l1)
print(t1)



# d....program to convert a tuple to a string.
t1 = ('p','r','a','t','h','a','m')
s1 = ''.join(t1)
print(s1)

# e....program to find the length of a tuple.
t1 = ("Item1","Item2","Item3","Item4")
print("Tuple is",t1)
print("length of tuple is",len(t1))



#                                    ***********set***********
# a....Python program to add member(s) in a set and clear a set
s1 = {"Item1","Item2","Item3","Item4"}
s1.add("Item5")
print("After adding Item5")
print(s1)
s1.clear()
print("After Clear a set")
print(s1)


#b....Python program to remove an item from a set if it is present in the set. 
s1 = {"Item1","Item2","Item3","Item4"}
s1.remove("Item2")
print(s1)


# c....Python program to create an intersection, Union, difference of sets.
# union 
s1 = {"Item1","Item2","Item3","Item4"}
s2 = {"Item5","Item2","Item3","Item6"}
s3 = s1.union(s2)
print(s3)


# intersection
s1 = {"Item1","Item2","Item3","Item4"}
s2 = {"Item5","Item2","Item3","Item6"}
s4 = {"Item5","Item2","Item1","Item6"}
s3 = s1.intersection(s2,s4)
print(s3)


# difference
s1 = {"Item1","Item2","Item3","Item4"}
s2 = {"Item5","Item2","Item3","Item6"}
s3 = s1.difference(s2)
print(s3)

# d....Python program to find maximum and the minimum value in a set.
from typing import Counter
s1 = {1,2,3,4,5,4,4,6}
print(s1)
print("maximum value is",max(s1))
print("minimum value is",min(s1))
print(Counter(s1))


# e....Python program to find the most common elements and their counts from list, tuple, dictionary.


from statistics import mode

# # in list
l1 =[1,2,3,4,4,4,4,4,4,5,4,4,6]
print(l1)
print(mode(l1))

# in tuple
t1 = (1,2,3,4,4,4,4,4,4,5,4,4,6)
print(t1)
print(mode(t1))

# in dictonary
d1 = {
    "a1" : "1",
    "a2" : "2",
    "a3" : "3",
    "a4" : "4"
}
print(d1)
t1 = list(d1)
print(t1)