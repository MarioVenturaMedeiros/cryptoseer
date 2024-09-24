# Criação do modelo ARIMA + LSTM

## Features Utilizadas

Com a possibilidade de utilizar mais features para treinamento do modelo, foram incluídas todas as features que haviam no dataset para um treinamento inicial. Sendo assim, as features utilizadas são:

- `Data`: O dia
- `Close`: O valor que a ação da Dogecoin fechou
- `Open`: O valor que a ação da Dogecoin abriu
- `High`: O maior valor que a ação chegou no dia
- `Low`: O menor valor que a ação chegou no dia
- `Volume`: Quantas ações foram vendidas em determinado dia

## Análise de resultados

### 1. **Erro Médio Absoluto (MAE): 0.026524900600267836**

O **MAE** é a diferença absoluta média entre os valores previstos e os valores reais. No caso, o **erro médio absoluto** é de **0.0265**, indicando que, em média, o modelo erra o valor real em aproximadamente **0.0265 unidades** do preço. Este é um valor maior do que o esperado para um modelo de previsão de séries temporais e sugere que o modelo não está prevendo com alta precisão. Porém, ao observarmos o **R²**, na verdade o modelo foi sortudo em errar de forma igual para cima e para baixo, assim mesmo que o MAE esteja pequeno, não significa que o modelo esteja bom.

---

### 2. **Erro Quadrático Médio (MSE): 0.0009150324838985702**

O **MSE** é a média dos quadrados dos erros. Um **MSE** de **0.000915** indica que o modelo apresenta erros significativos em suas previsões. O valor do MSE é relativamente pequeno, mas ainda indica que há espaço para melhorias no desempenho do modelo. Porém, ao observarmos o **R²**, na verdade o modelo foi sortudo em errar de forma igual para cima e para baixo, assim mesmo que o MSE esteja pequeno, não significa que o modelo esteja bom.

---

### 3. **Raiz do Erro Quadrático Médio (RMSE): 0.030249503862023425**

O **RMSE** é a raiz quadrada do MSE e traz os erros para a escala original dos dados, facilitando a interpretação. Um **RMSE** de **0.0302** indica que o erro médio entre as previsões e os valores reais está em torno de **0.0302 unidades** do preço. Esse valor sugere que o modelo está cometendo erros relativamente grandes para um modelo de séries temporais. Porém, ao observarmos o **R²**, na verdade o modelo foi sortudo em errar de forma igual para cima e para baixo, assim mesmo que o RMSE esteja pequeno, não significa que o modelo esteja bom.

---

### 4. **R-quadrado (R²): -0.7930946831950931**

O **R²** mede a proporção da variação dos dados que é explicada pelo modelo. Um valor de **-0.793** é um indicativo de que o modelo não está explicando corretamente a variabilidade dos dados e está, na verdade, performando pior do que um modelo que fizesse previsões simples com a média dos dados. Um **R²** negativo aponta para um modelo sub-otimizado e com graves problemas de ajuste, sendo um forte indicativo de que ele não está capturando bem os padrões dos dados.

---

## Conclusão

Os resultados deste modelo **ARIMA + LSTM** não são satisfatórios, com métricas que indicam erros consideráveis nas previsões. O **MAE**, **MSE**, **RMSE** e o valor negativo do **R²** mostram que o modelo não está performando bem para este conjunto de dados de séries temporais. A baixa qualidade das previsões pode ser resultado de **overfitting**, subajuste, ou da incapacidade do modelo de capturar padrões complexos. Ajustes adicionais serão necessários, como ajustes de hiperparâmetros, mais dados de treinamento, ou até mesmo uma abordagem diferente para melhorar o desempenho preditivo.
