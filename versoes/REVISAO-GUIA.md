# Roteiro de revisão das questões

Objetivo: encontrar e corrigir **questões erradas** e **melhorar o que for claramente melhorável**, sem descaracterizar o caderno. Leia antes `GUIA-QUESTOES.md` (formato, tipos de campo, estilo).

## Arquivos de uma ficha (ano A, ficha F)

| Arquivo | O que contém | Versões |
|---|---|---|
| `originais/A-ficha-FF.json` (fichas 1–10) | as 5 questões originais (`qs` é uma **lista** de `{n, html, gab}`) | versão 1 |
| `A/ficha-FF.json` (fichas 1–10) | `qs: {"n": [v2, v3, v4]}` das 5 originais | versões 2–4 |
| `A/extra-FF.json` (fichas 11–12) | `qs: {"n": [v1, v2, v3, v4]}` dos 10 primeiros problemas | versões 1–4 |
| `A/mais-FF.json` (todas) | `qs: {"n": [v1, v2, v3, v4]}` das 10 questões a mais | versões 1–4 |

A versão `i` de todas as questões aparece junto na rodada `i`. Questões que se referem a outra ("Ainda sobre o gráfico…") devem casar versão a versão.

## O que conferir em CADA versão

1. **Conta certa.** Refaça todas as contas com Python (Fraction/Decimal), a partir dos números do enunciado e do desenho. `data-a` e `gab` devem estar certos e coerentes entre si.
2. **Resposta aceita.** Toda resposta correta razoável que a criança possa digitar deve ser aceita:
   - `t` (texto): variantes comuns com `|` (ex.: com e sem "e" depois de "mil"; "um meio|meio").
   - `f` (fração): compara texto exato — se o enunciado **não** pede "simplificada", aceite as formas equivalentes óbvias com `|`.
   - `h` (hora): manhã/tarde quando o relógio de ponteiros não diz qual (ex.: `3:00|15:00`).
   - `n`: o corretor já aceita 1.346 = 1346 e 2,5 = 2,50; não precisa duplicar.
   - Nunca aceite uma resposta errada.
3. **Uma só resposta.** O enunciado não pode permitir duas respostas certas (empates em "mais votado", arredondamento terminado em 5/50, enigmas com 2 soluções, ordem de fatores quando os campos exigem uma ordem sem `|`).
4. **Desenho bate com o texto e a resposta.** Conte no SVG (por script) objetos, partes pintadas, células da malha, ponteiros (ângulo da hora inclui os minutos), barras do gráfico versus escala, posição na régua/reta, coordenadas. Rótulos não podem ficar cortados nem sobrepostos.
5. **Enunciado claro para a idade.** Frases curtas, sem ambiguidade, palavras que a criança do ano conhece. A pergunta precisa dizer a unidade quando a resposta tem unidade. Os campos precisam deixar claro o que vai em cada um.
6. **Português.** Ortografia, acentos, concordância, crase, "de o" → "do", artigos (um/uma), pontuação, espaço sobrando antes de pontuação.
7. **Nível e BNCC.** Compatível com o ano e o assunto da ficha (sem conteúdo de ano seguinte; 3º ano: divisão exata, tabuada até 10).
8. **Variedade.** Nas 4 versões, a resposta certa de botões/menus não deve estar sempre na mesma posição; versões não podem ser praticamente iguais.
9. **Celular.** SVG com no máximo ~460 px de largura; tabelas grandes dentro de `<div class="tw">`.

## Como corrigir

- **Erros (itens 1–4, 6):** corrija direto.
- **Melhorias claras (itens 5, 7–9):** corrija direto quando a melhoria for objetiva e pequena (reescrever uma frase confusa, aceitar uma variante, redesenhar um SVG que não bate, trocar números para evitar empate).
- **Mudanças grandes ou de gosto** (trocar o tipo de atividade, mudar a didática): **não aplique** — anote como sugestão.
- Edite os JSON **por script Python** (`json.load` → alterar → `json.dump(..., ensure_ascii=False, indent=1)`), mantendo a estrutura. Não mude o número das questões nem a quantidade de versões.
- Depois rode `python3 -I /Users/marcosnoronha/Matemática/versoes/validar.py A F` até dar 0 problemas.
- **Não** edite o HTML, `validar.py`, `montar.py`, nem arquivos de outras fichas. **Não** rode `montar.py`. **Não** faça commit. Use nomes de arquivo únicos na pasta de rascunho (outros revisores trabalham ao mesmo tempo).

## Relatório

Grave `revisao/A-ficha-FF.md` (crie a pasta se não existir) com:

```
# A º ano · ficha F · <título>
## Corrigido
- Q<n> v<i> — <o que estava errado> → <como ficou>
## Melhorado
- Q<n> v<i> — <o que mudou e por quê>
## Sugestões (não aplicadas)
- Q<n> — <ideia>
## Conferido sem problemas
<quantas versões revisadas, que verificações automáticas rodou>
```

Use a numeração interna (`Q<n>`, o número no JSON) e também a posição na ficha quando ajudar (ex.: "Q123 (questão 13 da ficha)"). As 5 originais ficam nas posições 1–5, as `mais` nas posições 6–15 (fichas 1–10); nas fichas 11–12, `extra` = posições 1–10 e `mais` = 11–20.
