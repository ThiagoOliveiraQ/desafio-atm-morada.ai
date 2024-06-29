# Desafio Técnico Morada.ai: Caixa Eletrônico API

## Objetivo
Criar uma API que simula o funcionamento de um caixa eletrônico que recebe um valor de saque desejado e retorna a quantidade de cédulas de cada valor necessárias para compor esse saque, 
utilizando a ***menor quantidade de cédulas possível***.

## Desafios para a conclusão deste projeto:
O maior desafio enfrentado foi garantir que os dados fornecidos pelo usuário sejam válidos. </br>
- **Nisso foi necessário**: 
  - Verificar se era de fato um número
  - Verificar se era possível resolver o número inserido com as notas disponíveis
  - Verificar se o número era positivo e diferente de zero
- **Algoritmo de destribuição**:
  - Garantir que o valor seja distribuído corretamente entre as notas disponíveis.
  - O loop distribui primeiro as maiores notas e vai reduzindo o valor até chegar a Zero </br> ou entrar no `Erro: Não possuímos notas para tal valor`

## Requisitos e Ferramentas
- **Tecnologias Utilizadas**:
  - Backend: Python
  - Testes: Postman

- **Ambiente de Desenvolvimento**:
  - Sistema Operacional: Windows 10
  - IDE: VS Code

## Execução do projeto
1 -> Clone o repositório: https://github.com/ThiagoOliveiraQ/desafio-atm-morada.ai.git </br>
2 -> Navegue até o diretório do projeto: desafio-atm morada.ai </br>
3 -> Execute o código no terminal: `python main.py`

## Teste unitário
### Sucesso:
<div align="center"><img src="https://github.com/ThiagoOliveiraQ/desafio-atm-morada.ai/blob/main/img/teste_sucesso.png"></div>

### Entrada inválida por falta de notas de R$ 1:
<div align="center"><img src="https://github.com/ThiagoOliveiraQ/desafio-atm-morada.ai/blob/main/img/teste_valor_impossivel.png"></div>

### Entrada inválida por conter letras:
<div align="center"><img src="https://github.com/ThiagoOliveiraQ/desafio-atm-morada.ai/blob/main/img/teste_valor_invalido.png"></div>


