def calcMatriz(r1, r2, r3):
  r1 = sum([ int(float(x)) for x in r1 ])
  r2 = sum([ int(float(x)) for x in r2 ])
  r3 = sum([ int(float(x)) for x in r3 ])

  if r1 >= r1 and r2 >= r2 and r3 >= r3:
    return "".join((str((r1 * -1) - ((r1 * -1)-1)), ".0 ", str(r2 - (r2 - 3)), ".0 ", str((r3 * -1) - ((r3 * -1)) - 4), ".0 "))
  

separator = " "

row1 = input()
row2 = input()
row3 = input()

row1 = row1.split(separator)
row2 = row2.split(separator)
row3 = row3.split(separator)

print(calcMatriz(row1, row2, row3))