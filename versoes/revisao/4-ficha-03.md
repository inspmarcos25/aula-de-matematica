# 4º ano · ficha 3 · Multiplicação

## Corrigido
- Q122 v1 e v4 (questão 7 da ficha, cartelas de adesivos) — concordância: "Quantos estrelinhas Bia/Enzo tem ao todo?" → "Quantas estrelinhas…".
- Q129 v1–v4 (questão 14 da ficha, receitas) — "Quantos ovos de ovos vão usar?" (repetição) → "Quantos ovos vão usar?".

## Melhorado
- Q129 v3 — "Para a festa da família, a turma vai fazer…" não fazia sentido (turma da escola numa festa de família) → "Para o lanche coletivo da escola, a turma vai fazer 5 receitas de panqueca."
- Q124 v1–v4 (questão 9 da ficha, canteiro com lona) — "As flores estão em linhas e colunas completas, como as que aparecem…" → "Embaixo da lona, as flores continuam arrumadas em linhas e colunas, iguais às que aparecem na primeira linha e na primeira coluna." Deixa claro que há flores escondidas e como contá-las.

## Sugestões (não aplicadas)
- Q127 (número que falta com ×10/×100) — as 4 versões têm exatamente o mesmo padrão (?×10, n×?=100, ?×100, n×?=10) e nunca usam ×1.000; dá para variar a posição e incluir um ×1.000.
- Q125 (tabela das caixas) — o desenho da caixa mostra só 6 lápis na ponta, com o rótulo "12/24/18/15"; está claro pelo rótulo, mas poderia mostrar a caixa fechada para não sugerir contagem.
- Q12 v1 — gabarito "7 × 9 = 63" sem a unidade (as v2–v4 têm "árvores/bombons/azulejos"); detalhe de padronização (arquivo das originais).

## Conferido sem problemas
60 versões revisadas (15 questões × 4; validar.py conta 55 porque as originais da v1 ficam no arquivo de originais). Por script: todas as contas armadas (Q11), produtos de Q12–Q15, Q121–Q125, Q129, Q130; unicidade do algarismo escondido em Q126 (só uma solução em cada conta); Q127 (fator que falta); Q128 (opção mais próxima do produto e posição da certa varia: 0,1,2,1). Desenhos contados a partir do SVG: Q12 linhas × colunas = fileiras × itens do enunciado nas 4 versões (7×9, 6×8, 8×7, 6×9), e os campos aceitam a ordem dos fatores das duas formas (`a|b` / `b|a`); Q121 colunas verdes/laranja × linhas batem com os rótulos; Q122 grade da cartela = gabarito (4×5, 3×6, 5×4, 4×6); Q124 flores 12×8, 11×9, 13×7, 15×6 e a lona cobre exatamente tudo menos a 1ª linha e a 1ª coluna (checado pelas coordenadas e renderizado); Q13 e Q123 quantidade de roupas/bonés/casquinhas/copinhos. SVGs renderizados no Chrome headless: nada cortado, todos ≤ 416 px. `validar.py 4 3`: 0 problemas.
