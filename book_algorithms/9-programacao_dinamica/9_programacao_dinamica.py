"A programação dinâmica é útil quando você está tentando otimizar algo em relação a um limite."
"Você pode utilizar a programação dinâmica quando o problema puder ser dividido em subproblemas discretos."
"Toda solução de programação dinâmica envolve uma tabela."
"Os valores nas células são, geralmente, o que você está tentando otimizar."
"Cada célula é um subproblema, portanto, pense em como você pode dividi-lo em outros subproblemas, pois isso lhe ajudará a descobrir quais são os seus eixos."

"Maior substring comum"
if palavra_a[i] == palavra_b[j]: 
    celula[i][j] = celula[i-1][j-1] + 1
else: 
    celula[i][j] = 0

"Maior subsequencia em comum"
if palavra_a[i] == palavra_b[j]: 
    celula[i][j] = celula[i-1][j-1] + 1
else: 
    celula[i][j] = max(celula[i-1][j], celula[i][j-1])