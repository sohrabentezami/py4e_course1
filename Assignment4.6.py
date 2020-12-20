

hrs=input('Enter Hours: ')
try :
  hours = float(hrs)
except :
  print('Error, please enter numeric point')
  quit()

rte=input('Enter Rate: ')
try :
  rate = float(rte)
except :
  print('Error, please enter numeric point')
  quit()

def computepay(a,b) :
    sum = 0
    if a <= 40 :
        sum = a * b
        return sum
    else :
        sum = 40 * b + (a - 40) * 1.5 * b
        return sum

print("payment is ", computepay(hours,rate))
