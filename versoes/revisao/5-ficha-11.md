# 5º ano · ficha 11 · Probleminhas

## Corrigido
- Q203 v1–v4 (questão 13 da ficha) — "leva **no máximo** 4/5/6/4 pessoas" não garantia uma resposta só: dava para dividir a fila de outro jeito (ex.: v1, 27 pessoas: a viagem com só 3 pode ser a 1ª e a última sair com 4; ou 8 viagens, 5 de 4 + 2 de 3 + 1 de 1), então "Quantas pessoas vão na última viagem?" tinha mais de uma resposta. Acrescentado "A cabine/O elevador/A cabine/O barquinho só sai **cheia/cheio**; só a **última** viagem pode sair com menos gente." A dica antiga ("na última viagem pode ir menos gente — mas ela também conta!") ficou repetindo a regra → "faça a divisão e pense no resto: essas pessoas também precisam de uma viagem." Respostas mantidas (27/7/3/14h36; 23/5/3/9h26; 31/6/1/11h25; 26/7/2/16h20).
- Q201 v1 e v4 (questão 11) — gabarito "sobram 1 adesivo" / "sobram 1 colar" → "sobra 1 adesivo" / "sobra 1 colar".

## Melhorado
- Q55 v4 (questão 5) — "Um pedaço ficou **4 vezes maior** que o outro" pode ser lido como "5 vezes o outro" → "Um pedaço ficou com o **quádruplo** (4 vezes) do comprimento do outro." (resposta 9 m e 36 m mantida).
- Q58 v3 (questão 8) — "quantos caminhos haverá ao todo?" → "quantos caminhos **de casa à escola** haverá ao todo?" (deixa claro que não é para contar os trechos casa–praça).
- Q60 v4 (questão 10) — a resposta certa dos botões estava na 3ª posição nas duas versões com botões (v3 e v4) → v4 reordenada (Tubarões, Águias, Leões; certa na 1ª).
- Q207 v4 (questão 17) — "Quanto suco vai sobrar?" numa versão de **limonada** → "Quanta limonada vai sobrar?"

## Sugestões (não aplicadas)
- Q209 — nas versões 1, 2 e 3 a quantidade de pacotes dá sempre 2 · 4 · 3 (só a v4 dá 2 · 4 · 5). Vale variar os números (ex.: lotação de pacote) para as respostas não se repetirem entre rodadas.
- Q210 e Q60 v4 — os dois problemas são de pontos de campeonato (vitória 3, empate 1); na rodada 4 aparecem quase iguais. Trocar o contexto da Q60 v4 (ex.: uma conta de feira/lanche como nas v1 e v3).
- Q57 — média aritmética: está na ficha 10 do 5º ano (originais), então serve; só lembrar que a BNCC coloca média formalmente no 6º/7º ano. Pode manter como desafio.
- Q58 v4 (6 times, todos contra todos = 15 jogos) é bem mais difícil que v1–v3 (princípio multiplicativo direto). A dica ajuda; se quiser equilibrar, usar 4 ou 5 times.
- Q202 — "Ele é mais curto quantos metros?" é coloquial; poderia ser "Quantos **metros** a menos ele tem?".

## Conferido sem problemas
80 versões revisadas (Q51–Q60 em `extra-11.json`, Q201–Q210 em `mais-11.json`). Todas as contas refeitas em Python (Decimal) a partir do enunciado e do desenho: lanches, troco, porcentagens e frações de quantidade (Q51–Q53, Q59–Q60), proporcionalidade (Q54), partes/diferença (Q55–Q56), médias (Q57), contagem (Q58), trocas com resto lidas da tabela do SVG (Q201: 3/4, 5/3, 4/3, 6/2), caminhos lidos do mapa (Q202), divmod e horário da última viagem (Q203), caminho de volta (Q204), cofrinhos — empate em 5, 7, 6 e 7 semanas com o mesmo valor nos dois (Q205), garrafas/copos/sobra (Q207), barras de fração (Q208), pacotes fechados e desconto (Q209), vitórias/empates do time apagado e campeão único (Q210). Força bruta no número secreto (Q206): solução única nas 4 versões (345, 648, 435, 748), e cada pista extra é necessária. SVGs renderizados no Chrome headless e conferidos por script: pessoas na fila = 27, 23, 31, 26; barras da Q208 com 2+1, 3+2, 3+1, 5+3 quadradinhos e chave sobre as partes a mais; rótulos sem corte nem sobreposição; todos com ≤ 440 px. Posições das respostas certas nos botões variadas (Q202: 1ª, 2ª, 1ª, 2ª; Q210 menu: 4ª, 1ª, 2ª, 4ª). `validar.py 5 11`: 0 problemas. (Obs.: `mais-11.json` foi regravado com `indent=1`, como pede o roteiro; antes estava numa linha só — o diff fica grande, mas o conteúdo mudou só nos pontos acima.)
