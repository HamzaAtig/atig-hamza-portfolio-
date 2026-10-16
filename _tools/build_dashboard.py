#!/usr/bin/env python3
"""Génère l'exemple de tableau de bord (données fictives) du cas d'usage
observabilité : jauges, camemberts, barres, courbe, en SVG et HTML.

Sortie : _includes/uc-obs-dashboard-fr.html et _includes/uc-obs-dashboard-en.html
Relancer après modification : python3 _tools/build_dashboard.py
Les données sont volontairement fictives et cohérentes entre elles :
budget restant = (disponibilité - objectif) / (100 - objectif).
"""

import html
import math
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SLO = 99.9
OK, WARN, CRIT = "#27ae60", "#e67e22", "#e74c3c"

COUNTRIES = {"fr": ["France", "Espagne", "Maroc", "Portugal"], "en": ["France", "Spain", "Morocco", "Portugal"]}
AVAIL = [99.95, 99.91, 99.82, 99.97]
TRAFFIC = [42, 23, 21, 14]
ERRORS = [46, 27, 18, 9]
P99 = [390, 380, 370, 365, 372, 395, 430, 455, 470, 460, 450, 440,
       445, 520, 950, 610, 470, 450, 440, 430, 420, 410, 400, 395]
P99_TARGET = 800
BLUES = ["#1f618d", "#3498db", "#7fb8e6", "#c3dcf2"]
ORANGES = ["#c0392b", "#e67e22", "#f0b27a", "#f6ddcc"]

T = {
    "fr": dict(
        title="Exemple de tableau de bord multi-pays", sub="données fictives, pour illustrer la lecture",
        kpis=[("Trafic", "1 240 req/s"), ("Taux d'erreur", "0,08 %"), ("Latence p99", "420 ms"), ("Saturation CPU", "61 %")],
        avail="Disponibilité sur 30 jours, par pays", target=f"objectif {SLO:.1f} %".replace(".", ","),
        traffic="Trafic par pays", errors="Erreurs par type (24 h)",
        err_labels=["Délais base de données", "API partenaire", "Validation des données", "Autres"],
        budget="Budget d'erreur restant (30 jours)", exhausted="épuisé",
        p99="Latence p99 sur 24 h (ms)", p99_target=f"objectif {P99_TARGET} ms", alert="alerte",
        hours=["0 h", "6 h", "12 h", "18 h", "24 h"],
        caption="Ce qu'un responsable lit en dix secondes : le Maroc a consommé tout son budget d'erreur, l'Espagne approche de la limite, et le pic de latence de 14 h explique l'alerte.",
        dec=",", pct=" %",
    ),
    "en": dict(
        title="Example multi-country dashboard", sub="fictional data, to illustrate how it reads",
        kpis=[("Traffic", "1,240 req/s"), ("Error rate", "0.08%"), ("p99 latency", "420 ms"), ("CPU saturation", "61%")],
        avail="30-day availability, by country", target=f"target {SLO:.1f}%",
        traffic="Traffic by country", errors="Errors by type (24 h)",
        err_labels=["Database timeouts", "Partner API", "Data validation", "Other"],
        budget="Remaining error budget (30 days)", exhausted="exhausted",
        p99="p99 latency over 24 h (ms)", p99_target=f"target {P99_TARGET} ms", alert="alert",
        hours=["0 h", "6 h", "12 h", "18 h", "24 h"],
        caption="What a manager reads in ten seconds: Morocco has used up its error budget, Spain is close to the limit, and the 2 pm latency spike explains the alert.",
        dec=".", pct="%",
    ),
}


def fmt(v, t, digits=2):
    return f"{v:.{digits}f}".replace(".", t["dec"]) + t["pct"]


def status(a):
    if a < SLO:
        return CRIT
    return WARN if a < SLO + 0.03 else OK


def gauge(value, label, t):
    """Demi-cercle de 99 % à 100 %, repère à l'objectif."""
    r, cx, cy = 46, 60, 58
    length = math.pi * r
    f = max(0.0, min(1.0, value - 99.0))
    ang = math.pi * (1 - (SLO - 99.0))
    tx1, ty1 = cx + (r - 9) * math.cos(ang), cy - (r - 9) * math.sin(ang)
    tx2, ty2 = cx + (r + 9) * math.cos(ang), cy - (r + 9) * math.sin(ang)
    arc = f"M{cx - r},{cy} A{r},{r} 0 0 1 {cx + r},{cy}"
    return (f'<svg class="dash-gauge" viewBox="0 0 120 92" role="img" aria-label="{html.escape(label)} {fmt(value, t)}">'
            f'<path d="{arc}" fill="none" class="dash-track" stroke-width="12"/>'
            f'<path d="{arc}" fill="none" stroke="{status(value)}" stroke-width="12" stroke-dasharray="{f * length:.1f} {length:.1f}"/>'
            f'<line x1="{tx1:.1f}" y1="{ty1:.1f}" x2="{tx2:.1f}" y2="{ty2:.1f}" class="dash-tick"/>'
            f'<text x="{cx}" y="{cy - 4}" text-anchor="middle" class="dash-gv">{fmt(value, t)}</text>'
            f'<text x="{cx}" y="{cy + 22}" text-anchor="middle" class="dash-gl">{html.escape(label)}</text></svg>')


def donut(values, colors, labels, aria, t):
    r, c = 38, 2 * math.pi * 38
    segs, offset = [], 0.0
    for v, col in zip(values, colors):
        seg = c * v / 100
        segs.append(f'<circle r="{r}" cx="50" cy="50" fill="none" stroke="{col}" stroke-width="18" '
                    f'stroke-dasharray="{seg:.2f} {c - seg:.2f}" stroke-dashoffset="{-offset:.2f}" transform="rotate(-90 50 50)"/>')
        offset += seg
    legend = "".join(f'<li><i style="background:{col}"></i>{html.escape(lb)}<b>{v}{t["pct"]}</b></li>'
                     for v, col, lb in zip(values, colors, labels))
    return (f'<div class="dash-donut"><svg viewBox="0 0 100 100" role="img" aria-label="{html.escape(aria)}">{"".join(segs)}</svg>'
            f'<ul class="dash-legend">{legend}</ul></div>')


def budget_bars(t):
    rows = []
    for name, a in zip(COUNTRIES_LANG, AVAIL):
        rem = max(0.0, (a - SLO) / (100 - SLO) * 100)
        txt = t["exhausted"] if rem == 0 else f"{rem:.0f}{t['pct']}"
        rows.append(f'<div class="dash-brow"><span>{html.escape(name)}</span><span class="dash-btrack">'
                    f'<span class="dash-bbar" style="width:{max(rem, 1.5):.0f}%;background:{status(a)}"></span></span>'
                    f'<span class="dash-bval">{txt}</span></div>')
    return "".join(rows)


def latency(t):
    w, h, top, bottom = 300, 120, 10, 98
    xs = [10 + i * (w - 20) / (len(P99) - 1) for i in range(len(P99))]
    y = lambda v: bottom - v / 1000 * (bottom - top)
    pts = " ".join(f"{x:.1f},{y(v):.1f}" for x, v in zip(xs, P99))
    area = f"10,{bottom} {pts} {xs[-1]:.1f},{bottom}"
    peak = max(range(len(P99)), key=lambda i: P99[i])
    ticks = "".join(f'<text x="{10 + k * (w - 20) / 4:.0f}" y="{h - 4}" text-anchor="middle" class="dash-ax">{lb}</text>'
                    for k, lb in enumerate(t["hours"]))
    return (f'<svg class="dash-line" viewBox="0 0 {w} {h}" role="img" aria-label="{html.escape(t["p99"])}">'
            f'<polygon points="{area}" class="dash-area"/>'
            f'<line x1="10" y1="{y(P99_TARGET):.1f}" x2="{w - 10}" y2="{y(P99_TARGET):.1f}" class="dash-target"/>'
            f'<text x="12" y="{y(P99_TARGET) - 4:.1f}" class="dash-ax">{html.escape(t["p99_target"])}</text>'
            f'<polyline points="{pts}" class="dash-poly"/>'
            f'<circle cx="{xs[peak]:.1f}" cy="{y(P99[peak]):.1f}" r="4" fill="{CRIT}"/>'
            f'<text x="{xs[peak] + 7:.1f}" y="{y(P99[peak]) + 4:.1f}" class="dash-alert">{html.escape(t["alert"])} · {P99[peak]} ms</text>'
            f'{ticks}</svg>')


for lang, t in T.items():
    COUNTRIES_LANG = COUNTRIES[lang]
    kpis = "".join(f'<div class="dash-kpi"><span class="k">{html.escape(k)}</span><span class="v">{html.escape(v)}</span></div>'
                   for k, v in t["kpis"])
    gauges = "".join(gauge(a, c, t) for a, c in zip(AVAIL, COUNTRIES_LANG))
    parts = [
        '<figure class="dash">',
        f'<p class="dash-title">{html.escape(t["title"])} <span>{html.escape(t["sub"])}</span></p>',
        f'<div class="dash-kpis">{kpis}</div>',
        f'<div class="dash-card"><p class="dash-h">{html.escape(t["avail"])} <span>{html.escape(t["target"])}</span></p><div class="dash-gauges">{gauges}</div></div>',
        '<div class="dash-two">',
        f'<div class="dash-card"><p class="dash-h">{html.escape(t["traffic"])}</p>{donut(TRAFFIC, BLUES, COUNTRIES_LANG, t["traffic"], t)}</div>',
        f'<div class="dash-card"><p class="dash-h">{html.escape(t["errors"])}</p>{donut(ERRORS, ORANGES, t["err_labels"], t["errors"], t)}</div>',
        '</div>',
        '<div class="dash-two">',
        f'<div class="dash-card"><p class="dash-h">{html.escape(t["budget"])}</p>{budget_bars(t)}</div>',
        f'<div class="dash-card"><p class="dash-h">{html.escape(t["p99"])}</p>{latency(t)}</div>',
        '</div>',
        f'<figcaption>{html.escape(t["caption"])}</figcaption>',
        '</figure>',
    ]
    dest = ROOT / "_includes" / f"uc-obs-dashboard-{lang}.html"
    dest.write_text("\n".join(parts) + "\n", encoding="utf-8")
    txt = dest.read_text(encoding="utf-8")
    assert "—" not in txt and "–" not in txt and "\n\n" not in txt
    print(f"{dest.relative_to(ROOT)} : {len(txt) / 1024:.1f} Ko")
