
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








# # Question 4 
# Write a Python program to check a dictionary is empty or not

# In[5]:


my_dict = {}

if not bool(my_dict):
    print("Dictionary is empty")










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




