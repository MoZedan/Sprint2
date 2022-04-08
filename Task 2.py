#!/usr/bin/env python
# coding: utf-8

# # Question 1:
# Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
# 
# Hints:
# 
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.

# In[4]:


def printDict():
    dict={i:i**2 for i in range(1,3)}    
    print(dict)

printDict()


# # Question 2:
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.
# 
# Hints:
# 
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
# 

# In[ ]:





# # Question 3:
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.
# 
# Hints:
# 
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
# 

# In[ ]:





# # Question 4 
# Write a Python program to check a dictionary is empty or not

# In[5]:


my_dict = {}

if not bool(my_dict):
    print("Dictionary is empty")


# # Question 5
# 
# Write a Python program to test whether every element in s is in t and every element in t is in s.
# 
# 

# In[ ]:





# # Question 6
# Create set 1 and set 2 then 
# Write a Python program to 1- create an intersection of sets.
# 2-  a union of sets.
# 3- create set difference.
# 4- a symmetric difference.

# In[ ]:





# # Question  7
# Write a Python program to use of frozensets.

# In[ ]:


# Python program to understand frozenset() function
 
# tuple of numbers
nu = (1, 2, 3, 4, 5, 6, 7, 8, 9)
 
# converting tuple to frozenset
fnum = frozenset(nu)
 
# printing details
print("frozenset Object is : ", fnum)


# # Question 8
# Write a Python program to find maximum and the minimum value in a set.

# In[6]:


setn = {2, 5, 3, 1, 20}
print("Original set elements:")
print(setn)
print(type(setn))
print("\nMaximum value of the said set:")
print(max(setn))
print("\nMinimum value of the said set:")
print(min(setn))


# # Question9 :
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 
# 
# Hints:
# 
# Use [n1:n2] notation to get a slice from a tuple.

# In[7]:


tp=(1,2,3,4,5,6,7,8,9,10)

tp1=tp[:5]

tp2=tp[5:]

print(tp1)

print(tp2)


# # Question 10 :
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
# 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use itemgetter to enable multiple sort keys.
# 
# Solutions:
# from operator import itemgetter, attrgetter
# 

# In[ ]:





# # Question 11:
# 
# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
# 
# 
# 
# Hints:
# Use random.sample() to generate a list of random values.

# In[8]:





# # Question 12
# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
# 
# Hints:
# Use random.sample() to generate a list of random values.

# In[9]:


import random
print(random.sample([i for i in range(100,200) if i%2==0], 5))


# # Question 13
# Please write a program to randomly print a integer number between 7 and 15 inclusive.
# 
# Hints: Use random.randrange() to a random integer in a given range.
# 
# 

# In[12]:


import random
x = random.randint(7,15)
print(x)


# # Question 14
# 
# Please write a program to print the running time of execution of "1+1" for 100 times.
# Hints:
# Use timeit() function to measure the running time.
# 

# In[ ]:





# # Question 15 :
# 
# Please write a program to shuffle and print the list [3,6,7,8].
# 
# Hints:
# Use shuffle() function to shuffle a list.
# 

# In[13]:


from random import shuffle
number = [3,6,7,8]
shuffle(number)
print(number)


# In[ ]:




