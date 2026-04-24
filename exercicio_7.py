freq_pop = float(input("Digite a frequencia populacional (em porcentagem): "))
gene = input("Digite o gene: ")
impacto = input("Digite a Impacto (ALTO ou BAIXO): ")
reads = int(input("Digite os reads: "))
vaf = float(input("Digite a frequencia alélica (em porcentagem): "))

if reads < 10 or vaf < 20:
    print("Não é relevante.")

else:
    if impacto != "ALTO":
        print("Não é relevante.")

    else:
        genes_excecao = ["HFE", "MEFV", "GJB2"]

        if freq_pop > 5 and gene not in genes_excecao:
            print("Não é relevante.")
        else:
            print("É relevante.")
