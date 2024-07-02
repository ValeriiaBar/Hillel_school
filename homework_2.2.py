
abcde=int(input('vvedi tseloe polozhutelnoe chislo:'))
if abcde <= 0:
    print('pozhaluysta,vvedi tseloe polozhutelnoe chislo:')

#x=10
#digit=abcde
#abcd,e=divmod(digit,x) one more way to do this task
e=(abcde%10)
d=(abcde%100)//10
c=((abcde%1000)//100)
b=((abcde%10000)//1000)
a=(abcde//10000)

print(e, d, c, b, a)