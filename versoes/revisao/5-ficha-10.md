# 5º ano · ficha 10 · Estatística e probabilidade (gráficos, tabelas, média e chances)

## Corrigido
- Q50 v2 (questão 5, duas moedas) — as duas moedas eram iguais (as duas com "1" no desenho), e o texto só dizia "duas moedas". A criança podia responder **3** (contando "cara e coroa" uma vez só), mas o gabarito é **4** e separa cara-coroa de coroa-cara. Agora o texto diz "**duas moedas**, uma de **1 real** e outra de **50 centavos**", e a segunda moeda do desenho mostra "50". A resposta continua 4.
- Q48 v4 (questão 3, circo) — o texto falava em "ingressos vendidos **no fim de semana**", mas a tabela traz quinta e sexta. Ficou "de **quinta a domingo**".
- Q196 v1 (questão 11, basquete) — "Total de pontos em **todas as jogos**" → "em **todos os jogos**".
- Frações equivalentes que não eram aceitas, em campos que não pedem a forma simplificada:
  - Q49 v2 (questão 4, campo "Fração"): agora aceita **2/6**, além de 4/12 e 1/3.
  - Q197 v3 (questão 12, roleta): agora aceita **2/6**, além de 4/12 e 1/3.
  - Q198 v2 (questão 13, cartas): agora aceita **2/6**, além de 4/12 e 1/3.
  - Q198 v3: agora aceita **2/4**, além de 4/8 e 1/2.
  - O campo "Simplificada" da Q49 continua aceitando só a forma irredutível.

## Melhorado
- Q191 v3 (questão 6, picolés) — a barra de **chocolate** era azul e a de **morango** era laranja. Agora a de chocolate é marrom e a de morango é rosa. Os valores não mudaram (conferido no desenho).
- Q192 v1–v4 (questão 7, médias) — a dica dizia "divida pelo **número de colunas** de cada cor". Isso podia confundir, porque cada cor tem 4 barras e o gráfico tem 8 colunas no total. Agora diz "divida pela **quantidade de rodadas / meses / dias / partidas**".
- Q194 v1–v4 (questão 9, pictograma) — o item c) não dizia a unidade e escrevia dia da semana com letra maiúscula no meio da frase ("Terça tem quantos a mais que Quarta?"). Ficou, por exemplo, "Na terça foram vendidas quantas **casquinhas** a mais que na quarta?". Fiz o mesmo com livros, figurinhas e maçãs.
- Q195 v3 (questão 10, bichos) — o texto dizia que as crianças "disseram qual bicho **têm**", mas as perguntas falam em "escolheram", e uma criança pode ter mais de um bicho. Ficou "votaram no **bicho de estimação preferido**".
- Q199 v2–v4 (questão 14, caixas) — a menina se chamava **Bia** nas 4 versões. Agora são Bia, **Nina**, **Sofia** e **Lia**, sem repetir os nomes das outras questões da mesma rodada.

## Sugestões (não aplicadas)
- Q199 v3 — para comparar 2/5 com 3/6 "com o mesmo denominador", a criança precisa chegar a 30. A dica poderia sugerir também comparar com a **metade** (3/6 é metade, 2/5 é menos que a metade).
- Q197 — as cores da roleta não têm legenda. Na v1, o "vermelho" (#d6455f) pode parecer rosa-escuro. Uma legenda pequena com o nome das cores (ou um tom de vermelho mais puro) evitaria dúvida.
- Q198 — o texto diz que Pedro "embaralhou estas cartas", mas o desenho mostra as cartas de frente e em ordem. Poderia ser "Pedro vai embaralhar estas cartas, virar para baixo e sortear uma".
- Q48 (originais e v2–v4) — as tabelas não estão dentro de `div.tw`. Hoje são estreitas (2 colunas) e cabem no celular, mas ficaria mais padronizado.

## Conferido sem problemas
- 60 versões revisadas (15 questões × 4): `originais/5-ficha-10.json` (v1), `5/ficha-10.json` (v2–v4) e `5/mais-10.json` (v1–v4).
- Contas refeitas por script:
  - Médias da Q47 (8, 5, 11, 40, todas inteiras).
  - Totais e diferenças da Q48.
  - Tabelas de dupla entrada da Q195.
  - Valor que sumiu do placar na Q196 (média × quantidade − soma).
  - Q50: 12, 4, 8 e 18 resultados.
- Gráficos lidos do SVG por script:
  - Q46: todos os pontos caem nas linhas de 2 em 2 °C. Mais quente e mais frio sem empate.
  - Q191: as barras caem nas linhas da escala. Totais 16/8, 80/60, 180/160 e 36/32. Em cada versão, só um período tem a barra laranja maior que a azul.
  - Q192: médias inteiras (4/2, 20/15, 45/40, 9/8). Casam versão a versão com a Q191.
  - Q193: os pontos caem nas linhas de 2 em 2 cm. A maior subida é única (+6, +6, +6, +8).
- Pictogramas e risquinhos contados por script:
  - Q194: símbolos inteiros e meios símbolos, legenda 10/5.
  - Q200: grupos de 5 com risco atravessado. Totais 35, 36, 36 e 37. Vencedor sem empate.
- Desenhos contados por script:
  - Bolas da Q49 e das caixas da Q199.
  - Fatias da roleta da Q197: 8, 10, 12 e 6 partes. Na comparação, só uma cor vence.
  - Cartas da Q198.
- Posição da resposta certa varia nos botões (Q192, Q197, Q199) e nos menus (Q46, Q191, Q193, Q200). Todos os SVGs têm até 424 px.
- Desenhos renderizados (qlmanage) e olhados, antes e depois das mudanças.
- `python3 -I validar.py 5 10` → 0 problemas.
