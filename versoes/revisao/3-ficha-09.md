# 3º ano · ficha 9 · Grandezas e medidas (comprimento, massa e capacidade)

## Corrigido
- Q188 v1–v4 (questão 13 da ficha, balde) — o traço **0** da escala ficava 6 px acima do fundo do balde, mas a água começava no fundo: pela escala, o balde já tinha água abaixo do zero e cada nível ficava fora de lugar em relação ao fundo. A escala foi refeita: agora o 0 fica no fundo (y=170) e o valor máximo perto da borda, com espaçamento igual. A água foi redesenhada a partir dos mesmos números da resposta (4/10, 7/10, 3/8 e 5/12 L). As respostas não mudaram.

## Melhorado
- Q41 v3 (questão 1, borracha na régua) — a parte azul da borracha cobria o contorno do lado direito. Agora o contorno é desenhado por cima, e a borracha continua de 0 a 4 cm.
- Q188 v4 — a frase repetia o verbo: "enchendo o balde para encher a piscininha". Ficou "enchendo o balde para levar água até a piscininha".

## Sugestões (não aplicadas)
- Q184 (questão 9, copos) — a v2 (2 L em copos de 250 mL = 8) é a mais difícil das quatro para o 3º ano. Vale pensar numa dica do tipo "Quantos copos enchem 1 litro?", sem dar a resposta.
- Q186 (questão 11, mochilas) — mochilas de 6 e 7 kg são pesadas demais para uma criança de 8 anos. Dá para trocar por massas menores (2 a 5 kg), mas isso muda os números, os rótulos e as respostas.
- Q188 — o balde é mais largo em cima, então litros iguais deveriam ficar mais próximos perto da borda. A escala com espaços iguais é uma simplificação aceitável para a idade. Só vale mudar se quiserem um desenho realista (por exemplo, um balde de paredes retas).
- Q183 (questão 8, balança) — o campo "Prato da direita: __ kg" ficaria mais claro como "Os pesos do prato da direita somam: __ kg".

## Conferido sem problemas
- 60 versões revisadas (15 questões × 4): 5 originais (v1) + `3/ficha-09.json` (v2–v4) + `3/mais-09.json` (v1–v4).
- Contas refeitas por script: Q42, Q44, Q45, Q183, Q184, Q186, Q187, Q189 e Q190. `data-a` e `gab` batem em todas.
- Régua conferida por coordenadas do SVG:
  - Q41: o 0 fica em x=14 e cada cm mede 30 px. Lápis de 0 a 9 e de 0 a 7, borracha de 0 a 4, canudo de 0 a 11.
  - Q181: começo e fim da lagarta ou minhoca (círculos ± raio) caem exatamente nas linhas tracejadas 2–9, 3–11, 1–7 e 4–13.
- Q182: o topo da cabeça da girafa e o topo da copa da árvore caem exatamente em 5/3, 4/7, 6/2 e 5/6 m.
- Contagens nos desenhos: pacotes, latas e potes na Q44 (3, 3, 4, 2); garrafas na Q45 (4, 3, 2, 7); pesos da balança na Q183; rótulos das mochilas na Q186; pedaços da fita na Q190 (4 ou 5).
- Posição da opção certa em botões e menus varia entre as versões (Q44, Q182, Q185, Q186, Q189). Todas as larguras de SVG têm até 430 px.
- Desenhos renderizados e olhados (qlmanage): nenhum rótulo cortado ou sobreposto.
- `python3 -I validar.py 3 9` → 0 problemas.
