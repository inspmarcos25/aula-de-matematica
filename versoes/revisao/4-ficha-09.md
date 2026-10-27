# 4º ano · ficha 9 · Geometria (ângulos, simetria, retas, sólidos e localização)

## Corrigido
- Q44 v1 (questão 4 da ficha, cubo original) — o SVG tinha 100 px de altura, mas o vértice de baixo do cubo fica em y=105: a ponta de baixo do cubo aparecia cortada. Altura e viewBox passaram para 110. As respostas não mudaram (6 · 8 · 12).

## Melhorado
- Q185 v4 (questão 10, mapa do bairro de Felipe) — o item a) perguntava sobre a Rua Chile e a Rua Ipiranga. Elas são concorrentes, mas no desenho não se cruzam: só se encontrariam bem fora do mapa, o que confunde a criança. Agora o item pergunta sobre a **Rua Brasil e a Rua Uruguai**, que se cruzam no mapa (45°). A resposta continua "concorrentes" e o item d) não muda (1).
- Q189 v1–v4 (questão 14, giro do ponteiro) — os ponteiros cinza e azul (62 px) passavam por cima dos números do relógio (o "12" na v1/v3, o "3" e o "9" na v2, o "5" na v4). Encurtei os dois ponteiros para 54 px, na mesma direção. Ângulos e respostas não mudaram.
- Q181 v2 e v4 (questão 6) — concordância no gabarito: "1 menores · 1 maiores" → "1 menor · 1 maior" e "1 retos" → "1 reto".

## Sugestões (não aplicadas)
- Q41 v2/v3 (questão 1) — "agudo" e "obtuso" vão além do que a BNCC pede no 4º ano (EF04MA18 fala em ângulos retos e não retos). Os parênteses explicam bem os termos. Só vale trocar se quiserem seguir a BNCC à risca (por exemplo: "menor que o ângulo reto").
- Q185 v3 — a etiqueta "Rua dos Girassóis" (125 px, na vertical) fica por cima da Rua das Rosas e da Rua das Dálias à direita do mapa. Dá para ler, mas um nome mais curto (por exemplo, "Rua dos Ipês") deixaria o mapa mais limpo.
- Q182 v3 — o lugar "pipoca" ficaria mais natural como "pipoqueiro" ou "carrinho de pipoca" ("Fica de frente para: pipoca"). A mudança mexe no desenho e no menu.
- Q43 v2 (C) e v4 (A) — as retas perpendiculares estão inclinadas (em X ou giradas 30°) e não têm marquinha de ângulo reto. Está correto, mas fica difícil para a idade. Uma dica do tipo "use o canto de uma folha" (como na Q181) ajudaria.

## Conferido sem problemas
- 60 versões revisadas (15 questões × 4): 5 originais (v1), `4/ficha-09.json` (v2–v4) e `4/mais-09.json` (v1–v4).
- **Ângulos calculados pelas coordenadas:**
  - Q41: v1 42°/90°/124°, v2 90°/40°/130°, v3 125°/50°/90°, v4 35°/140°/90°. A opção certa varia de posição.
  - Q181: ângulos internos de cada polígono, com soma conferida (540°, 360°, 720°, 360°). Contagem: 3/0/2, 2/1/1, 0/0/6, 1/2/1. Todos os vértices caem nos nós da malha.
- **Retas (Q43 e Q185):** ângulo e interseção de cada par.
  - Q43: paralelas = 0°, perpendiculares = 90,0°, concorrentes entre 55° e 59°. Nenhuma concorrente fica perto de 90°.
  - Q185: as perpendiculares contadas no item d) foram conferidas (2, 2, 1, 1).
- **Simetria (Q42):** as 4 grades foram desenhadas espelhadas em texto: losango, coração, casinha com porta e árvore em camadas, todos reconhecíveis. Em todas as versões, cols = 2·axis e as células ficam na metade esquerda.
- **Eixos de simetria (Q188):** posição de cada eixo comparada com o centro da figura (sim/não certos nas 12 figuras).
- **Sólidos (Q44 v2–v4):**
  - Faces, vértices e arestas: prisma triangular 5/6/9, pirâmide quadrada 5/5/8, pirâmide triangular 4/4/6.
  - Arestas tracejadas conferidas como as realmente escondidas.
- **Planificações (Q186):** cruz do cubo, prisma triangular (triângulos equiláteros de lado igual à largura dos retângulos), pirâmide quadrada e tetraedro, todas válidas.
- **Dado (Q187):** faces opostas na tira de 4 e nas abas de cima e de baixo. A=6/B=3, A=1/B=5, A=5/B=6, A=1/B=3, sempre com soma 7.
- **Localização:**
  - Q45: posição de cada desenho na malha (12 itens).
  - Q183: os 4 percursos do robô simulados (E3 direita, A4 esquerda, B2 esquerda, B3 baixo).
  - Q184: deslocamentos barco→X e objeto da casa pedida.
  - Q182: giros (1/4, meia, 3/4 de volta) a partir da direção inicial.
- **Relógios (Q189):** 12→3 = 15 min, 3→9 = 30, 12→9 = 45, 2→5 = 15. As setas giram no sentido horário.
- **Q190:** objetos e sólidos conferidos.
- Todos os SVGs foram renderizados (qlmanage) e olhados. Largura máxima de 420 px; fora os casos corrigidos acima, nenhum rótulo cortado ou sobreposto.
- `python3 -I validar.py 4 9` → 0 problemas.
