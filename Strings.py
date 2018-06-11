eingabe = input("Hallo: wer bist du?")
print(eingabe)

for i in range(0,len(eingabe)):
    print(eingabe[i], end=".")

print()

for i in range(len(eingabe) -1, -1, -1 ):
    print(eingabe[i], end=".")
print()