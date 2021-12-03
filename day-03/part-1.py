import numpy as np

test = False
inputFile = 'input-test' if test else 'input'


def getInput():
  with open(inputFile) as file:
    raw = file.read()
  data = np.array([list(map(int, line)) for line in raw.splitlines()])
  return data


def getPowerConsumption(input):
  h, w = input.shape
  powers = 2 ** np.arange(w)[::-1]
  one_most_common = input.sum(axis=0) > (h / 2)
  gamma_rate = powers @ one_most_common
  epsilon_rate = powers @ ~one_most_common
  return gamma_rate * epsilon_rate


def main():
  input = getInput()
  print(getPowerConsumption(input))

main()

