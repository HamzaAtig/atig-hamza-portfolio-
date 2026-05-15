---
layout: default
title: "Solutions, cloud security & agentic AI architect freelance | Hamza Atig"
permalink: /en/
lang: en
description: "Freelance architect in Paris specialized in modernization, cloud security, DevSecOps and agentic AI (LangGraph, RAG, HITL). Fixed-price packages and products: Aegis Defend (autonomous SOAR), AgentForge (multi-agent factory)."
keywords: "solutions architect freelance Paris, cloud architect, cloud security, agentic AI, LangGraph, RAG pgvector, HITL, multi-agent, autonomous SOAR, AgentForge, Aegis Defend, DevSecOps, IAM, legacy modernization, Spring Boot"
alternate: /
hero_title: "Agentic AI & cloud security architect — freelance, Paris"
hero_subtitle: "AI platforms that hold up in production. No prompt magic."
---

<div style="display: flex; align-items: center; gap: 2rem; margin-top: 2rem;">
  <img src="{{ site.author.photo | relative_url }}" alt="{{ site.author.name }}" width="140" height="140" loading="lazy" decoding="async" style="width: 140px; height: 140px; border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.1);" />

  <div>
    <h2>{{ site.author.name }}</h2>
    <p><strong>{{ site.author.title_en }} · <span class="exp-years" data-exp-start-year="{{ site.author.experience_start_year }}" data-exp-start-month="{{ site.author.experience_start_month }}">15</span> years on critical platforms (finance, insurance, SaaS).</strong></p>
    <p>Creator of <a href="{{ '/en/ai-architecture#aegis-defend' | relative_url }}"><strong>Aegis Defend</strong></a> (autonomous SOAR) and <a href="{{ '/en/ai-architecture#agentforge' | relative_url }}"><strong>AgentForge</strong></a> (multi-agent software factory).</p>
    <p>What I deliver: turning AI ideas into platforms that hold up in production — LangGraph orchestration, HITL, guardrails, observability. No prompt magic, fixed-price deliverables.</p>
  </div>
</div>

<div class="trusted-by">
  <p class="trusted-by-label">Trusted by</p>
  <p class="trusted-by-list">Amundi&nbsp;·&nbsp;Crédit Agricole Assurance&nbsp;·&nbsp;Allianz Trade&nbsp;·&nbsp;Orange Bank&nbsp;·&nbsp;INNSO (Foundever)</p>
</div>

{% include svg-pillars.html %}

---

## Positioning

- Solutions architect for SMEs, scale-ups, and B2B organizations with security and integration challenges.
- Specialist in legacy migrations, resilience, and DevSecOps industrialization.
- **Agentic AI** expertise applied to security and productivity — two products designed end to end: [see the AI architecture]({{ "/en/ai-architecture" | relative_url }}).

---

## Fixed-price offers

<div class="offer-grid">
{% for offer in site.offers %}
  <div class="offer-card">
    <h3>{{ offer.name_en }} ({{ offer.duration_en }})</h3>
    <p>{{ offer.description_en }}</p>
    <div class="offer-meta">Deliverables: {{ offer.deliverables_en }}</div>
  </div>
{% endfor %}
</div>

More details: [see the strategy]({{ "/en/strategy" | relative_url }}).

---

## Today

{% for exp in site.experiences limit:3 %}
### {% if exp.logo %}<img src="{{ exp.logo | relative_url }}" alt="{{ exp.company }}" width="28" height="28" style="vertical-align: middle; margin-right: 0.4rem; border-radius: 4px;"/>{% else %}<i class="fas fa-{{ exp.icon }}"></i>{% endif %} {{ exp.company }} — {{ exp.role_en }} *({{ exp.period_en }})*
- {{ exp.description_en }}
{% for h in exp.highlights_en %}- {{ h }}
{% endfor %}
{% endfor %}

<p style="margin-top: 1.5rem;"><a href="{{ '/en/projects' | relative_url }}"><strong>See all my experiences and clients →</strong></a></p>

---

## Core expertise

<div class="skills expert">
{% for skill in site.skills.expert_en %}  <span>{{ skill }}</span>
{% endfor %}</div>

---

## Standard skills

<div class="skills standard">
{% for skill in site.skills.standard %}  <span>{{ skill }}</span>
{% endfor %}</div>

---

## Contact

- **Email**: {{ site.author.email }}
{% if site.social.linkedin %}- [LinkedIn]({{ site.social.linkedin }}){% endif %}
