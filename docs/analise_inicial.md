# Análise Inicial dos dados

## Introdução

Essa seção demonstra como foi feita a análise inicial dos dados da dogecoin e quais foram os _insights_ gerados.

## Análise do Preço da Dogecoin

Como pode ser observado no arquivo `data_exploration.ipynb`, a Dogecoin teve uma alta enorme no meio de 2021. A Dogecoin começou como um meme, e por isso não teve uma grande valorização no início de 2021. Porém, com o apoio de Elon Musk à moeda, ela obteve seu pico. No entanto, por causa do aperto monetário do Banco Central dos EUA, entrou em um período de declínio.

Com a aquisição do Twitter por Elon Musk, a moeda começou a se estabilizar, e havia profissionais no final de 2023 com esperanças de que a moeda voltasse a ter uma alta. Como observado no gráfico, a moeda realmente obteve uma alta em seu valor, mas não chegou perto do seu pico e, novamente, está voltando ao valor estabilizado. Mesmo assim, as altas e baixas da moeda demonstram que a cripto que começou como um meme não pode mais ser ignorada.

Dito isso, o pico que a Dogecoin teve no início representa um comportamento atípico por causa da pandemia, que tornou o assunto de criptos e NFTs famosos e populares, além do incentivo claro de Elon Musk. Sendo assim, não será incluso esse período para o treinamento, já que seria um overfitting gigante que desregularia o modelo.

# Análise da Decomposição 

Como pode ser observado no gráfico abaixo, a Dogecoin apresenta uma sazonalidade bem definida e repetitiva. Sendo assim, podemos extrair que o modelo deve ter essa sazonalidade de base, combinada com a tendência de aumento, queda e os ruidos para prever corretamente quando o usuário deve comprar dogecoin e quando deve vender.

![decompose table](../static/decompose_table.png)

# Análise do dataset

Com o dataset, foi começado a análise dos dados em si para seu tratamento e eventual utilização para criação de um modelo de IA. Porém, como observado no heatmap abaixo, há uma grande relação entre quase todas as features, menos o volume venvido. Sendo assim, foram criados mais dados no dataset como `TODO MÁRIO PELO AMOR LEMBRA DE MUDAR`. Com o novo dataset criado, foram criados duas IA's, uma com o novo dataset e uma com o dataset puro para poderem ser comparadas e investigar se o tratamento de dados está na direção correta ou não. 

Além disso, foram dropadas duas colunas: `Dividends` e `Stock Splits`, já que nenhuma das duas apresentava algum valor, sendo percorridos valores numéricos 0 por todo o dataset.

![Heatmap](../static/heatmap.png)

## Referencias

https://br.cointelegraph.com/news/dogecoin-soared-23-000-in-2021-is-history-starting-to-repeat-for-doge-price