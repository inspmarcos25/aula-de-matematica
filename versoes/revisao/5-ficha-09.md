# 5º ano · ficha 9 · Geometria (plano cartesiano, polígonos, ampliação e sólidos)

## Corrigido
- Q181 v4 (questão 6 da ficha, mapa do tesouro) — "O pirata **Lola**" e "o pirata anda" → "**A** pirata Lola" e "**a** pirata anda" (concordância com nome feminino).
- Q190 v4 (questão 15, pirâmide de base hexagonal) — a aresta escondida que vai do vértice de trás até o topo ficava a menos de 2 px da aresta visível da frente. Parecia uma linha só, e não dava para contar as 12 arestas no desenho. Redesenhei a base, com o hexágono "deitado" (vértices em 0°, 60°, …). Agora as 2 arestas laterais escondidas ficam bem separadas das 4 visíveis. Continuam 7 sólidas + 5 tracejadas = 12 arestas, com o tracejado desenhado por último. A tabela não mudou.

## Melhorado
- Q183 v1–v4 (questão 8, cerca da horta) e Q185 v1–v4 (questão 10, quadriláteros na malha) — o quadrado também é retângulo (e também losango e paralelogramo), mas o menu só aceita uma opção. Uma criança que escolhesse "retângulo" para o quadrado levaria errado com uma resposta verdadeira. Os enunciados agora pedem o **nome mais preciso**:
  - Q183: "Nome mais preciso da forma da cerca: [menu]".
  - Q185: "Escolha o nome mais preciso de cada um (…)".
- Q44 v2 e v4 (questão 4, ampliação) — a malha tinha 12 × 5 quadradinhos. A figura ampliada (6 × 6 na v2, 4 × 6 na v4) não cabia nela. A malha passou a ter 6 linhas. Nas v1 e v3, a ampliada (6 × 4 e 8 × 4) já cabia.
- Q45 v1 (questão 5, original, prisma triangular) — o enunciado não explicava o tracejado, ao contrário das v2–v4. Acrescentei "(as linhas tracejadas são as arestas escondidas)".

## Sugestões (não aplicadas)
- Q190 (questão 15) — a relação de Euler (V + F = A + 2) é conteúdo do 6º ano (EF06MA17). No 5º ano, a BNCC (EF05MA16) pede reconhecer os sólidos e as planificações e comparar faces, vértices e arestas. A questão funciona, porque a fórmula é dada, mas pode virar "conte no desenho e complete" para os sólidos que aparecem.
- Q187 v2/v4 (questão 12) — "ficou 2 vezes menor" é comum na escola, mas é impreciso. "ficou com a **metade** das medidas" ou "dividiu cada medida por 2" seria mais rigoroso. Além disso, v2 e v4 têm as mesmas respostas finais (20 cm e 100 cm). Vale trocar os números de uma delas.
- Q43 v1 (questão 3, original) — o triângulo "equilátero" A mede 80,6 / 80,6 / 80 px. Visualmente está certo, e os risquinhos mandam. Se quiserem exatidão, basta subir o topo de y = 20 para y = 20,7.
- Q186 v1 e v2 (questão 11) — as duas versões dão 108 quadradinhos na ampliada. O raciocínio é diferente (×4 e ×9), mas daria para variar o resultado.

## Conferido sem problemas
- **60 versões revisadas** (15 questões × 4): `originais/5-ficha-09.json` (v1), `5/ficha-09.json` (v2–v4) e `5/mais-09.json` (v1–v4).
- **Coordenadas (Q41, Q181–Q183):** posição de cada ponto calculada pela escala do SVG (x = 30 + 28·X, y = 178 − 28·Y), com todos os gabaritos certos.
  - Q181: saídas do pirata até o baú: (1,1)→(4,3), (0,2)→(3,5), (2,0)→(5,4), (1,2)→(3,6).
  - Q182: percursos do robô simulados: (3,5)/8, (5,2)/9, (1,3)/9, (1,1)/11. Nenhum percurso sai da malha.
  - Q183: D e perímetros conferidos (14, 12, 18, 16).
- **Polígonos (Q42):** número de vértices de cada polígono contado no SVG, todos batendo com o menu.
- **Q184:** contagem de vértices das placas e placa redonda conferidas.
- **Triângulos (Q43):** os 3 lados de cada triângulo medidos. A classificação real bate com os risquinhos e com o gabarito nas 12 figuras.
- **Quadriláteros (Q185):** classificados automaticamente por lados paralelos, ângulos retos e lados iguais (16 figuras, todas certas). Todos os vértices caem nos pontinhos da malha.
- **Ampliação:**
  - Q44: 4×, 9×, 2× (perímetro) e 24 quadradinhos.
  - Q186: malha original e ampliada lidas célula a célula. A ampliada é exatamente a original ×2/×3; contagens 27→108, 12→108, 12→48, 10→90.
  - Q187: contas refeitas.
- **Sólidos:**
  - Q45: arestas visíveis e tracejadas conferidas (prisma triangular 5/6/9, pirâmide quadrada 5/5/8, paralelepípedo 6/8/12, pirâmide pentagonal 6/6/10). O tracejado é mesmo o escondido e é desenhado por último.
  - Q190: os 4 desenhos têm 18, 10, 15 e 12 arestas. Euler foi conferido nas 12 linhas da tabela.
- **Planificações:**
  - Q188: cubo em cruz; pirâmide quadrada; prisma triangular com triângulos equiláteros de lado = largura dos retângulos (40); tetraedro.
  - Q189: os 4 moldes do dado dobrados por cálculo 3D, com faces opostas X/Y = 6/5, 5/4, 6/5, 6/3.
- **Escolha (ch) da Q186:** a posição da resposta certa alterna (0, 1, 0, 1).
- Todos os SVGs foram renderizados (qlmanage) e olhados. Largura máxima de 440 px; nenhum rótulo cortado (checagem por script).
- `python3 -I validar.py 5 9` → 0 problemas.
