lst = ['defvar', 'nom', '0', 'defvar', 'x', '0', 'defvar', 'y', '0', 'defvar', 'one', '0', 'defproc', 'putcb', '(c', ',', 'b', ')', '{', 'drop(', 'c', ')', ';', 'letgo', '(', 'b', ')', ';', 'walk(', 'n', ')', '}', 'defproc', 'gonorth', '()', '{', 'while', 'can(walk(1', ',', 'north', ')', ')', '{', 'walk(1', ',', 'north', ')', '}', '}', 'defproc', 'gowest', '()', '{', 'if', 'can(walk(1', ',', 'west', ')', ')', '{', 'walk(1', ',', 'west', ')', '}', 'else', 'nop', '()', '}', '{', 'jump', '(3', ',3)', ';', 'putcb', '(2', ',1)', '}']
Tlst = ['3)','0','def']
nLst = []
for i in range(0,len(lst)):
    print(f'Indice: {i}')
    print(lst[i])
    if len(lst[i]) == 1:
            nLst.append(lst[i])
    try:
        print('')
        if int(lst[i][0]) % 1 == 0 and len(lst[i]) != 1:
                nLst.append(lst[i][0])
                restElem = lst[i][1:]
                nLst.append(restElem)
    except:
        
        if (lst[i]).isdigit() == False:
            nLst.append(lst[i])
    print(nLst)

#print(nLst)

#print(lst[2])

#print((lst[2]).isdigit())