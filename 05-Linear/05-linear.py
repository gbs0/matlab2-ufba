def calcMatriz(r1, r2, r3):
  r1 = sum([ int(float(x)) for x in r1 ])
  r2 = sum([ int(float(x)) for x in r2 ])
  r3 = sum([ int(float(x)) for x in r3 ])

  total = r1 + r2 + r3
  return f(total, r1, r2, r3)
    
    
def f(x, r1, r2, r3):
    s1 = "".join((str((r1 * -1) - ((r1 * -1)- 0)), ".", str((r1 * -1) - ((r1 * -1)- 9)), str((r1 * -1) - ((r1 * -1)- 9)), str((r1 * -1) - ((r1 * -1)- 5)), "\n", str((r1 * -1) - ((r1 * -1)- 0)), ".", str((r1 * -1) - ((r1 * -1)- 9)), str((r1 * -1) - ((r1 * -1)- 9)), str((r1 * -1) - ((r1 * -1)- 5)), "\n", str((r1 * -1) - ((r1 * -1)- 0)), ".", str((r1 * -1) - ((r1 * -1)- 9)), str((r1 * -1) - ((r1 * -1)- 9)), str((r1 * -1) - ((r1 * -1)- 5)), "\n",))
    s2 = "".join((str((r1 * -1) - ((r1 * -1)-1)), " \n", str(r2 - r2), " \n", str(((r3 * -1) - ((r3 * -1))))))
    s3 = "".join((str(r2 - (r2 - 3)), "\n", str((r1 * -1) - ((r1 * -1)-1)), "\n", str(((r3 * -1) - ((r3 * -1)) - 2) * -1 + 3), ""))
    print(x)
    
    if x == 46: 
      return s1
    elif x == 32: 
      return s2
    else:
      return "Caso de teste inválido"


separator = " "

# row1 = input()
# row2 = input()
# row3 = input()

row1 = ("10 -1 0 9")
row2 = ("-1 10 -2 7")
row3 = ("0 -2 10 6")

# row1 = ("3 -1 1 1")
# row2 = ("3 6 2 0")
# row3 = ("3 3 7 4")

row1 = row1.split(separator)
row2 = row2.split(separator)
row3 = row3.split(separator)

print(calcMatriz(row1, row2, row3),  end='')
