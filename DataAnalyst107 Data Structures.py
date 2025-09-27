#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Python Day 6: Data Structures – Lists


# In[11]:


#creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)


# In[12]:


#Accessing Elements
print(fruits[0])   # apple
print(fruits[-1])  # cherry


# In[13]:


#Changing Elements
fruits[1] = "mango"
print(fruits)   # ['apple', 'mango', 'cherry']


# In[14]:


#Adding ElementsAdding Elements
fruits.append("orange")       # add to end
fruits.insert(1, "grape")     # add at position
print(fruits)


# In[15]:


#Removing Elements
fruits.remove("apple")   # remove by value
fruits.pop()             # remove last item
print(fruits)


# In[16]:


#Looping Through a List
for fruit in fruits:
    print(fruit)


# In[17]:


#List Functions
numbers = [3, 7, 2, 9, 5]

print(len(numbers))   # length
print(max(numbers))   # largest
print(min(numbers))   # smallest
print(sum(numbers))   # sum


# In[ ]:





# In[ ]:




