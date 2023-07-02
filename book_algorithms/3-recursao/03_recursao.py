"Quando você escreve uma função recursiva, deve informar quando a recursão deve parar. É por isso que toda função recursiva tem duas partes: o caso-base e o caso recursivo."

def regressiva(i):
    print(i)
    if i <= 1: 
        return
    else: 
        regressiva(i-1)

regressiva(10)

"______Pilha de Chamada______"
def sauda(nome):
    print("Olá, " + nome + "!")
    sauda2(nome)
    print("preparando para dizer tchau...")
    tchau()
def sauda2(nome):
    print("Como vai, " + nome + "?")
def tchau():
    print("ok, tchau!")

sauda("Lucas")


"______Pilha de Chamada com recursividade______"
"Utilizar a pilha é conveniente porque você não precisa acompanhar todos os dados - a pilha faz isso para você. Usar a pilha é bom, porém, existe um custo: salvar toda essa informação pode ocupar muita memória."
"Uma pilha tem duas operações: push e pop."
"A pilha é uma estrutura de dados LIFO (Last In, First Out)"
"Todas as chamadas de função vão para a pilha de chamada."
"A pilha de chamada pode ficar muito grande e ocupar muita memória."

def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)

print(fat(10))