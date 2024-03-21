"""
SYNOPSIS
    python <program_name.py> -parameter <value>

DESCRIPTION
    Un script que ...

OPTIONS
    - 

EXAMPLES
    Ejemplo de uso:
        python program_name.py [-parameter] [value]
"""

## library


## functions

def function_name(arguments):
    """Function Description

    Args:
        argument (type):description

    Raises:
        ErrorName: Description

    Returns:
        type: description
    """


## main

# Definir las variables para contar las ocurrencias
count_A = 0
count_T = 0
count_G = 0
count_C = 0

# Leer el archivo con la cadena de ADN
with open('archivo.txt', 'r') as file:
    dna_sequence = file.read()

# Contar las ocurrencias de cada símbolo
for symbol in dna_sequence:
    if symbol == 'A':
        count_A += 1
    elif symbol == 'T':
        count_T += 1
    elif symbol == 'G':
        count_G += 1
    elif symbol == 'C':
        count_C += 1

# Imprimir los resultados
print("Ocurrencias de 'A':", count_A)
print("Ocurrencias de 'T':", count_T)
print("Ocurrencias de 'G':", count_G)
print("Ocurrencias de 'C':", count_C)
