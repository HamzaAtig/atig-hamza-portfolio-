#!/usr/bin/env python3
"""Génère les diagrammes de séquence (SVG en ligne) du cas d'usage IAM.

Sortie : _includes/uc-iam-diagrams-fr.html et _includes/uc-iam-diagrams-en.html
Relancer après toute modification : python3 _tools/build_seq_diagrams.py
Les couleurs viennent des variables CSS du site (classes .seq-* dans style.css),
donc les schémas suivent le mode clair ou sombre.
"""

import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHAR_W = 7.3          # largeur moyenne d'un caractère à 13,5 px
STEP_H = 44           # espace vertical entre deux étapes
TOP = 78              # première étape


def text_w(s):
    return len(s) * CHAR_W


def diagram(uid, title, participants, steps, footer, width=880):
    """steps : (de, vers, libellé, style) ; de == vers pour une action locale.
    style : 'call' (trait plein) ou 'reply' (pointillés)."""
    n = len(participants)
    margin = 75
    xs = [margin + i * (width - 2 * margin) / (n - 1) for i in range(n)]
    height = TOP + len(steps) * STEP_H + 30
    out = [f'<svg class="seq" viewBox="0 0 {width} {height}" role="img" aria-labelledby="{uid}-t">',
           f'<title id="{uid}-t">{html.escape(title)}</title>',
           f'<defs><marker id="{uid}-arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
           f'<path class="seq-head" d="M0,0 L10,5 L0,10 z"/></marker></defs>']
    for x, name in zip(xs, participants):
        lines = name.split("\n")
        out.append(f'<line class="seq-life" x1="{x:.0f}" y1="56" x2="{x:.0f}" y2="{height - 18}"/>')
        out.append(f'<rect class="seq-actor" x="{x - 66:.0f}" y="8" width="132" height="46" rx="7"/>')
        for k, line in enumerate(lines):
            y = 36 if len(lines) == 1 else 28 + k * 15
            out.append(f'<text class="seq-actor-t" x="{x:.0f}" y="{y}" text-anchor="middle">{html.escape(line)}</text>')
    for i, (a, b, label, style) in enumerate(steps, start=1):
        y = TOP + (i - 1) * STEP_H + 14
        xa, xb = xs[a], xs[b]
        num = f'<circle class="seq-num" cx="{{cx:.0f}}" cy="{y - 13}" r="8"/><text class="seq-num-t" x="{{cx:.0f}}" y="{y - 9}" text-anchor="middle">{i}</text>'
        if a == b:
            w = text_w(label) + 16
            right = xa + 10 + w + 20 <= width - 6
            bx = xa + 22 if right else xa - 22 - w
            out.append(num.format(cx=(xa + 12) if right else (xa - 12)))
            out.append(f'<rect class="seq-note" x="{bx:.0f}" y="{y - 22}" width="{w:.0f}" height="22" rx="5"/>')
            out.append(f'<text class="seq-label" x="{bx + 8:.0f}" y="{y - 7}">{html.escape(label)}</text>')
        else:
            cls = "seq-msg reply" if style == "reply" else "seq-msg"
            out.append(f'<line class="{cls}" x1="{xa:.0f}" y1="{y}" x2="{xb:.0f}" y2="{y}" marker-end="url(#{uid}-arr)"/>')
            left = min(xa, xb)
            lx = left + 22
            if lx + text_w(label) > width - 6:
                lx = width - 6 - text_w(label)
            out.append(num.format(cx=lx - 12))
            out.append(f'<text class="seq-label halo" x="{lx:.0f}" y="{y - 6}">{html.escape(label)}</text>')
    out.append("</svg>")
    body = "".join(out)
    return (f'<figure class="seq-fig">\n<p class="seq-title">{html.escape(title)}</p>\n'
            f'<div class="seq-wrap">{body}</div>\n<figcaption>{html.escape(footer)}</figcaption>\n</figure>')


T = {
    "fr": {
        "intro": "Deux schémas de principe pour illustrer l'approche (modèles génériques, pas l'architecture d'un client).",
        "sso": (
            "Connexion SSO : OpenID Connect avec PKCE, fédération d'annuaire et MFA",
            ["Utilisateur\n(navigateur)", "Application web", "Keycloak\n(SSO)", "Annuaire\n(AD / LDAP)", "API métier"],
            [
                (0, 1, "Ouvre l'application", "call"),
                (1, 0, "Redirection vers Keycloak (code + PKCE)", "reply"),
                (0, 2, "Saisit identifiant et mot de passe", "call"),
                (2, 3, "Vérifie l'identité (fédération)", "call"),
                (3, 2, "Identité valide + groupes", "reply"),
                (2, 2, "Second facteur (MFA)", "call"),
                (2, 0, "Redirection avec un code d'autorisation", "reply"),
                (0, 1, "Retour vers l'application avec le code", "call"),
                (1, 2, "Échange le code (+ PKCE) contre des jetons", "call"),
                (2, 1, "ID token + access token court (JWT, rôles mappés)", "reply"),
                (1, 4, "Appel avec l'access token", "call"),
                (4, 4, "Vérifie signature, expiration, audience, rôles", "call"),
                (4, 1, "Données autorisées", "reply"),
            ],
            "Ouvrir une deuxième application ne redemande rien : la session Keycloak suffit (SSO). La déconnexion est centralisée.",
        ),
        "zt": (
            "Échange B2B entre composants, en zero trust",
            ["Système\npartenaire", "Keycloak", "Passerelle API", "Service métier", "Base de\ndonnées", "Journal\nd'audit"],
            [
                (0, 1, "Demande un jeton : client credentials + certificat (mTLS)", "call"),
                (1, 1, "Vérifie le certificat, applique le moindre privilège", "call"),
                (1, 0, "Jeton court (5 min), lié au certificat, scope limité", "reply"),
                (0, 2, "Requête + jeton, sur un canal mTLS", "call"),
                (2, 2, "Contrôle : certificat = jeton, signature, scope, quota", "call"),
                (2, 3, "Transmet sur un nouveau canal mTLS", "call"),
                (3, 3, "Revérifie le jeton, applique la règle métier", "call"),
                (3, 4, "Compte de service dédié, droits minimaux", "call"),
                (4, 3, "Résultat", "reply"),
                (3, 0, "Réponse (via la passerelle)", "reply"),
                (2, 5, "Trace : qui, quoi, quand, décision", "call"),
            ],
            "Aucune confiance implicite : chaque saut est authentifié (mTLS), chaque appel est autorisé (jeton court, audience, scope), tout est tracé.",
        ),
    },
    "en": {
        "intro": "Two reference diagrams to illustrate the approach (generic patterns, not a client's architecture).",
        "sso": (
            "SSO login: OpenID Connect with PKCE, directory federation and MFA",
            ["User\n(browser)", "Web application", "Keycloak\n(SSO)", "Directory\n(AD / LDAP)", "Business API"],
            [
                (0, 1, "Opens the application", "call"),
                (1, 0, "Redirect to Keycloak (code + PKCE)", "reply"),
                (0, 2, "Enters username and password", "call"),
                (2, 3, "Checks the identity (federation)", "call"),
                (3, 2, "Valid identity + groups", "reply"),
                (2, 2, "Second factor (MFA)", "call"),
                (2, 0, "Redirect with an authorization code", "reply"),
                (0, 1, "Back to the application with the code", "call"),
                (1, 2, "Exchanges the code (+ PKCE) for tokens", "call"),
                (2, 1, "ID token + short-lived access token (JWT, mapped roles)", "reply"),
                (1, 4, "Call with the access token", "call"),
                (4, 4, "Checks signature, expiry, audience, roles", "call"),
                (4, 1, "Authorized data", "reply"),
            ],
            "Opening a second application asks for nothing: the Keycloak session is enough (SSO). Logout is centralized.",
        ),
        "zt": (
            "B2B exchange between components, zero trust",
            ["Partner\nsystem", "Keycloak", "API gateway", "Business\nservice", "Database", "Audit log"],
            [
                (0, 1, "Requests a token: client credentials + certificate (mTLS)", "call"),
                (1, 1, "Checks the certificate, applies least privilege", "call"),
                (1, 0, "Short-lived token (5 min), bound to the certificate, narrow scope", "reply"),
                (0, 2, "Request + token, over an mTLS channel", "call"),
                (2, 2, "Checks: certificate = token, signature, scope, quota", "call"),
                (2, 3, "Forwards over a new mTLS channel", "call"),
                (3, 3, "Re-checks the token, applies the business rule", "call"),
                (3, 4, "Dedicated service account, minimal rights", "call"),
                (4, 3, "Result", "reply"),
                (3, 0, "Response (through the gateway)", "reply"),
                (2, 5, "Log: who, what, when, decision", "call"),
            ],
            "No implicit trust: every hop is authenticated (mTLS), every call is authorized (short-lived token, audience, scope), everything is logged.",
        ),
    },
}

OBS = {
    "fr": {
        "intro": "Un schéma de principe pour illustrer l'approche (modèle générique, pas l'architecture d'un client).",
        "detect": (
            "Détection d'incident : du symptôme à la cause",
            ["Application\n(pays X)", "Collecte\n(agents, Logstash)", "Elasticsearch", "Dynatrace\n(SLO)", "Équipe\nd'astreinte", "Kibana /\nGrafana"],
            [
                (0, 1, "Logs, métriques, traces + ID de corrélation", "call"),
                (1, 1, "Enrichit : pays, client, version", "call"),
                (1, 2, "Indexe par pays et par jour", "call"),
                (0, 3, "Latence et erreurs mesurées en continu", "call"),
                (3, 3, "Le budget d'erreur du pays X baisse trop vite", "call"),
                (3, 4, "Alerte ciblée : pays, service, gravité", "call"),
                (4, 5, "Ouvre le tableau de bord du pays X", "call"),
                (5, 2, "Recherche par ID de corrélation", "call"),
                (2, 5, "Parcours complet de la requête en erreur", "reply"),
                (4, 0, "Correctif ou bascule", "call"),
                (3, 4, "Retour sous l'objectif de service", "reply"),
            ],
            "L'alerte part d'un objectif de service par pays, pas d'un seuil technique : moins de fausses alertes, et la cause se retrouve en quelques recherches.",
        ),
    },
    "en": {
        "intro": "A reference diagram to illustrate the approach (generic pattern, not a client's architecture).",
        "detect": (
            "Incident detection: from symptom to cause",
            ["Application\n(country X)", "Collection\n(agents, Logstash)", "Elasticsearch", "Dynatrace\n(SLO)", "On-call\nteam", "Kibana /\nGrafana"],
            [
                (0, 1, "Logs, metrics, traces + correlation ID", "call"),
                (1, 1, "Enriches: country, client, version", "call"),
                (1, 2, "Indexes by country and by day", "call"),
                (0, 3, "Latency and errors measured continuously", "call"),
                (3, 3, "Country X's error budget drops too fast", "call"),
                (3, 4, "Targeted alert: country, service, severity", "call"),
                (4, 5, "Opens country X's dashboard", "call"),
                (5, 2, "Search by correlation ID", "call"),
                (2, 5, "Full path of the failing request", "reply"),
                (4, 0, "Fix or failover", "call"),
                (3, 4, "Back within the service objective", "reply"),
            ],
            "The alert comes from a per-country service objective, not a technical threshold: fewer false alarms, and the cause is found in a few searches.",
        ),
    },
}

SETS = [
    ("uc-iam-diagrams", T, ["sso", "zt"]),
    ("uc-obs-diagrams", OBS, ["detect"]),
]

for name, texts, keys in SETS:
    for lang, t in texts.items():
        parts = [f'<div class="seq-block">\n<p class="seq-intro">{html.escape(t["intro"])}</p>']
        parts += [diagram(f"{k}-{lang}", *t[k]) for k in keys]
        parts.append("</div>")
        dest = ROOT / "_includes" / f"{name}-{lang}.html"
        dest.write_text("\n".join(parts) + "\n", encoding="utf-8")
        txt = dest.read_text(encoding="utf-8")
        assert "—" not in txt and "–" not in txt, "tiret long interdit"
        print(f"{dest.relative_to(ROOT)} : {len(txt) / 1024:.1f} Ko")
