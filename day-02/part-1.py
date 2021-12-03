import re
import numpy as np;

test = False
inputFile = 'input-test' if test else 'input'

def getInput():
  raw = ''
  with open(inputFile) as file:
    raw = file.read()
  data = [(direction, int(amount)) for direction, amount in re.findall(r'(\w+) (\d+)', raw)]
  return data

def drive(directions):
  depth = x = 0
  for direction, amount in directions:
    match direction:
      case 'forward':
        x += amount
      case 'down':
        depth += amount
      case 'up':
        depth -= amount
  return depth * x

def main():
  input = getInput()
  result = drive(input)
  print(result)

main()

