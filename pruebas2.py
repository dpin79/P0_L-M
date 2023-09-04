lst = ['defvar', 'nom', '0', 'defvar', 'x', '0', 'defvar', 'y', '0', 'defvar', 'one', '0', 'defproc', 'putcb', '(c', ',', 'b', ')', '{', 'drop(', 'c', ')', ';', 'letgo', '(', 'b', ')', ';', 'walk(', 'n', ')', '}', 'defproc', 'gonorth', '()', '{', 'while', 'can(walk(1', ',', 'north', ')', ')', '{', 'walk(1', ',', 'north', ')', '}', '}', 'defproc', 'gowest', '()', '{', 'if', 'can(walk(1', ',', 'west', ')', ')', '{', 'walk(1', ',', 'west', ')', '}', 'else', 'nop', '()', '}', '{', 'jump', '(3', ',3)', ';', 'putcb', '(2', ',1)', '}']
flst = ['defvar', 'nom', '0', 'defvar', 'x', '0', 'defvar', 'y', '0', 'defvar', 'one', '0', 'defproc', 'putcb', '(', 'c', ',', 'b', ')', '{', 'drop', '(', 'c', ')', ';', 'letgo', '(', 'b', ')', ';', 'walk', '(', 'n', ')', '}', 'defproc', 'gonorth', '(', ')', '{', 'while', 'can', '(', 'walk', '(', '1', ',', 'north', ')', ')', '{', 'walk', '(', '1', ',', 'north', ')', '}', '}', 'defproc', 'gowest', '(', ')', '{', 'if', 'can','(', 'walk', '(', '1', ',', 'west', ')', ')', '{', 'walk', '(', '1', ',', 'west', ')', '}', 'else', 'nop', '(', ')', '}', '{', 'jump', '(', '3', ',', '3', ')', ';', 'putcb', '(', '2', ',', '1', ')', '}']
nLst = []
###
#       lstToFilter = ['(c', 'drop(', 'walk(', '()', 'can(walk(1', 'walk(1', 'walk(1', '(3', ',3)', '(2', ',1)']
###
#print(f'LIST: {lst}')
#print('')
#print('---------------')
#print('')
for i in range(len(lst)-1):
        if(len(lst[i]) == 1):
                nLst.append(lst[i])
        try:


            ###TODO CASOS DE NUMERO EN PRIMERA O ÚLTIMA POSICIÓN (NUMERO DE UNA CIFRA)

            if int(lst[i][0]) % 1 == 0:    #PRIMER CHAR NUMERO EN CADENA ERRONEA
                nLst.append(lst[i][0])
                restElem = lst[i][2:]
                nLst.append(restElem)

            elif int(lst[i][-1]) % 1 == 0:    #ULTIMO CHAR NUMERO EN CADENA ERRONEA
                nLst.append(lst[i][-1])
                restElem = lst[i][:-2]
                nLst.append(restElem)
        except:
                nLst.append(lst[i])

#print(nLst)

import re

def separar_elementos_lista(lista):
    # Combina todos los elementos de la lista en una sola cadena
    cadena = ' '.join(lista)
    
    # Define una expresión regular para buscar paréntesis, números, cadenas y comas
    patron = r'(\(|\)|\d+|"[^"]*"|,)'
    
    # Utiliza findall para obtener todos los elementos que coinciden con el patrón
    elementos = re.findall(patron, cadena)
    
    # Elimina los espacios en blanco alrededor de cada elemento
    elementos = [elemento.strip() for elemento in elementos]
    
    return elementos

# Ejemplo de uso:
mi_lista = ['Esto es un (ejemplo 123) de "cadenas de texto",1,2,3']
elementos_separados = separar_elementos_lista(lst)
#print(elementos_separados)

import re

def separar_elementos_lista(lista):
    # Combina todos los elementos de la lista en una sola cadena
    cadena = ' '.join(lista)
    
    # Define una expresión regular para buscar paréntesis, números, cadenas y comas
    patron = r'(\(|\)|\d+|"[^"]*"|,)'
    
    # Utiliza findall para obtener todos los elementos que coinciden con el patrón
    elementos = re.findall(patron, cadena)
    
    # Elimina los espacios en blanco alrededor de cada elemento
    elementos = [elemento.strip() for elemento in elementos]
    
    return elementos

# Ejemplo de uso:
mi_lista = ['Esto es un (ejemplo 123) de "cadenas de texto",1,2,3']
elementos_separados = separar_elementos_lista(lst)
#print(elementos_separados)

def convertir_lista(A):
    lista_B = []
    i = 0

    while i < len(A):
        if A[i] == '(':
            # Buscar el índice del cierre de paréntesis
            j = i + 1
            while j < len(A) and A[j] != ')':
                j += 1

            # Agregar los elementos entre paréntesis a lista_B
            lista_B.append('(')
            lista_B.extend(A[i + 1:j])
            lista_B.append(')')

            # Actualizar el índice i
            i = j + 1
        else:
            lista_B.append(A[i])
            i += 1

    return lista_B

# Ejemplo de uso
A = ['defvar', 'nom', '0', 'defvar', 'x', '0', 'defvar', 'y', '0', 'defvar', 'one', '0', 'defproc', 'putcb', '(c', ',', 'b', ')', '{', 'drop(', 'c', ')', ';', 'letgo', '(', 'b', ')', ';', 'walk(', 'n', ')', '}', 'defproc', 'gonorth', '()', '{', 'while', 'can(walk(1', ',', 'north', ')', ')', '{', 'walk(1', ',', 'north', ')', '}', '}', 'defproc', 'gowest', '()', '{', 'if', 'can(walk(1', ',', 'west', ')', ')', '{', 'walk(1', ',', 'west', ')', '}', 'else', 'nop', '()', '}', '{', 'jump', '(3', ',3)', ';', 'putcb', '(2', ',1)', '}']

#B = convertir_lista(lst)


def convert_list(A):
  """
  Convierte la lista A a la lista B.

  Args:
    A: La lista a convertir.

  Returns:
    La lista convertida.
  """
  B = []
  for token in A:
    if token[0] == "defproc":
      B.append(token[0:2])
      for arg in token[2:-1]:
        B.append(arg)
      B.append(")")
    else:
      B.append(token)
  return B

B = convert_list(lst)
print('LISTA B: \n')
print(B)
print(B == flst)