def pal(string):
    foo = str(string)
    if foo[::-1].startswith(foo):
        print('True')
    else:
        print('False')
    
pal("шалаш")