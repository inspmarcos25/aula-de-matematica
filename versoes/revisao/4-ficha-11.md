# 4º ano · ficha 11 · Probleminhas

## Corrigido
- Q203 v1–v4 (questão 13 da ficha) — dois problemas de resposta única. (1) "leva **no máximo** 9 pessoas" permitia dividir de outro jeito (ex.: 76 = 4 viagens de 9 + 5 de 8, só 4 cheias), então "Quantas viagens saem cheias?" e "Quantas pessoas vão na última?" não tinham uma só resposta → acrescentado "O elevador/bondinho só sai **cheio**; só a **última** viagem pode sair com menos gente." (2) "Cada viagem (ida e volta) demora 3 min. Quanto tempo leva para todos subirem?": na última viagem as pessoas já chegaram em cima antes da volta, então 27 min ou 25,5 min → pergunta virou "Quanto tempo leva para fazer **todas** as viagens?" (respostas 27, 32, 45, 24 min mantidas). A dica antiga ("a última viagem sai mesmo sem estar cheia") ficou redundante com a regra → "faça a divisão e pense no resto: essas pessoas também precisam de uma viagem."
- Q205 v1 (questão 15) — Ana e Bia (duas meninas): "Os dois guardam", "os dois terão", "cada um terá" → "As duas guardam", "as duas terão", "cada uma terá".
- Q209 v2 (questão 19) — Clara e Bia: "Os dois juntos têm" → "As duas juntas têm".
- Q208 v4 (questão 18) — gabarito "sobram 1" → "sobra 1".

## Melhorado
- Q52 v1 e v3 (questão 2) — "Quantas vans são necessárias" / "Quantas mesas é preciso montar" → com "**no mínimo**", para "lugares vazios" (v3) depender de uma só quantidade de mesas.
- Q53 v4 (questão 3) — 3/5 de R$ 500,00 sem nenhum apoio (a v2, com 2/3, tem dica) → dica "ache primeiro quanto vale 1/5 do dinheiro."
- Q55 v1–v4 (questão 5) — "multipliquei por 3 **e depois** somei 7 **e deu** 52" (dois "e" seguidos) → "multipliquei por 3, depois somei 7 e deu 52" (igual nas 4).
- Q57 v2 (questão 7) — "Dona Cida" no meio da frase → "dona Cida" (como "seu Raimundo" da Q54).
- Q209 v1–v4 (questão 19) — "Assim, Lucas tem 84 a mais" sugeria que o "a mais" é consequência do triplo (é um dado novo) e não dizia de quê → "Lucas tem **84 figurinhas a mais**" (pontos / bolinhas nas outras versões).
- Q210 v2 e v4 (questão 20) — "Ainda falta dar" (vovó não precisa dar todos os biscoitos) e "Ainda falta usar" (corda) → "Ficaram na lata:" e "Sobraram:", com a legenda do desenho "falta" → "ficou na lata" / "sobrou" (conferido no render, sem sobreposição).

## Sugestões (não aplicadas)
- Q53 v2 e v4 — "2/3 de 240" e "3/5 de R$ 500,00" são frações **não unitárias** de quantidade; a ficha 5 do 4º ano só calcula frações unitárias (1/4 de 20, 1/3 de 18…), e a BNCC do 4º ano (EF04MA09) foca nas unitárias. Com as dicas dá para fazer, mas a dificuldade fica acima de v1/v3. Pode trocar por frações unitárias (ex.: 1/3 de 240, 1/5 de R$ 500,00) ou manter como desafio consciente.
- Q58 — as 4 versões são contagens de tipos bem diferentes (combinação 3×3×2, apertos de mão, números com cartões e o 0, caminhos 3×4); apertos de mão é bem mais difícil que caminhos. Vale deixar o mesmo tipo nas 4 rodadas.
- Q60 e Q53 v3 — estrutura de campos varia entre versões (Q60 v2 tem botões + 2 campos; v1/v3/v4 têm 2 campos de conta; Q53 v3 tem 3 campos). Não está errado.
- Q206 — a pista "ele é ímpar/par" não é necessária (a soma dos algarismos já fixa as unidades); serve só para conferir. Se quiser que ela pese, a pista da soma poderia virar "a soma é maior que X".

## Conferido sem problemas
80 versões revisadas (Q51–Q60 em `extra-11.json`, Q201–Q210 em `mais-11.json`). Todas as contas refeitas em Python a partir do enunciado e do desenho (data-a e gab coerentes): trocas com resto (Q201), somas dos caminhos lidas do mapa (Q202), divmod e tempo (Q203), trem de trás para frente com valores do SVG e sem descer mais gente do que havia (Q204), cofrinhos semana a semana — empate único em 8, 7, 11 e 6 semanas (Q205), pacotes fechados (Q208), pedaços do diagrama (Q209), frações da barra (Q210), galinhas/coelhos, carros/motos, idades e figurinhas (Q56). Força bruta no número secreto (Q206): solução única nas 4 versões (3.607, 2.646, 8.415, 4.832); Q58 v3 (9 números) conferido por enumeração. SVGs renderizados no Chrome headless e conferidos por script: pessoas no elevador/bondinho = lotação (9, 8, 12, 7), corredores na pista (4, 6, 6, 7), pedaços das barras (3/4/2/3 pedaços), partes pintadas das barras de fração (3+4, 3+5, 2+3, 5+2), rótulos sem corte. Posição da resposta certa nos botões variada (Q202: 2ª, 1ª, 1ª, 2ª). `validar.py 4 11`: 0 problemas.
