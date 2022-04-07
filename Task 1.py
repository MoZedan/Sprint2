#!/usr/bin/env python
# coding: utf-8

# # Task 1 ( Basics )

# # Question 1 :
# Define a function which can compute the sum of two numbers.
# 
# Hints:
# Define a function with two numbers as arguments. You can compute the sum in the function and return the value.

# In[1]:


num1 = input('Enter first number: ')
num2 = input('Enter second number: ')


sum = float(num1) + float(num2)


print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# # Question 2:
# 
#     Write a method which can calculate square value of number
# 
# Hints:
#     Using the ** operator
# 

# In[ ]:


num = int (input("Enter an any number: "))
 

sq = num**2
 

print("Square of {0} is {1} ".format(num, sq))


# # Question 3
# Define a function that can convert a integer into a string and print it in console.
# 
# Hints:
# 
# Use str() to convert a number to string.

# In[ ]:


num = 10
 

print(type(num))
 

converted_num = "{}".format(num)
print(type(converted_num))


# # Question 4 :
# Define a function that can receive two integral numbers in string form and compute their sum and then print it in console.
# 
# Hints:
# 
# Use int() to convert a string to integer.

# In[ ]:


def calculateSumFor(first,second):
  return int(first) + int(second)

firstNumber = "100"
secondNumber = "200"

print(calculateSumFor(firstNumber,secondNumber))


# # Question 5 :
# Define a function that can accept two strings as input and concatenate them and then print it in console.
# 
# Hints:
# 
# Use + to concatenate the strings
# 

# In[ ]:


s1 = input('Please enter the first string:\n')
s2 = input('Please enter the second string:\n')

print('Concatenated String =', s1 + s2)


# # Question 6 :
# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.
# 
# Hints:
# 
# Use len() function to get the length of a string

# In[ ]:


def length_of_string(str1, str2):
if (len(str1) == len(str2)):
     print(str1)

        print(str2)

    elif (len(str1) < len(str2)):
        print(str2)
 
    else:
        print(str1)

stri1 = input(str("enter First String: "))
stri2 = input(str("enter Second String: "))

print("\n")

length_of_string(stri1, stri2)


# # Question 7 :
# Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
# 
# Hints:
# 
# Use % operator to check if a number is even or odd.

# In[ ]:


print ("Enter an integer number to check:\n")

x = int (input ())

if (x % 2 == 0):
    print ("The input number is even.\n")
else:
    print ("The input number is odd.\n")


# # Question 8 :
# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 
# 
# Hints:
# 
# Use if statement to judge condition.

# In[ ]:


Join = input('are you hungry?')
if Join.lower() == 'yes':
  print("let`s eat," +  me too + '!')
else:
  print ("Sorry for asking...")


# In[ ]:





# # Question 9 :
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# 
# Hints: 
# Consider use range(#begin, #end) method

# In[3]:


al=[]

for x in range(2000, 3200):

if (x%7==0) and (x%5!==0):

al.append(str(x))

print (','.join(nl))


# In[ ]:





# In[ ]:





# # Question 10 :
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
# 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

# In[10]:


#Search about it please


# In[ ]:





# In[ ]:





# In[ ]:





# # Question 11 :
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
# 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# 

# In[ ]:





# In[ ]:




