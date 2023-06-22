def binary_array_to_number(arr):
  # your code
  integer=int(''.join(map(str,arr)))
  binary_code = int(str(integer),2)
  return binary_code