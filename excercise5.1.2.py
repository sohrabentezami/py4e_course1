count = 0
sum = 0
avg = 0
a = None

while True :
    a = input("Enter a number: ")



    if a == 'done' :
        break
    elif  a != 'done':
        try :
            b = float(a)
            count = count + 1
            sum = sum + b
        except :
            print("Invalid input")
            continue



print("count: ", count)
print("sum: ", sum)
print("average: ", sum/count)
