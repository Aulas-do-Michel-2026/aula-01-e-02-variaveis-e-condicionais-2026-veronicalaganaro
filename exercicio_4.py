cromossomo = input ("Digite o cromossomo : "). strip()
posição = int (input("Digite a posição: "))

inicio_brca1 = 41196312
fim_brca1 = 41277500

if cromossomo == "chr17" and inicio_brca1 <= posição <= fim_brca1:
 Resposta: "Sim"
else:
Resposta: "Não"
