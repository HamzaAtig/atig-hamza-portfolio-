---
layout: default
title: "Agentic AI architecture: Aegis Defend & AgentForge | Hamza Atig"
permalink: /en/ai-architecture
lang: en
description: "Agentic AI expertise applied to security and productivity. LangGraph architecture, pgvector RAG, HITL, LLM guardrails, multi-LLM. Discover Aegis Defend (autonomous SOAR for SOCs) and AgentForge (multi-agent software factory)."
keywords: "agentic AI, LangGraph, RAG pgvector, HITL, LLM guardrails, multi-agent orchestration, autonomous SOAR, Aegis Defend, AgentForge, MITRE ATT&CK, multi-LLM, OpenAI, Anthropic, Ollama, AI architecture Paris, freelance AI architect"
alternate: /archi-ia
hero_title: "Agentic AI architecture for security & productivity"
hero_subtitle: "Orchestrated, observable, secure systems — LangGraph, RAG, HITL, guardrails"
---

## Why a distinct agentic AI expertise

Generative AI is now within reach. But moving from a prompt prototype to a production-grade platform is still an architecture problem: orchestration, state, observability, security, human control.

With **<span class="exp-years" data-exp-start-year="{{ site.author.experience_start_year }}" data-exp-start-month="{{ site.author.experience_start_month }}">15</span> years of experience** on critical platforms (finance, insurance, SaaS) and two AI products designed end to end, I bring an architecture-first view of agentic systems: **no prompt magic — deterministic pipelines where they belong, controlled non-determinism where it adds value.**

---

## Architecture principles

- **Explicit orchestration** — agent graphs (LangGraph), persistent state, traceable conditional routing.
- **Human-in-the-Loop** — humans stay in control of sensitive actions, with reliable state resume.
- **Multi-layer guardrails** — prompt injection detection, output validation, token budgeting, defense in depth.
- **Domain-grounded RAG** — vectorized corpora (pgvector) to prevent hallucination and trace sources.
- **Multi-LLM by default** — no single-vendor lock-in (OpenAI, Anthropic, Mistral, Ollama).
- **Native observability** — structured logs, Prometheus metrics, decision audit trail.

---

## Reference stack

<div class="skills expert">
{% for tech in site.ai_stack %}  <span>{{ tech }}</span>
{% endfor %}</div>

---

## Solutions

{% for solution in site.ai_solutions %}
### {{ solution.name }} — {{ solution.tagline_en }}

<p><strong>Status:</strong> {{ solution.status_en }}</p>

{{ solution.description_en }}

{% if solution.id == "aegis-defend" %}
{% include svg-aegis.html %}
{% elsif solution.id == "agentforge" %}
{% include svg-agentforge.html %}
{% endif %}

**Key capabilities**
{% for cap in solution.capabilities_en %}
- {{ cap }}
{% endfor %}

---
{% endfor %}

## Pilot offers

<div class="offer-grid">
{% for offer in site.ai_offers %}
  <div class="offer-card">
    <h3>{{ offer.name_en }} ({{ offer.duration_en }})</h3>
    <p><strong>For whom:</strong> {{ offer.for_whom_en }}</p>
    <p><strong>Scope:</strong> {{ offer.scope_en }}</p>
    <div class="offer-meta">
      <strong>Deliverables:</strong>
      <ul style="margin: 0.5rem 0 0 0; padding-left: 1.2rem;">
        {% for d in offer.deliverables_en %}<li>{{ d }}</li>{% endfor %}
      </ul>
    </div>
    {% if offer.note_en %}<p style="margin-top: 0.8rem; font-style: italic; opacity: 0.85;">{{ offer.note_en }}</p>{% endif %}
  </div>
{% endfor %}
</div>

---

## Beyond the products

Agentic AI expertise transfers to your own internal use cases: SOC assistant, dev copilot, documentation generation, conditional ticket automation, domain-specific RAG. The technical foundation stays the same — orchestration, human control, observability, security.

[Let's discuss a use case]({{ "/en/contact" | relative_url }}).
