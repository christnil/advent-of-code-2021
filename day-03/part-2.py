import numpy as np

test = False
inputFile = 'input-test' if test else 'input'


def getInput():
  with open(inputFile) as file:
    raw = file.read()
  data = np.array([list(map(int, line)) for line in raw.splitlines()])
  return data


def getGasRating(ratings, position, mask_bit, cmp):
  # print('-------------------------------------------------------')
  # print(ratings)
  if len(ratings) == 1:
    return ratings[0]

  mask = ratings[:, position] == mask_bit
  # print('mask ' + str(mask))
  # print('mask sum ' + str(mask.sum()))
  # print('half_len ' + str(len(ratings) / 2))
  return getGasRating(ratings[mask == cmp(mask.sum(), len(ratings) / 2)], position + 1, mask_bit, cmp)


def main():
  input = getInput()
  h, w = input.shape
  powers = 2 ** np.arange(w)[::-1]

  oxygen = getGasRating(input, 0, 1, lambda a, b: a >= b)
  oxygen_dec = oxygen @ powers
  co2 = getGasRating(input, 0, 0, lambda a, b: a <= b)
  co2_dec = co2 @ powers
  res = oxygen_dec * co2_dec
  print('oxygen ' + str(oxygen_dec))
  print('co2 ' + str(co2_dec))
  print('product ' + str(res))

main()

