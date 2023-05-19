class NoPuedeEscribirDosException(Exception):
    def __init__(self, _message):
        self.message = _message

try:
    number = input("Intruduce un numero: ")
    if (number == "2"):
        raise NoPuedeEscribirDosException("Introdujo un numero 2 y este no es válido")
    else:
        print("Numero intriducido correctamente")
except Exception as error:
    print(type(error))
    print(error.args)