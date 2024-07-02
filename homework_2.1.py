
chislo=int(input('vvedi chetyrehznachnoe chislo:'))
x=1000
digit=chislo
left,right=divmod(digit,x)
print(left)

second=(chislo%1000)//100
print(second)

third=(chislo%100)//10
print(third)

x=10
digit=chislo
left,right=divmod(digit,x)
print(right)
