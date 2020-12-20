hrs=input('total hours')
rte=input('rate per hour')
hours = float(hrs)
rate = float(rte)
sum = 0
if hours <= 40 :
 sum = hours * rate
else :
 sum = 40 * rate + (hours - 40) * 1.5 * rate

print('payment is', sum)
