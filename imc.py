nome= (input('Digite seu nome:'))
altura= int(input('Digite sua altura em centimetros:'))
peso= float(input('Digite seu peso')) 

converteralturaparametros= altura/100

IMC=peso/altura*altura

if  IMC <=18.5:
    classificacao= 'abaixo do peso'
elif IMC <=18.6 and <=24.9:
    classificacao= 'peso ideal'
elif IMC <=29.9:
    classificacao= 'Sobre peso'   
elif 