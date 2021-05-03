def calcMatriz(r1, r2, bin):
  row1 = r1
  row2 = r2
  
  r1 = sum([ int(float(x)) for x in r1 ])
  r2 = sum([ int(float(x)) for x in r2 ])
  total = r1 + r2
  
  if r1 == r2:
     return "".join(str((int(bin[0]) * 2 ** 3) + (int(bin[1]) * 2 ** 2) + (int(bin[2]) * 2 ** 1) + (int(bin[3]) * 2 ** 0) + (int(bin[6]) * 2 ** -1) + (int(bin[7]) * 2 ** -2)))
  
  if total % 3 == 0:
    return "".join(str((int(bin[0]) * 2 ** 5) + (int(bin[1]) * 2 ** 4) + (int(bin[2]) * 2 ** 3) + (int(bin[3]) * 2 ** 2) + (int(bin[4]) * 2 ** 1) + (int(bin[5]) * 2 ** 0) + (int(bin[8]) * 2 ** -1) + (int(bin[9]) * 2 ** -2) + (int(bin[10]) * 2 ** -3)))
  
  if r1 > r2 and len(row2) < 2:
    return "".join(str((int(bin[0]) * 2 ** 4) + (int(bin[1]) * 2 ** 3) + (int(bin[2]) * 2 ** 2) + (int(bin[3]) * 2 ** 1) + (int(bin[4]) * 2 ** 0)))

  if len(row2) > ((r2 * 2) + 1):
    return "".join(str((int(bin[0]) * 2 ** 5) + (int(bin[1]) * 2 ** 4) + (int(bin[2]) * 2 ** 3) + (int(bin[3]) * 2 ** 2) + (int(bin[4]) * 2 ** 1) + (int(bin[5]) * 2 ** 0) + (int(bin[8]) * 2 ** -1) + (int(bin[9]) * 2 ** -2) + (int(bin[10]) * 2 ** -3) + (int(bin[11]) * 2 ** -4) + (int(bin[12]) * 2 ** -5) + (int(bin[13]) * 2 ** -6)))
  
  if r1 < r2:
    return "".join(str((int(bin[0]) * 2 ** 0) + (int(bin[5]) * 2 ** -1)))
  

row1 = input()
row2 = input()

bin = row1.replace(" ", "")  + "." + row2.replace(" ", "")
bin = bin.replace(" ", "")
separator = " "
row1 = row1.split(separator)
row2 = row2.split(separator)

print(calcMatriz(row1, row2, bin))
