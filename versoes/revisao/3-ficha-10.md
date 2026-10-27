# 3º ano · ficha 10 · Geometria e estatística

## Corrigido
- Q193 v4 (questão 8 da ficha) — no palhaço, a gravata-borboleta (2 triângulos de 18 px) ficava espremida entre a cabeça (base em y=104) e o corpo (topo em y=118). Os vãos brancos ficavam contornados pelas bordas da cabeça e do corpo e pareciam mais 2 triângulos (um "retângulo com X"), o que deixava a contagem de triângulos ambígua (5 ou 7). → O corpo, os braços, os botões e os pés desceram 10 px (`<g transform="translate(0,10)">`, altura do SVG 238 → 248) e a gravata foi centralizada no vão. Agora aparecem só 2 triângulos soltos. As contagens continuam 5 · 4 · 6.
- Q192 v4 (questão 7) — a porta da barraca (um triângulo com contorno escuro) tinha a ponta exatamente no vértice escondido (55,80), onde se encontram as 3 arestas tracejadas. As linhas da porta pareciam arestas e confundiam a contagem de vértices e arestas. → A porta ficou menor (ponta em y=93) e sem contorno, só a mancha verde-escura. Conferi: 5 faces · 6 vértices · 9 arestas (6 contínuas + 3 tracejadas).
- Q196 v3 (questão 11) — "O mais votado foi:" referia-se a *brincadeira* → "A mais votada foi:".
- Q198 v3 (questão 13) — alfaces é feminino: "Quantos na sexta?" / "Quantos a mais na segunda…" → "Quantas…" (2 trocas).

## Melhorado
- Q196 v3 — a opção "Esconde" virou "Esconde-esconde", no rótulo do pictograma, nas opções do menu, no `data-a` e no `gab`. O pictograma ficou 20 px mais largo (280 → 300, conteúdo deslocado com `translate(20,0)`), para o rótulo maior não ser cortado na borda esquerda. Conferi renderizando.
- Q192 v3 — a linha da tampa da caixa de sapato (contínua, escura, 1,6 px) podia ser contada como aresta → ficou num vermelho mais escuro e mais fina (1,2 px). Continua visível como detalhe, mas não se confunde com as arestas.
- Q193 v2 — as 3 "estrelinhas" (círculos) ficam fora do foguete e a criança podia não contá-las (o gabarito pede 5 círculos). → "Davi desenhou um foguete no céu só com figuras planas. Quantas há de cada tipo no **desenho todo**?"
- Q200 v1–v4 (questão 15) — os itens b, c e d ("sair um número par: [escolha]") não diziam o que escolher. Acrescentei ao enunciado: "Nos itens **b**, **c** e **d**, escolha se é **certo**, **possível** ou **impossível**."
- Q194 v1–v4 (questão 9) — o glacê dos biscoitos tinha o atributo `stroke` repetido (`stroke="#2b2b3a" … stroke="none"`): é HTML inválido e quebra a renderização como SVG/XML. Tirei o `stroke="none"` repetido. Nada muda na tela, porque `stroke-width="0"`.
- Q46 v1–v4 (questão 1) — SVG com 480 px de largura (o limite é ~460) → `width="460" height="123"`, com o mesmo `viewBox`. O desenho fica igual, só um pouco menor.

## Sugestões (não aplicadas)
- Q192 v4 — o termo **prisma** é adequado: a BNCC EF03MA14 cita "prismas retos" no 3º ano. A criança não precisa saber o nome, só contar; o desenho e "barraca" já mostram o sólido. Se quiser reforçar: "…de um **prisma** de base triangular (as duas pontas da barraca são triângulos)".
- Q195 — v1 e v4 têm a mesma resposta no item a (cubo). Para variar, a v4 a) poderia descrever o bloco retangular por vértices e arestas ("8 vértices, 12 arestas e faces que **não** são todas iguais").
- Q49 v3 — pergunta a diferença (cachorro − peixe), e as outras versões perguntam o total. Está certo e casa com a Q48 v3, mas a habilidade muda um pouco entre as rodadas. Se quiser uniformizar: "quantos alunos votaram ao todo? (36)".
- Q50 — o desenho é sempre o mesmo pote/cesto, mas o texto fala em "caixa", "saco" e "saquinho". Poderia trocar "caixa/saco" por "pote" ou desenhar um saquinho.
- Q191 — v1 e v4 repetem 3 dos 4 objetos (dado, lata de suco e cone/chapéu). Daria para trocar um deles por pirâmide (ex.: embalagem de chocolate em pirâmide), a única opção do menu que nunca é resposta.

## Conferido sem problemas
- 60 versões revisadas (15 questões × 4): Q46–Q50 (originais + `ficha-10.json`) e Q191–Q200 (`mais-10.json`).
- Todos os SVGs foram renderizados (qlmanage) e conferidos visualmente. As medições foram feitas por script:
  - **Q48**: alturas das barras em relação à escala de 0 a 14: v1 8/12/5/10 (total 35), v2 10/6/12/3 (31), v3 14/10/4/8 (diferença 10), v4 12/8/6/2 (28). Sem empate no mais votado nem no menos votado. A Q49 casa versão a versão.
  - **Q198**: comprimento das barras em relação à escala de 5 em 5: todos os valores batem. Não há empate no maior nem no menor; as diferenças estão certas (10, 20, 15, 20).
  - **Q196**: ícones por linha × 2 batem com as respostas, sem empate no mais votado.
  - **Q197**: risquinhos (grupos de 5 + soltos) batem com 12/7/9/4, 8/13/6/3, 11/14/5/9 e 16/7/4/10, sem empate no maior nem no menor.
  - **Q199**: setores iguais por cor: v1 azul 4, vermelho 2, amarelo 2, verde 1; v2 amarelo 4, verde 3, azul 2, vermelho 1; v3 rosa 5, verde 2, amarelo 2, azul 1; v4 laranja 4, azul 3, roxo 2, verde 1. A resposta "Sim/Não" varia de posição.
  - **Q50**: contagem de bolas por cor 6/2, 3/7, 4/4 e 2/5. A posição da resposta certa varia (0, 1, 2, 0).
  - **Q47 e Q194**: número de lados das figuras, comprimento dos lados (quadrado ≠ retângulo) e trapézio isósceles conferidos.
  - **Q192**: arestas contínuas e tracejadas contadas uma a uma (cubo e bloco 12, pirâmide 8, prisma 9); faces e vértices também batem.
  - **Q193**: elementos `polygon`, `rect` e `circle` contados, e os "quadrados" conferidos (largura = altura).
  - **Q200**: números diferentes nos saquinhos e classificação certo/possível/impossível.
- Q46, Q191, Q195: sólidos e objetos batem com as letras e o gabarito; não há duas respostas certas.
- `python3 -I validar.py 3 10` → 0 problemas.
