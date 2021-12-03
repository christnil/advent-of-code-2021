import re

test = False
inputFile = 'input-test' if test else 'input'

def getInput():
  raw = ''
  with open(inputFile) as file:
    raw = file.read()
  data = [(direction, int(amount)) for direction, amount in re.findall(r'(\w+) (\d+)', raw)]
  return data

def drive(directions):
  depth = x = aim = 0
  for direction, amount in directions:
    match direction:
      case 'forward':
        x += amount
        depth += (aim * amount)
      case 'down':
        aim += amount
      case 'up':
        aim -= amount
  return depth * x

def main():
  input = getInput()
  result = drive(input)
  print(result)

main()

