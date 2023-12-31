"""
OBJETIVO DEL ARCHIVO EN EL PROGRAMA
La idea principal del LEXER es convertir las palabras que se espera
recibir a tokens conocidos y estandarizar lo que es recibido por 
parametros para posteriormente ser analizado sintacticamente por el PARSER.

"""
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
"""

###LECTURA DE ARCHIVO
#INGRESO DE CADENA POR NOMBRE DE ARCHIVO
with open("entradaAValidar.txt", "r") as entrada:
    lista = entrada.read().split()
    ###print(lista)


###FILTRAR LISTA PARA TENER ELEMENTOS INDIVIDUALES
#ELIMINAR ESPACIOS, TABULADORES Y SALTOS DE LINEA ADICIONALES && HACER LA CADENA MINUSCULA(COMPLETA Y FUNCIONAL)
lowCaseStr = ""
for i in lista:
    element = str(i)
    strLowCase = element.lower()
    lowCaseStr += f" {strLowCase}"

###print("Cadena completa en minusculas: \n ")
###print(lowCaseStr)       #strDECADENAENMINUSC

lowerLst = lowCaseStr.split()
#####print("Lista completa en minusculas: \n ")
#####print(lowerLst)       #lstDECADENAENMINUSC


###RECORRIDO PARA EMPEZAR A TOKENIZAR
#####print("")
#####print("Cada uno de los elementos: \n")
do = 0

#TODO CAMBIAR FILTRO
''' 
for i in (range(len(lowerLst)-1) ):
    
    
    #####print(lowerLst[i])
    editLst = []
    ###TODO CODIGO PARA ORGANIZAR Y REMOVER CADENAS ERRONEAS EJ: "(3"
    
    while do < 21:
    #while len(lowerLst[i]) != 1:
       
      try:
          #CASOS DE PAREJAS DE PARENTESIS O CORCHETES EN UN MISMO ELEMENTO

          if lowerLst[i] == '()':
             editLst.append('(')
             editLst.append(')')
          elif lowerLst[i] == '{}':
             editLst.append('{')
             editLst.append('}')
          #CASOS DE PARENTESIS EN PRIMERA O ULTIMA POSICIÓN

          elif lowerLst[i][0] == '(':    #CASO ERROR EN CADENA POR PRIMER PARENTESIS APERTURA
            editLst.append('(')
            restElem = lowerLst[i][1:]
            editLst.append(restElem)
          elif lowerLst[i][0] == ')':    #CASO ERROR EN CADENA POR PRIMER PARENTESIS CLAUSURA
              editLst.append(')')
              restElem = lowerLst[i][1:]
              editLst.append(restElem)
          elif lowerLst[i][-1] == '(':    #CASO ERROR EN CADENA POR ULTIMO PARENTESIS APERTURA
              editLst.append('(')
              restElem = lowerLst[i][:-1]
              editLst.append(restElem)
          elif lowerLst[i][-1] == ')':    #CASO ERROR EN CADENA POR ULTIMO PARENTESIS CLAUSURA
              editLst.append(')')
              restElem = lowerLst[i][:-1]
              editLst.append(restElem)
          #CASOS DE CORCHETES EN PRIMERA O ULTIMA POSICIÓN

          elif lowerLst[i][0] == '{':    #CASO ERROR EN CADENA POR PRIMER CORCHETES APERTURA
            editLst.append('{')
            restElem = lowerLst[i][1:]
            editLst.append(restElem)
          elif lowerLst[i][0] == '}':    #CASO ERROR EN CADENA POR PRIMER CORCHETES CLAUSURA
              editLst.append('}')
              restElem = lowerLst[i][1:]
              editLst.append(restElem)
          elif lowerLst[i][-1] == '{':    #CASO ERROR EN CADENA POR ULTIMO CORCHETES APERTURA
              editLst.append('{')
              restElem = lowerLst[i][:-1]
              editLst.append(restElem)
          elif lowerLst[i][-1] == '}':    #CASO ERROR EN CADENA POR ULTIMO CORCHETES CLAUSURA
              editLst.append('}')
              restElem = lowerLst[i][:-1]
              editLst.append(restElem)
          #CASOS DE COMAS EN PRIMERA O ULTIMA POSICIÓN

          elif lowerLst[i][0] == ',':    #CASO ERROR EN CADENA POR PRIMER CORCHETES CLAUSURA
              editLst.append(',')
              restElem = lowerLst[i][1:]
              editLst.append(restElem)
          elif lowerLst[i][-1] == ',':    #CASO ERROR EN CADENA POR ULTIMO CORCHETES APERTURA
              editLst.append(',')
              restElem = lowerLst[i][:-1]
              editLst.append(restElem)

          #CASOS DE PUNTO Y COMA EN PRIMERA O ULTIMA POSICIÓN

          elif lowerLst[i][0] == ';':    #CASO ERROR EN CADENA POR PRIMER PUNTO Y COMA
              editLst.append(';')
              restElem = lowerLst[i][1:]
              editLst.append(restElem)
          elif lowerLst[i][-1] == ';':    #CASO ERROR EN CADENA POR ULTIMO PUNTO Y COMA
              editLst.append(';')
              restElem = lowerLst[i][:-1]
              editLst.append(restElem)
          ###TODO CASOS DE NUMERO EN PRIMERA O ÚLTIMA POSICIÓN (NUMERO DE UNA CIFRA)

          elif int(lowerLst[i][0]) % 1 == 0:    #PRIMER CHAR NUMERO EN CADENA ERRONEA
              editLst.append(lowerLst[i][0])
              restElem = lowerLst[i][1:]
              editLst.append(restElem)

          elif int(lowerLst[i][-1]) % 1 == 0:    #ULTIMO CHAR NUMERO EN CADENA ERRONEA
              editLst.append(lowerLst[i][-1])
              restElem = lowerLst[i][:-1]
              editLst.append(restElem)     
          
          do += 1   

      except:
        ###CASOS DE PARENTESIS EN MEDIO DE UN ELEMENTO (PARENTESIS ABIERTO)
        if (len(lowerLst[i]) >= 3) and ('(' in lowerLst[i]):
           chain = str(strLowCase[i])
           index = chain.find('(')
           editLst.append(chain[:index])
           editLst.append('(')
           editLst.append(chain[index +1:])

        ###CASOS DE PARENTESIS EN MEDIO DE UN ELEMENTO (PARENTESIS CERRADO)
        elif (len(lowerLst[i]) >= 3) and (')' in lowerLst[i]):
           chain = str(strLowCase[i])
           index = chain.find(')')
           editLst.append(chain[:index])
           editLst.append(')')
           editLst.append(chain[index +1:])

        ###CASOS DE CORCHETE EN MEDIO DE UN ELEMENTO (CORCHETE ABIERTO)
        elif (len(lowerLst[i]) >= 3) and ('{' in lowerLst[i]):
           chain = str(strLowCase[i])
           index = chain.find('{')
           editLst.append(chain[:index])
           editLst.append('{')
           editLst.append(chain[index +1:])

        ###CASOS DE CORCHETE EN MEDIO DE UN ELEMENTO (CORCHETE CERRADO)
        elif (len(lowerLst[i]) >= 3) and ('}' in lowerLst[i]):
           chain = str(strLowCase[i])
           index = chain.find('}')
           editLst.append(chain[:index])
           editLst.append('}')
           editLst.append(chain[index +1:])
           
        else:
          ###EN CASO DE NO CUMPLIR CON ALGUNA DE LAS ANTERIORES OPCIONES SIMPLEMENTE NO MODIFICAR NADA
           editLst.append(lowerLst[i])

#####print('LA LISTA EDITADA PARA QUE NO HAYA IRREGULARIDADES ES: \n')
#####print(editLst)
'''

############################################################################################################################
############------------------------------------LST FILTRADA ARTIFICIALMENTE------------------------------------############
############################################################################################################################

#ORIGINAL
flst = ['defvar', 'nom', '0', 'defvar', 'x', '0', 'defvar', 'y', '0', 'defvar', 'one', '0', 'defproc', 'putcb', '(', 'c', ',', 'b', ')', '{', 'drop', '(', 'c', ')', ';', 'letgo', '(', 'b', ')', ';', 'walk', '(', 'n', ')', '}', 'defproc', 'gonorth', '(', ')', '{', 'while', 'can', '(', 'walk', '(', '1', ',', 'north', ')', ')', '{', 'walk', '(', '1', ',', 'north', ')', '}', '}', 'defproc', 'gowest', '(', ')', '{', 'if', 'can','(', 'walk', '(', '1', ',', 'west', ')', ')', '{', 'walk', '(', '1', ',', 'west', ')', '}', 'else', 'nop', '(', ')', '}', '{', 'jump', '(', '3', ',', '3', ')', ';', 'putcb', '(', '2', ',', '1', ')', '}']
#TESTER
flstTester = ['defvar', 'nom', '0', 'defvar', 'x', '0', 'defvar', 'y', '0', 'defvar', 'one', '0', 'defproc', 'putcb', '(', 'nom', ',', 'one', ')', '{', 'drop', '(', 'c', ')', ';', 'letgo', '(', 'b', ')', ';', 'walk', '(', 'n', ')', '}', 'defproc', 'gonorth', '(', ')', '{', 'while', 'can', '(', 'walk', '(', '1', ',', 'north', ')', ')', '{', 'walk', '(', '1', ',', 'north', ')', '}', '}', 'defproc', 'gowest', '(', ')', '{', 'if', 'can','(', 'walk', '(', '1', ',', 'west', ')', ')', '{', 'walk', '(', '1', ',', 'west', ')', '}', 'else', 'nop', '(', ')', '}', '{', 'jump', '(', '3', ',', '3', ')', ';', 'putcb', '(', '2', ',', '1', ')', '}']
#---------------------------------------------------------------------------------------------------------------------------********-----*****-----...

DEF = ['defvar','defproc']

SIN_COMM = ['walk(#)','leap(#)','turn(DIR)', 'turnto(ORI)','drop(#)','get(#)', 'grab(#)', 'letgo(#)']       #SINGLE/SIMPLE COMMANDS - GREEN

TUP_COMM = ['jump(#,#)','walk(#, DIR)','walk(#, ORI)','leap(#,DIR)','leap(#,ORI)']       #TUPLE COMMANDS - BLUE
####jump caso puntual, puede NO tener números pero llamar el número de la variable contenida
#se puede solucionar guardando los valores en un dict y haciendo el cambio antes y luego validando si son numeros
SPE_COMM = []       #SPECIAL COMMANDS - YELLOW

ALL_COMM = SIN_COMM + TUP_COMM + SPE_COMM       #CUANDO SEA NECESARIO SOLO VERIFICAR SI ES UN COMANDO (VERIFICAR)
#north  south   east    west
CONDS = ['facing(ORI)','can(ALL_COMM)']

DIR = ['front','right','left','back']

ORI = ['north','south','east','west']

NOT_STRUC = ['not: COND']      #CONDITIONS - JUST 3 GENERAL CASES
tokenLst = []


###TODO HACER DICT CON DEFINICION DE VARIABLES DECLARADAS

#INSERTAR DICT

###TOKENIZAR defVar y defProc con sus elementos - DONE
i = 0
while i < ((len(flst))):
        
    
    if flst[i] in DEF:
        try:
            if int(flst[i+2]) % 1 == 0:
                tokenLst.append('DEFV')
                tokenLst.append(flst[i+1])
                tokenLst.append('#')
                i +=3
        except:
        
            tokenLst.append('DEFP')
            i+=1
    else:
        tokenLst.append(flst[i])
        i+=1

#print("")
#print(f"La lista original: \n{flst}\n")        
print("")
print(f"La lista cambiando palabras clave es: \n{tokenLst}")
###CREACION DE DICCIONARIO DE VARIABLES DEFINIDAS - DOME

varDict = {}

j = 0
while j < len(tokenLst):
    try:
            
        if tokenLst[j] == 'DEFV':
            varDict[tokenLst[j+1]] = tokenLst[j+2]

    except:
        continue
    j+=1


print("")
print(f"Nueva lista tokenizada: \n{tokenLst}\n")        
print("")
print(f"Diccionario con variables definidas es: \n{varDict}")

###TODO ELIMINAR DEFV CON SUS ELEMENTOS (3 ELEMENTOS TOTALES)

print("")
print(f"ANTES Lista tokenizada filtrada de DEFV: \n{tokenLst}\n")        
print("")

for i in tokenLst:
     
     if i == 'DEFV':
          
          indexP = tokenLst.index(i)
          
          print(f"ANTES DE POP token  List: {tokenLst}")
          tokenLst.pop(indexP)
          tokenLst.pop(indexP)
          tokenLst.pop(indexP)
          print(f"LUEGO DE POP token  List: {tokenLst}")


print("")
print(f"DESPUES Lista tokenizada filtrada de DEFV: \n{tokenLst}\n")        
print("")


###REEMPLAZO DE VARIABLES CON LA LISTA "TesterDeflst" - DONE
"""
varKeys = varDict.keys()

for i in tokenLst:

    if i in varKeys:

        index = tokenLst.index(i)       #SE IDENTIFICA INDICE DEL ELEMENTO ACTUAL

        value = varDict[i]      #EXTRAER VALOR DE DICCIONARIO DE VARIABLES
        tokenLst[index] = value     #CAMBIAR VALORES CON LIST INDEXING

print("")
print(f"***Nueva lista tokenizada: \n{tokenLst}\n")        
print("")
"""       









############################################################################################################################
############################################################################################################################
############-----------------------------------------------PARSER-----------------------------------------------############
############################################################################################################################
############################################################################################################################

"""

La idea principal del PARSER es verificar que los tokens esten en el orden
correcto y la sintaxis sea la correcta

"""








#HACER FUNCION PARA VERIFICAR PARENTESIS(COMPLETA Y FUNCIONAL)
ansParen = True
paren = ['(',')','[',']','{','}']
check = []
for i in lowCaseStr:
    if i in paren:
        check.append(i)     #LISTA DE 
##print("")
##print(check, len(check))
##print("")

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

##print(f"El resultado del validParen es: {ansParen}")

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