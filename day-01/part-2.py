import numpy as np;

def getInput():
  with open("input") as file:
    return list(map(int, file.readlines()))

def getDecresing(depths):
  p1 = depths.pop(0)
  p2 = depths.pop(0)
  p3 = depths.pop(0)
  count = 0
  for depth in depths:
    if p1 + p2 + p3 < p2 + p3 + depth:
      count = count + 1
    p1 = p2
    p2 = p3
    p3 = depth
  print(count)

def main():
  input = getInput()
  getDecresing(input)

main()

