#!/usr/bin/env python3
"""Confere os arquivos do banco de versões (versoes/<ano>/ficha-XX.json).

Uso:  python3 versoes/validar.py 3            (todo o 3º ano)
      python3 versoes/validar.py 3 4          (só a ficha 4 do 3º ano)

Formato de cada arquivo:
  {"ficha": 1, "qs": {"1": [ {"html": "...", "gab": "..."}, ... ], "2": [...], ...}}
Cada questão traz as versões novas (a original continua no HTML como versão 1).
"""
import json, re, sys
from html.parser import HTMLParser
from pathlib import Path

BASE = Path(__file__).resolve().parent
VOID = {"input", "br", "img", "hr", "meta", "link", "path", "circle", "rect", "line",
        "ellipse", "polygon", "polyline", "stop", "use"}
NUM = re.compile(r"^-?\d+([.,]\d+)?$")


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errs, self.fields, self.opts = [], [], [], []
        self.cur_sel = None
        self.cur_choice = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "data-t" in a:
            f = {"tag": tag, **a, "options": []}
            self.fields.append(f)
            if tag == "select":
                self.cur_sel = f
            if a["data-t"] == "ch":
                self.cur_choice = f
        if tag == "option" and self.cur_sel is not None:
            self.cur_sel["options"].append(a.get("value", ""))
        if tag == "button" and self.cur_choice is not None and "data-v" in a:
            self.cur_choice["options"].append(a["data-v"])
        if tag not in VOID:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID and self.stack and self.stack[-1] == tag:
            self.stack.pop()

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if tag == "select":
            self.cur_sel = None
        if tag == "span" and self.cur_choice is not None and self.stack.count("span") == 1 + self._choice_depth():
            pass
        if not self.stack or self.stack[-1] != tag:
            self.errs.append(f"tag </{tag}> fora de ordem (aberta: {self.stack[-1] if self.stack else 'nenhuma'})")
            if tag in self.stack:
                while self.stack and self.stack.pop() != tag:
                    pass
            return
        self.stack.pop()
        if tag == "span" and self.cur_choice is not None and "span" not in self.stack:
            self.cur_choice = None

    def _choice_depth(self):
        return 0


def reachable(target_cents, items_cents):
    ok = [False] * (target_cents + 1)
    ok[0] = True
    for i in range(1, target_cents + 1):
        ok[i] = any(c <= i and ok[i - c] for c in items_cents)
    return ok[target_cents]


def check_version(v, label):
    errs = []
    if not isinstance(v, dict) or not v.get("html") or not v.get("gab"):
        return [f"{label}: precisa de 'html' e 'gab' preenchidos"]
    c = Checker()
    c.feed(v["html"])
    c.close()
    errs += [f"{label}: {e}" for e in c.errs]
    if c.stack:
        errs.append(f"{label}: tags sem fechar: {c.stack}")
    if not c.fields:
        errs.append(f"{label}: nenhum campo de resposta (data-t)")
    for i, f in enumerate(c.fields):
        t, a, where = f["data-t"], f.get("data-a"), f"{label} campo {i+1} ({f['data-t']})"
        if t in ("n", "s", "t", "f", "h", "c", "ch") and not a:
            errs.append(f"{where}: sem data-a")
            continue
        if t == "n":
            for alt in a.split("|"):
                if not NUM.match(alt.strip()):
                    errs.append(f"{where}: data-a '{alt}' não é número simples (use 1346, não 1.346)")
        elif t == "s":
            if a not in f["options"]:
                errs.append(f"{where}: data-a '{a}' não está entre as opções {f['options']}")
        elif t == "ch":
            if a not in f["options"]:
                errs.append(f"{where}: data-a '{a}' não é um data-v dos botões {f['options']}")
        elif t == "f":
            for alt in a.split("|"):
                if not re.match(r"^\d+/\d+$", alt.replace(" ", "")):
                    errs.append(f"{where}: fração '{alt}' deve ser como 3/4")
        elif t == "h":
            for alt in a.split("|"):
                if not re.match(r"^\d{1,2}:\d{2}$", alt):
                    errs.append(f"{where}: hora '{alt}' deve ser como 7:30")
        elif t == "m":
            try:
                tgt = round(float(f["data-target"]) * 100)
                its = [round(float(x) * 100) for x in f["data-items"].split(",")]
                if not reachable(tgt, its):
                    errs.append(f"{where}: não dá para formar {f['data-target']} com {f['data-items']}")
            except Exception as e:  # noqa
                errs.append(f"{where}: data-target/data-items inválidos ({e})")
        elif t == "sym":
            for k in ("data-cols", "data-rows", "data-axis", "data-cells"):
                if k not in f:
                    errs.append(f"{where}: falta {k}")
        if t in ("n", "h", "c", "t", "f") and f["tag"] != "input":
            errs.append(f"{where}: tipo {t} deve ser <input>")
    if "<svg" in v["html"] and 'class="ill"' not in v["html"]:
        errs.append(f"{label}: todo <svg> de ilustração deve ter class=\"ill\"")
    return errs, [f["data-t"] for f in c.fields]


def main():
    ano = sys.argv[1] if len(sys.argv) > 1 else "3"
    so = int(sys.argv[2]) if len(sys.argv) > 2 else None
    orig_dir = BASE / "originais"
    total_err, total_v = 0, 0
    for fn in sorted((BASE / ano).glob("ficha-*.json")):
        data = json.loads(fn.read_text(encoding="utf-8"))
        nf = data.get("ficha")
        if so and nf != so:
            continue
        orig = json.loads((orig_dir / f"{ano}-ficha-{nf:02d}.json").read_text(encoding="utf-8"))
        nums = [q["n"] for q in orig["qs"]]
        errs = []
        if sorted(int(k) for k in data["qs"]) != nums:
            errs.append(f"questões esperadas {nums}, encontradas {sorted(int(k) for k in data['qs'])}")
        counts = set()
        for n in nums:
            vs = data["qs"].get(str(n), [])
            counts.add(len(vs))
            o = next(q for q in orig["qs"] if q["n"] == n)
            _, otypes = check_version(o, "orig")
            for i, v in enumerate(vs):
                r = check_version(v, f"Q{n} v{i+2}")
                if isinstance(r, list):
                    errs += r
                    continue
                e, types = r
                errs += e
                total_v += 1
                if v["html"] == o["html"]:
                    errs.append(f"Q{n} v{i+2}: igual à original")
                if sorted(types) != sorted(otypes):
                    errs.append(f"Q{n} v{i+2}: aviso — campos {types} diferentes da original {otypes}")
            htmls = [v.get("html") for v in vs]
            if len(set(htmls)) != len(htmls):
                errs.append(f"Q{n}: versões repetidas")
        if len(counts) > 1:
            errs.append(f"número de versões diferente entre questões: {sorted(counts)}")
        status = "OK" if not errs else f"{len(errs)} problema(s)"
        print(f"{fn.name}: {status}")
        for e in errs:
            print("   -", e)
        total_err += len(errs)
    # fichas extras (ex.: extra-11.json — Probleminhas): todas as versões são novas
    for fn in sorted((BASE / ano).glob("extra-*.json")):
        data = json.loads(fn.read_text(encoding="utf-8"))
        if so and data.get("ficha") != so:
            continue
        errs = [f"falta '{k}'" for k in ("ficha", "title", "sub", "bncc", "tip", "mascot", "qs") if k not in data]
        counts = {len(vs) for vs in data.get("qs", {}).values()}
        if len(counts) != 1 or min(counts) < 2:
            errs.append(f"cada questão precisa do mesmo número de versões (>=2); achei {sorted(counts)}")
        for n, vs in data.get("qs", {}).items():
            for i, v in enumerate(vs):
                r = check_version(v, f"Q{n} v{i+1}")
                if isinstance(r, list):
                    errs += r
                else:
                    errs += r[0]
                    total_v += 1
            if len({v.get("html") for v in vs}) != len(vs):
                errs.append(f"Q{n}: versões repetidas")
        print(f"{fn.name}: {'OK' if not errs else f'{len(errs)} problema(s)'}")
        for e in errs:
            print("   -", e)
        total_err += len(errs)
    print(f"\nTotal: {total_v} versões conferidas, {total_err} problema(s).")
    sys.exit(1 if total_err else 0)


if __name__ == "__main__":
    main()
