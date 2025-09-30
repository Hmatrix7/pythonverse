#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#What is a Function?
#A function is a block of code that only runs when it is called.
#def → keyword to define a function.
#greet → function name.
#() → parentheses for parameters.
#Indented block → code that runs when the function is called.


# In[2]:


def greet():
    print("Hello, Data Analyst!")

greet()  # Calling the function


# In[3]:


#Default Parameters
def greet(name="Barrack"):# you can set Parameters inside a function
    print(f"Hello {name}")
greet()
greet("Monkey")


# In[4]:


def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result)  


# In[12]:


def add(a, b):
    print(a + b)

result = add(3, 4)
print(result)  # This shows 7 and then None


# In[18]:


def introduce(name, age):# function name is introduce
    print(f"My name is {name}, and I am {age} years old.")

introduce(age=25, name="Barrack")


# In[ ]:




