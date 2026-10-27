# 4º ano · ficha 12 · Mais probleminhas

## Corrigido
- Q62 v1 (questão 2 da ficha) — "Quanto pesa cada um?" e "os 3 juntos pesam" falando de **caixas** (concordância) → "Quanto pesa cada caixa?", "as 3 caixas juntas pesam", "Cada caixa pesa".
- Q69 v3 (questão 9) — sobra de 4/12 aceitava só "4/12" e "1/3"; faltava a forma equivalente óbvia "2/6" → `4/12|1/3|2/6`. A dica falava em "12 pedaços" numa barra de "12 quadradinhos" → "quadradinhos".
- Q217 v2 (questão 17) — o texto dizia que o sapo pula "de vitória-régia em vitória-régia", mas o desenho e os campos são de **pedras** → "O sapo Tonico pula de pedra em pedra no lago."
- Q220 v1 e v3 (questão 20) — "quantos laranjas" e "quantos peras" (concordância, 2 vezes em cada) → "quantas laranjas" e "quantas peras".
- Q220 v4 — os 5 cachos de uva da balança 2 se sobrepunham (30 bolinhas encostadas umas nas outras) e não dava para contar 5 cachos, que é o dado da questão → redesenhados como 5 cachos separados (6 uvas e um cabinho cada), nas mesmas posições das laranjas da v1; contas e respostas iguais.

## Melhorado
- Q61 v2 e v4 (questão 1) — as dicas entregavam a resposta da pergunta "Qual informação não foi usada?" ("a idade de alguém muda a quantidade de figurinhas?", "a pergunta é sobre balas ou sobre dinheiro?") → dicas gerais: "para cada número do problema, pergunte: ele muda o total de figurinhas / a quantidade de balas?".
- Q62 v2–v4 — "cada um" / "os N juntos" → nome do objeto ("cada melão", "os 4 melões juntos", "cada pacote", "cada tijolo"…), igual à v1.
- Q63 v2 e v4 (questão 3) — "4 vezes menos" / "3 vezes menos" é expressão ambígua (e matematicamente imprecisa) → "a quarta parte do que vendeu no domingo" / "a terça parte do que Rita leu"; dicas ajustadas ("a quarta parte é dividir por 4").
- Q63 v3 — "4 vezes mais andares que o A" (pode ser lido como 8 + 32) → "o quádruplo (4 vezes) dos andares do A", no padrão da v1 (triplo) e v4 (quíntuplo); ganhou a dica que as outras versões têm ("descubra primeiro o prédio B; o C depende dele").
- Q214 v1 (questão 14) — "Marina partiu uma barra de chocolate em quadradinhos" sugere pedaços soltos (aí não haveria quadrados 2 × 2 e 3 × 3) → "A barra de chocolate de Marina é dividida em quadradinhos iguais".
- Q214 v2–v4 — "…lajotas quadradas, assim: Quantos…" (dois-pontos seguidos da pergunta, com a figura só depois) → "…, como na figura. Quantos…".

## Sugestões (não aplicadas)
- Q64 — as pistas dos enigmas de ordem estão em `div.note` (caixa amarela usada para "Dica"); por serem dados do problema, ficariam mais claras em `div.ex` ou numa lista normal.
- Q218 — v2 e v4 (3 dobras) mostram o quadro "2ª dobra"; v1 e v3 (2 dobras) pulam direto de "1ª dobra" para "3 furos/5 furos". Está correto, mas um rótulo "2ª dobra + furos" no último quadro deixaria as 4 versões no mesmo padrão.
- Q220 v4 — pesos pouco realistas: melão de 600 g e cacho de uva de 40 g. Trocar por, por exemplo, cacho de 100 g (melão 1.500 g) exigiria mudar o gabarito (não aplicado).
- Q70 — v1, v3 e v4 são de cartões com algarismos; a v2 é de apertos de mão. Se a ideia for "mesma questão", trocar a v2 por cartões (ou deixar as quatro com contagem de combinações variadas, como está).
- Q68 — v1 e v3 pedem perímetro, v2 e v4 pedem área; dá para alinhar ou manter de propósito como alternância.
- Q62 — os objetos aparecem sempre como caixinhas laranja com "?", mesmo quando são melões ou tijolos; um desenho próprio por versão deixaria mais lúdico.
- Q217 — SVG com 464 px de largura (um pouco acima dos ~460 px); se for mexer, reduzir o espaçamento entre as pedras de 50 para 49 px.

## Conferido sem problemas
80 versões (20 questões × 4) revisadas. Verificações por script (Python, Fraction): todas as contas e `data-a`/`gab` (Q61 informação supérflua, Q62 balanças 3x+2=14 etc., Q63 dobro/triplo/partes, Q65 dias entre datas e horários de chegada, Q67 preço por unidade com escolha certa em posições 1-1-0-0, Q68 perímetro/área, Q69 frações, Q70 contagem de números/apertos por permutação, Q219 semanas mínimas por divisão com resto e sobra). Força bruta de solução única: 4 enigmas de ordem (Q64, uma permutação cada), 4 sudokus 4 × 4 (Q215, 1 solução cada, A–D conferidos, bordas grossas no meio), 4 quadrados mágicos (Q213, linhas, colunas e diagonais), 4 muros mágicos (Q211, incluindo a conferência do topo), 4 cripto-contas de figuras (Q212, figuras identificadas no SVG por forma/cor em cada linha e resolvidas em cadeia). Desenhos conferidos por script e por renderização: objetos nas balanças (Q62: 3, 4, 2, 5), palitos/quadradinhos das sequências (Q66: 3n+1, 2n+1, escadinha, cruz 4n+1), malhas 3×3 a 3×6 (Q214), ângulos dos ponteiros (Q216: 2h25, 1h50, 9h35, 3h10, coerentes com as durações), números das pedras e regras alternadas (Q217), dobras e furos (Q218), cofrinho e etiqueta (Q219), frutas em cada prato das balanças duplas (Q220). Horários: Q216 aceita 12h/24h nas versões da tarde; Q65 v2 e v4 também. Quadrados mágicos e sudokus são SVG de 206–220 px (cabem no celular). `validar.py 4 12`: 0 problemas.
