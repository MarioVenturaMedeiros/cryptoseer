# Documentação das Rotas

## Rota para Recuperar Todos os Logs

- **Método**: `GET`
- **Endpoint**: `/logs`
- **Descrição**: Retorna todos os registros da tabela de logs.
- **Parâmetros**:
  - `db`: Sessão do banco de dados (injetado automaticamente pelo `Depends(get_db)`).
- **Respostas Possíveis**:
  - **200**: Retorna uma lista de registros da tabela de logs.
  - **404**: Nenhum log encontrado.
  - **500**: Erro interno do servidor.

---

## Rota para Obter Dados do Dogecoin

- **Método**: `GET`
- **Endpoint**: `/dogecoin-data`
- **Descrição**: Retorna os dados históricos do Dogecoin, incluindo as decomposições de componentes observados, tendência, sazonalidade e ruído.
- **Respostas Possíveis**:
  - **200**: Retorna um objeto JSON contendo:
    - `observed`: Imagem codificada em Base64 do componente observado dos últimos 2 anos.
    - `trend`: Imagem codificada em Base64 da tendência dos últimos 2 anos.
    - `seasonal`: Imagem codificada em Base64 da sazonalidade dos últimos 2 anos.
    - `residual`: Imagem codificada em Base64 do ruído dos últimos 2 anos.
    - `data`: Lista dos preços de fechamento do Dogecoin dos últimos 5 anos.
    - `data_2y`: Lista dos preços de fechamento do Dogecoin dos últimos 2 anos.
  - **500**: Erro interno do servidor.

---

## Funções Auxiliares

### 1. Função `plot_observed(data)`
- **Descrição**: Gera um gráfico do componente observado dos dados fornecidos.
- **Parâmetros**:
  - `data`: Dados históricos da série temporal.
- **Retorno**: Imagem do gráfico codificada em Base64.

### 2. Função `plot_trend(data)`
- **Descrição**: Gera um gráfico da tendência dos dados fornecidos.
- **Parâmetros**:
  - `data`: Dados históricos da série temporal.
- **Retorno**: Imagem do gráfico codificada em Base64.

### 3. Função `plot_seasonality(data)`
- **Descrição**: Gera um gráfico da sazonalidade dos dados fornecidos.
- **Parâmetros**:
  - `data`: Dados históricos da série temporal.
- **Retorno**: Imagem do gráfico codificada em Base64.

### 4. Função `plot_residual(data)`
- **Descrição**: Gera um gráfico do ruído (residual) dos dados fornecidos.
- **Parâmetros**:
  - `data`: Dados históricos da série temporal.
- **Retorno**: Imagem do gráfico codificada em Base64.

### 5. Função `plot_decomposition(data)`
- **Descrição**: Gera gráficos dos componentes observados, tendência, sazonalidade e ruído dos dados fornecidos.
- **Parâmetros**:
  - `data`: Dados históricos da série temporal.
- **Retorno**: Imagens dos gráficos codificadas em Base64.

---

## Observação

Os gráficos são gerados utilizando a biblioteca `matplotlib` e codificados em formato Base64 para que possam ser retornados nas respostas JSON. A decomposição é feita utilizando o método `seasonal_decompose` da biblioteca `statsmodels`, com um período de 30 dias para análise sazonal.
