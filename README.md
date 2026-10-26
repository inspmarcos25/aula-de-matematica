# Aula de Matemática

Caderno interativo de matemática do 3º ao 5º ano (BNCC), num único arquivo HTML que funciona sem internet.

**Abrir online:** https://inspmarcos25.github.io/aula-de-matematica/

- **Caderno de Matemática.html**: abra no navegador. São 12 fichas por ano (incluindo duas de Probleminhas), correção na hora, aba Tabuada (estudar, treinar e desafio do minuto) e aba Resultados para conferência.
- **Rodadas:** o botão "Novas questões" troca as questões do ano. Cada questão tem 4 versões, e as respostas da rodada anterior ficam no histórico.

## Editar as questões

As questões ficam em `versoes/<ano>/`, em arquivos `ficha-XX.json` (versões novas das fichas 1 a 10) e `extra-XX.json` (fichas de Probleminhas). As originais estão em `versoes/originais/`.

Depois de editar:

```bash
python3 versoes/validar.py 3      # confere o 3º ano (troque por 4 ou 5)
python3 versoes/montar.py         # coloca o banco dentro do HTML
```
