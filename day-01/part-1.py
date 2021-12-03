import numpy as np;

def getInput():
  with open("input") as file:
    return list(map(int, file.readlines()))

def getDecresing(depths):
  last = 0
  count = -1
  for depth in depths:
    if depth > last:
      count = count + 1
    last = depth
  print(count)

def main():
  input = getInput()
  getDecresing(input)

main()

