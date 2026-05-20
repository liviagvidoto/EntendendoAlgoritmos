estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
estacoes = {}
estacoes["kone"] = set(["id", "nv", "ut"])
estacoes["ktwo"] = set(["wa", "id", "mt"])
estacoes["kthree"] = set(["or", "nv", "ca"])
estacoes["kfour"] = set(["nv", "ut"])
estacoes["kfive"] = set(["ca", "az"])

while estados_abranger:
    melhor_estacao = None
    estados_cobertos = set()
    for estacao, estados in estacoes.items():
        cobertos = estados_abranger & estados
        if len(cobertos) > len(estados_cobertos):
            melhor_estacao = estacao
            estados_cobertos = cobertos
    estados_abranger -= estados_cobertos

print(melhor_estacao) #kfive

