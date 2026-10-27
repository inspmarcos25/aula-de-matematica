# 3º ano · ficha 5 · Multiplicação

## Corrigido
- Q21 v3 (questão 1 da ficha) — "Quantas limões há ao todo?" → "Quantos limões há ao todo?" (concordância).
- Q143 v2 (questão 8) — "há estes bicicletas" → "há estas bicicletas" (concordância).
- Q146 v1 (questão 11) — Laura e a vovó Cida (duas mulheres): "Os dois juntos" → "As duas juntas".

## Melhorado
- Q25 v1–v4 (questão 5) — cada caixa/estojo desenhava sempre 4 lápis aparecendo, mas o texto diz 12, 8, 6 e 24 por caixa; a criança podia contar 4 e errar. Agora cada caixa tem uma etiqueta com a quantidade (12, 8, 6, 24), que bate com o enunciado.
- Q142 v2 (questão 7) — na formiga, as patas da frente terminavam junto das antenas (pareciam antenas a mais) e as de trás entravam no abdômen. Patas redesenhadas: 6 patas bem separadas, saindo do tórax.
- Q21 v3 — SVG tinha 468 px de largura; reduzido para 460 px (mesmo viewBox).

## Sugestões (não aplicadas)
- Q21, Q141, Q144, Q145 (campos dos fatores "a × b") — a ordem dos fatores já é aceita das duas formas ("4|6" e "6|4"), mas, como o corretor confere cada campo sozinho, ele também aceita "4 × 4" ou "6 × 6" desde que o produto esteja certo. Resolver exige um recurso no corretor (ex.: um atributo de grupo que aceite o par {4, 6} em qualquer ordem) — mudança no HTML, fora do escopo da revisão.
- Q146 — "comprou o triplo de ovos que Laura" é comum em livros, mas "comprou o triplo dos ovos de Laura" soaria mais natural (gosto; não alterado).

## Conferido sem problemas
- 60 versões revisadas (15 questões × 4 versões): Q21–Q25 (originais + ficha-05) e Q141–Q150 (mais-05).
- Contas refeitas por script / conferidas uma a uma: tabuadas da roda (Q22) batem com os números do desenho; dobro/triplo (Q23); armadas (Q24, Q150); tabelas de patas/braços (Q142); números que faltam (Q148, cada um com resposta única); comparações > < = (Q149).
- Desenhos renderizados (qlmanage → PNG) e contados: cestas × frutas (Q21), caixas (Q25), joaninhas e pintinhas (Q141, contagem de círculos por script: 18, 20, 32, 14), veículos e rodas (Q143), pulos na reta (Q144), fileiras × cadeiras (Q145), ovos na caixa (Q146), aquários × peixinhos (Q147) — todos batem com `data-a` e `gab`.
- Posição da resposta certa nos botões da Q143 varia (0, 1, 2, 1); sinais da Q149 variados.
- `python3 -I versoes/validar.py 3 5` → 0 problemas.
