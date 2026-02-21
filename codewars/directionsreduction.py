# 5 kyu - Directions Reduction
directionArray = ["SOUTH", "EAST", "WEST", "NORTH", "WEST"]

def dir_reduc(arr):
  for i in range(len(arr) - 1):
    if arr[i] == "NORTH" and arr[i + 1] == "SOUTH" or arr[i] == "SOUTH" and arr[i + 1] == "NORTH" or arr[i] == "EAST" and arr[i + 1] == "WEST" or arr[i] == "WEST" and arr[i + 1] == "EAST":
      arr.pop(i)
      arr.pop(i)
      return dir_reduc(arr)
  return arr

print(dir_reduc(directionArray))
