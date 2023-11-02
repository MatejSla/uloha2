# 13 ka úloha ;)
cislo = int(input("Zadaj mi číslo:"))
while cislo !=1:
  if cislo % 2 == 0:
    cislo = cislo / 2
    print(int(cislo))
  else:
    cislo = 3 * cislo + 1
    print(int(cislo))
