# Título do projeto: network_analysis_imd1155

## Descrição do projeto

O presente projeto foi criado com o objetivo de compor a nota parcial da 2º unidade da disciplina de Análise de Redes do Instituto Metrópole Digital (código 1155).

O conjunto de dados consiste em um arquivo CSV que contém o registro do valor importado e exportado entre pares de países, bem como a abreviação e identificadores únicos locais dos respectivos componentes.

A partir de tal conjunto, foi possível construir uma rede utilizando as bibliotecas networkx (para construir o grafo bidirecionado, calcular métricas e construir sub-grafos) e pyviz (para exibir o grafo completo e os sub-grafos).

Convém mencionar que para melhor visualização da rede, recomenda-se reduzir a quantidade 'k' de nós que constituem a rede (limitando-se a cerca de 40 nós para uma visualização menos poluída, embora você possa adicionar até 238 nós). Você pode ajustar o código para substituir alguns parâmetros como: quantidade 'n' de nós na rede, quantidade de 'k' nós existentes nas sub-redes (k<=n) e ano de registro dos dados (por padrão, selecionei 2023).

Ressalta-se que a seleção dos nós ocorre de forma aleatória (você acrescenta 'n' nós aleatórios dentre os 238) por meio da função 'sample(n)'. 

Por fim, cada sub-rede gera um arquivo com extensão '.html' de maneira que você poderá visualizar e interagir com a disposição dos nós e arestas do respectivo conjunto. Com tantos parâmetros, métricas e combinações diferentes de redes, você poderá treinar sua análise e obter insights valiosos no âmbito da análise de redes. Não esqueça de ir além e pesquisar outras métricas do seu interesse!

## Requisitos 

1. Faça um 'fork' do repositório
2. Cadastre-se no streamlit Cloud
3. Passe a URL de referência do arquivo 'main.py' que consta no repositório (exemplo: https://github.com/cleziojr/network_analysis_imd1155/blob/main/main.py)
