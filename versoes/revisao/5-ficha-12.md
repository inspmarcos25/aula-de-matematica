# 5º ano · ficha 12 · Mais probleminhas

## Corrigido
- Q62 v1 (questão 2 da ficha) — gabarito "1 caixas" (concordância) → "1 caixa".
- Q62 v3 e v4 — no desenho, as caixas e o peso do prato da esquerda passavam para fora do prato (4 sacos + peso iam de x=12 a 144; 5 latas + peso iam de x=0 a 156, com a 1ª lata cortada na borda do SVG) → caixas empilhadas em 2 fileiras (2+2 e 3+2), tudo dentro do prato; mesmas quantidades (4 e 5) e mesmos pesos.
- Q66 v4 (questão 6) — "Quantos cadeiras" (3 vezes) → "Quantas cadeiras".
- Q67 v2 e v3 (questão 7) — "Uma caixa plástica / caixa-d'água … Quando está cheio" → "Quando está cheia".
- Q69 v4 (questão 9) — "1 bolas vermelhas" → "1 bola vermelha".

## Melhorado
- Q61 v3 (questão 1) — a dica "o número do tênis ajuda a correr? E a fazer a conta?" entregava a resposta de "Qual informação não era necessária?" → dica geral das outras versões ("marque só os dados que a pergunta usa"). Tirado também "Ele tem 12 anos", que era um 2º dado sobrando (a pergunta fala em "a informação").
- Q61 v4 — "A fita é azul e tem 2,5 cm de largura" → "A fita tem 2,5 cm de largura" (a cor era um 2º dado desnecessário fora das opções).
- Q62 v1–v4 — "Quanto pesa o prato da esquerda?" (pode ser lido como o peso do próprio prato) → "Quanto pesa tudo o que está no prato da esquerda?".
- Q64 v3 (questão 4) — faltava "Cada um tem só uma." que as outras versões têm (garante a lógica de eliminação).
- Q65 v2 e v3 (questão 5) — "Um trem sai da rodoviária" → "da estação"; "Um carro sai da rodoviária" → "de casa". Gabarito v2 "3 h 00 min" → "3 h".
- Q68 v2 (questão 8) — rótulos "manhã: / tarde: / noite:" minúsculos → "De manhã: / À tarde: / À noite:" (as outras versões começam com maiúscula).
- Q211 v1–v4 (questão 11) — "números das casas com letra" num muro de tijolos → "números dos tijolos com letra" (os campos dizem "Tijolo A").
- Q214 v1 (questão 14) — "Bia partiu uma barra de chocolate em quadradinhos" sugere pedaços soltos (sem quadrados 2 × 2 e 3 × 3) → "A barra de chocolate de Bia é dividida em quadradinhos iguais".

## Sugestões (não aplicadas)
- Q61–Q70 (problemas 1–10) — só Q62 e Q69 têm desenho; o guia pede SVG em pelo menos 6 de 10. Bons candidatos: Q66 (palitos/mesas de cada figura — hoje são só pílulas "Figura 1: 4", sem figura), Q67 (aquário/caixa em bloco com o nível da água), Q70 (pilhas de figurinhas/cestas), Q63 (etiquetas de preço).
- Q66 v4 — as pílulas dizem "Figura 1/2/3", mas a história é de mesas; "1 mesa: 4 · 2 mesas: 6 · 3 mesas: 8" e "com 5 mesas / com 10 mesas" ficaria mais natural.
- Q216 — o ponteiro dos minutos passa por cima dos números do mostrador (ex.: cobre o "8" em 7h40); encurtar o ponteiro para não cobrir os algarismos.
- Q211 v2 — C e D valem os dois 2,25; correto (o muro não exige números diferentes), mas valores distintos evitariam a criança achar que errou.
- Q220 v4 — abóbora de 1,8 kg desenhada só um pouco maior que o melão de 0,9 kg; ok, mas um desenho mais "abóbora" (gomos) ajudaria a reconhecer.

## Conferido sem problemas
80 versões (20 questões × 4) revisadas. Verificações por script (Python, Fraction):
- Contas e `data-a`/`gab` de todas as versões: Q61 (compras e troco), Q62 (balanças 2x+3=x+10 etc.), Q63 (descontos de 10/25/50%; escolha certa nas posições 0-1-2-1), Q65 (duração em minutos e chegada), Q66 (3n+1, 2n+1, 5n+1, 2n+2), Q67 (volume e litros), Q68 (frações do que sobrou), Q69 (chances; formas simplificadas aceitas), Q70 (média e quanto cede), Q216 (soma de durações + fuso), Q217 (regras alternadas), Q218 (camadas, furos, área), Q219 (porcentagem da mesada e meses), Q220 (balanças em cadeia).
- Força bruta / solução única: 4 sudokus 6 × 6 (Q215: 1 solução cada, grade completa válida, gabarito "por linha" confere, bordas grossas após a coluna 3 e as linhas 2 e 4); 4 quadrados mágicos com decimais (Q213: sistema linear com posto completo → solução única, números todos diferentes, existe sempre uma linha/coluna/diagonal completa para começar); 4 muros mágicos (Q211: lidos do SVG, todas as somas conferem, inclusive dados redundantes como 7,1 e 17,4); 4 cripto-contas de figuras (Q212: figuras identificadas no SVG por forma, permutação de algarismos → 1 solução cada, nenhum número começando com 0); enigmas de lógica Q64 (1 solução cada).
- Desenhos conferidos por script e renderização (Chrome headless): itens nas balanças (Q62: 2/1, 3/1, 4/2, 5/2; Q220: 1:4 e 2:5, 1:4 e 2:3, 1:6 e 3:8, 1:2 e 1:6), bolas das urnas (Q69), ângulos dos ponteiros (Q216: 7h40, 6h25, 9h50, 5h45), números das pedras (Q217) e distratores que falham em algum número, dobras/furos e proporções do papel dobrado (Q218), malhas 3×3 a 6×3 (Q214: 14, 20, 26, 32), barras de meta (Q219).
- Fusos (Q216) corretos: Acre −2 h de Brasília, Manaus −1 h de São Paulo, Cuiabá −1 h de Recife, Fernando de Noronha +1 h de Porto Alegre. Horários aceitam 12h/24h quando a chegada é à tarde (13:30|1:30, 15:30|3:30, 16:00|4:00, 15:00|3:00, 13:35|1:35; Q65 v3 15:20|3:20); o corretor aceita "16h" como 16:00.
- Celular: SVGs ≤ 456 px; sudoku (6 × ~44 px) e quadrados mágicos dentro de `div.tw`; `<div>` balanceados em todas as versões.
- `validar.py 5 12`: 0 problemas.
