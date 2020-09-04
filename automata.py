# Función para corroborar que el carácter es una letra:
def esLetra(caracter):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letra in alfabeto:
        if caracter.lower() == letra:
            return True
    return False

# Función para corroborar que el carácter es un número:
def esNumero(caracter):
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for num in numeros:
        if caracter == num:
            return True
    return False

# Función para corroborar que el carácter es un guion bajo:
def esGuion(caracter):
    if caracter.lower() == '_':
        return True
    else:
        return False

# Autómata:
def automata(cadena):
    estado = 0
    for caracter in cadena:
        if estado == 0:
            if esGuion(caracter):
                estado = 1
            elif esLetra(caracter):
                estado = 2
            else:
                print("La cadena '" + cadena + "' es inválida")
                break
        elif estado == 1:
            if esGuion(caracter):
                estado = 1
            elif esLetra(caracter):
                estado = 3
            else:
                print("La cadena '" + cadena + "' es inválida")
                break
        elif estado == 2:
            if esNumero(caracter):
                estado = 4
            elif esLetra(caracter):
                estado = 2
            else:
                print("La cadena '" + cadena + "' es inválida")
                break
        elif estado == 3:
            if esNumero(caracter):
                estado = 4
            else:
                print("La cadena '" + cadena + "' es inválida")
                break
    if estado == 4:
        print("Cadena '" + cadena + "' válida")

# Main:
cadena1 = " __servidor1" 
cadena2 = "3servidor"
print("Laboratorio de Lenguajes Formales y de Programación")
print("Nombre: Romeo Ernesto Marroquín Sánchez")
print("Carné: 201902157")
print("")
automata(cadena1)
automata(cadena2)
input()