---
layout: default
title: "Architecture IA agentique : Aegis Defend & AgentForge | Hamza Atig"
permalink: /archi-ia
lang: fr
description: "Expertise IA agentique applique a la securite et a la productivite. Architecture LangGraph, RAG pgvector, HITL, guardrails LLM, multi-LLM. Decouvrez Aegis Defend (SOAR autonome SOC) et AgentForge (software factory multi-agents)."
keywords: "IA agentique, agentic AI, LangGraph, RAG pgvector, HITL, guardrails LLM, multi-agents, orchestration agents IA, SOAR autonome, Aegis Defend, AgentForge, MITRE ATT&CK, multi-LLM, OpenAI, Anthropic, Ollama, architecture IA Paris, freelance IA"
alternate: /en/ai-architecture
hero_title: "Architecture IA agentique pour la securite & la productivite"
hero_subtitle: "Systemes orchestres, observables et securises — LangGraph, RAG, HITL, guardrails"
---

## Pourquoi une expertise IA agentique distincte

L'IA generative est devenue accessible. Mais passer d'un prototype de prompt a une plateforme exploitable en production reste un sujet d'architecture: orchestration, etat, observabilite, securite, controle humain.

Avec **<span class="exp-years" data-exp-start-year="{{ site.author.experience_start_year }}" data-exp-start-month="{{ site.author.experience_start_month }}">15</span> ans d'experience** sur des plateformes critiques (finance, assurance, SaaS) et deux produits IA conçus de bout en bout, j'apporte une lecture archi-first des systemes agentiques: **pas de prompt magic, des pipelines deterministes la ou il faut, du non-deterministe encadre la ou il apporte de la valeur.**

---

## Principes d'architecture

- **Orchestration explicite** — graphes d'agents (LangGraph), etats persistants, routes conditionnelles tracables.
- **Human-in-the-Loop** — l'humain reste decisionnaire sur les actions sensibles, avec reprise d'etat fiable.
- **Guardrails multi-couches** — detection d'injection prompt, validation de sortie, budget de tokens, defense en profondeur.
- **RAG ancre dans le metier** — corpus vectorises (pgvector) pour eviter l'hallucination et tracer les sources.
- **Multi-LLM par defaut** — pas de dependance a un seul fournisseur (OpenAI, Anthropic, Mistral, Ollama).
- **Observabilite native** — logs structures, metriques Prometheus, audit trail des decisions.

---

## Stack de reference

<div class="skills expert">
{% for tech in site.ai_stack %}  <span>{{ tech }}</span>
{% endfor %}</div>

---

## Solutions

{% for solution in site.ai_solutions %}
### {{ solution.name }} — {{ solution.tagline }}

<p><strong>Statut:</strong> {{ solution.status }}</p>

{{ solution.description }}

{% if solution.id == "aegis-defend" %}
{% include svg-aegis.html %}
{% elsif solution.id == "agentforge" %}
{% include svg-agentforge.html %}
{% endif %}

**Capacites cles**
{% for cap in solution.capabilities %}
- {{ cap }}
{% endfor %}

---
{% endfor %}

## Offres pilotes

<div class="offer-grid">
{% for offer in site.ai_offers %}
  <div class="offer-card">
    <h3>{{ offer.name }} ({{ offer.duration }})</h3>
    <p><strong>Pour qui:</strong> {{ offer.for_whom }}</p>
    <p><strong>Perimetre:</strong> {{ offer.scope }}</p>
    <div class="offer-meta">
      <strong>Livrables:</strong>
      <ul style="margin: 0.5rem 0 0 0; padding-left: 1.2rem;">
        {% for d in offer.deliverables %}<li>{{ d }}</li>{% endfor %}
      </ul>
    </div>
    {% if offer.note %}<p style="margin-top: 0.8rem; font-style: italic; opacity: 0.85;">{{ offer.note }}</p>{% endif %}
  </div>
{% endfor %}
</div>

---

## Et au-dela des produits

L'expertise IA agentique se transpose sur vos propres cas d'usage internes: assistant SOC, copilote dev, generation de documentation, automatisation conditionnelle de tickets, RAG metier. Le socle technique reste le meme — orchestration, controle humain, observabilite, securite.

[Discutons d'un cas d'usage]({{ "/contact" | relative_url }}).
