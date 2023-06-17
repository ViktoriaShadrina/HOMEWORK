x = str(input())

def pal():
    wor = list(x)
    print(wor)
    
    rev = []
    index = len(x)
    while index > 0:
        rev += x[index -1]
        index = index -1
        print(rev)

    if wor == rev:
        print('True')
    else:
        print('False')

pal()
