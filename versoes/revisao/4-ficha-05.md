# 4º ano · ficha 5 · Frações

## Corrigido
- Q142 v3 (questão 7 da ficha) — "Os 20 joaninhas … estão arrumados" → "As 20 joaninhas … estão arrumadas" (concordância).
- Q147 v1 (questão 12) — "Dois pizzas … O de Caio foi cortado … o de Léo" → "Duas pizzas … A de Caio foi cortada … a de Léo".
- Q147 v3 — "Dois tortas de amora … O de Tiago foi cortado … o de Mel" → "Duas tortas de amora … A de Tiago foi cortada … a de Mel".
- Q147 v4 — "Dois quiches … O de Alice foi cortado" (quiche é feminino e pouco conhecido pelas crianças) → "Dois pudins … O de Alice foi cortado" (o desenho amarelo com borda de caramelo combina com pudim).
- Q150 v4 (questão 15) — "suas chicletes / Quantas chicletes / todas as chicletes" → "seus chicletes / Quantos chicletes / todos os chicletes" (chiclete é masculino).
- Q142 v4 — o texto dizia "18 passarinhos no fio do poste … em 3 fileiras", mas um fio só não forma 3 fileiras e o desenho não tinha fio. Agora: "Os 18 passarinhos estão pousados nos fios do poste, em 3 fileiras iguais", e o SVG ganhou 3 fios, um embaixo de cada fileira (6 passarinhos por fio, igual ao antes).

## Melhorado
- Q147 v1–v4 — agora também aceita a fração equivalente que aparece na outra figura (a criança pode usá-la para comparar): v1 a) 1/4|2/8; v2 b) 2/3|4/6; v3 b) 2/5|4/10; v4 a) 1/3|2/6. (O "1/3" de Nina e "1/5" de Tiago já eram aceitos.)
- Q143 v1–v4 (questão 8) — a escala da garrafa só tinha as marcas do meio; a parte de cima (até o ombro da garrafa) não tinha marca, e a criança podia contar só os tracinhos (ex.: 3 em vez de 4 partes). Acrescentei marcas no começo e no fim da escala. A pergunta b) "Que fração vai ficar com suco de laranja?" → "Depois disso, que fração da garrafa ainda terá suco de laranja?" (mais claro).
- Q25 v2 (questão 5) — a resposta certa estava no 1º botão em 3 das 4 versões; botões de v2 trocados (1/5, 1/3; data-a="1"). Posições agora 0, 1, 1, 0.

## Sugestões (não aplicadas)
- Q146 v2 — "trinta centésimos" = 30/100; quem escrever 3/10 erra. Como a atividade é escrever "com números" a fração lida, deixei só 30/100; se o pai preferir, dá para aceitar 30/100|3/10.
- Q148 — as frações a ordenar são todas de mesmo denominador nas 4 versões; uma versão com frações unitárias (1/2, 1/3, 1/5, 1/8) daria mais variedade (mudança de didática).
- Q143 — a parte "cheia" da garrafa vai até o ombro, não até o gargalo; funciona com a escala, mas uma garrafa de corpo reto (tipo jarra) deixaria a ideia de "inteiro" mais evidente.

## Conferido sem problemas
- 60 versões revisadas (15 questões × 4 versões): Q21–Q25 (originais + ficha-05) e Q141–Q150 (mais-05).
- Contas refeitas: frações de quantidade (Q22, Q142, Q149, Q150), sobra na garrafa (Q143 b), repartição da barra (Q145), comparações (Q144, Q25), ordem crescente (Q148) — todas batem com `data-a` e `gab`.
- Desenhos contados por script (fills por cor) e renderizados (qlmanage → PNG): figuras da Q21 (soma de partes pintadas/brancas confere em todas as versões), pizzas/chocolate da Q23, barras da Q25, bandeirinhas da Q141 (4/3/1, 5/2/3, 6/4/2, 3/2/4), malhas de bichinhos da Q142 (3×4, 3×5, 4×5, 3×6), marcas da garrafa da Q143 (4, 5, 6, 8 partes), régua de frações da Q144, quadradinhos da Q145 (12, 10, 18, 20), pizzas/bolos/tortas/pudins da Q147, saquinhos/potes da Q150.
- Leitura de frações por extenso (Q24) com variantes ("um meio|meio" etc.); todos os SVG ≤ 460 px; posições de resposta da Q147 c) variam (0, 1, 1, 0).
- `python3 -I versoes/validar.py 4 5` → 0 problemas.
