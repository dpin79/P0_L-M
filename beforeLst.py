flst = ['defvar', 'nom', '0', 'defvar', 'x', '0', 'defvar', 'y', '0', 'defvar', 'one', '0', 'defproc', 'putcb', '(', 'c', ',', 'b', ')', '{', 'drop', '(', 'c', ')', ';', 'letgo', '(', 'b', ')', ';', 'walk', '(', 'n', ')', '}', 'defproc', 'gonorth', '(', ')', '{', 'while', 'can', '(', 'walk', '(', '1', ',', 'north', ')', ')', '{', 'walk', '(', '1', ',', 'north', ')', '}', '}', 'defproc', 'gowest', '(', ')', '{', 'if', 'can','(', 'walk', '(', '1', ',', 'west', ')', ')', '{', 'walk', '(', '1', ',', 'west', ')', '}', 'else', 'nop', '(', ')', '}', '{', 'jump', '(', '3', ',', '3', ')', ';', 'putcb', '(', '2', ',', '1', ')', '}']

TesterDeflst = ['defvar', 'nom', '0', 'defvar', 'x', '0', 'defvar', 'y', '0', 'defvar', 'one', '0', 'defproc', 'putcb', '(', 'nom', ',', 'one', ')', '{', 'drop', '(', 'c', ')', ';', 'letgo', '(', 'b', ')', ';', 'walk', '(', 'n', ')', '}', 'defproc', 'gonorth', '(', ')', '{', 'while', 'can', '(', 'walk', '(', '1', ',', 'north', ')', ')', '{', 'walk', '(', '1', ',', 'north', ')', '}', '}', 'defproc', 'gowest', '(', ')', '{', 'if', 'can','(', 'walk', '(', '1', ',', 'west', ')', ')', '{', 'walk', '(', '1', ',', 'west', ')', '}', 'else', 'nop', '(', ')', '}', '{', 'jump', '(', '3', ',', '3', ')', ';', 'putcb', '(', '2', ',', '1', ')', '}']
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

###TOKENIZAR defVar y defProc con sus elementos
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
###CREACION DE DICCIONARIO DE VARIABLES DEFINIDAS

varDict = {}

j = 0
while j < len(tokenLst):
    try:
            
        if tokenLst[j] == 'DEFV':
            varDict[tokenLst[j+1]] = tokenLst[j+2]
            #tokenLst.pop(j)
            #tokenLst.pop(j+1)
            #tokenLst.pop(j+2)

    except:
        continue
    j+=1


print("")
print(f"Nueva lista tokenizada: \n{tokenLst}\n")        
print("")
print(f"Diccionario con variables definidas es: \n{varDict}")

###HACER EL REEMPLAZO DE VARIABLES CON LA LISTA "TesterDeflst"

#INSERT CODE
    

