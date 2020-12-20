count = 0
flag = None
d = 10000
c = 0

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
        if b < d :
            d = b
        if b > c :
            c = b

print('Smallest: ' , d)
print('Biggest: ' , c)
print('count: ' , count)
