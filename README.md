# Restaurant Orders

## Descrição

O Restaurant Orders é um projeto desenvolvido para ajudar a gerência da lanchonete Pão na Chapa a aumentar suas vendas e melhorar sua gestão interna. O sistema de faturamento da lanchonete salva o nome da pessoa, o pedido realizado e o dia da semana do atendimento, e o objetivo do projeto é gerar relatórios com informações sobre os pedidos e as pessoas clientes que frequentam a lanchonete. Esses dados irão auxiliar o trabalho de uma agência de marketing com o objetivo de alavancar as vendas e o número de pessoas clientes.

## Funcionalidades

O projeto possui as seguintes funcionalidades:

-   Geração de relatórios com informações sobre pedidos e clientes;
-   Controle de estoque de ingredientes para garantir que o menu digital do restaurante sempre ofereça produtos disponíveis em estoque.

## Tecnologias utilizadas
<div align="left">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="50" width="62" alt="python logo" />

</div>

## Como utilizar
Clone o repositório usando o comando:

    git clone git@github.com:leonanfecosta/restaurant-orders.git
Crie o ambiente virtual para o projeto

    python3 -m venv .venv && source .venv/bin/activate
Instale as dependências

    python3 -m pip install -r dev-requirements.txt
### Campanha de publicidade 
#### O sistema gera um arquivo txt no caminho `data/mkt_campaign.txt` com as seguintes informações:

-   Qual o prato mais pedido por 'maria'?
-   Quantas vezes 'arnaldo' pediu 'hambúrguer'?
-   Que pratos 'joão' nunca pediu?
-   Em que dias o 'joão' nunca foi a lanchonete?

Para executá-lo, use o comando `python3 -m src.analyze_log`

### Análise Contínua
#### Sistema que permite, a qualquer momento, a extração de informações:

-   Prato favorito por cliente
-   Pratos nunca encomendados por cada cliente
-   Dias nunca visitados por cada cliente
-   Dia mais movimentado
-   Dia menos movimentado

Para executá-lo, use o comando `python3 -m src.track_orders`

 ## Autor

O projeto foi desenvolvido por [Leonan Costa](https://github.com/leonanfecosta) como parte de um projeto para a curso de Desenvolvimento Web da Trybe.
