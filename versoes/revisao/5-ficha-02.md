# 5º ano · ficha 2 · Frações (equivalência, simplificação e comparação)
## Corrigido
- Q111 (questão 6 da ficha) v2 — "**Caio** comeu a parte pintada da pizza **dela**" → "da pizza **dele**".
- Q111 (questão 6) v3 — "**Lucas** comeu a parte pintada da pizza **dela**" → "da pizza **dele**".

## Melhorado
- Q111 (questão 6) v4 — "Que fração da pizza Júlia vai comer?" aceitava só `3/4`; agora aceita também `6/8` (o enunciado não pede forma simplificada e as v1–v3 já aceitam a equivalente).
- Q10 (questão 5) v1 — o campo "Como fração" já aceitava `3/2|6/4`; o de número misto passou a aceitar `1 1/2|1 2/4`, coerente com isso.
- Q113 (questão 8) v1–v4 — rótulo "Fração brilhante (sobre o total de 24)" → "Fração das figurinhas brilhantes (sobre o total de 24)" ("fração brilhante" soava estranho e podia confundir).
- Q114 (questão 9) v1–v4 — "Léo tem 2/3 **de garrafa** de suco" → "2/3 **de uma garrafa** de suco".
- Q114 (questão 9) v3, v4 — nas 4 versões o "=" era sempre o 3º item (respostas > < = repetidas); trocados os itens 2 e 3 em v3 e v4 (o 1º continua sendo o das garrafas desenhadas). Gabaritos agora: v1 `> · < · =`, v2 `< · > · =`, v3 `> · = · <`, v4 `> · = · <`.

## Sugestões (não aplicadas)
- Q10 (questão 5) — o enunciado não diz que cada círculo é 1 inteiro; um "Cada círculo é **1 inteiro**." ajudaria a criança que ainda confunde "parte do desenho" com "parte do inteiro".
- Q116 (questão 11) — "Qual letra está mais perto do 1?" tem resposta A em v1, v2 e v4 (só B em v3). Trocar a posição de B em uma delas (ex.: v2 com B = 4/3) equilibraria, mas exige redesenhar a reta.
- Q111 (questão 6) — na pizza, a parte "pintada" é a de cobertura laranja com calabresa e o resto é bege (massa). Funciona, mas "a parte com cobertura" ou uma legenda deixaria mais claro que o bege não foi comido.

## Conferido sem problemas
60 versões revisadas (Q6–Q10: original + 3 versões; Q111–Q120: 4 versões cada).
Verificações por script (Fraction): frações equivalentes e números que faltam (Q6, Q112), formas irredutíveis (Q7, Q113, Q118), comparações >, <, = (Q8, Q114), fração de quantidade (Q9), frações impróprias ↔ números mistos (Q10, Q117), passos da simplificação ÷2/÷3/÷7 (Q115), ordem crescente com denominador comum, sem empates (Q119), alternativa "NÃO representa" única (Q118).
Desenhos conferidos por script: barras de comparação de Q8 batem com o item ilustrado; pizzas de Q10 (meios, quartos, terços, oitavos; 3, 7, 7 e 13 partes pintadas); fatias pintadas e total de fatias das duas pizzas (Q111); fileiras do muro de frações (Q112); figurinhas amarelas/azuis = total e fração (Q113); partes cheias e altura das partes das garrafas (Q114); marcas da reta e posição de A e B (Q116, inclusive "mais perto do 1"); pedaços marrons/brancos do chocolate (Q118); partes pintadas, total de partes e posição da bolinha em cada pista (Q120).
Formato do número misto: o corretor de `f` remove os espaços, então "1 1/2" é aceito; os campos têm placeholder `_ _/_` e Q117 traz o exemplo "(ex.: 1 1/2)". Varredura de português ("de o/de a", espaço antes de pontuação, palavras repetidas, concordância dele/dela). SVGs com no máximo 460 px. `validar.py 5 2`: 0 problemas.
