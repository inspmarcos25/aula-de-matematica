# 3º ano · ficha 12 · Mais probleminhas

## Corrigido
- Q63 v3 e v4 (questão 3 da ficha) — as 4 caixas/5 pacotes e o peso não cabiam no prato da balança (saíam até 16 px para fora dos dois lados) → objetos empilhados (3 embaixo + 1 ou 2 em cima) dentro do prato; contagem e pesos iguais.
- Q69 v2, v3, v4 (questão 9) — a dica dizia "18,90 fica perto de 19; 9,80 fica perto de 10", preços que só existem na v1 → dica geral nas 4 versões: "centavos de 50 para cima, arredonde para o real de cima; menos de 50, para o real de baixo. Ex.: 5,80 fica perto de 6 e 5,30 fica perto de 5" (exemplos que não aparecem em nenhuma lista).
- Q70 v3 (questão 10) — "Quantos lápis a mais seriam necessárias" (concordância) e "cada um recebe / dar para cada um" falando de estojos → "Quantos lápis vão em cada estojo?" e "Quantos lápis a mais seriam necessários para colocar 1 a mais em cada estojo?"; dica ajustada.
- Q67 v1 e v2 (questão 7) — falta de artigo: "Mãe de Ana precisa" → "A mãe de Ana precisa"; "Professor Jorge precisa de 12 unidades de lápis" → "O professor Jorge precisa de 12 lápis".

## Melhorado
- Q62 v1–v4 (questão 2) — os campos "Quanto já tem?" / "Quanto falta para completar?" não combinavam com páginas lidas e kg arrecadados → perguntas próprias de cada versão ("Quantas páginas Lara já leu?", "Quantos kg já chegaram?", "Quantas faltam para chegar à meta?"…).
- Q64 v4 (questão 4) — a 2ª pergunta tinha resposta "3º" em 3 das 4 versões → v4 agora pergunta o lugar de Otávio (2º); gabarito atualizado.
- Q67 v2 e v4 — placa "MERCADINHO" vendendo lápis e figurinhas → "PAPELARIA" e "BANCA DE JORNAL".
- Q211 v2–v4 (questão 11) — enunciado, campos e dica falavam em "tijolo" numa pirâmide de caixas / torre de blocos / pirâmide de latas → "caixa", "bloco" e "lata" (com concordância).
- Q214 v1 (questão 14) — "Bia partiu uma barra de chocolate" sugeria pedaços separados (aí não haveria quadrados maiores) → "A barra de chocolate de Bia é dividida em quadradinhos".
- Q215 v1–v4 (questão 15) — dica dizia "quadradinho" para a região 2 × 2 → "quadrado 2 × 2", como no enunciado.

## Sugestões (não aplicadas)
- Q63 — o gerador da balança usa um prato de 116 px fixo; se novas versões tiverem mais objetos, vale alargar os pratos em vez de empilhar.
- Q64 — as pistas estão em `div.note` (caixa amarela de "Dica"); ficariam mais claras em `div.ex` ou numa lista normal, já que são dados do problema e não dica.
- Q65 — cada versão usa um contexto de tempo diferente (dias do mês, ano de nascimento, diferença de idade, semanas de férias); se a ideia for "mesma questão", dá para alinhar as 4 num só tipo.
- Q68 — junta duas habilidades diferentes (quantas notas iguais formam um valor + menor número de cédulas); a v3 começa com moedas de 25 centavos e depois fala de cédulas. Poderia separar ou deixar o 1º item sempre com cédulas.

## Conferido sem problemas
80 versões (20 questões × 4) revisadas. Verificações por script (Python): todas as contas e `data-a`/`gab`; força bruta de solução única nos 4 enigmas de ordem (Q64), nos 4 sudokus 4 × 4 (Q215, 1 solução cada, A/B conferidos) e nos 4 quadrados mágicos (Q213, linhas, colunas e diagonais); pirâmides (Q211) e contas de frutas (Q212, frutas identificadas no SVG por cor/forma em cada linha) com solução única; menor número de cédulas por programação dinâmica (Q68: 3, 5, 4, 6); contagem nos SVGs de objetos na balança (Q63), quadradinhos/palitos das sequências (Q66), grade 2 × n (Q214), ângulos dos ponteiros (Q216: 6h30, 6h45, 7h10, 6h50), números das pedras (Q217), furos (Q218) e frutas em cada prato das balanças duplas (Q220). Tabelas de Q213 (3 × 64 px) e Q215 (4 × 48 px) dentro de `div.tw`, cabem no celular. SVGs com até 456 px. `validar.py 3 12`: 0 problemas.
