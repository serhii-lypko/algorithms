import string

# Maybe you’re wondering: as you go through the operations, the number
# of elements you have to check keeps decreasing. Eventually, you’re down
# to having to check just one element. So how can the run time still be
# O(n2)? That’s a good question, and the answer has to do with constants
# in Big O notation. I’ll get into this more in chapter 4, but here’s the gist.
# You’re right that you don’t have to check a list of n elements each time.
# You check n elements, then n – 1, n - 2 … 2, 1. On average, you check a
# list that has 1/2 × n elements. The runtime is O(n × 1/2 × n). But constants
# like 1/2 are ignored in Big O notation (again, see chapter 4 for the full
# discussion), so you just write O(n × n) or O(n2).

# Selection sort is a simple sorting algorithm. 
# This sorting algorithm is an in-place comparison-based 
# algorithm in which the list is divided into two parts,
# the sorted part at the left end and the unsorted part at 
# the right end. Initially, the sorted part is empty and the
# unsorted part is the entire list.

# The smallest element is selected from the unsorted array 
# and swapped with the leftmost element, and that element
# becomes a part of the sorted array. This process continues
# moving unsorted array boundary by one element to the right.

# This algorithm is not suitable for large data sets as its
# average and worst case complexities are of Ο(n2),
# where n is the number of items.

def selection_sort(arr):
  for i in range(len(arr)):
    min_index = i

    for k in range(i + 1, len(arr)):
      if arr[k] < arr[min_index]:
        min_index = k
    
    if min_index != i:
      arr[i], arr[min_index] = arr[min_index], arr[i]

  return arr



# alternate implementation
def find_smallets_index(arr):
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < arr[smallest_index]:
      smallest_index = i
  return smallest_index

def selection_sort_alternate(arr):
  newArr = []
  for i in range(len(arr)):
    smallest_index = find_smallets_index(arr)
    # arr.pop modifies the arr in closure
    newArr.append(arr.pop(smallest_index))
  return newArr



# sort names alphabetically
alphabet = list(string.ascii_lowercase)
names = ['Dan', 'Alice', 'Ethan', 'Bob', 'Clark', 'Amanda']

def is_symbol_before(a, b):
  return alphabet.index(a.lower()) < alphabet.index(b.lower())

def selection_sort_names(names):
  for i in range(len(names)):
    min_index = i

    for k in range(i + 1, len(names)):
      for j in range(len(names[min_index])):
        # case when len(names[min_index]) < len(names[k]) is not covered
        if names[min_index][j] == names[k][j]:
          continue
        else:
          is_before = is_symbol_before(names[min_index][j], names[k][j])
          if not is_before:
            min_index = k
          break

    if min_index != i:
      names[i], names[min_index] = names[min_index], names[i]

  return names


print(selection_sort_names(names))
