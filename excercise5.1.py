count = 0
sum = 0
avg = 0
a = None
while a != 'done' :
    a = input("Enter a number: ")

    try :
        b = float(a)
    except :
        print("Invalid input")
        continue

    if a == 'done' :
        break
    else :
        count = count + 1
        sum = sum + b

print("count: ", count)
print("sum: ", sum)
print("average: ", sum/count)
