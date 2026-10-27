# 5º ano · ficha 8 · Grandezas e medidas

## Corrigido
- Q175 v1–v4 (questão 10 da ficha) — o texto diz "jarra **cheia**" e "copos… todos **cheios**", mas o desenho mostrava a jarra e o copo só ~¾ cheios (a criança poderia achar que na jarra cabe mais que 1,5 L / 2 L / 2,4 L / 3 L) → suco subido quase até a borda na jarra e no copo (mesmos rótulos e respostas).
- Q37 v1 (questão 2) — o rótulo "8 cm" (x=16, centralizado) encostava/encavalava na borda do retângulo, que começava em x=30 → retângulo e rótulo "12 cm" deslocados 4 px para a direita, igual ao layout das versões 2–4.
- Q177 v1–v4 (questão 12) — "Quanto pesa o peso amarelo **?**" (espaço antes da interrogação e "pesa o peso") → "Descubra quanto pesa o bloco amarelo marcado com **?**."

## Melhorado
- Q39 v1–v4 (questão 4) — perímetro e área sem unidade nenhuma → acrescentado "Cada quadradinho tem **1 cm** de lado." e "cm" / "cm²" depois dos campos; `gab` com as unidades ("Perímetros 16 e 16 cm · áreas 12 e 16 cm²"). Respostas (`data-a`) inalteradas.
- Q172 v1–v4 (questão 7) — "um bloco completo com **3** de comprimento, 2 de largura…" (3 o quê?) → "com **3** caixinhas de comprimento, **2** de largura e **3** de altura".
- Q174 v1–v4 (questão 9) — "deu 4 voltas completas **em volta** da quadra" (repetição) → "**ao redor** da quadra".

## Sugestões (não aplicadas)
- Q37 (questão 2) — os retângulos não estão na proporção das medidas (v1 12 × 8 desenhado 150 × 66 px, quase 2,3 : 1); daria para desenhar na escala para a criança associar forma e números.
- Q175 (questão 10) — v1 e v4 usam o mesmo copo de 250 mL; uma das duas poderia usar outro tamanho (ex.: 150 mL ou 400 mL) para variar.
- Q172 v4 (questão 7) — a "escada" desce nas duas direções (alturas 4/3/3/2/2/1 numa base 3 × 2), bem mais difícil de enxergar que as outras três versões (escada simples); se quiser equilibrar a dificuldade entre as rodadas, trocar por uma escada simples (ex.: 4 degraus × 2 de largura com bloco 4 × 2 × 4 já existe na v3; outra opção seria 3 degraus × 4 de largura, 24 caixinhas, bloco 3 × 4 × 3 → faltam 12) ou manter como desafio.

## Conferido sem problemas
- 15 questões × 4 versões = 60 versões revisadas (originais + ficha-08 + mais-08).
- Cubinhos por script: SVGs renderizados (qlmanage) e conferidos; Q38 = blocos 4×3×2 = 24, 3×3×2 = 18, 5×2×2 = 20, 3×3×3 = 27 (cada SVG desenha exatamente esse nº de cubos, inclusive os escondidos). Q172: escadas 3+2+1 × 2 = 12, × 3 = 18, (4+3+2+1) × 2 = 20; v4 reconstruída por força bruta (todas as 5⁶ alturas numa base 3 × 2, rasterizadas e comparadas pixel a pixel com o SVG) → única forma compatível com alturas 4,3,3,2,2,1 = 15 cubos; blocos completos 18/27/32/24 → faltam 6, 9, 12, 9; a escada cabe nas dimensões do bloco citado em todas as versões.
- Malhas por script: Q39 células rosa/azul 12/16, 18/18, 20/14, 24/24 = rótulos (6×2, 4×4…); perímetros 16/16, 22/18, 18/18, 20/22. Q178 células pintadas 18, 23, 24, 20 e segmentos de contorno 22, 24, 28, 24 = `data-a`.
- Conversões e contas refeitas por script (Decimal): Q36 (km→m, cm→m, kg→g, mL→L), Q40, Q171 (volume = produto dos 3 rótulos; L = cm³ ÷ 1.000: 60, 30, 63, 27), Q173 (sala, cozinha, casa = retângulo externo; larguras de cima e de baixo somam igual e o desenho está na proporção), Q174 (perímetro, × voltas, 1.000 − total), Q175 (mL ÷ copo, divisões exatas), Q176 (soma em m e km), Q177 (massa da fruta − pesos), Q179 (todas as 16 comparações e alternância da posição certa), Q180 (cm, quociente e resto).
- Unidades presentes em todas as perguntas/campos; Q171 traz a dica 1 L = 1.000 cm³.
- SVGs ≤ 437 px de largura; rótulos não cortados (renderização conferida).
- `python3 -I validar.py 5 8` → 55 versões conferidas, 0 problema(s).
