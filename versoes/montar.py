#!/usr/bin/env python3
"""Coloca o banco de versões (versoes/<ano>/ficha-XX.json) dentro do Caderno de Matemática.html.

Uso:  python3 versoes/montar.py

Junta todos os anos que tiverem pasta (3, 4, 5) e reescreve a linha `const BANK = ...;` do HTML.
Rode o validar.py antes. O HTML continua sendo um arquivo único, que funciona sem internet.
"""
import json, re
from pathlib import Path

BASE = Path(__file__).resolve().parent
HTML = BASE.parent / "Caderno de Matemática.html"

bank, resumo = {}, []
for ano in ("3", "4", "5"):
    pasta = BASE / ano
    arquivos = sorted(pasta.glob("*.json")) if pasta.is_dir() else []
    if not arquivos:
        continue
    bank[ano] = {}
    for fn in [a for a in arquivos if a.name.startswith("ficha-")]:
        data = json.loads(fn.read_text(encoding="utf-8"))
        for n, vs in data["qs"].items():
            bank[ano][n] = [{"html": v["html"], "gab": v["gab"]} for v in vs]
    for fn in sorted(pasta.glob("extra-*.json")):
        data = json.loads(fn.read_text(encoding="utf-8"))
        qs = sorted(data["qs"].items(), key=lambda kv: int(kv[0]))
        ficha = {k: data[k] for k in ("title", "sub", "bncc", "tip", "mascot")}
        ficha["qs"] = [{"n": int(n), "html": vs[0]["html"], "gab": vs[0]["gab"]} for n, vs in qs]
        bank.setdefault("_extra", {}).setdefault(ano, []).append(ficha)
        for n, vs in qs:
            bank[ano][n] = [{"html": v["html"], "gab": v["gab"]} for v in vs[1:]]
        resumo.append(f"{ano}º ano: ficha extra {data['ficha']} '{data['title']}' com {len(qs)} questões")
    for fn in sorted(pasta.glob("mais-*.json")):
        data = json.loads(fn.read_text(encoding="utf-8"))
        qs = sorted(data["qs"].items(), key=lambda kv: int(kv[0]))
        bank.setdefault("_more", {}).setdefault(ano, {})[str(data["ficha"])] = [
            {"n": int(n), "html": vs[0]["html"], "gab": vs[0]["gab"]} for n, vs in qs]
        for n, vs in qs:
            bank[ano][n] = [{"html": v["html"], "gab": v["gab"]} for v in vs[1:]]
        resumo.append(f"{ano}º ano: ficha {data['ficha']} ganhou {len(qs)} questões a mais")
    nv = {len(v) for v in bank[ano].values()}
    resumo.append(f"{ano}º ano: {len(bank[ano])} questões, {'/'.join(map(str, sorted(nv)))} versões novas cada")

texto = HTML.read_text(encoding="utf-8")

# As 150 questões originais (versão 1 das fichas 1–10) vêm de originais/<ano>-ficha-XX.json.
md = re.search(r"^const DATA = (.*);$", texto, flags=re.M)
if not md:
    raise SystemExit("Não achei a linha 'const DATA = ...;' no HTML.")
data = json.loads(md.group(1))
trocadas = 0
for fn in sorted((BASE / "originais").glob("*-ficha-*.json")):
    o = json.loads(fn.read_text(encoding="utf-8"))
    ficha = data["grades"][fn.name[0]][o["ficha"] - 1]
    for q in o["qs"]:
        alvo = next(x for x in ficha["qs"] if x["n"] == q["n"])
        if alvo["html"] != q["html"] or alvo["gab"] != q["gab"]:
            alvo["html"], alvo["gab"] = q["html"], q["gab"]
            trocadas += 1
if trocadas:
    linha_data = "const DATA = " + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + ";"
    texto = texto[:md.start()] + linha_data + texto[md.end():]
resumo.append(f"originais atualizadas no HTML: {trocadas}")
linha = "const BANK = " + json.dumps(bank, ensure_ascii=False).replace("</", "<\\/") + ";"
novo, n = re.subn(r"^const BANK = .*;$", lambda _: linha, texto, count=1, flags=re.M)
if n != 1:
    raise SystemExit("Não achei a linha 'const BANK = ...;' no HTML.")
HTML.write_text(novo, encoding="utf-8")
print("Banco montado no HTML:")
for r in resumo or ["(nenhum ano com versões)"]:
    print("  -", r)
print(f"Tamanho do HTML: {HTML.stat().st_size / 1024:.0f} KB")
