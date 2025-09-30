#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#What is a Module?
#A module in Python is simply a file that contains Python code (functions, variables, classes).
#Think of it as a toolbox: instead of writing everything from scratch, you just import the tools you need.
#Example: Python has a built-in math module that gives you math functions like square roots and trigonometry.
#You use the import keyword


# In[1]:


import math


# In[2]:


print(math.sqrt(16))


# In[3]:


print(math.pi)


# In[4]:


#You can also import specific functions:
from math import sqrt, pi

print(sqrt(25))   
print(pi)        


# In[ ]:


#Built-in Modules Examples
#random → generate random numbers
#datetime → work with dates & times
#os → interact with your computer’s file system


# In[5]:


import random


# In[9]:


print(random.randint(10,23))


# In[7]:


import random
print(random.randint(1, 10))  # random number between 1 and 10

import datetime
print(datetime.datetime.now())  # current date and time


# In[10]:


print(random.randint(1,25))


# In[ ]:


#External Packages
#Sometimes built-in modules aren’t enough.
#You can install extra ones using pip (Python’s package manager).
#Example (run in terminal, not Python):


# In[ ]:




