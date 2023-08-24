"""

La idea principal del LEXER es convertir las palabras que se espera
recibir a tokens conocidos y estandarizar lo que es recibido por 
parametros para posteriormente ser analizado sintacticamente por el PARSER.

"""
"""

###ACLARACIONES LITERALES DEL DOCUMENTO...

"""
def lexer():
    interrupt = False
    while interrupt == False:
        
        originalStr = input("Ingrese la cadena a analizar: \n")
        strFiltered = "".join(originalStr.split())
        
        
        strConverted = ""


        ###LÓGICA PARA TOKENIZAR CADENA

        return strFiltered
        #return strConverted


###PRUEBAS
#SIMULACIÓN DE INGRESO DE CADENA 
with open("entradaAValidar.txt", "r") as entrada:
    lista = entrada.read().split()
    print(lista)

print("")
print("-------------------")
print("")
#ELIMINAR ESPACIOS, TABULADORES Y SALTOS DE LINEA ADICIONALES && HACER LA CADENA MINUSCULA(COMPLETA Y FUNCIONAL)
lowCaseStr = ""
for i in lista:
    element = str(i)
    strLowCase = element.lower()
    #print(strLowCase)
    lowCaseStr += f" {strLowCase}"
print("Cadena completa en minusculas: \n ")
print(lowCaseStr)       #strDECADENAENMINUSC

#HACER FUNCION PARA VERIFICAR PARENTESIS(COMPLETA Y FUNCIONAL)
ansParen = True
paren = ['(',')','[',']','{','}']
check = []
for i in lowCaseStr:
    if i in paren:
        check.append(i)     #LISTA DE 
print("")
print(check, len(check))
print("")

par_dict = {'(':')','{':'}','[':']'}
stack = []
for char in check:
      # push opening bracket to stack
      if char in par_dict.keys():
        stack.append(char)
      else:
        # closing bracket without matching opening bracket
        if stack == []:
            ansParen = False
        # if closing bracket -> pop stack top
        open_brac = stack.pop()
        # not matching bracket -> invalid!
        if char != par_dict[open_brac]:
          ansParen = False
ansParen =  stack == []

print(f"El resultado del validParen es: {ansParen}")

###
"""
for i in range(len(check) - 1):
    print(f"i: {i}")
    for j in range(len(check) - 1):
        print(f"j: {j}")
        if (check[i] == '(' and check[j] == ')') or (check[i] == '[' and check[j] == ']') or (check[i] == '{' and check[j] == '}'):
            check.pop(i)
            check.pop(j)
"""

###---------FUNCION PLANTILLA PARA VERIFICAR PARENTESIS
def validParentesis(cadenaTokenizada: str):
  
      
    """Verifica si una cadena tokenizada tiene los parentesis, corchetes bien puestos.
  
    Args:
      test_str (str): La cadena a ser validada
    
    Returns:
      True si test_str es válido; else False 
    """
    list = cadenaTokenizada.split()
    parentList = ["(",")","[","]","{","}"]
    filterList = []
    for char in list:
     if char in parentList:
       filterList.append(char)
  
    test_str = "".join(filterList)
    #print(test_str)
    # si la longitud es impar -> invalida!
    if len(test_str)%2 != 0:
      return False
    # initialize parentheses dict
    par_dict = {'(':')','{':'}','[':']'}
    stack = []
    for char in test_str:
      # push opening bracket to stack
      if char in par_dict.keys():
        stack.append(char)
      else:
        # closing bracket without matching opening bracket
        if stack == []:
            return False
        # if closing bracket -> pop stack top
        open_brac = stack.pop()
        # not matching bracket -> invalid!
        if char != par_dict[open_brac]:
          return False
    return stack == []
###REORGANIZAR CODIGO PARA TOKENIZAR FACIL




#SE DEBE TENER EN CUENTA LAS ASIGNACIONES (name = v), donde v es un valor


"""
lowCaseLst.replace("defvar","DEFV")
lowCaseLst.replace("defproc","DEFP")
lowCaseLst.replace("putcb","CB")
"""
#TOKENIZAR 


#print(lexer())