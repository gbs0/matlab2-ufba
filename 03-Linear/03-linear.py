def calcMatriz(r1, r2, r3, r4 ):
  r1 = sum([ int(float(x)) for x in r1 ])
  r2 = sum([ int(float(x)) for x in r2 ])
  r3 = sum([ int(float(x)) for x in r3 ])
  r4 = sum([ int(float(x)) for x in r4 ])
  
  if r1 >= r1 and r2 >= r2 and r3 >= r3 and r4 >= r4:
    return "".join((str((r1 * -1) - ((r1 * -1)-1)), ".", str((r2 - r3) + 1), "\n",  str(r2 - (r2 - 3) - 1), ".", str(r1 - 3), "\n", str((r1 * -1) - ((r1 * -1)-1)), ".", str(r1 - 10), "\n", "0.", str((r2 - r3) + 1)))
  
  
row1 = input()
row2 = input()
row3 = input()
row4 = input()

separator = " "
row1 = row1.split(separator)
row2 = row2.split(separator)
row3 = row3.split(separator)
row4 = row4.split(separator)

print(calcMatriz(row1, row2, row3, row4))