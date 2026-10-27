# 5º ano · ficha 3 · Operações com frações

## Corrigido
- Q124 v1–v4 (questão 9 da ficha, garrafa de suco) — o texto dizia "Ela tem **8/6/10/12 marquinhas** iguais", mas o desenho tem 7/5/9/11 tracinhos (que dividem a garrafa em 8/6/10/12 partes). Quem contasse os tracinhos não achava o número. → "As marquinhas dividem a garrafa em **8 (6, 10, 12) partes iguais**."
- Q15 v2–v4 (questão 5 da ficha) — faltava o espaço depois da fração ("½no domingo", "3/10na terça", "3/8depois") → espaço incluído.
- Q12 v1 (questão 2) — 2/3 − 1/6 não aceitava 9/18 (resultado de quem multiplica os denominadores), que as versões 2–4 já aceitam → `3/6|9/18|1/2`.
- Q15 v2–v4 — passam a aceitar também a forma com o produto dos denominadores, como na Q12 (v2: 6/8 e 2/8; v3: 35/50 e 15/50; v4: 20/32 e 12/32).

## Melhorado
- Q13 v1 (questão 3, torta de João e Maria) — a torta das originais não tinha nada pintado, enquanto as v2–v4 pintam as fatias de cada um com legenda. → pintadas 2/8 em laranja (João) e 3/8 em azul (Maria), com a mesma legenda das outras versões.
- Q15 v1–v4 — "Que fração ela correu?" era ambíguo (de manhã? à tarde?) → "Que fração do percurso/livro/muro/trilha … **ao todo**?"; "Quanto falta?" → "Que fração ainda falta?".
- Q122 v1–v4 (questão 7, tanque de gasolina) — "Na viagem para a praia, gastou ½ do tanque" ficava sem sujeito (logo depois de "O tanque … estava com…") → "o carro / a moto / a van / o carro gastou…".
- Q126 v1–v4 (questão 11, fração dos que sobraram) — "Quantos … saíram na 1ª etapa / 2ª etapa? … ficaram no fim?" era abstrato → perguntas ligadas à história (ex.: "Quantos brigadeiros as crianças comeram?", "Quantos brigadeiros foram para a vizinha?", "Quantos brigadeiros sobraram no fim?"). v4: "a mamãe usou no bolo ½ deles" (repetia "a mamãe") → "ela usou ½ deles no bolo".
- Q127 v1–v4 (questão 12, xícaras da receita) — "Quanto falta para completar 1 xícara cheia?" → "Juntando tudo em **1 xícara**, quanto falta para ela ficar cheia?" (deixa claro que é juntar as medidas).
- Q14 v1–v4 (questão 4) — gabarito mostrava só a forma simplificada (ex.: "2/3 · 5/8 · 2/3" para 2 × 3/9 e 4 × 2/12) → mostra as duas, como na Q11: "6/9 = 2/3 · 5/8 · 8/12 = 2/3".

## Sugestões (não aplicadas)
- Q14 v2 — dois dos três itens dão 2/3 (2 × 3/9 e 4 × 2/12); dá para trocar um deles para ter resultados diferentes.
- Q126 — é "fração de quantidade" em duas etapas (bom para o 5º ano), mas não usa a escrita de fração × número no campo; poderia mostrar "⅓ de 24 = ⅓ × 24" no enunciado para ligar ao assunto da ficha (multiplicação).
- Q122, Q124, Q125 — com desenho dividido em partes, só aceitam a forma nas partes do desenho e a simplificada (ex.: 7/8 − 1/2 aceita 3/8, não 6/16). Coerente com o desenho; se o pai preferir, dá para aceitar também o produto dos denominadores como na Q12/Q15.

## Conferido sem problemas
60 versões revisadas (15 questões × 4; `validar.py` conta 55 porque a v1 das originais fica no arquivo de originais). Por script (Fraction): todas as somas, subtrações e produtos de Q11–Q15 e Q121–Q130, inclusive a fração que sobra/falta; todas as alternativas `|` de cada campo `f` são equivalentes entre si (nenhuma resposta errada aceita); Q128 (número escondido) tem solução única nas 12 contas; Q129 sinal certo em todas (posição da certa: 2/1, 2/0, 1/0, 2/0). Desenhos contados no SVG: fatias pintadas por cor das pizzas/tortas (Q13 v1–v4, Q121 v1–v4) batem com cada criança e com a legenda; tanque Q122 = 7/8, 5/6, 9/10, 11/12; muro Q123 por dia (2+1+3 de 8, 2+1+2 de 6, 2+3+1 de 10, 2+5+1 de 12); garrafa Q124 cheia com n partes; pista Q125 com 10/8/12/6 partes e corredores em 3/10 e 1/2, 3/8 e 3/4, 1/3 e 7/12, 1/6 e 2/3; Q126 com 24/30/36/40 doces; Q127 com 2/4/2/7 xícaras e medida 1/3, 1/6, 3/8, 1/10 em cada. SVGs renderizados no Chrome headless: nada cortado nem sobreposto, largura máxima 444 px. `validar.py 5 3`: 0 problemas.
