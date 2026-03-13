---
layout: default
title: "A propos"
permalink: /about
description: "Architecte solutions & securite cloud. Modernisation, IAM, integration et fiabilisation de plateformes critiques."
alternate: /en/about
hero_title: "Architecte solutions & securite cloud freelance"
hero_subtitle: "<span class=\"exp-years\" data-exp-start-year=\"2011\" data-exp-start-month=\"7\">14</span> ans d'experience en modernisation et fiabilisation"
---

<div style="display: flex; align-items: center; gap: 2rem; margin-top: 2rem;">
  <img src="{{ site.author.photo | relative_url }}" alt="{{ site.author.name }}" width="140" height="140" loading="lazy" decoding="async" style="width: 140px; height: 140px; border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.1);" />

  <div>
    <h2>A propos de moi</h2>
    <p>{{ site.author.title }} avec <span class="exp-years" data-exp-start-year="{{ site.author.experience_start_year }}" data-exp-start-month="{{ site.author.experience_start_month }}">14</span> ans d'experience, j'interviens sur des plateformes critiques ou la performance, la resilience et la conformite sont centrales.</p>
    <p>Mon role: stabiliser le run, securiser les echanges et construire des trajectoires de modernisation realistes, sans rupture de service.</p>
  </div>
</div>

---

## Ce que j'apporte

- **Modernisation pragmatique** : passage legacy vers architectures cloud-ready, decouplage, industrialisation.
- **Securite et IAM** : mise en place SSO/OAuth2, durcissement OWASP, gouvernance des acces.
- **Integration & interoperabilite** : API design, event-driven, mediation et echanges B2B.
- **Observabilite & fiabilite** : metriques, logs, alerting, SLO et plans de stabilisation.

---

## IA au service de la qualite

J'utilise l'IA pour accelerer l'analyse, fiabiliser les diagnostics et ameliorer la qualite des livrables.
L'IA est un accelerateur, pas un substitut: chaque recommandation est validee techniquement et adaptee au contexte.

---

## Mon approche

- Diagnostic rapide et factuel
- Blueprint d'architecture et priorisation des quick wins
- Livraison par paliers, avec transfert d'exploitation

---

## Infos complementaires

- **Localisation** : {{ site.author.location }}
- **Statut** : {{ site.author.status }}
- **Formats** : missions courtes, forfaits, ou accompagnement au sprint
- **Langues** : Francais / Anglais

---

## Formation

{% for edu in site.education %}
- **{{ edu.year }}** — {{ edu.degree }}{% if edu.school %}, {{ edu.school }}{% endif %}
{% endfor %}

---

## Certifications

{% for cert in site.certifications %}
- **{{ cert.name }}** — {{ cert.description }}
{% endfor %}

---

## Telecharger mon CV

<div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1rem;">
  <a href="{{ '/assets/cv/cv-hamza-atig-fr.pdf' | relative_url }}" target="_blank" style="display: inline-block; padding: 0.6rem 1.2rem; background: #2c3e50; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 500;">CV Francais (PDF)</a>
  <a href="{{ '/assets/cv/cv-hamza-atig-en.pdf' | relative_url }}" target="_blank" style="display: inline-block; padding: 0.6rem 1.2rem; background: #3498db; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 500;">CV English (PDF)</a>
</div>

---

Merci de votre visite sur mon portfolio. N'hesitez pas a me contacter pour echanger sur vos enjeux techniques.
