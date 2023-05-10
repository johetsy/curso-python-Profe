Z = 10
K = 100000
Y = 0.2

años = range(Z)
I = Y / 100

for elemento in años:
    K = K * (1 + I)


print(f'El capital acumulado en {Z} años es de: {K}')
