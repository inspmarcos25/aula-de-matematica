# 4º ano · ficha 7 · Grandezas e medidas

## Corrigido
- Q167 v1–v4 (questão 12 da ficha) — faltava o nome do objeto no aviso: "**Atenção:** a não começa no zero!" / "o não começa no zero!" → "a lagarta / o lápis / o giz de cera / o palito de picolé não começa no zero!".
- Q168 v2, v3, v4 (questão 13) — artigos errados: "trilha **do** Entrada até **o** Gruta", "até **o** Lagoa", "**do** Entrada até o Mirante" → "**da** Entrada até **a** Gruta", "até **a** Lagoa", "**da** Entrada até o Mirante".
- Q166 v2, v4 (questão 11) — "**Quanto** limonada há na jarra?" / "**Quanto** água de coco…" → "**Quanta** limonada…" / "**Quanta** água de coco…".
- Q170 v1 (questão 15) — "3 bolos. Cada **uma** leva…" → "Cada **um** leva…".

## Melhorado
- Q161 v1–v4 (questão 6) — item c) "Quantos graus a mais quente tinha **a mais** que a mais fria?" (confuso, "mais" três vezes) → "Qual é a **diferença** de temperatura entre a cidade mais quente e a mais fria?" (mesmo cálculo e resposta).
- Q162 v1–v4 (questão 7) — "4 graus menos que…" / "5 graus mais que…" → "4 graus **a menos** que…" / "5 graus **a mais** que…".
- Q163 v1–v4 (questão 8) — "A que horas vai o filme terminar?" (ordem estranha) → "A que horas o filme vai terminar?" (idem treino, festa, família).
- Q166 v3 — o leite estava pintado de branco puro (#ffffff) sobre a jarra quase branca (#f4fbff), quase sem contraste → cor creme (#fbeccb); nível (450 mL) inalterado.

## Sugestões (não aplicadas)
- Q35 (questão 5) — o desenho sempre mostra **4 copos**, sem rótulo; na v2 a resposta é justamente 4 (pode parecer "dica") e nas outras (8, 6, 10) não bate com o desenho. Melhor desenhar um só copo com o rótulo "250 mL" / "500 mL" / "200 mL".
- Q165 (questão 10) — os rótulos dos pesos (fonte 8,5 px) ficam bem pequenos no celular; aumentar os pesos ou escrever a lista de pesos também no texto.
- Q166 — as 4 versões começam com "Mamãe fez…"; variar a personagem (Papai, Vovó, Tio…).
- Q170 — a) "Quantos gramas de farinha vai precisar?" poderia ganhar o sujeito ("…**ela** vai precisar?" / "…**ele**…").

## Conferido sem problemas
60 versões revisadas (15 questões × 4: originais Q31–Q35, `ficha-07.json` v2–v4, `mais-07.json` Q161–Q170 v1–v4).
- Todas as contas refeitas por script (diferenças de temperatura, durações, conversões h/min/s/dias, km/m, cm/mm, kg/g, L/mL, somas da trilha, sobras de receita) — todos os `data-a` e `gab` batem.
- Termômetros lidos por script a partir do SVG: Q31 (escala 0–40 °C, risquinho = 2 °C: 28/18/34/12 °C) e Q161 (escala 10–40 °C, risquinho = 1 °C: as 12 cidades batem com o gabarito, sem empate de mais quente/mais fria).
- Ponteiros dos relógios por ângulo: Q32 (8 relógios) e Q163 (4) — minuto certo e ponteiro da hora avançado conforme os minutos (ex.: 7h20 → 220°, 4h25 → 132,5°). Q163: "à tarde" aceita 3:20|15:20 e o término 17:10|5:10; "de manhã" aceita só a hora da manhã (o texto diz qual).
- Réguas fora do zero (Q167): pontas pelas linhas tracejadas e pela figura — 3→10,5 cm; 2→14,3 cm; 4→9,6 cm; 1,5→10,2 cm.
- Jarras (Q166): marcas de 50 mL e nível 650/800/450/850 mL; balanças (Q165): pesos somam 2.700/2.750/1.500/1.250 g; previsão (Q162): maior diferença única em cada versão; cronômetros (Q164) batem.
- Selects/botões: posição da resposta varia entre versões (Q161, Q162, Q164, Q170). Todos os SVG ≤ 440 px. Renderização em PNG (Chrome headless) conferida visualmente.
- `python3 -I versoes/validar.py 4 7` → 0 problemas.
