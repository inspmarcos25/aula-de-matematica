# 3º ano · ficha 8 · Medidas de tempo

## Corrigido
- Q38 v3 (questão 3 da ficha) — "Quantos sextas-feiras tem o mês?" → "Quantas sextas-feiras…" (concordância).
- Q38 v4 (questão 3) — "Quantos segundas-feiras" → "Quantas segundas-feiras".
- Q175 v3 (questão 10) — "A gelatina precisa mexer por 10 minutos" (a gelatina não mexe sozinha) → "É preciso mexer a gelatina por 10 minutos."
- Q177 v1 (questão 12) — "As férias do meio do ano começam é em julho" → "começam em julho".
- Q178 v3 (questão 13) — "Três vizinhas" com Heitor no grupo → "Três vizinhos".
- Q180 v3 (questão 15) — rótulo "hoje" sobre o domingo ficava em y=3 do SVG (cortado no topo) → movido para o lado direito do círculo do domingo (x=135, y=16 no SVG), sem sobrepor a segunda-feira.

## Melhorado
- Q37 v4 (questão 2) — "meio dia = 12 horas" se confunde com "meio-dia" (12h) → "metade de 1 dia = 12 horas".
- Q171 v1–v4 (questão 6) — "Na cozinha tem dois relógios…", mas o desenho mostra 1 digital + 3 de ponteiros → "O relógio digital da cozinha da vovó marca 09:15. Qual destes relógios de ponteiros mostra a mesma hora?" (idem sala de aula, quarto de Davi, biblioteca).
- Q173 v2 (questão 8) — jogo de futebol "do recreio" durando 1h15 não é plausível → "na quadra do bairro".
- Q175 v1 (questão 10) — "O ovo cozido precisa ficar na panela 12 minutos" → "Para cozinhar, o ovo precisa ficar 12 minutos na panela."
- Q178 v4 (questão 13) — "115 min" em fonte 16 quase encostava na borda do mostrador do cronômetro → fonte 14.

## Sugestões (não aplicadas)
- Q37 v4 — "1 semestre" pode ser palavra nova para o 3º ano; avaliar trocar por "meio ano = 6 meses" ou manter e explicar.
- Q179 (questão 14) — item b) (horas de sono atravessando a meia-noite) é o mais difícil da ficha; considerar uma dica do tipo "conte de 21h até 24h e depois de 0h até 6h".
- Q40 v4 (questão 5) — "3 treinos por semana em 4 semanas" é mais multiplicação do que medida de tempo; poderia virar uma conversão semanas↔dias como as outras versões.

## Conferido sem problemas
- 15 questões × 4 versões = 60 versões revisadas (originais + ficha-08 + mais-08).
- Relógios: ângulo dos ponteiros calculado por script em todos os relógios (Q36, Q171, Q173, Q174) — hora e minuto batem com `data-a`/`gab`, ponteiro da hora avançando com os minutos (erro ≤ 0,1°); campos `h` de relógio de ponteiros aceitam manhã e tarde (Q36, Q173); Q172 pede o formato 0–23h e aceita só a forma de 24h, como deve ser (o corretor já aceita "06:30" = "6:30").
- Calendários (Q38 ×4, Q176 ×4): dias da semana de cada data conferidos com `datetime`, número de dias do mês, contagem de sábados/domingos/sextas/segundas, dias pintados e contas de diferença de dias — tudo certo.
- Contas: durações (Q39, Q174, Q179), somas de tempo (Q173), conversões (Q37, Q40, Q175, Q178), meses (Q177) e roda dos dias (Q180) refeitas por script — todas certas; posição da resposta certa varia nos botões (Q171: B, C, A, B; Q178: Beto, Enzo, Gabi, Kaká em posições 2, 3, 1, 2).
- SVGs com no máximo 460 px de largura; rótulos conferidos (Q179 linha do tempo, Q180 roda, Q178 cronômetros).
- `python3 -I validar.py 3 8` → 55 versões conferidas, 0 problema(s).
