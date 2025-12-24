#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Sorting Algorithm


# In[7]:


#Bubble sort python
def bubble_sort(arr):
    n = len(arr)
    print("Initial Array:", arr)
    
    for i in range(n):
        print(f"\nPass {i+1}:")
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)
    
    return arr


data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = bubble_sort(data.copy())
print("\nSorted Array:", sorted_data)


# In[8]:


#Time Complexity:

#Best: O(n)

#Average/Worst: O(n²)


# In[9]:


#Selection sort python
def selection_sort(arr):
    n = len(arr)
    print("Initial Array:", arr)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"After pass {i+1}: {arr}")
    
    return arr


data = [64, 25, 12, 22, 11]
sorted_data = selection_sort(data.copy())
print("\nSorted Array:", sorted_data)


# In[10]:


#⏱ Time Complexity: O(n²)


# In[11]:


#Insertion sort python
def insertion_sort(arr):
    print("Initial Array:", arr)
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
        print(f"After inserting element {i}: {arr}")
    
    return arr


data = [12, 11, 13, 5, 6]
sorted_data = insertion_sort(data.copy())
print("\nSorted Array:", sorted_data)


# In[12]:


#⏱ Time Complexity:

#Best: O(n)

#Worst: O(n²)


# In[13]:


#Merge sort python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


data = [38, 27, 43, 3, 9, 82, 10]
print("Initial Array:", data)
merge_sort(data)
print("Sorted Array:", data)


# In[14]:


#⏱ Time Complexity: O(n log n)


# In[15]:


#Quick sort python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        
        return quick_sort(left) + [pivot] + quick_sort(right)


data = [10, 7, 8, 9, 1, 5]
print("Initial Array:", data)
sorted_data = quick_sort(data)
print("Sorted Array:", sorted_data)


# In[16]:


#⏱ Time Complexity:

#Best/Average: O(n log n)

#Worst: O(n²)


# In[ ]:


| Algorithm      | Best Case  | Average Case | Worst Case |
| -------------- | ---------- | ------------ | ---------- |
| Bubble Sort    | O(n)       | O(n²)        | O(n²)      |
| Selection Sort | O(n²)      | O(n²)        | O(n²)      |
| Insertion Sort | O(n)       | O(n²)        | O(n²)      |
| Merge Sort     | O(n log n) | O(n log n)   | O(n log n) |
| Quick Sort     | O(n log n) | O(n log n)   | O(n²)      |

