---
layout: default
title: "Architecte solutions, sécurité cloud & IA agentique freelance | Hamza Atig"
description: "Architecte freelance à Paris spécialisé en modernisation, sécurité cloud, DevSecOps et IA agentique (LangGraph, RAG, HITL). Offres forfaitaires et produits : Aegis Defend (SOAR autonome), AgentForge (multi-agents)."
keywords: "architecte solutions freelance Paris, architecte cloud, sécurité cloud, IA agentique, LangGraph, RAG pgvector, HITL, multi-agents, SOAR, AgentForge, Aegis Defend, DevSecOps, IAM, modernisation legacy, Spring Boot"
alternate: /en/
hero_title: "Architecte IA agentique & sécurité cloud — freelance à Paris"
hero_subtitle: "Des plateformes IA qui tiennent en production. Pas de prompt magic."
---

<div id="about-pitch" style="display: flex; align-items: center; gap: 2rem; margin-top: 2rem;">
  <img src="{{ site.author.photo | relative_url }}" alt="{{ site.author.name }}" width="140" height="140" loading="lazy" decoding="async" style="width: 140px; height: 140px; border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.1);" />

  <div>
    <h2>{{ site.author.name }}</h2>
    <p><strong>{{ site.author.title }} · <span class="exp-years" data-exp-start-year="{{ site.author.experience_start_year }}" data-exp-start-month="{{ site.author.experience_start_month }}">15</span> ans sur des plateformes critiques (finance, assurance, SaaS).</strong></p>
    <p>Concepteur d'<a href="{{ '/archi-ia#aegis-defend' | relative_url }}"><strong>Aegis Defend</strong></a> (SOAR autonome) et d'<a href="{{ '/archi-ia#agentforge' | relative_url }}"><strong>AgentForge</strong></a> (software factory multi-agents).</p>
    <p>Ma valeur : transformer une idée d'IA en plateforme qui tient en production — orchestration LangGraph, HITL, guardrails, observabilité. Pas de prompt magic, des livrables au forfait.</p>
  </div>
</div>

<div class="trusted-by">
  <p class="trusted-by-label">Ils m'ont fait confiance</p>
  <p class="trusted-by-list">Amundi&nbsp;·&nbsp;Crédit Agricole Assurance&nbsp;·&nbsp;Allianz Trade&nbsp;·&nbsp;Orange Bank&nbsp;·&nbsp;INNSO (Foundever)</p>
</div>

{% include svg-pillars.html %}

---

## Positionnement

- Architecte solutions pour PME, scale-ups et acteurs B2B avec enjeux de sécurité et d'intégration.
- Spécialiste des migrations legacy, de la résilience et de l'industrialisation DevSecOps.
- Expertise **IA agentique** appliquée à la sécurité et à la productivité — deux produits conçus de bout en bout : [voir l'archi IA]({{ "/archi-ia" | relative_url }}).

---

## Offres forfaitaires

<div class="offer-grid">
{% for offer in site.offers %}
  <div class="offer-card">
    <h3>{{ offer.name }} ({{ offer.duration }})</h3>
    <p>{{ offer.description }}</p>
    <div class="offer-meta">Livrables: {{ offer.deliverables }}</div>
  </div>
{% endfor %}
</div>

Pour plus de détails : [voir la stratégie]({{ "/strategie" | relative_url }}).

---

## Aujourd'hui

{% for exp in site.experiences limit:3 %}
### {% if exp.logo %}<img src="{{ exp.logo | relative_url }}" alt="{{ exp.company }}" width="28" height="28" style="vertical-align: middle; margin-right: 0.4rem; border-radius: 4px;"/>{% else %}<i class="fas fa-{{ exp.icon }}"></i>{% endif %} {{ exp.company }} — {{ exp.role }} *({{ exp.period }})*
- {{ exp.description }}
{% for h in exp.highlights %}- {{ h }}
{% endfor %}
{% endfor %}

<p style="margin-top: 1.5rem;"><a href="{{ '/projects' | relative_url }}"><strong>Voir toutes mes expériences et clients →</strong></a></p>

---

## Expertises clés

<div class="skills expert">
{% for skill in site.skills.expert %}  <span>{{ skill }}</span>
{% endfor %}</div>

---

## Compétences standards

<div class="skills standard">
{% for skill in site.skills.standard %}  <span>{{ skill }}</span>
{% endfor %}</div>

---

## Me contacter

- **Email** : {{ site.author.email }}
{% if site.social.linkedin %}- [LinkedIn]({{ site.social.linkedin }}){% endif %}
