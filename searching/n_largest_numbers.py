def find_max_index(n, num, result):
  max_index = None
  for k in range(n):
    if result[k] is None or num > result[k]:
      max_index = k
  return max_index


def find_n_largest_numbers(nums, n):
  result = [None for i in range(n)]

  for num in nums:
    max_index = find_max_index(n, num, result)

    if max_index is not None:
      if max_index != 0:
        for j in range(max_index):
          result[j], result[j + 1] = result[j + 1], result[j]
        result[max_index] = num
      else:
        result[0] = num

  print(result)
  return result

 
data = [-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7]
find_n_largest_numbers(data, 3)