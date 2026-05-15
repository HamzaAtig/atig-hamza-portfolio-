---
layout: default
title: "A propos — Hamza Atig, architecte freelance"
permalink: /about
description: "Hamza Atig, architecte solutions, securite cloud et IA agentique freelance a Paris. 15 ans d'experience en modernisation, IAM, DevSecOps et IA agentique. Concepteur d'Aegis Defend et AgentForge."
keywords: "Hamza Atig, architecte solutions freelance, architecte securite cloud, IA agentique, 15 ans experience, modernisation, IAM, DevSecOps, Paris, Aegis Defend, AgentForge"
alternate: /en/about
hero_title: "Architecte solutions, securite cloud & IA agentique freelance"
hero_subtitle: "<span class=\"exp-years\" data-exp-start-year=\"2011\" data-exp-start-month=\"7\">15</span> ans d'experience en modernisation, securite et IA agentique"
---

<div style="display: flex; align-items: center; gap: 2rem; margin-top: 2rem;">
  <img src="{{ site.author.photo | relative_url }}" alt="{{ site.author.name }}" width="140" height="140" loading="lazy" decoding="async" style="width: 140px; height: 140px; border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.1);" />

  <div>
    <h2>A propos de moi</h2>
    <p>{{ site.author.title }} avec <span class="exp-years" data-exp-start-year="{{ site.author.experience_start_year }}" data-exp-start-month="{{ site.author.experience_start_month }}">15</span> ans d'experience, j'interviens sur des plateformes critiques ou la performance, la resilience et la conformite sont centrales.</p>
    <p>Mon role : stabiliser le run, securiser les echanges et construire des trajectoires de modernisation realistes, sans rupture de service.</p>
    <p>Avec deux produits IA agentique conçus de bout en bout (Aegis Defend, AgentForge), j'apporte aussi une lecture archi-first des systemes LLM — orchestration, controle humain, observabilite, securite.</p>
  </div>
</div>

---

## Ce que j'apporte

- **Modernisation pragmatique** : passage legacy vers architectures cloud-ready, decouplage, industrialisation.
- **Securite et IAM** : mise en place SSO/OAuth2, durcissement OWASP, gouvernance des acces.
- **Integration & interoperabilite** : API design, event-driven, mediation et echanges B2B.
- **Observabilite & fiabilite** : metriques, logs, alerting, SLO et plans de stabilisation.
- **IA agentique appliquee** : architecture LangGraph, RAG pgvector, HITL, guardrails LLM. Aegis Defend (SOAR autonome) et AgentForge (multi-agents) comme references produits.

---

## IA agentique & qualite

J'ai conçu et developpe deux produits IA agentiques (Aegis Defend, AgentForge) avec une approche archi-first: LangGraph, RAG pgvector, HITL, guardrails. Cette expertise transfere sur vos propres cas d'usage — assistant SOC, copilote dev, RAG metier.

Au quotidien, j'utilise aussi l'IA pour accelerer l'analyse, fiabiliser les diagnostics et ameliorer la qualite des livrables. L'IA est un accelerateur, pas un substitut: chaque recommandation est validee techniquement.

[Voir l'expertise et les solutions IA]({{ "/archi-ia" | relative_url }})

---

## Mon approche

- Diagnostic rapide et factuel — pas de tunnel
- Blueprint d'architecture et priorisation des quick wins
- Archi-first sur les sujets IA : orchestration, HITL, guardrails, observabilite — pas de prompt magic
- Livraison par paliers, avec transfert d'exploitation
- Mesure d'impact : SLO, metriques de remediation, audit trail

---

## Secteurs servis

Finance & asset management · Assurance · Banque en ligne · SaaS B2B · Cybersecurite PME

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

## Telecharger mon CV ou reserver un creneau

<div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1rem;">
  <a href="{{ '/assets/cv/cv-hamza-atig-fr.pdf' | relative_url }}" target="_blank" style="display: inline-block; padding: 0.6rem 1.2rem; background: #2c3e50; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 500;">CV Francais (PDF)</a>
  <a href="{{ '/assets/cv/cv-hamza-atig-en.pdf' | relative_url }}" target="_blank" style="display: inline-block; padding: 0.6rem 1.2rem; background: #2c3e50; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 500;">CV English (PDF)</a>
  {% if site.social.calendly %}<a href="{{ site.social.calendly }}" target="_blank" rel="noopener" style="display: inline-block; padding: 0.6rem 1.2rem; background: #3498db; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 600;">📅 Reserver un creneau (Calendly)</a>{% endif %}
</div>

---

Merci de votre visite sur mon portfolio. N'hesitez pas a me contacter pour echanger sur vos enjeux techniques.
