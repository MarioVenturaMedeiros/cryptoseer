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

## Análise de resultados

## Conclusão