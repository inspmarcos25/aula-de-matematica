# 4º ano · ficha 1 · Números até 99.999
## Corrigido
- Q108 v2 (questão 13 da ficha) — concordância: "setenta mil **quatrocentos** e seis sementes" → "setenta mil **quatrocentas** e seis sementes" (sementes é feminino). Resposta 70.406 não muda.
- Q108 v4 (questão 13 da ficha) — concordância: "vinte e cinco mil e **trezentos** tampinhas" → "vinte e cinco mil e **trezentas** tampinhas". Resposta 25.300 não muda.
- Q107 v3 (questão 12 da ficha) — "**1** unidades" → "**1** unidade".
- Q103 v4 (questão 8 da ficha) — "No mapa **do** caça ao tesouro" → "No mapa **da** caça ao tesouro".
- Q102 v1–v4 (questão 7 da ficha) — no desenho do painel, o arco pontilhado (raio menor que meia corda, então o navegador aumentava o raio para 105) saía por cima da borda do painel e passava em cima do rótulo "km" → arco redesenhado dentro do painel (`M55 124 A110 110 0 0 1 275 124`) e "km" puxado para perto dos números (x=236, fonte 15). Renderizado e conferido: nada sai da borda nem fica sobreposto. Os algarismos do hodômetro não mudaram.
## Melhorado
- Q106 v1–v4 (questão 11 da ficha) — a dica dizia "trocar 10 delas por 1 ficha **da fileira de cima**". Na v2 não há fileira de 1.000 (a fileira acima da de 100 é a de 10.000) e na v3 não há fileira de 10, então a dica podia induzir a uma troca errada → "trocar 10 delas por 1 ficha que vale 10 vezes mais!" (vale para todas as versões).
- Q104 v2 (questão 9 da ficha) — "três jogos **na final do campeonato**" (uma final é um jogo só) → "três jogos **na última rodada do campeonato**".
- Q1 v1 e v3 (questão 1 da ficha) — gabarito para os pais com vírgula entre o milhar e a centena ("Quarenta e cinco mil, trezentos e oito", "Oitenta mil, quinhentos e quarenta") → sem vírgula, como na norma e nas v2/v4. Só o `gab` mudou; o `data-a` não mudou.
## Sugestões (não aplicadas)
- Q1 — política do "e" depois de "mil": não mexi, como foi pedido. Situação atual: a v1 (45.308) e a v3 (80.540) aceitam só a forma da norma (sem "e" antes de centena não redonda), e não há forma alternativa de norma a acrescentar. A v2 (27.091) e a v4 (63.017) aceitam a forma da norma ("… mil e noventa e um", "… mil e dezessete") e **também** a forma sem "e". Nas 4 versões a forma da norma culta é aceita.
- Q105 — os "furos" dos ingressos são círculos brancos com contorno inteiro. Entre dois ingressos vizinhos os círculos se sobrepõem (aparece um "anel duplo"), e o da direita do último ingresso (cx=450, r=10) encosta na borda do SVG. É só estética: daria para desenhar meias-luas ou afastar os ingressos 10 px.
- Q106 v2/v3 — a fileira vazia (1.000 na v2, 10 na v3) não aparece no desenho. Mostrar a fileira com o rótulo e nenhuma ficha deixaria mais claro que aquela ordem vale 0.
- Q102 — o artigo antes dos nomes varia ("família de Pedro", "de Ana Clara", "do Davi", "da Júlia"). Os dois jeitos estão certos; daria para uniformizar.
## Conferido sem problemas
60 versões revisadas (15 questões × 4): originais (v1), ficha-01 (v2–v4) e mais-01 (101–110, v1–v4).
Verificações por script:
- Extenso: Q1 e Q108 conferidos contra os números.
- Decomposição: Q2.
- Quadro de ordens: Q3 (sem algarismo repetido).
- Cartões: Q4 (maior número e menor com 5 algarismos, sem zero na frente).
- Ordem decrescente: Q5.
- Ábaco: Q101 (contas por haste, inclusive o item b, sem passar de 9).
- Hodômetro: Q102 (algarismos do SVG; +1.000 e +100, inclusive 29.950 → 30.050).
- Reta numérica: Q103 (tracinhos de 1.000 em 1.000 e posição de A/B/C).
- Telões: Q104 (maior e menor sem empate; cor de cada placa bate com o nome).
- Ingressos: Q105 (antecessor e sucessor).
- Fichas por fileira: Q106 (contagem e total, com trocas).
- Números secretos: Q107.
- Trem: Q109 (padrão ±; 3º e 5º vagão contando a partir da locomotiva).
- Valor do algarismo: Q110 (uma só opção certa).

Todos os SVGs foram renderizados e olhados. Todos têm no máximo 460 px. Fora o caso já corrigido da Q102, nenhum rótulo fica cortado ou sobreposto. A posição da resposta certa nos botões varia entre as versões: Q104 (a: 1,2,0,1; b: 2,1,1,0) e Q110 (1,3,2,0).
`validar.py 4 1`: 0 problemas (55 versões).
