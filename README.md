# 🏨 Reserva de Quartos em Python

Sistema simples de reservas pelo terminal, desenvolvido para praticar lógica de programação em Python.

O programa controla a disponibilidade de **10 quartos**, numerados de 1 a 10.

## Funcionalidades

- Consultar os quartos disponíveis.
- Reservar um quarto disponível.
- Cancelar uma reserva e devolver o quarto à lista de disponíveis.
- Exibir os quartos disponíveis em ordem numérica.
- Tratar entradas não numéricas na reserva e no cancelamento.
- Encerrar o programa pelo menu.

## Como executar

É necessário ter **Python 3** instalado. Não é preciso instalar bibliotecas externas.

1. Baixe o arquivo do projeto.
2. Abra o terminal na pasta onde ele está salvo.
3. Execute:

```bash
python main.py
```

Se o arquivo tiver outro nome, substitua `main.py` pelo nome correspondente.

## Como usar

Ao executar, o programa apresenta o menu:

```text
=== RESERVA DE QUARTOS ===

1 - Disponibilidade
2 - Reservar Quarto
3 - Cancelar Reserva
4 - Sair
```

Você pode escolher pelo número ou pelo texto da opção, como `1` ou `disponibilidade`.

### Exemplo

1. Escolha `2` para reservar.
2. Informe o quarto `5`.
3. Consulte a disponibilidade: o quarto `5` não aparecerá na lista.
4. Escolha `3` e informe `5` para cancelar.
5. O quarto voltará a ficar disponível.

## Conceitos praticados

- Listas e geração de sequências com `range()`.
- Repetição com `while`.
- Condições com `if`, `elif` e `else`.
- Verificação de elementos com `in` e `not in`.
- Métodos de listas: `remove()`, `append()` e `sort()`.
- Métodos de strings: `lower()` e `strip()`.
- Tratamento de erros com `try` e `except ValueError`.
- Controle do fluxo com `continue` e `break`.

## Limitações

As reservas são mantidas apenas durante a execução. Ao fechar e abrir o programa, todos os quartos ficam disponíveis novamente.

Esta versão não registra hóspedes, datas, pagamentos ou histórico de reservas.

## Possíveis melhorias

- Salvar as reservas em arquivo.
- Registrar o nome do hóspede.
- Adicionar datas de entrada e saída.
- Consultar os quartos reservados.
- Criar uma interface gráfica.
