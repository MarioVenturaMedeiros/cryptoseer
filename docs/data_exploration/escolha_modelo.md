# Escolha do Modelo

## Comparação

Após a análise dos resultados, o modelo **Prophet** utilizando regressores apresentou as melhores métricas de desempenho. No entanto, é importante notar que esse modelo tem uma alta probabilidade de estar `overfittado`, o que pode impactar negativamente a sua capacidade de generalizar para novos dados. Para mitigar esse risco, foi decidido utilizar o modelo **Prophet** com cross-validation. Embora suas métricas sejam ligeiramente inferiores ao modelo originl, ele oferece um equilíbrio mais confiável entre desempenho e robustez, com menor chance de estar `overfittado`.

## Consequências

A escolha do modelo **Prophet** traz tanto benefícios quanto potenciais desafios para o projeto. Abaixo estão as principais consequências dessa decisão:

### Consequências Positivas:

- **Modelo leve**: O modelo **Prophet** é conhecido por sua leveza e simplicidade. Isso significa que o backend do projeto não terá problemas em carregar e operar o modelo de forma eficiente, mesmo em ambientes de produção com limitações de recursos.

- **Resposta rápida**: A utilização do **Prophet** permite que as previsões sejam geradas de maneira extremamente rápida. Isso melhora diretamente a experiência do usuário, pois o tempo de espera para uma resposta do modelo será reduzido significativamente, tornando o sistema mais ágil e interativo.

- **Facilidade de treinamento**: Como o **Prophet** é um modelo voltado para séries temporais, ele pode ser re-treinado rapidamente. Dado que o modelo deverá ser atualizado constantemente com novos dados, sua facilidade de re-treinamento se alinha bem com a necessidade de adaptação contínua do sistema.

- **Integração simplificada**: A arquitetura simples do **Prophet** facilita sua integração com outras partes do sistema, permitindo que seja facilmente ajustado para futuras necessidades ou mudanças no projeto.

- **Menos risco de overfitting**: A escolha de usar cross-validation no treinamento do modelo ajuda a reduzir o risco de overfitting, garantindo maior confiabilidade nas previsões e maior capacidade de generalização para dados futuros.

- **Escalabilidade**: Devido ao seu baixo custo computacional, o modelo **Prophet** pode ser facilmente escalado para lidar com um maior volume de dados sem comprometer significativamente a performance do sistema.

### Consequências Negativas:

- **Possível perda de acurácia**: Embora o modelo com cross-validation reduza o risco de overfitting, ele pode apresentar uma leve perda de acurácia em comparação com o modelo que utiliza regressores, especialmente em cenários onde o histórico de dados tem padrões mais complexos.

- **Menor adaptabilidade a mudanças bruscas**: O **Prophet**, por ser um modelo voltado para séries temporais, pode não reagir tão bem a mudanças abruptas nos padrões de dados. Se o mercado ou contexto analisado sofrer alterações rápidas, o modelo pode levar mais tempo para se adaptar.

- **Necessidade de monitoramento constante**: Como o modelo **Prophet** requer re-treinamento constante, será necessário implementar um processo robusto de monitoramento para garantir que o modelo esteja sempre atualizado com os dados mais recentes, o que pode aumentar a complexidade operacional do projeto.

- **Simplicidade em excesso**: A simplicidade do **Prophet** pode ser uma limitação em casos onde a complexidade dos dados demanda modelos mais sofisticados, como redes neurais ou modelos baseados em deep learning, que podem captar melhor padrões complexos e relações não lineares.

Ao equilibrar essas consequências, a escolha do modelo **Prophet** com cross-validation parece ser a decisão mais adequada para garantir uma boa performance do sistema, sem sacrificar a capacidade de generalização e escalabilidade no longo prazo.
