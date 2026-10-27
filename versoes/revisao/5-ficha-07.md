# 5º ano · ficha 7 · Proporcionalidade e problemas

## Corrigido
- Q33 v3 (questão 3 da ficha) — "Ana e Rosa… Quanto **cada um** recebe?" → "Quanto **cada uma** recebe?".
- Q163 v1–v4 (questão 8) — a legenda da escala do mapa era um retângulo 30 × 16 px, mas dizia "lado de 1 quadradinho" (os quadradinhos da malha têm 30 × 30 px) → legenda redesenhada como quadradinho 30 × 30, igual ao da malha.

## Melhorado
- Q165 v1–v4 (questão 10) — o enunciado não fazia a pergunta → acrescentado "Quantas bolinhas / Quantas figurinhas / Quantos adesivos / Quanto cada um recebe?". A legenda "Cada **quadradinho** é uma parte igual" não batia com o desenho (os blocos são retângulos 46 × 24) → "Cada **retângulo** é uma parte igual."
- Q166 v1–v4 (questão 11) — a árvore não dizia qual coluna é qual; na v1 as duas colunas são cores (camisetas azul/verde × bermudas preta/cinza/bege), e o item b) ("mais 1 camiseta" → 9, e não 8) depende de saber isso → rótulos no alto de cada coluna: camiseta/bermuda, suco/lanche, papel/rabiola, chapéu/máscara (SVG 18 px mais alto, resto deslocado).
- Q164 v3 (questão 9) — "O 5º B **tem** 14 latinhas a mais… descubra quanto cada um tem" → "O 5º B **arrecadou** 14 latinhas a mais… descubra quanto cada turma arrecadou" (combina com "arrecadaram juntos").
- Q34 v4 (questão 4) — rótulos "faixa de cima/de baixo" com `font-family="Fredoka"` sem fonte reserva (caíam em fonte serifada) → `Fredoka, sans-serif`.

## Sugestões (não aplicadas)
- Q169 (questão 14) — as lojas são sempre "Loja Sol" × "Loja Lua" e o preço por unidade dá sempre inteiro; uma versão poderia ter empate aparente (ex.: mais itens e preço total maior) para forçar a conta em vez do palpite.
- Q161 (questão 6) — "de Vó Lurdes / de Tio Beto / de Seu Jorge" (registro coloquial); se preferir a forma escolar, "da Vó Lurdes / do Tio Beto / do Seu Jorge".
- Q35 (questão 5) — as 4 versões usam sempre "x horas **e meia**"; uma versão com "2 horas e 15 minutos" (¼ h) aumentaria a variedade sem sair do nível.

## Conferido sem problemas
60 versões revisadas (15 questões × 4: originais Q31–Q35, `ficha-07.json` v2–v4, `mais-07.json` Q161–Q170 v1–v4).
- Todas as contas refeitas por script: tabelas de proporção (Q31), números escondidos (Q32), partilhas desiguais com dobro/triplo/quádruplo (Q33, Q165: totais 6, 7 e 8 partes, todas com valores inteiros e resposta única), partes com diferença (Q164: (total − diferença) ÷ 2 inteiro), velocidade × tempo (Q35), receitas (Q161), misturas de tinta (Q168), preço unitário (Q169), igualdades de trocas (Q170). Todos os `data-a` e `gab` batem.
- Contagens por força bruta: Q167 (permutações de 2 cartões: 6/2, 12/6, 12/9, 20/8) e Q166 (folhas da árvore = raízes × ramos; 6→9, 6→9, 8→12, 9→12, conferindo qual nível ganha o item novo). Q34: 12, 10, 18, 20, com a quantidade de figuras igual ao texto e cores das duas faixas da bandeira diferentes entre si.
- Mapas (Q163): distâncias medidas nas polilinhas do SVG (malha de 30 px) × escala: 350/250, 1.000/300, 180/80, 1.000/1.200 m — batem.
- Balanças (Q162): 3c+2=14, 2c+5=17, 4c+1=13, 3c+3=18 → 4, 6, 3, 5 kg; itens b) coerentes (na v4 há 3 kg em peças dos dois lados para tirar). Ícones das receitas (Q161), latas (Q168), barras (Q164) e blocos (Q165) contados no desenho.
- Botões: posição da certa varia (Q162: 0,1,2,0; Q169: 1,0,0,1). Todos os SVG ≤ 440 px. Renderização em PNG (Chrome headless) conferida antes e depois das mudanças.
- `python3 -I versoes/validar.py 5 7` → 0 problemas.
