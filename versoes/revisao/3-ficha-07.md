# 3º ano · ficha 7 · Sistema monetário

## Corrigido
- Q34 v2, v3 (questão 4 da ficha) — "Quanto **custa** 2 pipocas…" / "…3 pães de queijo…" (o item mais próximo está no plural) → "Quanto **custam** …".
- Q163 v1 (questão 8) — "os patins que **custa**" → "os patins, que **custam** R$ 50,00".
- Q162 v2, v4 (questão 7) — no desenho da loja, a pipa (topo em y=25) invadia a faixa vermelha e, na v4, ficava por cima do título "LOJA DE BRINQUEDOS"; a antena do robô encostava na faixa → pipa um pouco menor e mais baixa, antena encurtada (preços e itens inalterados).

## Melhorado
- Q31 v1–v4 (questão 1) — SVG das cédulas com 500/576/552/512 px de largura → `width="460"` com o mesmo `viewBox` (escala proporcional; cédulas e moedas iguais, só menores), para caber no celular.
- Q33 v2, v3 (questão 3) — bandeja só com cédulas dizia "Clique num item da bandeja para devolvê-lo" → "Clique numa cédula da bandeja para devolvê-la" (igual à original).
- Q33 v4 e Q167 v1–v4 (questões 3 e 12) — bandejas com cédulas e moedas → "Clique numa cédula ou moeda da bandeja para devolvê-la" (mais claro que "item").
- Q34 v1 e v4 — "Quanto custa" → "Quanto custam" (sujeito composto; uniformiza com v2/v3).
- Q34 v3 — cardápio dizia "Bolo R$ 7,00" e a pergunta "1 fatia de bolo" → cardápio "Fatia de bolo" (sem dúvida se o preço é do bolo inteiro).
- Q164 v1–v4 (questão 9) — "trocar uma cédula por outras de mesmo valor" (dava a entender que cada nota vale o mesmo) → "por outras que, **juntas**, valem o mesmo".
- Q168 v1–v4 (questão 13) — "Quanto ela economiza?" → "Quanto ela economiza comprando na loja mais barata?".
- Q168 v4 — "Pacote com 6 pacotes de figurinhas" → "Kit com 6 pacotes de figurinhas".

## Sugestões (não aplicadas)
- Q31 — em vez de só encolher o SVG, redesenhar em duas fileiras (cédulas em cima, moedas embaixo) para as cédulas ficarem maiores no celular.
- Q35 — v2 e v3 têm o mesmo alvo (R$ 2,00); a v3 poderia usar outro valor (ex.: 10 centavos para R$ 3,00 = 30 moedas) para variar mais.
- Q166 (questão 11) — o desenho mostra 2 tomates, 3 cenouras, 2 maçãs etc. com um preço só; uma criança pode multiplicar. Escrever no rótulo a unidade (ex.: "Tomate (pacote)", "Banana (dúzia)") ou desenhar um só item.
- Q168 — as 4 versões começam com "Mamãe precisa de…"; variar a personagem (Papai, Vovó, Tio…).

## Conferido sem problemas
60 versões revisadas (15 questões × 4: originais Q31–Q35, `ficha-07.json` v2–v4, `mais-07.json` Q161–Q170 v1–v4).
- Todas as contas refeitas com `Fraction` (totais de cédulas/moedas, trocos, somas com centavos, divisões exatas, conversões em moedas/centavos) — todos os `data-a` e `gab` batem.
- Peças de dinheiro contadas por script nos SVG e conferidas visualmente (renderização em PNG): Q31, Q161, Q163, Q164, Q165 (nº de fichas), Q169, Q170 (nº de envelopes = nº de netos) batem com o enunciado e a resposta.
- Bandejas `data-t="m"` (Q33, Q167): alvos formáveis com os itens oferecidos; valores ≥ 2 aparecem como cédula e 1/centavos como moeda (todas as cores de cédula existem no widget).
- Botões de escolha: Q161 (0,1,0,1) e Q168 (1,0,1,0) alternam a posição; sem empates.
- `python3 -I versoes/validar.py 3 7` → 0 problemas.
