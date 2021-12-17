# initial idea assumes comparisons on each pair of elements
# so it has strategy "pass to begin"
# on each element initial swap it has kind of wave effect
def insertion_sort(arr):
  for i in range(1, len(arr)):
    j = i

    while j > 0 and arr[j] < arr[j - 1]:
      arr[j], arr[j - 1] = arr[j - 1], arr[j]
      j -= 1
    

# my naive implementation (it does not use "pass to begin strategy")
def insertion_sort(arr):
  done = False
  pointer = 0
  swaps = 0

  while not done:
    if pointer != len(A) - 1:
      if A[pointer] > A[pointer + 1]:
        A[pointer], A[pointer + 1] = A[pointer + 1], A[pointer]
        swaps += 1
      pointer += 1
    elif swaps == 0:
      done = True
    else:
      pointer = 0
      swaps = 0