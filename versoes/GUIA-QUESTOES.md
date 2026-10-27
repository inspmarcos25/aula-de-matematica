# Guia para escrever questões do Caderno de Matemática

Público: crianças do 3º ao 5º ano (8 a 11 anos). Tudo em português do Brasil, linguagem simples e acolhedora, nomes brasileiros variados, contextos do dia a dia de criança (escola, recreio, festa junina, feira, futebol, figurinhas, bichos de estimação, parque, aniversário, sorveteria, horta, biblioteca).

## Onde ficam

- `originais/<ano>-ficha-XX.json`: as 5 questões originais de cada ficha de assunto. **Use como referência de estilo, nível e HTML.**
- `<ano>/ficha-XX.json`: 3 versões novas de cada questão original (mais exemplos de estilo e de desenhos SVG).
- `<ano>/mais-XX.json`: **10 questões a mais** de cada ficha de assunto, com 4 versões cada.

## Formato do `mais-XX.json`

```json
{"ficha": 3, "qs": {"121": [v1, v2, v3, v4], "122": [...], ..., "130": [...]}}
```

- Números das questões: `100 + 10*(ficha-1) + 1` até `+10`. Ficha 1 → 101–110, ficha 2 → 111–120, …, ficha 10 → 191–200, ficha 11 (Probleminhas) → 201–210, ficha 12 (Mais probleminhas) → 211–220.
- Cada versão: `{"html": "...", "gab": "..."}`. `gab` é o gabarito curto mostrado aos pais (ex.: `"3.777 · 4.224 · 965"`; milhar com ponto, decimal com vírgula).
- As 4 versões são da **mesma** questão (mesmo tipo de raciocínio e mesma estrutura de campos), mudando números, nomes, objetos, contexto e desenho. A versão `i` aparece na rodada `i`.
- Questões em sequência que dependem uma da outra (ex. "Ainda sobre o gráfico…") devem casar versão a versão.

## Campos de resposta (`data-t`)

| data-t | Elemento | data-a (resposta) | Como corrige |
|---|---|---|---|
| `n` | `<input class="in" data-t="n" data-a="1346" style="width:70px" inputmode="decimal" placeholder="" autocomplete="off" spellcheck="false">` | número sem ponto de milhar; decimal com vírgula (`2,50`); alternativas com `\|` | compara o valor (aceita 1.346, 1346, 2,5 = 2,50) |
| `t` | `<input class="in" data-t="t" data-a="dois mil e cinco" style="width:380px" ...>` | texto em minúsculas sem vírgulas; alternativas com `\|` (números por extenso: aceite **sempre** com e sem o "e" depois de "mil", ex. `sete mil e cinquenta e dois\|sete mil cinquenta e dois`) | ignora acento, maiúscula, espaço e pontuação |
| `f` | `<input class="in" data-t="f" data-a="3/4" style="width:64px" placeholder="_/_" ...>` | fração `a/b`; alternativas com `\|` (ex. `6/8\|3/4`) | compara o texto exato sem espaços |
| `h` | `<input class="in" data-t="h" data-a="7:30\|19:30" style="width:80px" placeholder="_h_" ...>` | hora `h:mm` | aceita 7h30, 7:30 |
| `c` | `<input class="in" data-t="c" data-a="B3" style="width:56px" ...>` | coordenada letra+número | ignora maiúscula/espaço |
| `s` | `<select class="sel" data-a="cubo" data-t="s"><option value="">escolha</option><option value="cubo">cubo</option>…</select>` | **igual** a um `value` | exato |
| `ch` | `<span class="choice" data-a="1" data-t="ch"><button type="button" class="opt" data-v="0">mais</button><button type="button" class="opt" data-v="1">menos</button></span>` | `data-v` do botão certo | exato — **varie a posição da certa entre as versões** |
| `m` | `<div class="money" data-target="85" data-items="50,20,10,5,2" data-t="m"></div>` | — | a criança clica cédulas/moedas até somar o alvo (precisa ser possível com os itens) |
| `sym` | `<div class="sym" data-t="sym" data-cols="8" data-rows="7" data-axis="4" data-cells="0,3;1,2;…"></div>` | — | completar a figura simétrica (`cols = 2*axis`, células da metade esquerda) |

Uma questão pode ter vários campos; ela só fica certa quando todos estão certos.

## Blocos de layout disponíveis (classes CSS)

- `div.row` (itens lado a lado que quebram linha), `div.grid` (vários itens curtos em grade), `div.ql` (lista vertical de itens a/b/c), `div.seq` (sequência com setas), `div.big` (texto/conta grande).
- `div.ex` (exemplo destacado), `div.note` (dica amarela — **não entregue a resposta**), `span.chip` (número em pílula), `span.card` (cartão de algarismo).
- Contas armadas: `<div class="arm"><div class="r">2.345</div><div class="r"><b class="op">+</b>1.432</div><div class="bar"></div><input …></div>` (alinhe à direita com espaços no `.r` quando a parcela for menor).
- Divisão na chave: `<div class="chave"><div class="cg"><span class="dvd">96</span><span class="dvs">3</span></div><label>Quociente <input …></label></div>`.
- Tabelas: `<div class="tw"><table class="tab"><tr><th>…</th></tr><tr><td>…</td></tr></table></div>` ou quadro de ordens `table.ord`; cardápio `div.menu` (`.mh` título, `.mi` linhas); calendário `table.cal`; relógio dentro de `div.cc`.
- Fração na linha: `<span class="fr"><span>3</span><span>4</span></span>`.

## Figuras lúdicas (SVG) — muito importante

As crianças prendem a atenção com desenhos. **Em pelo menos 6 das 10 questões novas de cada ficha, coloque um desenho SVG**, e prefira desenhos que **façam parte do raciocínio** (contar, medir, comparar, ler), não só enfeite.

- Sempre `<svg class="ill" width="W" height="H" viewBox="0 0 W H" xmlns="http://www.w3.org/2000/svg">…</svg>`, com largura de no máximo ~460 px (o celular encolhe sozinho).
- Estilo: formas simples e arredondadas, contorno `#2b2b3a` fino (1.5–2), cores alegres: verde `#2E9E6B`, laranja `#F07E26`, azul `#3D6FD1`, amarelo `#f5b301`/`#ffd34d`, rosa `#ff8a80`/`#d6455f`, roxo `#a77bd1`, bege `#f2e3c6`. Textos no SVG com `font-family="Fredoka, sans-serif"` ou herdando.
- Ideias: bichinhos (gatos, peixes, joaninhas, passarinhos), frutas, doces, figurinhas, bolas, brinquedos, potes, cestas, cofrinho, cédulas e moedas, balança, régua, relógio, termômetro, malha quadriculada, gráfico de barras, pizza/barra de fração, sólidos geométricos, mapas simples.
- **O desenho TEM que bater com o enunciado e a resposta** (quantidade de objetos, posição na régua, ponteiros do relógio, barras do gráfico, partes pintadas da fração, células da malha, coordenadas). Gere o SVG por script a partir dos mesmos números da resposta.
- Rótulos de texto no SVG não podem ficar cortados na borda (deixe margem; `text-anchor="middle"` precisa de espaço dos dois lados).
- Arestas escondidas tracejadas de sólidos devem ser desenhadas **por último**.

## Didática

- Mesma habilidade BNCC e mesmo nível do ano da ficha (olhe as originais). Varie os tipos de atividade dentro da ficha: conta armada, completar, cálculo mental, situação-problema com história, leitura de figura/gráfico/tabela, escolher a opção, descobrir o número que falta, sequência, comparação.
- Enunciados curtos, com **negrito** (`<b>`) nos números e palavras-chave.
- As 10 questões novas não podem repetir as 5 originais nem as versões já existentes da ficha; entre si também devem ser diferentes.
- Cada problema com **uma única resposta**. Divisões do 3º ano exatas; tabuada até 10 no 3º ano.

## Conferência obrigatória

1. Gere o JSON por um script Python (`json.dump(..., ensure_ascii=False)`), calculando todas as respostas no próprio script (nada de conta de cabeça) e conferindo os desenhos a partir dos mesmos números.
2. Rode `python3 -I /Users/marcosnoronha/Matemática/versoes/validar.py <ano> <ficha>` até dar **0 problemas**.
3. Não edite o HTML, o `validar.py`, o `montar.py` nem arquivos de outras fichas. Não faça commit.
