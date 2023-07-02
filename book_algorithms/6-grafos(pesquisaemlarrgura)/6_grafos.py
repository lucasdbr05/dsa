"Um modelo de grafo é um conjunto de conexões."
"A fila é uma estrutura de dados FIFO (First In, First Out)"
"A pesquisa em largura lhe diz se há um caminho de A para B."
"Em grafos, cada vértice é conectado aos vértices vizinhos.(usando tabelas hash)"
"Todos os algoritmos de grafos podem ser feitos por meio de programação linear. A programação linear é um framework muito mais geral, enquanto o problema de grafos é apenas um subconjunto dela."

grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []
print(grafo)

"Cada vez que você precisar verificar alguém, procure não verificá-lo novamente. Caso contrário, poderá acabar em um loop infinito."

from collections import deque
def fila(grafo):
    fila_de_pesquisa = deque() #DOUBLE ENDED QUEUE
    verificadas = []
    fila_de_pesquisa += grafo["voce"]
    while fila_de_pesquisa: 
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa): 
                print(pessoa + " é um vendedor de manga!" )
                return True
        else:
            verificadas.append(pessoa)
            fila_de_pesquisa += grafo[pessoa] 

    return False

def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'

print(fila(grafo))
"Tempo de execucao= O(numero de pessoas + numero de estradas entre pessoas) = O(vertices+arestas)"