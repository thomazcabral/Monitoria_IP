def criar_dict(nome):
    return {"nome": nome, "pontuacao": 0, "saldo de gols": 0, "vitorias": 0, "gols marcados": 0, "gols sofridos": 0}


torneio = input()
parar = False
times = []
dict_times = []

while not parar:
    time1 = input()
    if (time1 == "FIM"):
        parar = True
    else:
        time2 = input()

        if (time1 not in times):
            times.append(time1)
            dict_times.append(criar_dict(time1))
        if (time2 not in times):
            times.append(time2)
            dict_times.append(criar_dict(time2))
        
        index_time1 = times.index(time1)
        index_time2 = times.index(time2)
        placar_time1 = int(input())
        placar_time2 = int(input())

        if (placar_time1 > placar_time2):
            dict_times[index_time1]["pontuacao"] += 3
            dict_times[index_time1]["saldo de gols"] += (placar_time1 - placar_time2)
            dict_times[index_time1]["vitorias"] += 1
            dict_times[index_time2]["saldo de gols"] += (placar_time2 - placar_time1)
        elif (placar_time2 > placar_time1):
            dict_times[index_time2]["pontuacao"] += 3
            dict_times[index_time2]["saldo de gols"] += (placar_time2 - placar_time1)
            dict_times[index_time2]["vitorias"] += 1
            dict_times[index_time1]["saldo de gols"] += (placar_time1 - placar_time2)
        else:
            dict_times[index_time1]["pontuacao"] += 1
            dict_times[index_time2]["pontuacao"] += 1
        
        dict_times[index_time1]["gols marcados"] += placar_time1
        dict_times[index_time1]["gols sofridos"] += placar_time2
        dict_times[index_time2]["gols marcados"] += placar_time2
        dict_times[index_time2]["gols sofridos"] += placar_time1
        
        if (placar_time1 == placar_time2 == 0):
            print(f"Que partida terrível! Era melhor ter visto o filme do Pelé. Nenhum gol entre a equipe {time1} e {time2}.")
        if (placar_time1 - placar_time2 >= 3):
            print(f"Que jogo animado! Menos para a equipe {time2}, que foi amassada pela equipe {time1}.")
        if (placar_time2 - placar_time1 >= 3):
            print(f"Que jogo animado! Menos para a equipe {time1}, que foi amassada pela equipe {time2}.")
        if (placar_time1 + placar_time2 < 2):
            print("Que sono... Nem consegui ver o jogo direito.")
        if (placar_time1 + placar_time2 > 4):
            print("É GOL QUE NÃO ACABA MAIS!!! Que jogo maravilhoso entre as equipes!")

copia_defesa = dict_times.copy()
copia_defesa_sorted = sorted(copia_defesa, key=lambda x: (x["gols sofridos"], x["nome"]))
print(f"Melhor defesa: {copia_defesa_sorted[0]['nome']}")

copia_ataque = dict_times.copy()
copia_ataque_sorted = sorted(copia_ataque, key=lambda x: (-x["gols marcados"], x["nome"]))
print(f"Melhor ataque: {copia_ataque_sorted[0]['nome']}")

copia_classificacao = dict_times.copy()
copia_classificacao_sorted = sorted(copia_classificacao, key=lambda x: (-x["pontuacao"], -x["saldo de gols"], -x["vitorias"], x["nome"]))
print(f"Classificação do torneio {torneio}:")
print("Time    Pontos    Saldo de gols")
for i in range(len(copia_classificacao_sorted)):
    print(f"{i+1}.{copia_classificacao_sorted[i]['nome']}     {copia_classificacao_sorted[i]['pontuacao']}     {copia_classificacao_sorted[i]['saldo de gols']}")
print(f"O grande vencedor da competição foi: {copia_classificacao_sorted[0]['nome']}")
