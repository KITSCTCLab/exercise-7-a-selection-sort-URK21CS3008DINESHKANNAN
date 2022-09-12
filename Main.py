from typing import List

def selectionSort(array, size) -> List[int]:  
  
  for i in range(1,size-1):
    small_index = i
    for index in range(i + 1,size):
      if array[index] < array[small_index]:
        small_index = index
  return array     

# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))

