cromossomo = input ("Digite o cromossomo : "). strip()
posicao = int (input("Digite a posição: "))
genoma = input ("Digite o genoma de referência: "). strip().lower()

inicio_brca1 = 41196312
fim_brca1 = 41277500

if cromossomo == "chr17" and inicio_brca1 <= posicao <= fim_brca1:
    resposta = "Sim"
else:
    resposta = "Não"

if cromossomo == "chr17":
    if genoma == "hg19" and 41196312 <= posicao <= 41277500:
        print("Sim")
    elif genoma == "hg38" and 43044295 <= posicao <= 43125483:
        print("Sim")
    else:
        print("Não")
else:
    print("Não")

 
print("\nResposta:")
print(resposta)
