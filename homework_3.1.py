
chislo_1=float(input('pervoe chislo:'))
chislo_2=float(input('vtoroe chislo:'))
deystvie=input('vvedi znak:')
if deystvie=='+':
    resultat=chislo_1+chislo_2
elif deystvie=='-':
    resultat=chislo_1-chislo_2
elif deystvie=='*':
    resultat=chislo_1*chislo_2
elif deystvie== '/':
    if chislo_2==0 :
        print('nelza delit na nol')
    else:resultat=chislo_1/chislo_2
print('resultat:', resultat)