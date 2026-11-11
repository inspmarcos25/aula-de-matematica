# Aula de Matemática

Caderno interativo de matemática do 3º ao 6º ano (BNCC), num único arquivo HTML que funciona sem internet.

**Abrir online:** https://inspmarcos25.github.io/aula-de-matematica/

- **Caderno de Matemática.html**: abra no navegador. São 10 fichas de assuntos com 15 questões e 2 de Probleminhas com 20 em cada ano, mais a ficha de Educação financeira (30 questões) no 5º ano. O 6º ano tem 10 fichas com 5 questões. São 650 atividades no total, correção na hora, aba Tabuada (estudar, treinar e desafio do minuto) e aba Resultados para conferência.
- **Rodadas:** o botão "Novas questões" troca as questões do ano. Do 3º ao 5º ano cada questão tem 4 versões, e as respostas da rodada anterior ficam no histórico. O 6º ano ainda tem uma versão só de cada questão (em `versoes/originais/6-ficha-XX.json`), por isso não mostra o botão.

## Login com o Google (site da Netlify)

No site https://aula-de-matematica.netlify.app o caderno pede login com o Google. O responsável entra, cria um perfil para cada criança (até 8) e o progresso de cada perfil fica salvo na conta, em qualquer aparelho. O arquivo `Caderno de Matemática.html` aberto direto (ou pelo GitHub Pages) continua funcionando sem login, com o progresso salvo só no navegador.

- `scripts/build.mjs`: monta `dist/` para a Netlify, ligando o login no HTML.
- `auth.js`: biblioteca de login da Netlify já empacotada (`npm run build:auth` refaz a partir de `src/auth.js`).
- `netlify/functions/dados/`: função que guarda perfis e progresso por conta (Netlify Identity + Netlify Blobs).

Para publicar:

1. Uma vez só, em https://app.netlify.com/projects/aula-de-matematica/identity: **Enable Identity**, Registration **Open** e, em External providers, **Google**.
2. Ligue este repositório ao projeto na Netlify (o `netlify.toml` já tem o build) ou rode `npm install && npx netlify-cli deploy --build --prod`.

Testes:

```bash
npm test                                  # regras do servidor
npm run build && python3 tests/e2e.py     # fluxo completo com login simulado (precisa do Playwright)
python3 tests/offline.py                  # arquivo único sem login e as 50 questões do 6º ano
```

## Editar as questões

As questões ficam em `versoes/<ano>/`, em arquivos `ficha-XX.json` (versões novas das fichas 1 a 10) e `extra-XX.json` (fichas de Probleminhas) e `mais-XX.json` (10 questões a mais de cada ficha). O guia de estilo para escrever questões novas está em `versoes/GUIA-QUESTOES.md`. As originais estão em `versoes/originais/`.

Depois de editar:

```bash
python3 versoes/validar.py 3      # confere o 3º ano (troque por 4 ou 5)
python3 versoes/montar.py         # coloca o banco dentro do HTML
```

## Revisão

Todas as questões foram revisadas em todas as versões. O resumo está em [REVISAO.md](REVISAO.md), e os detalhes de cada ficha ficam em `versoes/revisao/`.
