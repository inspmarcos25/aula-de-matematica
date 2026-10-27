# 4º ano · ficha 8 · Perímetro e área

## Corrigido
- Q171 v2 (questão 6 da ficha) — "a casinha que Luna montou, **feito** de quadradinhos… Qual é a área **do** casinha?" → "…montou, **feita** de quadradinhos… Qual é a área **da** casinha?" (concordância).
- Q178 v2 (questão 13) — "Dona Fátima quer um canteiro… **Ele** pensou em várias larguras" → "**Ela** pensou".
- Q178 v3 (questão 13) — "Tia Rosângela quer um canteiro… **Ele** pensou" → "**Ela** pensou".

## Melhorado
- Q176 v1–v4 (questão 11) — "Quantos azulejos ainda **faltam colocar**?" (regência popular; o verbo deveria ficar no singular com infinitivo) → "Quantos azulejos ainda **faltam** para cobrir o fundo?" (mais claro e correto).

## Sugestões (não aplicadas)
- Q38 (questão 3) — o retângulo do desenho é o mesmo (150×74 px) nas 4 versões, inclusive em 11 m × 4 m e 10 m × 6 m; poderia ser desenhado na proporção das medidas para a criança associar forma e números.
- Q173 (questão 8) — a resposta certa do item c) é "Tapete B" em 3 das 4 versões (v2–v4); para variar, uma versão poderia ter o tapete de maior contorno à esquerda (Tapete A).
- Q175 (questão 10) — o enunciado diz que o tapete fica "no meio", mas em todas as versões ele está 1 fileira mais perto da parede de baixo (2 fileiras livres em cima, 1 embaixo); trocar por "Sobre o chão fica um tapete" ou centralizar o tapete numa malha com número ímpar de fileiras livres.

## Conferido sem problemas
- 15 questões × 4 versões = 60 versões revisadas (originais + ficha-08 + mais-08).
- Malhas contadas por script (células `rect` por posição, última cor vence): Q36 (24, 21, 16, 25), Q37 (18, 20, 15, 24), Q171 (33, 31, 27, 23 — todas as cores somadas, figuras conexas), Q175 (chão 35/36/40/42, tapete 6/12/8/9, sem tapete 29/24/32/33) — tudo bate com `data-a`/`gab`; cores citadas no texto (laranja, azul, verde, roxa) batem com o `fill`.
- Contornos (Q172): arestas de borda calculadas a partir das células pintadas e comparadas uma a uma com as `line` grossas do SVG — conjuntos idênticos; perímetros 16, 16, 18, 22 cm conferem; formas (escadinha, cruz, T, U) batem com o texto.
- Q173: tapetes separados por componente conexa; áreas iguais (12/12, 16/16, 10/10, 18/18) e perímetros 16×14, 16×20, 14×18, 18×22 palmos; rótulo "Tapete A/B" centrado sobre o tapete certo; `data-a` do item c) correto.
- Q174: comprimento das cercas (linhas marrons) somado por script = 18, 19, 18, 22 m; portão (linha amarela) = 2, 1, 2, 2 m, igual ao texto; área de grama 24, 21, 25, 32 m².
- Q176: fileiras × colunas deduzidas do retângulo da piscina (9×4, 8×5, 10×3, 7×6) e 12 azulejos colocados em cada versão (= colunas + fileiras − 1); faltam 24, 28, 18, 30.
- Q180 (meias células): cada `polygon` conferido como triângulo retângulo de catetos 1 dentro de uma célula **não** pintada (sem sobreposição); inteiros + meios/2 = 14+4=18, 20+4=24, 12+6=18, 24+3=27 cm².
- Contas refeitas por script: Q38 (26, 32, 38, 30 m), Q39, Q40, Q177 (lado = fita ÷ 4; área), Q178 (comprimento = área ÷ largura; perímetro), Q179 (todas as hortas com perímetro igual à cerca dada; retângulos do SVG na escala 13 px/m; `data-a` do item c) alterna 1, 0, 1, 0).
- SVGs ≤ 460 px; viewBox coerente; nenhum rótulo cortado (estimativa de largura do texto); tabela do Q178 dentro de `div.tw`.
- `python3 -I validar.py 4 8` → 55 versões conferidas, 0 problema(s).
