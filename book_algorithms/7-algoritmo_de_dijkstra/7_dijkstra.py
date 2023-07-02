"Algoritmo de Dijkstra: é um dos algoritmos que calcula o caminho de custo mínimo entre vértices de um grafo. Escolhido um vértice como raiz da busca, este algoritmo calcula o custo mínimo deste vértice para todos os demais vértices do grafo. Ele é bastante simples e com um bom nível de performance."

"O algoritmo de Dijkstra é usado para calcular o caminho mínimo para um grafo ponderado."
"O algoritmo de Dijkstra funciona quando todos os pesos são positivos."
"Se o seu grafo tiver pesos negativos, use o algoritmo de Bellman-Ford."


"Implementacao de Dijkstra"
grafo = {}
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2
grafo["a"] = {}
grafo["a"]["fim"] = 1
grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5
grafo["fim"] = {}

custos = {}
infinito = float("inf")
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []

def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")          #custo infinito
    nodo_custo_mais_baixo = None
    for nodo in custos:             #Vá por cada vértice.
        custo = custos[nodo]
        if custo<custo_mais_baixo and nodo not in processados: #Se for o vértice de menor custo até o momento e ainda não tiver sido processado
            custo_mais_baixo = custo      #atribua como o novo vértice de menor custo.
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo


nodo = ache_no_custo_mais_baixo(custos) #Encontra o custo mais baixo que ainda não foi processado.
while nodo is not None:     #Caso todos os vértices tenham sido processados, esse laço while será finalizado.
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys(): #Percorre todos os vizinhos desse vértice.
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:  #Caso seja mais barato chegar a um vizinho a partir desse vértice...
            custos[n] = novo_custo   #atualiza o custo dele.
            pais[n] = nodo    #Esse vértice se torna o novo pai para o vizinho.
    processados.append(nodo)  #Marca o vértice como processado.
    nodo = ache_no_custo_mais_baixo(custos)  #Encontra o próximo vértice a ser processado e o algoritmo é repetido.


print(custos["fim"])
print(pais["fim"])
print("__________________")
print(grafo)
print(pais)
print(custos)