# 5º ano · ficha 6 · Multiplicação e divisão

## Corrigido
- Nenhum erro encontrado: todas as contas, gabaritos, `data-a` e desenhos conferem nas 60 versões.

## Melhorado
- Q153 (questão 8 da ficha) v1–v4 — "Quantos ônibus ficam completamente cheios?" → "Enchendo um ônibus de cada vez, quantos ficam completamente cheios?" (deixa claro que não se trata de distribuir os alunos igualmente entre os ônibus; só assim a resposta é o quociente).
- Q160 (questão 15) v1–v4 — "repartiu **todos** os picolés igualmente em 8 freezers, e os que sobraram…" era contraditório → "repartiu os picolés igualmente em 8 freezers, o máximo possível em cada um, e os que sobraram…".
- Q152 (questão 7) v1–v4 — acrescentado "Todas as caixas aparecem na figura." (o palete é desenhado de frente; evita a dúvida sobre caixas escondidas atrás).
- Q155 (questão 10) v1–v4 — "O sítio recebeu…" → "A horta recebeu…", coerente com o início ("Na horta, cada canteiro…").
- Q157 (questão 12) v1–v4 — expressão "( 15 + 9 ) × 4 − …" sem os espaços dentro dos parênteses, no mesmo padrão das outras questões.

## Sugestões (não aplicadas)
- Q151 (questão 6) — o desenho do estádio é o mesmo nas versões 1 e 3 (4 setores) e nas 2 e 4 (6 setores), e as faixas tracejadas de cada setor não representam as fileiras; poderia variar a forma/cores ou mostrar algumas fileiras com rótulo "24 fileiras".
- Q158 (questão 13) — os colchetes [ ] aparecem em uma expressão por versão; conferir se o pai quer esse conteúdo no 5º ano (a BNCC trata parênteses no 5º ano; colchetes e chaves são mais típicos do 6º).
- Q154 (questão 9) — a porta do prédio é só uma faixa de 4 px no chão; poderia ser desenhada maior (puramente estético).

## Conferido sem problemas
- 15 questões × 4 versões = 60 versões (Q26–Q30 originais + versões 2–4; Q151–Q160 v1–v4).
- Todas as contas refeitas por script Python (multiplicações, divisões exatas, divisões com resto/quociente/arredondamento para cima, expressões com ordem das operações, parênteses e colchetes, máquina de engrenagens, árvore de cálculo).
- Desenhos contados por script: estádio (4/6 setores com rótulos S1…), paletes (15 = 5×3, 16 = 4×4, 18 = 6×3, 20 = 5×4 caixas), prédio (48 = 4×12, 60 = 6×10, 42 = 3×14, 55 = 5×11 janelas acesas), canteiros (63 = 9×7, 48 = 8×6, 72 = 9×8, 60 = 12×5 mudas), ônibus com a capacidade certa, engrenagens e árvore com os números e operações do enunciado. SVGs da árvore, das engrenagens, do ônibus e do prédio renderizados e inspecionados (sem rótulos cortados). Larguras ≤ 460 px.
- Q159: em cada item só uma das 3 expressões dá o valor pedido; posição da certa varia (0/2, 1/0, 2/1, 1/2).
- `python3 -I validar.py 5 6`: 55 versões conferidas, 0 problemas.
