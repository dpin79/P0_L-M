lst = ['defvar', 'nom', '0', 'defvar', 'x', '0', 'defvar', 'y', '0', 'defvar', 'one', '0', 'defproc', 'putcb', '(c', ',', 'b', ')', '{', 'drop(', 'c', ')', ';', 'letgo', '(', 'b', ')', ';', 'walk(', 'n', ')', '}', 'defproc', 'gonorth', '()', '{', 'while', 'can(walk(1', ',', 'north', ')', ')', '{', 'walk(1', ',', 'north', ')', '}', '}', 'defproc', 'gowest', '()', '{', 'if', 'can(walk(1', ',', 'west', ')', ')', '{', 'walk(1', ',', 'west', ')', '}', 'else', 'nop', '()', '}', '{', 'jump', '(3', ',3)', ';', 'putcb', '(2', ',1)', '}']
nLst = []
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

print(nLst)