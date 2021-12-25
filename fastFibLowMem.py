def commaNumber(num):
    'This function takes a numeric type (int/float) and returns a striing representation with commas seperating groups of three digits starting with the ones, tens, and hundreds place in the first (right-most) group'
    fullNumberStr = str(num)
    strList = []
    numList = fullNumberStr.split('.')
    intStr = numList[0]
    while len(intStr) > 0:
        strList.append(intStr[-3:]) # Builds a list with groups of three digits on the lhs of the .
        intStr = intStr[:-3]
    fStr = ''
    for i in range(len(strList)):
        fStr += strList.pop()
        if len(strList) > 0:
            fStr += ','
    for elem in numList[1:]:
        fStr += '.' + elem # Adds the rhs of the . to the string
    return fStr

def sayName(num):
    if not num:
        return '0'
    name = ''
    cStr = commaNumber(num)
    cLst = cStr.split(',')
    significance = ['Centitillion','Novenonagintatillion','Octononagintatillion','Septenonagintatillion','Senonagintatillion','Quinquanonagintatillion','Quattuornonagintatillion','Trenonagintatillion','Duononagintatillion','Unonagintatillion','Nonagintatillion','Noveoctogintatillion','Octoctogintatillion','Septeoctogintatillion','Seoctogintatillion','Quinquaoctogintatillion','Quattuoroctogintatillion','Treoctogintatillion','Duoctogintatillion','Unoctogintatillion','Octogintatillion','Noveseptuagintatillion','Octoseptuagintatillion','Septeseptuagintatillion','Seseptuagintatillion','Quinquaseptuagintatillion','Quattuorseptuagintatillion','Treseptuagintatillion','Duoseptuagintatillion','Unseptuagintatillion','Septuagintatillion','Novesexagintatillion','Octosexagintatillion','Septesexagintatillion','Sesexagintatillion','Quinquasexagintatillion','Quattuorsexagintatillion','Tresexagintatillion','Duosexagintatillion','Unsexagintatillion','Sexagintatillion','Sexagintatillion','Novequinquagintatillion','Octoquinquagintatillion','Septequinquagintatillion','Sequinquagintatillion','Quinquaquinquagintatillion','Quattuorquinquagintatillion','Trequinquagintatillion','Duoquinquagintatillion','Unquinquagintatillion','Quinquagintatillion','Novequadragintatillion','Octoquadragintatillion','Septequadragintatillion','Sequadragintatillion','Quinquaquadragintatillion','Quattuorquadragintatillion','Trequadragintatillion','Duoquadragintatillion','Unquadragintatillion','Quadragintatillion','Novetrigintatillion','Octotrigintatillion','Septetrigintatillion','Setrigintatillion','Quinquatrigintatillion','Quattuortrigintatillion','Tretrigintatillion','Duotrigintatillion','Untrigintatillion','Trigintatillion','Novevigintilion','Octovigintilion','Septevigintilion','Sevigintilion','Quinquavigintilion','Quattuorvigintilion','Trevigintilion','Duovigintilion','Unvigintilion','Vigintillion','Novemdecillion','Octodecillion','Septendecillion','Sexdecillion','Quindecillion','Quattuordecillion','Tredecillion','Duodecillion','Undecillion','Decillion','Nonillion','Octillion','Septillion','Sextillion','Quintillion','Quadrillion','Trillion','Billion','Million','Thousand','']
    while len(cLst) and len(significance):
        if '.' not in cLst[-1]:
            group = int(cLst.pop())
            if group:
                name = ' ' + significance.pop() + ' ' + name
                name = str(group) + name
            else:
                significance.pop()
        else:
            name = ' ' + significance.pop() + ' ' + name
            name = cLst.pop() + name
    while cLst:
        name = cLst.pop() + ',' + name
    return name

cn = commaNumber
sn = sayName

def fastFibPrint():
    print('\nDglass\' Fancy Fast Low Memory Fibinacci Generator\nThis program displays each fibinacci number\nBoth as a comma seperated number\nAnd as a spoken english word\nThe Format is:\n\nfib(index): Comma Seperated Number\nSpoken English Word\n\nPress enter to see the next fibinacci number\nType \'exit\' to quit\n')
    ui = input('>>> ')
    if ui.lower() == 'exit':
        return
    print(f'fib(0): 0\n0')
    stlast = 0
    ui = input('>>> ')
    if ui.lower() == 'exit':
        return
    print(f'fib(1): 1\n1')
    last = 1
    ui = input('>>> ')
    if ui.lower() == 'exit':
        return
    i = 2
    while True:
        total = last + stlast
        print(f'fib({cn(i)}): {cn(total)}\n{sn(total)}')
        ui = input('>>> ')
        if ui.lower() == 'exit':
            return
        stlast = last
        last = total
        i += 1

fastFibPrint()

