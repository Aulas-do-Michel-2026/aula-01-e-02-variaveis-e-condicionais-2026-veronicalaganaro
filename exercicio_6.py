pais = input("Qual país você vai viajar? ")

if pais == "Estados Unidos":
    reais = float(input("Quantos reais você quer converter? "))
    valor = reais /5
    print(f"{valor:.2f} USD")
    
elif pais == "Argentina":
    reais = float(input("Quantos reais você quer converter? "))
    valor = reais * 180
    print(f"{valor:.2f} ARS")
    
elif pais == "Japão":
    reais = float(input("Quantos reais você quer converter? "))
    valor = reais * 30
    print(f"{valor:.2f} JPY")
    
else:
    print("Não temos essa moeda em caixa.")
