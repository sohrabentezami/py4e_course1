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

sum = 0
if hours <= 40 :
 sum = hours * rate
else :
 sum = 40 * rate + (hours - 40) * 1.5 * rate

print('payment is', sum)
