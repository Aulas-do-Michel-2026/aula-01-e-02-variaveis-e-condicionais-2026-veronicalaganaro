cromossomo = input ("Digite o cromossomo : "). strip()
posicao = int (input("Digite a posição: "))

inicio_brca1 = 41196312
fim_brca1 = 41277500

if cromossomo == "chr17" and inicio_brca1 <= posicao <= fim_brca1:
    resposta = "Sim"
else:
    resposta = "Não"
 
print("\nResposta:")
print(resposta)
