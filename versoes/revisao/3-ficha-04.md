# 3º ano · ficha 4 · Subtração
## Corrigido
- Q133 v1–v4 (questão 8 da ficha, pote antes/depois) — a conta `[ ] − [ ] = [ ]` aceitava só `antes − comeu = depois` (27 − 18 = 9), mas a pergunta é "quantas balas Nina comeu", e a criança tende a escrever `antes − depois = comeu` (27 − 9 = 18), que também está certo e era marcado como errado → acrescentada a linha "Complete a conta: balas de **antes** − balas que Nina **comeu** = balas de **depois**" (com o objeto/nome de cada versão), deixando só uma ordem possível. Na dica, "chegar ao de depois" → "chegar ao número de depois".
- Q136 v1–v4 (questão 11, caixa/bandeja) — "Confira: [ ] + [ ] = 24" aceitava só "já estão + faltam"; a ordem inversa (9 + 15 = 24) também é certa e era recusada → "Confira (os que já estão + os que faltam): …".

## Melhorado
- Q138 v1–v4 (questão 13, diagrama de barras) — os rótulos das barras diziam "1ª vez / 2ª vez", mas o texto fala em "1ª semana / 2ª semana" (v1, v3, v4) e "sábado / domingo" (v2) → rótulos iguais ao texto (conferido renderizando: cabem nas barras).
- Q137 v4 (questão 12, cálculo mental) — o 1º item (65 − 19) repetia o subtraendo do exemplo (47 − 19) → 81 − 59 (81 − 60 = 21; 21 + 1 = 22); gab atualizado.
- Q18 v2 (questão 3) — "Um sítio tinha 1.200 pés de alface e colheu 450. Quantos … ficaram na horta?" falava da horta sem tê-la apresentado → "… pés de alface na horta e colheu 450".

## Sugestões (não aplicadas)
- Q139 — nas 4 versões a conta da criança está sempre **errada**; com o tempo a criança pode marcar "errada" sem fazer a prova real. Poderia haver uma versão em que a conta está certa (aí a 3ª pergunta mudaria para algo como "Qual número foi tirado?").
- Q131 — em "18 − [ ] = [ ]" também é verdadeiro 18 − 11 = 7; como a linha pergunta "Quantos balões sobraram?" e o resultado é a resposta, o risco é pequeno, mas dá para rotular ("balões que estouraram") se aparecer confusão.

## Conferido sem problemas
60 versões (15 questões × 4). Por script: todas as contas de Q16–Q20 e Q131–Q140 refeitas (data-a e gab coerentes); Q135 (algarismos apagados) com solução única por força bruta nas 4 versões; contagens nos SVG por script — balões riscados/total (Q131), balas antes/depois (Q133: 27/9, 24/7, 26/12, 23/6), lugares cheios/tracejados (Q136: 15/24, 17/30, 13/20, 19/28), alturas e ordem das barras (Q132); SVGs renderizados no Chrome headless e conferidos (reta numérica da Q134, barras da Q138, ônibus da Q140). Q139: os erros da criança são o erro típico "não emprestou". Posição da opção certa varia nos botões (Q132: 1,0,2,1; Q139: 0,1,1,0). Larguras dos SVG ≤ 440 px. `validar.py 3 4`: 0 problemas.
