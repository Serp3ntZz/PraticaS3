
lista = ["A","B","C","D","E","F","G","H","I","L","M","N","O","P","Q","R","S","T","U","V","Z"]

messaggio = "HSNFRGH"

decodifica = []

for lett in messaggio:
    if lett in lista:
        x= lista.index(lett)
        y = x - 3
        decodifica.append(lista[y])

parola= ''.join(decodifica)

print("\nMessaggio decodificato:", parola)