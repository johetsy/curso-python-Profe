frase = input('introduce una frase')
letra = input('introduce una letra')

cnt = 0
for letter in frase:
    if letter == letra:
        cnt += 1

print(f'la cantidad de "{letra}" que hay es {cnt}')