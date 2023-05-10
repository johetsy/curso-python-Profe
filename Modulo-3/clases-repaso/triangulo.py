altura = int(input("dime la altura del triangulo"))

# *
# **
# ***
# ****

triangulo = ""
for ele in range(altura):
    triangulo = "*" + triangulo
    print(triangulo)


#[0, 1, 2, 3, 4]
for ele in range(altura):
    print("*"*(ele+1))