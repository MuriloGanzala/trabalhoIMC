# Solicitar informações ao usuário
nome = input("Qual é o seu nome? ")
altura = float(input("Qual é a sua altura em centímetros? "))
peso = float(input("Qual é o seu peso em quilogramas? "))

altura_m= altura/100

formula= peso/ (altura_m**2)

if formula <= 18.5:
    print(F'{nome},seu IMC é{formula} você está Abaixo do Peso (Pegue suplementos do Cariani)')
elif formula >= 18.6 and formula <= 24.9:
    print(f'{nome},o seu IMC é {formula} você está com o  Peso Ideal (Para Bens)')
elif formula >= 25.0 and formula <=29.9:
    print(f'{nome},o seu IMC é {formula} você esta com  Sobrepeso')
elif formula >= 30.0 and formula <= 34.9:
    print(f'{nome},o seu IMC é {formula} você está com Obesidade Grau 1')
elif formula >= 35.0 and formula <= 39.9:
    print(f'{nome},o seu IMC é {formula} você está com  Obesidade Grau 2')
else:
    print(f'{nome},o seu IMC é {formula} você está com Obesidade Grau 3 (Dr. Nowzaradan te espera)')
