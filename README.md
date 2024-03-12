# SonarMaps

Script para ordenar uma lista de endereços por proximidade à um lugar predeterminado.

Insira o caminho relativo do arquivo com os endereços em "entrada". Dependendo da extenção pode ser preciso baixar dependencias usando o pip.

A lista ordenada será salva no arquivo "ordenado.ods". 

Altere o ponto de referência antes de rodar o código.

O Nominatim, ferramenta de geolocalização, pode confundir nomes similares de ruas em cidades diferentes.

As distâncias levam em conta linhas retas seguindo a curvatura da Terra, portanto o programa é útil para ordenar os endereços mas não para estimar as distâncias exatas.  
