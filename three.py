def pal(data):
    data = data.replace('','').lower() 
    if data == data[::-1]:
        print('True')
    else: 
        print('False')
    
pal('шалаш')