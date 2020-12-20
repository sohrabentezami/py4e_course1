count = 0
flag = None
c = None
d = None

while True :
    a = input("Type an integer: ")

    if a == 'done' :
        break
    elif  a != 'done':
        try :
            b = int(a)
            count = count + 1
        except :
            print("Invalid input")
            continue

        if c is None :
            c = b
        elif b < c :
            c = b


        if d is None :
            d = b
        elif b > d :
            d = b

print('Smallest: ' , d)
print('Biggest: ' , c)
print('count: ' , count)
