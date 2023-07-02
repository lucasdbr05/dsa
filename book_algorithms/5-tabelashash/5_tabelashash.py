"Uma função hash é uma função na qual você insere uma string e, depois disso, a função retorna um número."
"Elas também são conhecidas como mapas hash, mapas, dicionários e tabelas de dispersão. Além disso, as tabelas hash são muito rápidas!"

"Tabela hash de votos"
voted = {}
def verifica_eleitor(nome):
    if voted.get(nome):
        print("Mande embora!")
    else:
        voted[nome] = True
        print("Deixe votar!")
verifica_eleitor("Lucas")
verifica_eleitor("Lucas")

"Tabela hash de chaching de web sites"
cache = {}
def pega_pagina(url):
    if cache.get(url):
        return cache[url] 
    else:
        dados = pega_dados_do_servidor(url)
        cache[url] = dados 
        return dados
def pega_dados_do_servidor(url):
    return url
"Para evitar colisões(um valor ser sobrescrito por outro de maneira indesejada) são necessários um baixo fator de carga;uma boa função hash."