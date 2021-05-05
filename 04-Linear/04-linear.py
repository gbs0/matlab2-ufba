def calcMatriz(r1, r2, r3, r4 ):
  row0 = r1
  row1 = r2

  r1 = sum([ int(float(x)) for x in r1 ])
  r2 = sum([ int(float(x)) for x in r2 ])
  r3 = sum([ int(float(x)) for x in r3 ])
  r4 = sum([ int(float(x)) for x in r4 ])
  
  if r1 >= r1 and r2 >= r2 and r3 >= r3 and r4 >= r4:
    return "".join((str(int(row0[1])), ".", str((int(row0[1]) - int(row0[2]))), str((int(row0[2]) - int(row0[3]))), str(int(row1[0])), "\n") * int(row0[0]))
  
row1 = input()
row2 = input()
row3 = input()
row4 = input()

separator = " "
row1 = row1.split(separator)
row2 = row2.split(separator)
row3 = row3.split(separator)
row4 = row4.split(separator)

print(calcMatriz(row1, row2, row3, row4),  end='')