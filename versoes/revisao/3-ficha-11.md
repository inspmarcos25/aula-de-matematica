# 3º ano · ficha 11 · Probleminhas

## Corrigido
- Q204 v1–v4 (questão 14 da ficha) — "leva **no máximo** 8 pessoas" permitia outras divisões (ex.: 30 = 8+8+7+7, só 2 viagens cheias), então "Quantas viagens saem cheias?" e "Quantas pessoas vão na última?" tinham mais de uma resposta → acrescentado: "O barco só sai **cheio**; só a **última** viagem pode sair com menos gente."
- Q208 v3 e v4 (questão 18) — "entre 50 e 80" / "entre 20 e 40": 80, 20 e 40 estão na tabuada (do 8 / do 4), então a contagem podia ser 3 ou 4 (v3) e 4 ou 6 (v4) → pista virou "Ele é **maior que** X e **menor que** Y", e a pergunta e a dica foram ajustadas do mesmo jeito. O número secreto continua único (conferido por força bruta).
- Q210 v2 e v4 (questão 20) — "Lara e Duda têm, juntos" / "Bela e Rosa têm, juntos" (duas meninas) → "juntas", também no rótulo do desenho ("40 juntas", "48 juntas").

## Melhorado
- Q51 v2, v3, v4 (questão 1) — rótulo "Primeiro, depois de ganhar" não combinava com a história (a biblioteca **comprou**, a granja **recolheu**, Caio recebeu mesada) → "depois de comprar", "depois da mesada", "depois de recolher". Na v3 (dinheiro) os dois campos ganharam "R$".
- Q53 v4 (questão 3) — Gabi e Téo apareciam do nada → "entre 4 amigos: Gabi, Téo, Rui e Bia."
- Q57 v3 (questão 7) — pagou com nota de R$ 100,00: "Quanto sobrou?" → "Quanto recebeu de troco?" e "Com o troco, dá para comprar…".
- Q59 v3 (questão 9) — "tinha 4 cm de altura e cresce" (tempo verbal misturado) → "tem 4 cm de altura hoje e cresce".
- Q60 v3 (questão 10) — "2 dúzias de banana" → "2 dúzias de bananas".
- Q204 v3 e v4 — a 4ª fileira de pessoas da fila aparecia dentro da água → fileiras um pouco mais juntas, todas acima da água (contagem 40 e 31 conferida no SVG).
- Q208 v1 e v2 — mesma redação "maior que / menor que" das v3–v4, para as 4 versões ficarem iguais na estrutura (aqui não havia ambiguidade).

## Sugestões (não aplicadas)
- Q204 — divisão com resto: está de acordo com a BNCC do 3º ano (EF03MA08 pede divisão "com resto zero e com resto diferente de zero"), e a questão é bem guiada (viagens cheias → quem sobra → total), com o desenho para contar. Mas o GUIA-QUESTOES diz "3º ano: divisão exata"; vale alinhar o guia com a BNCC ou aceitar esta como exceção consciente.
- Q55, Q58, Q59, Q53 — as 4 versões não têm a mesma estrutura de campos: Q55 v1–v2 têm 1 campo e v3–v4 têm 2 (e 2 operações); Q58 v4 (cartões 1, 5, 8) pede também o maior número; Q59 v3 (plantinha) não pede o total como as outras; Q53 v3/v4 fazem uma 2ª pergunta de outro tipo. Não está errado, mas a dificuldade varia de rodada para rodada.
- Q201 v2/v4 — os "patos" parecem pintinhos (bico triangular pequeno); um bico achatado laranja deixaria claro.
- Q205 — a frase "A compra 2 tem 2 lápis a mais que a compra 1" já faz a comparação pela criança; numa das versões poderia ficar só o desenho, para ela descobrir sozinha.
- Q203 — a resposta certa do botão está na 2ª posição em 3 das 4 versões (v2–v4); dá para inverter a ordem dos botões na v3 ou v4.

## Conferido sem problemas
80 versões revisadas (Q51–Q60 em `extra-11.json`, Q201–Q210 em `mais-11.json`). Todas as contas refeitas em Python a partir do enunciado e do desenho (data-a e gab coerentes). Força bruta nos enigmas: Q56 (bicicletas/triciclos, idades, galinhas/coelhos, bombons — solução única nas 4), Q58 v4 (6 números), Q208 (número secreto único), Q207 (cofrinhos se igualam numa só semana), Q204 (divmod). SVGs renderizados (Chrome headless) e conferidos por script: bichos e patas (Q201), trocas (Q202), distâncias dos caminhos (Q203), pessoas na fila (Q204: 30, 27, 40, 31), preços das compras (Q205), ônibus (Q206), cofrinhos (Q207), barras de partes (Q210). Posição da resposta certa nos botões variada (Q54, Q57). `validar.py 3 11`: 0 problemas.
