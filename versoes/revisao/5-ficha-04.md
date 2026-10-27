# 5º ano · ficha 4 · Números decimais (operações com decimais e dinheiro)
## Corrigido
- Q132 v1 (questão 7, cronômetros) — "Na **60 metros** do recreio" (faltava a palavra "corrida") → "Na **corrida de 60 metros** do recreio".
- Q137 v2 (questão 12, caixinha de suco avulsa × pacote) — concordância: "cada caixinha de suco pode ser **comprado sozinho (avulso)**" e "6 caixinhas **comprados um a um**" → "comprada sozinha (avulsa)" / "compradas uma a uma"; botão "6 avulsos" → "6 avulsas" (gab também). Etiqueta do desenho "caixinha de suco / (avulso)" → "**1** caixinha de suco / (avulsa)", igual às outras versões ("1 pote…", "1 picolé…").
- Q137 v4 (questão 12, canetas) — mesmo erro de concordância: "cada caneta colorida pode ser comprado sozinho (avulso)", "10 canetas comprados um a um" → "comprada sozinha (avulsa)", "compradas uma a uma"; botão e gab "10 avulsos" → "10 avulsas"; etiqueta "(avulso)" → "(avulsa)".
- Q140 v2 (questão 15, três primas na pizzaria) — "Quanto **cada um** vai pagar?", "Cada um pagou…", "Quanto cada um recebe de troco?" → "cada uma" nas três frases.
- Q18 v1 (original, questão 3) e v4 — o 3º/5º caderno passava da borda do SVG (v1: retângulo até x=122 numa figura de 120 px; v4: até y=74 numa figura de 72 px) e ficava cortado → `width/height/viewBox` ajustados (125×73 e 185×77). v2 e v3 também ganharam margem para o contorno não ser cortado (155×75, 95×71). Conferido renderizando.

## Melhorado
- (nenhuma além das correções acima)

## Sugestões (não aplicadas)
- Q137 v2 e v4 — nessas duas versões o pacote sai **mais caro** que os avulsos (bom para mostrar que é preciso conferir); está correto, só vale saber que é intencional. Se preferir, a nota pode lembrar "nem sempre o pacote é mais barato!".
- Q135 — "Encheram a moto … com 10 litros" pode sugerir tanque cheio; "Colocaram 10 litros na moto…" ficaria mais neutro (não é erro).
- Q138 — a dica "a vírgula anda para a esquerda" é a forma usual em sala; alguns professores preferem "os algarismos andam para a direita/esquerda". Manter conforme a forma que as crianças aprendem na escola.

## Conferido sem problemas
60 versões (15 questões × 4). Por script com `Decimal`: Q17 (soma, subtração com reserva e ×), Q18, Q19 (sobra após dois gastos), Q20 e Q138 (×/÷ 10 e 100), Q16 (frações decimais e formas simplificadas aceitas com `|`), Q131 (soma dos itens da nota = total e troco, itens lidos do SVG), Q132 (menor tempo e diferença 1º–último; nome certo em posições variadas no menu), Q133 (comprimento de cada lápis medido no SVG: ponta do lápis − 0, escala 40 px/cm → 9,4/6,7, 8,3/4,8, 7,5/9,2, 6,1/8,9; cor do lápis bate com o texto), Q134 (visor da balança: cheia − vazia), Q135 (preço da bomba no SVG = texto; ×10 e ×n), Q136 (valores nos cofrinhos e quanto falta), Q137 (avulsos × pacote, botão certo alternando 0/1/1/0), Q139 (operação inversa), Q140 (conta ÷ pessoas, troco; nº de pessoas no SVG = texto). Todos os SVGs renderizados no Chrome headless (rótulos sem corte nem sobreposição; larguras ≤ 440 px). `validar.py 5 4`: 0 problemas.
