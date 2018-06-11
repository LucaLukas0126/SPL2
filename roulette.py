#uebung3
import random

zahlen = []
anzahlRoulette = input("Wie oft soll es sich drehen?")
anzahlRoulette = int(anzahlRoulette)
for i in range (0,37):
    wurf = random.randint(1,6)
    zahlen.append(wurf)
    print(wurf, end="...")

print()
print ("Ergebnis: ")
print (zahlen)

for i in range(1,7):
print(i,"er: ",zahlen.count(1))