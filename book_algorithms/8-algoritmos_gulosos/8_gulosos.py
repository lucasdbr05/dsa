"Algoritmo guloso ou míope é técnica de projeto de algoritmos que tenta resolver o problema fazendo a escolha localmente ótima em cada fase com a esperança de encontrar um ótimo global."
"Algoritmos gulosos otimizam localmente na esperança de acabar em uma otimização global."
"Problemas NP-completo não têm uma solução rápida."
"Se você estiver tentando resolver um problema NP-completo, o melhor a fazer é usar um algoritmo de aproximação."
"Algoritmos gulosos são fáceis de escrever e têm tempo de execução baixo, portanto eles são bons algoritmos de aproximação."


"Aplicacao: cobertura de conjuntos"
estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut","ca","az"])
estacoes = {}
estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "id", "mt"])
estacoes["ktres"] = set(["or", "nv", "ca"])
estacoes["kquatro"] = set(["nv", "ut"])
estacoes["kcinco"] = set(["ca", "az"])

estacoes_final = set()
estacoes_final_list = list()
while estados_abranger:    #enquanto hoiuver estados sem cobertura
    estados_cobertos = set()
    melhor_estacao = None
    for estacao, estados in estacoes.items():
        cobertos = estados_abranger & estados   #cobertos : uniao dos conjuntos estados_abranger e estados_por_estacao
        if len(cobertos) > len(estados_cobertos): 
            melhor_estacao = estacao
            estados_cobertos = cobertos
    estados_abranger -= estados_cobertos  # retira de estados_abranger os elementos que serao cobertos pela proxima melho_estacao
    estacoes_final.add(melhor_estacao)
    estacoes_final_list.append(melhor_estacao)
print(estacoes_final)
print(estacoes_final_list)

