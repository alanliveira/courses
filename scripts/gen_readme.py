#!/usr/bin/env python3
"""Gera o README.md com o sumário dos repositórios migrados.

Uso local ou no GitHub Actions (ver .github/workflows/update-readme.yml).
Dados: scripts/repos.json (derivado do export de repositórios).
"""
import json
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "scripts" / "repos.json"
OUT = ROOT / "README.md"
BASE = "https://github.com/alanliveira/courses/tree/main"

# títulos legíveis por subcategoria
TITLES = {
    "alura": "Alura",
    "dio": "DIO",
    "django": "Django",
    "etec-desenvolvimento": "ETEC — Desenvolvimento",
    "etec-jogos": "ETEC — Jogos",
    "fatec-jogos": "FATEC — Jogos",
    "udemy": "Udemy",
}

# Badges de linguagem: label -> (cor hex, logo simple-icons, cor do logo)
LANG_BADGES = {
    "ActionScript":      ("882B0F", "adobeflash",  "white"),
    "C#":                ("178600", "csharp",      "white"),
    "CSS":               ("663399", "css",         "white"),
    "Dart":              ("0175C2", "dart",        "white"),
    "Dockerfile":        ("2496ED", "docker",      "white"),
    "HLSL":              ("555555", None,          None),
    "HTML":              ("E34F26", "html5",       "white"),
    "JavaScript":        ("F7DF1E", "javascript",  "black"),
    "Kotlin":            ("7F52FF", "kotlin",      "white"),
    "Nix":               ("5277C3", "nix",         "white"),
    "Procfile":          ("430A36", "heroku",      "white"),
    "Python":            ("3776AB", "python",      "ffd43b"),
    "Ruby":              ("CC342D", "ruby",        "white"),
    "SCSS":              ("CC6699", "sass",        "white"),
    "ShaderLab":         ("222222", "unity",       "white"),
    "Shell":             ("4EAA25", "gnubash",     "white"),
    "TypeScript":        ("3178C6", "typescript",  "white"),
}

def badge(lang: str) -> str:
    color, logo, logo_color = LANG_BADGES.get(lang, ("555555", None, None))
    # codificação do label no path do shields.io
    label = lang.replace("#", "%23").replace(" ", "%20").replace("-", "--")
    url = f"https://img.shields.io/badge/{label}-{color}"
    params = []
    if logo:
        params.append(f"logo={logo}")
    if logo_color:
        params.append(f"logoColor={logo_color}")
    if params:
        url += "?" + "&".join(params)
    return f"![{lang}]({url})"

rows = json.load(open(PLAN, encoding="utf-8"))
groups = OrderedDict()
for r in sorted(rows, key=lambda x: (x["sub"], x["repo"].lower())):
    groups.setdefault(r["sub"], []).append(r)

total = len(rows)
subs = len(groups)

lines = []
lines.append("# 📚 Courses")
lines.append("")
lines.append("Este repositório tem a finalidade de **centralizar todos os cursos que fiz**.")
lines.append("")
lines.append(f"**{total} repositórios** em **{subs} subcategorias**.")
lines.append("")
lines.append("## Sumário")
lines.append("")
for sub, repos in groups.items():
    lines.append(f"- [{TITLES.get(sub, sub)}](#{sub}) ({len(repos)})")
lines.append("")

for sub, repos in groups.items():
    lines.append(f"## {TITLES.get(sub, sub)}")
    lines.append("")
    lines.append("| Repositório | Linguagens | Acesso ao repositório |")
    lines.append("|---|---|---|")
    for r in repos:
        langs = " ".join(badge(l) for l in r["languages"]) or "—"
        mono = f"[{r['prefix']}]({r['prefix']})"  # link relativo à raiz do repo
        lines.append(f"| `{r['repo']}` | {langs} | {mono} |")
    lines.append("")

lines.append("---")
lines.append("")
lines.append("### Como clonar um repositório interno")
lines.append("")
lines.append("```bash")
lines.append("# história completa (todos os commits do monorepo)")
lines.append("git clone git@github.com:alanliveira/courses.git")
lines.append("")
lines.append("# apenas os arquivos de um curso, com o histórico daquele repo")
lines.append("git clone --filter=blob:none --sparse git@github.com:alanliveira/courses.git")
lines.append("cd courses")
lines.append("git sparse-checkout set cursos/<subcategoria>/<repositório>")
lines.append("```")
lines.append("")
lines.append("### Histórico de um repositório específico")
lines.append("")
lines.append("```bash")
lines.append("git log --oneline cursos/<subcategoria>/<repositório>")
lines.append("```")
lines.append("")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"README.md gerado: {total} repos em {subs} subcategorias")
