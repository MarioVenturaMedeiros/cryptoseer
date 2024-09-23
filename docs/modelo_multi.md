# Criação do modelo para incluir novas features

## Features Utilizadas

Com a possibilidade de utilizar mais features para treinamento do modelo, foram incluidas todas as features que haviam no dataset para um treinamento inicial. Sendo assim, as features utilizadas são:

-`Data`: O dia
-`Close`: O valor que a ação da Dogecoin fechou
-`Open`: O valor que a ação da Dogecoin abriu
-`High`: O maior valor que a ação chegou no dia
-`Low`: O menor valor que a ação chegou no dia
-`Volume`: Quantas ações foram vendidas em determinado dia

## Anáise dos resultados

## Análise de resultados

### 1. **Erro Médio Absoluto (MAE): 0.001253748755468757**

O **MAE** é a diferença absoluta média entre os valores previstos e os valores reais. Esse valor indica, em média, quanto as previsões estão distantes dos dados reais, independentemente de superestimarem ou subestimarem o valor. No caso, o **erro médio absoluto** é de **0.00125**, o que indica que, em média, o modelo erra o valor real em aproximadamente **0.00125 unidades** do preço. Esse valor é extremamente baixo, sugerindo que o modelo está muito próximo dos valores reais. No entanto, isso também pode ser um indicativo de **overfitting**, já que um erro tão pequeno pode significar que o modelo está "decorando" os dados de treino.

---

### 2. **Erro Quadrático Médio (MSE): 3.703833259442676e-06**

O **MSE** é a média dos quadrados dos erros, ou seja, penaliza erros maiores mais severamente, já que esses erros são elevados ao quadrado. Isso significa que o **MSE** dá mais peso a grandes desvios entre o valor previsto e o valor real. Um **MSE** de **0.0000037** indica que os erros gerais do modelo são extremamente pequenos. Embora o valor baixo do MSE seja um bom sinal, resultados excessivamente bons como esse também podem sugerir **overfitting**, especialmente se o modelo estiver sendo avaliado apenas com os dados de treino.

---

### 3. **Raiz do Erro Quadrático Médio (RMSE): 0.0019244176589150984**

O **RMSE** é simplesmente a raiz quadrada do MSE, e traz os erros de volta à escala original dos dados, o que facilita a interpretação. Um **RMSE** de **0.00192** indica que o erro médio entre as previsões e os valores reais está em torno de **0.00192 unidades** do preço. Esse é um valor extremamente baixo para a previsão de séries temporais, o que, à primeira vista, parece excelente. No entanto, esse resultado pode indicar que o modelo está se ajustando muito aos dados de treino, resultando em **overfitting**, que pode prejudicar o desempenho em dados novos ou não vistos.

---

### 4. **R-quadrado (R²): 0.9966795948944914**

O **R²** mede a proporção da variação dos dados que é explicada pelo modelo. Um valor de **0.9967** significa que aproximadamente **99,67%** da variação nos valores de preço é explicada pelo modelo de previsão. Embora um **R²** próximo de **1** seja geralmente o ideal, valores excessivamente altos, como este, podem ser um sinal de **overfitting**, indicando que o modelo está capturando até mesmo o ruído presente nos dados de treino, o que pode não se generalizar bem para novos dados.

---

## Overfitting:

Os resultados apresentados são extremamente bons, com erros quase insignificantes e um R² muito próximo de 1. Embora isso sugira que o modelo está performando de forma excelente nos dados de treino, é importante levantar a preocupação de **overfitting**. O **overfitting** ocorre quando o modelo ajusta-se muito bem aos dados de treino, mas não generaliza bem para dados novos ou não vistos.

- **Indicadores de overfitting**:
  - O erro extremamente baixo (MAE e RMSE) e o **R²** próximo de 1 podem indicar que o modelo está capturando tanto as tendências dos dados quanto o ruído, o que pode prejudicar a capacidade do modelo de fazer previsões robustas em um contexto do mundo real.
  - Para verificar se o modelo realmente generaliza bem, seria importante realizar uma avaliação mais aprofundada em **dados de teste** (não vistos durante o treino), ou até utilizar **validação cruzada** para garantir que o desempenho se mantenha consistente em diferentes partes do conjunto de dados.

Sendo assim, com altas suspeitas de **overfitting**, foi feito o treinamento mais uma vez, com as mesmas features, porém agora usando cross-validation.

## Cross-Validation:

A **validação cruzada (cross-validation)** é uma técnica utilizada para garantir que o modelo generalize bem para dados que ele ainda não viu. Ela divide o conjunto de dados em várias partes, chamadas de **folds**, e treina o modelo em uma parte dos dados (conjunto de treino) enquanto testa em outra (conjunto de teste). Isso é repetido várias vezes, garantindo que todas as partes do conjunto de dados sejam usadas tanto para treino quanto para teste.

No caso da **validação cruzada do tipo TimeSeriesSplit**, usada aqui, o modelo é treinado em subconjuntos crescentes de dados históricos (mantendo a ordem temporal), e testado em subconjuntos futuros. Isso é especialmente importante para séries temporais, onde a sequência dos dados não pode ser embaralhada.

### Porque a validação cruzada ajuda a combater o **overfitting**:
- Ao treinar e testar o modelo várias vezes em diferentes porções dos dados, a validação cruzada ajuda a verificar se o modelo está conseguindo **generalizar** em dados que ele nunca viu. 
- Se o modelo tiver um bom desempenho em todos os folds, isso indica que ele não está apenas ajustando-se aos dados de treino (como no caso de overfitting), mas que ele também está performando bem em dados novos.
- Em vez de confiar apenas em uma única divisão entre treino e teste, a validação cruzada permite uma avaliação mais robusta, pois o modelo é avaliado em diferentes momentos e contextos da série temporal.

Com isso, realizamos uma validação cruzada de **5 folds**. Abaixo, estão as métricas obtidas para cada fold e a média final dos resultados.

### Resultados das Métricas após Cross-Validation:

1. **Erro Médio Absoluto (MAE):**
   - O **MAE** médio entre os folds foi de **0.0015352668392564983**. Isso indica que, em média, o erro absoluto entre as previsões e os valores reais foi de **0.00153** unidades, o que é um valor muito baixo, indicando boa precisão do modelo em múltiplos contextos temporais.

2. **Erro Quadrático Médio (MSE):**
   - O **MSE** médio foi de **5.894157927332369e-06**, o que mostra que os erros gerais, considerando a penalização de grandes erros, foram extremamente pequenos, o que novamente reforça o bom desempenho do modelo.

3. **Raiz do Erro Quadrático Médio (RMSE):**
   - O **RMSE** médio foi de **0.0021004879321295873**, trazendo o erro de volta à escala original dos dados. Esse valor sugere que o modelo mantém um desempenho de erro muito baixo em todos os folds.

4. **R-quadrado (R²):**
   - O **R²** médio foi de **0.9800543964523818**, o que significa que, em média, o modelo foi capaz de explicar **98%** da variação nos dados de preço. Isso indica que o modelo tem um excelente desempenho em capturar as tendências dos dados.

## Conclusão:

A **validação cruzada** reduziu significativamente a preocupação com **overfitting**, uma vez que o modelo apresentou resultados consistentes em diferentes divisões dos dados, indicando que ele consegue generalizar bem, mesmo em diferentes partes da série temporal. As métricas, como **MAE**, **MSE**, **RMSE** e **R²**, continuaram muito boas, sem apresentar uma grande disparidade entre os folds, o que sugere que o modelo é robusto e eficaz para fazer previsões sobre o preço de criptomoedas.