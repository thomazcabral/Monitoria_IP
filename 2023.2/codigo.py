def negativou(infos, pessoa):
    if(infos[pessoa]["pontuacao"] < 0):
        print(f"{pessoa} ficou negativo!!! Bora que dá pra melhorar.")
        infos[pessoa]["pontuacao"] = 0


pessoa = int(input())
infos = {}

for i in range(pessoa):
    entrada = input().split(" -> ") # [{nome_pessoa}, {nome_mascara}: {cor_mascara}]
    entrada[1] = entrada[1].split(": ") # [{nome_pessoa}, [{nome_mascara}, {cor_mascara}]]
    infos[entrada[0]] = {"nome": entrada[0], "pontuacao": 0, "mascara": entrada[1][0], "cor": entrada[1][1], "nivel": 0, "trocas": 0} # nome e pontuação são fixos

max_trocas = int(input())

troca = ""
condicao = True
while(condicao):
    linha = input()

    if(linha == "FIM"):
        condicao = False

    elif("<->" in linha):
        linha = linha.split(" <-> ") # [pessoa1, pessoa2]
        if(linha[0] in infos.keys() and linha[1] in infos.keys()): # checa se as pessoas existem
            excedentes = []
            for i in range(2):
                if(infos[linha[i]]["trocas"] == max_trocas):
                    excedentes.append(linha[i])
            if(len(excedentes) != 0):
                excedentes.sort() # para printar o nome da máscara da 1ª pessoa alfabeticamente
                print(f"Eita, amigo, tas preso com a {infos[excedentes[0]]['mascara']}, visse? Pode trocar mais ela não.")
            else:
                if(infos[linha[0]]["nivel"] > infos[linha[1]]["nivel"]): # verifica a qualidade da troca e se a pontuação deve ser alterada
                    infos[linha[1]]["pontuacao"] += 2
                    infos[linha[0]]["pontuacao"] -= 1
                elif(infos[linha[0]]["nivel"] < infos[linha[1]]["nivel"]):
                    infos[linha[0]]["pontuacao"] += 2
                    infos[linha[1]]["pontuacao"] -= 1
                mascara, cor, nivel, trocas = infos[linha[0]]["mascara"], infos[linha[0]]["cor"], infos[linha[0]]["nivel"], infos[linha[0]]["trocas"] # criação de variáveis temporárias 
                for atributo in ["mascara", "cor", "nivel", "trocas"]: # iterando sobre essa lista para evitar repetição de código
                    infos[linha[0]][atributo] = infos[linha[1]][atributo]
                infos[linha[1]]["mascara"] = mascara
                infos[linha[1]]["cor"] = cor
                infos[linha[1]]["nivel"] = nivel
                infos[linha[1]]["trocas"] = trocas
                infos[linha[0]]["nivel"] += 1
                infos[linha[1]]["nivel"] += 1
                infos[linha[0]]["trocas"] += 1
                infos[linha[1]]["trocas"] += 1
                negativou(infos, linha[0]) # sempre verificar se a pontuação de alguém está negativa
                negativou(infos, linha[1])
        else:
            print("Esse cara aí não existe não…") # printar caso a pessoa não exista
 
    elif("Chuva de máscaras" in linha):
        linha = linha.split(" -> ") # [Evento especial!!! Chuva de máscaras, {nome_mascara_especial}: {nivel_mascara_especial}]
        linha[1] = linha[1].split(": ") # [Evento especial!!! Chuva de máscaras, [{nome_mascara_especial}, {nivel_mascara_especial}]]
        beneficiados = []
        for pessoa in infos.keys():
            if(infos[pessoa]["nivel"] % 2 == 1 and infos[pessoa]["nivel"] <= int(linha[1][1])): # verificar se é possível a troca
                infos[pessoa]["nivel"] = int(linha[1][1])
                infos[pessoa]["mascara"] = linha[1][0]
                infos[pessoa]["trocas"] = 1 # como é uma nova máscara, temos que resetar as trocas para 1, já que essa substituição também conta como troca
                beneficiados.append(pessoa)
        if(len(beneficiados) == 0):
            print("Vixe... Serviu pra nada o evento Chuva de máscaras :/")
        elif(len(beneficiados) == 1):
            print(f"Apenas {beneficiados[0]} é que aproveitou mesmo o evento Chuva de máscaras.") # difícil ou impossível de acontecer
        else:
            print(f"Arretaaado demais!! Teve um evento maneiro aqui e {', '.join(beneficiados)} foram beneficiados.")
    elif("?" in linha):
        linha = linha.split("cor ") # [Temos máscaras de cor, {cor_mascara}?]
        linha[1] = linha[1].split("?") # [Temos máscaras de cor, [{cor_mascara}, ""]]
        pessoas_cor = 0
        for pessoa in infos.keys():
            if(infos[pessoa]["cor"] == linha[1][0]):
                pessoas_cor += 1
        print(f"Um total de {pessoas_cor} pessoa(s) está(o) com máscara de cor {linha[1][0]}!")
        

for pessoa in infos.keys():
    infos[pessoa]["pontuacao"] = infos[pessoa]["pontuacao"] + infos[pessoa]["nivel"] * 3 # cálculo dos pontos a serem contabilizados no final

infos_sort = sorted(infos.keys()) # sortar em ordem alfabética
print("Agora é hora de ver quem ficou com que máscara!")
for pessoa in infos_sort:
    print(f"{infos[pessoa]['nome']} -> {infos[pessoa]['mascara']}: {infos[pessoa]['nivel']}")

infos_sort_2 = sorted(infos.items(), key=lambda x: (-x[1]["pontuacao"], -x[1]["nivel"], x[1]["nome"])) # sortar com base nos seguintes critérios: maior pontuação, maior nível e ordem alfabética
print(f"O grande vencedor dessa competição foi {infos_sort_2[0][1]['nome']} com {infos_sort_2[0][1]['pontuacao']} pontos!!! Com uma diferença de {(infos_sort_2[0][1]['pontuacao'] - infos_sort_2[1][1]['pontuacao'])} ponto(s) do segundo colocado.")
print("Troca de máscaras encerrada! Esperamos que todos tenham se divertido!") # fim do programa
