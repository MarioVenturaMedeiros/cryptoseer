# Criação dos Modelos Iniciais e sua comparação.

## Esolha do Modelo

### Análise de modelos
Durante a pesquisa de modelos adequados para análise de séries temporais de criptomoedas, com foco em sazonalidade repetida (uma característica do meu dataset), algumas opções se destacaram, cada uma com suas vantagens e desvantagens.

1. **Combinação de ARIMA com LSTM**:  
   Essa abordagem combina o modelo estatístico ARIMA (AutoRegressive Integrated Moving Average) com redes neurais LSTM (Long Short-Term Memory).
   - **Vantagens**:  
     - Potencial para maior acurácia ao capturar tanto a parte linear da série temporal (com ARIMA) quanto as dinâmicas mais complexas e não lineares (com LSTM).  
     - Capacidade de lidar com dados sequenciais de forma robusta, sendo mais eficaz em séries temporais com padrões complexos.
   - **Desvantagens**:  
     - Alto custo computacional, uma vez que a combinação de dois modelos pode exigir mais recursos de processamento e tempo de treinamento.  
     - Complexidade de implementação, dado que são necessários conhecimentos tanto em modelagem estatística quanto em redes neurais.

2. **Prophet**:  
   Prophet é um modelo desenvolvido pelo Facebook que é conhecido por sua simplicidade e eficiência ao lidar com dados que possuem padrões de tendência e sazonalidade.
   - **Vantagens**:  
     - Fácil de implementar e interpretar, com uma interface amigável que permite ajustar parâmetros de forma simples.  
     - Boa capacidade de lidar com dados que apresentam sazonalidade e tendências, especialmente em casos onde há repetições cíclicas claras.  
     - Menor custo computacional em comparação com abordagens mais complexas, como a combinação ARIMA-LSTM.
   - **Desvantagens**:  
     - Menor flexibilidade em capturar padrões não lineares e complexos que podem existir nos dados.  
     - Acurácia inferior em séries temporais que dependem de uma modelagem mais sofisticada, como no caso de dados altamente voláteis, comuns em criptomoedas.

3. **Holt-Winters (ETS - Exponential Smoothing)**:  
   O modelo Holt-Winters é uma técnica clássica de suavização exponencial que lida bem com dados sazonais.
   - **Vantagens**:  
     - Modelo simples de implementar e interpretar, especialmente adequado para dados com sazonalidade bem definida e padrão repetitivo.  
     - Menor custo computacional, sendo ideal para quem busca soluções rápidas e com menor carga de processamento.
   - **Desvantagens**:  
     - Pode não ser tão preciso em séries temporais com padrões complexos ou que exibem mudanças abruptas, o que é comum no mercado de criptomoedas.  
     - Focado em modelar padrões sazonais e tendência de forma linear, o que limita sua capacidade em capturar variações mais dinâmicas e não lineares.

Em resumo, a escolha entre esses modelos depende de um equilíbrio entre a simplicidade, custo computacional e a necessidade de capturar padrões complexos. Modelos como o ARIMA-LSTM são mais robustos, mas também mais exigentes em termos de recursos, enquanto Prophet e Holt-Winters oferecem soluções mais simples e rápidas, mas com possível perda de acurácia em cenários mais complexos.

### Modelo decidido

Foi decidido que será usado o Prophet para treinamentos iniciais e análise do dataset por causa de sua simplicidade de aplicação e menor tempo de processamento. Não foi usado o Holt-Winters, pois os dois modelos partem do mesmo princípio e assim foi escolhido o Prophet por ser um modelo que é conhecido por lidar bem com dados que possuem padroes de sazonalidade, que é o caso do projeto.

Depois que o modelo ficar mais robusto e todas as features serem otimizadas, será utilizado o modelo ARIMA + LSTM, a fim de obter resultados melhores no treinamento.

## Features utilizadas:

-`Data`: O dia
-`Close`: O valor que a ação da Dogecoin fechou

Sendo assim, podemos observar que todas as predições que o modelo fazer estarão relacionadas ao final do dia. 

## Análise de resultados

1. Erro Médio Absoluto (MAE): 0.00856494756810357

O MAE é a diferença absoluta média entre os valores previstos (yhat) e os valores reais (y). Esse valor indica, em média, quanto as previsões estão distantes dos dados reais, independentemente de superestimarem ou subestimarem o valor. No caso, o erro médio absoluto é de 0.0085, o que indica que, em média, o modelo erra o valor real em aproximadamente 0.0085 unidades do preço, um valor bem baixo e impressionante para.

2. Erro Quadrático Médio (MSE): 0.00013501139665331955

O MSE é a média dos quadrados dos erros, ou seja, penaliza erros maiores mais severamente, já que esses erros são elevados ao quadrado. Isso significa que o MSE dá mais peso a grandes desvios entre o valor previsto e o valor real. Um MSE de 0.000135 indica que os erros gerais do modelo são pequenos, e o fato de o MSE ser baixo é positivo, pois sugere que o modelo está performando bem.

3. Raiz do Erro Quadrático Médio (RMSE): 0.011619440462144446

O RMSE é simplesmente a raiz quadrada do MSE, e traz os erros de volta à escala original dos dados, o que facilita a interpretação. Um RMSE de 0.0116 indica que o erro médio entre as previsões e os valores reais está em torno de 0.0116 unidades do preço, o que é considerado um bom desempenho em muitos cenários de previsão de séries temporais.

4. R-quadrado (R²): 0.878950545678328

O R² mede a proporção da variação dos dados que é explicada pelo modelo. Um valor de 0.879 significa que aproximadamente 87,9% da variação nos valores de preço é explicada pelo modelo de previsão. Um R² próximo de 1 é ideal, pois indica que o modelo está capturando a maior parte da variação nos dados. Com um valor de 0.879, o modelo está se saindo muito bem ao capturar as tendências e padrões subjacentes no conjunto de dados.

## Conclusão