testLst = ['defvar', 'nom', '0', 'defvar', 'x', '0', 'defvar', 'y', '0', 'defvar', 'one', '0', 'defproc', 'putcb', '(c', ',', 'b', ')', '{', 'drop(', 'c', ')', ';', 'letgo', '(', 'b', ')', ';', 'walk(', 'n', ')', '}', 'defproc', 'gonorth', '()', '{', 'while', 'can(walk(1', ',', 'north', ')', ')', '{', 'walk(1', ',', 'north', ')', '}', '}', 'defproc', 'gowest', '()', '{', 'if', 'can(walk(1', ',', 'west', ')', ')', '{', 'walk(1', ',', 'west', ')', '}', 'else', 'nop', '()', '}', '{', 'jump', '(3', ',3)', ';', 'putcb', '(2', ',1)', '}']

###RECORRIDO PARA EMPEZAR A TOKENIZAR
print("")
print("Cada uno de los elementos: \n")
do = 0

while do != 2:
        
        for i in (range(0,len(testLst)-1) ):
            
            element = testLst[i]
            print(f'Elemento actual: {element}')

            editLst = []
            ###TODO CODIGO PARA ORGANIZAR Y REMOVER CADENAS ERRONEAS EJ: "(3"
            
            try:

                if len(element) == 1:
                    editLst.append(element)


                ###TODO CASOS DE NUMERO EN PRIMERA O ÚLTIMA POSICIÓN (NUMERO DE UNA CIFRA)

                elif int(element[0]) % 1 == 0:    #PRIMER CHAR NUMERO EN CADENA ERRONEA
                    editLst.append(element[0])
                    restElem = element[1:]
                    editLst.append(restElem)

                elif int(element[-1]) % 1 == 0:    #ULTIMO CHAR NUMERO EN CADENA ERRONEA
                    editLst.append(element[-1])
                    restElem = element[:-1]
                    editLst.append(restElem)
            except:
                    

                
                #CASOS DE PAREJAS DE PARENTESIS O CORCHETES EN UN MISMO ELEMENTO


                if element == '()':
                    editLst.append('(')
                    editLst.append(')')
                elif element == '{}':
                    editLst.append('{')
                    editLst.append('}')
                #CASOS DE PARENTESIS EN PRIMERA O ULTIMA POSICIÓN

                elif element[0] == '(':    #CASO ERROR EN CADENA POR PRIMER PARENTESIS APERTURA
                    editLst.append('(')
                    restElem = element[1:]
                    editLst.append(restElem)
                elif element[0] == ')':    #CASO ERROR EN CADENA POR PRIMER PARENTESIS CLAUSURA
                    editLst.append(')')
                    restElem = element[1:]
                    editLst.append(restElem)
                elif element[-1] == '(':    #CASO ERROR EN CADENA POR ULTIMO PARENTESIS APERTURA
                    editLst.append('(')
                    restElem = element[:-1]
                    editLst.append(restElem)
                elif element[-1] == ')':    #CASO ERROR EN CADENA POR ULTIMO PARENTESIS CLAUSURA
                    editLst.append(')')
                    restElem = element[:-1]
                    editLst.append(restElem)
                #CASOS DE CORCHETES EN PRIMERA O ULTIMA POSICIÓN

                elif element[0] == '{':    #CASO ERROR EN CADENA POR PRIMER CORCHETES APERTURA
                    editLst.append('{')
                    restElem = element[1:]
                    editLst.append(restElem)
                elif element[0] == '}':    #CASO ERROR EN CADENA POR PRIMER CORCHETES CLAUSURA
                    editLst.append('}')
                    restElem = element[1:]
                    editLst.append(restElem)
                elif element[-1] == '{':    #CASO ERROR EN CADENA POR ULTIMO CORCHETES APERTURA
                    editLst.append('{')
                    restElem = element[:-1]
                    editLst.append(restElem)
                elif element[-1] == '}':    #CASO ERROR EN CADENA POR ULTIMO CORCHETES CLAUSURA
                    editLst.append('}')
                    restElem = element[:-1]
                    editLst.append(restElem)
                #CASOS DE COMAS EN PRIMERA O ULTIMA POSICIÓN

                elif element[0] == ',':    #CASO ERROR EN CADENA POR PRIMER CORCHETES CLAUSURA
                    editLst.append(',')
                    restElem = element[1:]
                    editLst.append(restElem)
                elif element[-1] == ',':    #CASO ERROR EN CADENA POR ULTIMO CORCHETES APERTURA
                    editLst.append(',')
                    restElem = element[:-1]
                    editLst.append(restElem)

                #CASOS DE PUNTO Y COMA EN PRIMERA O ULTIMA POSICIÓN

                elif element[0] == ';':    #CASO ERROR EN CADENA POR PRIMER PUNTO Y COMA
                    editLst.append(';')
                    restElem = element[1:]
                    editLst.append(restElem)
                elif element[-1] == ';':    #CASO ERROR EN CADENA POR ULTIMO PUNTO Y COMA
                    editLst.append(';')
                    restElem = element[:-1]
                    editLst.append(restElem)

                    
                
                    

            
                ###CASOS DE PARENTESIS EN MEDIO DE UN ELEMENTO (PARENTESIS ABIERTO)
                #if (len(element) >= 3) and ('(' in element):
                elif (len(element) >= 3) and ('(' in element):
                    chain = str(element)
                    index = chain.find('(')
                    editLst.append(chain[:index])
                    editLst.append('(')
                    editLst.append(chain[index +1:])

                ###CASOS DE PARENTESIS EN MEDIO DE UN ELEMENTO (PARENTESIS CERRADO)
                elif (len(element) >= 3) and (')' in element):
                    chain = str(element)
                    index = chain.find(')')
                    editLst.append(chain[:index])
                    editLst.append(')')
                    editLst.append(chain[index +1:])

                ###CASOS DE CORCHETE EN MEDIO DE UN ELEMENTO (CORCHETE ABIERTO)
                elif (len(element) >= 3) and ('{' in element):
                    chain = str(element)
                    index = chain.find('{')
                    editLst.append(chain[:index])
                    editLst.append('{')
                    editLst.append(chain[index +1:])

                ###CASOS DE CORCHETE EN MEDIO DE UN ELEMENTO (CORCHETE CERRADO)
                elif (len(element) >= 3) and ('}' in element):
                    chain = str(element)
                    index = chain.find('}')
                    editLst.append(chain[:index])
                    editLst.append('}')
                    editLst.append(chain[index +1:])
                
                else:
                ###EN CASO DE NO CUMPLIR CON ALGUNA DE LAS ANTERIORES OPCIONES SIMPLEMENTE NO MODIFICAR NADA
                    editLst.append(element)
        print(f'Lista convertida: {editLst}')
        do+=1

print('')
print('LA LISTA EDITADA PARA QUE NO HAYA IRREGULARIDADES ES: \n')
print(editLst)