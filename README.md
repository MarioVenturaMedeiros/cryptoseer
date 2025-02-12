# Projeto de Sistema de Auxílio à Tomada de Decisões para Investimento em Criptoativos

## Introdução

Este projeto foi desenvolvido com o objetivo de criar um sistema que auxilie na tomada de decisões para investimento em criptoativos, especificamente utilizando Dogecoin como ativo principal. A escolha do Dogecoin se deu por ser uma criptomoeda com uma comunidade ativa e um histórico de volatilidade que oferece boas oportunidades para análise e previsão de preços. Além disso, o Dogecoin, apesar de sua origem como um "meme", tem demonstrado uma resiliência surpreendente no mercado, tornando-se um ativo interessante para estudos de padrões de mercado.

## Estrutura do Diretório

- `src` - Código do projeto
- `docs` - Documentação completa do projeto
- `README.md` - Documentação inicial

## Como Executar

Entre [nesse link](https://github.com/MarioVenturaMedeiros/cryptoseer) e baixe a versão ZIP do projeto.

Descompacte o arquivo ZIP

na janela do teminal, no repositório do projeto, execute os seguintes comandos:

```bash
sudo systemctl start docker

sudo usermod -aG docker $USER

newgrp docker

cd src/

docker compose up --build
```

## Ordem da documentação

### Data exploration

1. `analise_inicial.md`

2. `modelo_inicial.md`

3. `modelo_multi.md`

4. `modelo_arima_lstm.md`

5. `escolha_modelo.md`

### Pocketbase

1. `pocketbase.md`

### Backend

1. `backend_AI.md`

3. `Logs.md`

2. `backend_dashboard.md`

## Docker

1. `docker.md`

## Histórico de Patches

V0.1.0 - AI creation, documentation

V0.2.0 - AI comunication, retraining and logs

V0.3.0 - Dashboard backend

V0.4.0 - Frontend

V1.0.0 - Integration

V1.0.1 - bug fixes