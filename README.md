# Recomendar os top 10 produtos mais vendidos, a partir da categoria de um produto de interesse
O projeto de recomendação foi desenvolvido para recomendar os top 10 produtos mais vendidos da categoria do produto no qual o cliente demonstrou interesse.
Para isso, unificamos os 4 datasets fornecidos, alocados em 'Datasets Brutos'
Removemos os valores nulos, e as linhas duplicadas por inteiro
Desenvolvemos uma função para buscar pelo top 10 mais vendidos, dada a categoria, e uma função para buscar pela categoria do produto, dado o produto de interesse.
Ao final, tem-se a função que recebe um identificador do produto de interesse e retorna o top 10 mais vendidos da categoria deste produto de interesse