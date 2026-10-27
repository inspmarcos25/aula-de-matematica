# 4º ano · ficha 10 · Estatística e probabilidade (tabelas, gráficos e chances)

## Corrigido
- Q48 v1 (questão 3, livros por mês, original) — as barras de **fevereiro (22)** e **março (18)** paravam entre as linhas da escala, que vai de 5 em 5. Assim a criança não conseguia ler o valor exato, e o item c) (total) dependia disso. As barras foram redesenhadas para **25** e **20**, em cima das linhas. Abril continua sendo o maior e o item b) continua 15. O total mudou de **85 → 90** (`data-a` e `gab`).
- Q191 v4 (questão 6, gols) — "Águias **tem** quantos a mais que Onças?" estava com erro de concordância → "As Águias fizeram quantos **gols** a mais que as Onças?".
- Q197 v2 e v4 (questão 12, soma de dois dados) — o `gab` punha a contagem do resultado errado primeiro: "soma 9 (1 contra 4)" e "soma 6 (2 contra 5)". Ficou "soma 9 (**4 contra 1**)" e "soma 6 (**5 contra 2**)", no mesmo padrão da Q49.
- Q198 v3 (questão 13, cartas) — mesmo problema no `gab`: "estrela (3 contra 4)" → "estrela (**4 contra 3**)".

## Melhorado
- Q48 v3 (questão 3, gincana) — cada barra tinha a cor de outra equipe: a equipe Azul era laranja, a Verde era azul-clara, a Amarela era roxa e a Vermelha era verde. Isso confundia a leitura. Agora cada barra tem a cor da própria equipe (azul, verde, amarela, vermelha). Os valores não mudaram.
- Q191 v1–v3 (questão 6, pictograma) — o item b) não dizia a unidade. Agora diz: "quantos **votos** a mais", "quantos **sucos** a mais" e "Nina colou quantas **figurinhas** a mais".
- Q192 v4 (questão 7, flores) e Q196 v4 (questão 11, saquinho) — o "rosa" (#ff8a80, cor de salmão) ficava parecido com o "vermelho" (#d6455f) do mesmo desenho. Ele foi trocado por um rosa bem claro (#f79ac0). As contagens não mudaram.
- Q193 v2 e v4 (questão 8, barras duplas) — nas 4 versões, a resposta certa do menu era sempre a 2ª opção. Mudei a ordem das opções: na v2 ficaram em ordem alfabética (morango passa a ser a 4ª) e na v4 em ordem invertida (gato passa a ser a 3ª).
- Q196 v3 (questão 11) — havia só **1** bolinha laranja entre 7, e a resposta esperada era "provável". Agora são **3 laranjas e 4 verdes**, e as três respostas continuam as mesmas.
- Q197 v4 — o texto "= 10" encostava na borda do desenho. O SVG foi alargado de 180 para 192 px.
- Q198 v1–v4 (questão 13) — o enunciado dizia que as cartas "**foram** viradas para baixo", mas o desenho mostra as cartas de frente. Ficou "Estas cartas **vão ser** viradas para baixo e embaralhadas."
- Q199 v1–v4 (questão 14, três gráficos pequenos) — os números dos eixos e os nomes embaixo das barras estavam com letra de 8 px, ilegível no celular. Passaram para 10 px. Conferi no desenho: nada ficou cortado nem sobreposto.

## Sugestões (não aplicadas)
- Q196 (questão 11) — a palavra "provável" sugere "mais da metade". Nas v1, v2 e v4, as bolinhas pedidas são 3 de 8, 2 de 10 e 3 de 9. Vale trocar a opção por "**possível**" (certo / possível / impossível) ou usar cores que sejam maioria no saquinho.
- Q191 v2 (questão 6) — o símbolo do pictograma é uma laranja e uma das linhas também se chama "Laranja". Um copinho de suco evitaria a confusão "cada laranja vale 5".
- Q199 (questão 14) — mesmo com a letra maior, três gráficos lado a lado em 440 px ficam pequenos no celular. Vale pensar em colocá-los um embaixo do outro (ou 2 + 1).
- Q200 (questão 15) — nas 4 versões, o número apagado pela mancha é sempre o que saiu mais vezes. Daria para variar, mas isso muda os números da tabela.
- Q50 (questão 5, roleta) — as v1, v2 e v3 usam a mesma distribuição (4, 3 e 1 fatias, nas mesmas posições), mudando só as cores. Daria para variar o desenho.
- Q192 v2 (questão 7) — o reflexo curvo das bolinhas de gude parece uma "carinha triste". É só estética.

## Conferido sem problemas
- 60 versões revisadas (15 questões × 4): 5 originais (v1), `4/ficha-10.json` (v2–v4) e `4/mais-10.json` (v1–v4).
- Contas refeitas por script:
  - Tabelas de dupla entrada da Q46 e da Q195 (linhas, colunas e total geral).
  - Mais votado da Q47, sem empate.
  - Dado: chances da Q49; total que falta, par, "menor que" e mais frequente na Q200.
  - Tabela de somas da Q197: casas a completar, quantas vezes cada soma aparece e comparação das chances.
- Gráficos lidos do SVG por script:
  - Q48: 4 px por unidade, todas as barras partindo do 0.
  - Q193: 11 px por unidade. Totais de meninos e meninas batem com a Q194 versão a versão (26/22, 20/21, 26/20, 24/24). Em "meninas mais que meninos" só uma categoria vence; os empates, como natação 6 = 6, não contam.
  - Q199: 7,5 px por unidade. Só um gráfico bate com a tabela em cada versão (A, C, B, C).
- Pictogramas da Q191: símbolos contados por linha, multiplicados pelo valor da legenda (2 ou 5). Não há símbolos pela metade.
- Desenhos contados:
  - Roletas da Q50: fatias contadas por cor (4/3/1 e 3/2/2/1).
  - Balões, bolinhas de gude, pirulitos e flores da Q192: totais 20, 20, 20 e 22.
  - Saquinhos da Q196.
  - Cartas da Q198: número e desenho de cada carta, maior que N, par contra símbolo, desenho com menos chance.
  - Dados do exemplo da Q197.
- Posição da resposta certa nos botões varia (Q49, Q194, Q197, Q198, Q199). Todos os SVGs têm até 440 px. Tabelas estão dentro de `div.tw`.
- Desenhos renderizados (qlmanage) e olhados, antes e depois das mudanças.
- `python3 -I validar.py 4 10` → 0 problemas.
