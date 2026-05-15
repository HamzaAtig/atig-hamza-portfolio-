---
layout: default
title: "About — Hamza Atig, freelance architect"
permalink: /en/about
lang: en
description: "Hamza Atig, freelance solutions, cloud security and agentic AI architect in Paris. 15 years of experience in modernization, IAM, DevSecOps and agentic AI. Creator of Aegis Defend and AgentForge."
keywords: "Hamza Atig, freelance solutions architect, cloud security architect, agentic AI, 15 years experience, modernization, IAM, DevSecOps, Paris, Aegis Defend, AgentForge"
alternate: /about
hero_title: "Solutions, cloud security & agentic AI architect (freelance)"
hero_subtitle: "<span class=\"exp-years\" data-exp-start-year=\"2011\" data-exp-start-month=\"7\">15</span> years of experience in modernization, security and agentic AI"
---

<div style="display: flex; align-items: center; gap: 2rem; margin-top: 2rem;">
  <img src="{{ site.author.photo | relative_url }}" alt="{{ site.author.name }}" width="140" height="140" loading="lazy" decoding="async" style="width: 140px; height: 140px; border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.1);" />

  <div>
    <h2>About me</h2>
    <p>{{ site.author.title_en }} with <span class="exp-years" data-exp-start-year="{{ site.author.experience_start_year }}" data-exp-start-month="{{ site.author.experience_start_month }}">15</span> years of experience, working on critical platforms where performance, resilience, and compliance are key.</p>
    <p>My role: stabilize operations, secure data flows, and design realistic modernization paths without service disruption.</p>
    <p>With two agentic AI products designed end to end (Aegis Defend, AgentForge), I also bring an architecture-first view of LLM systems — orchestration, human control, observability, security.</p>
  </div>
</div>

---

## What I deliver

- **Pragmatic modernization**: legacy to cloud-ready architectures, decoupling, industrialization.
- **Security & IAM**: SSO/OAuth2, OWASP hardening, access governance.
- **Integration & interoperability**: API design, event-driven, B2B mediation.
- **Observability & reliability**: metrics, logs, alerting, SLOs, stabilization plans.
- **Applied agentic AI**: LangGraph architecture, pgvector RAG, HITL, LLM guardrails. Aegis Defend (autonomous SOAR) and AgentForge (multi-agent factory) as product references.

---

## Agentic AI & quality

I designed and built two agentic AI products (Aegis Defend, AgentForge) with an architecture-first approach: LangGraph, pgvector RAG, HITL, guardrails. This expertise transfers to your own use cases — SOC assistant, dev copilot, domain RAG.

Day to day, I also use AI to accelerate analysis, improve diagnostic reliability, and enhance delivery quality. AI is an accelerator, not a substitute: every recommendation is technically validated.

[See the AI expertise and solutions]({{ "/en/ai-architecture" | relative_url }})

---

## My approach

- Rapid, fact-based diagnosis — no tunneling
- Architecture blueprint and quick-win prioritization
- Architecture-first on AI topics: orchestration, HITL, guardrails, observability — no prompt magic
- Phased delivery with operational handover
- Impact measurement: SLOs, remediation metrics, audit trail

---

## Sectors served

Finance & asset management · Insurance · Online banking · B2B SaaS · SMB cybersecurity

---

## Additional info

- **Location**: {{ site.author.location }}
- **Status**: {{ site.author.status }}
- **Formats**: short missions, fixed-price packages, or sprint support
- **Languages**: French / English

---

## Education

{% for edu in site.education %}
- **{{ edu.year }}** — {{ edu.degree_en }}{% if edu.school_en %}, {{ edu.school_en }}{% endif %}
{% endfor %}

---

## Certifications

{% for cert in site.certifications %}
- **{{ cert.name }}** — {{ cert.description_en }}
{% endfor %}

---

## Download my CV or book a slot

<div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1rem;">
  <a href="{{ '/assets/cv/cv-hamza-atig-en.pdf' | relative_url }}" target="_blank" style="display: inline-block; padding: 0.6rem 1.2rem; background: #2c3e50; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 500;">CV English (PDF)</a>
  <a href="{{ '/assets/cv/cv-hamza-atig-fr.pdf' | relative_url }}" target="_blank" style="display: inline-block; padding: 0.6rem 1.2rem; background: #2c3e50; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 500;">CV Francais (PDF)</a>
  {% if site.social.calendly %}<a href="{{ site.social.calendly }}" target="_blank" rel="noopener" style="display: inline-block; padding: 0.6rem 1.2rem; background: #3498db; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 600;">📅 Book a slot (Calendly)</a>{% endif %}
</div>

---

Thanks for visiting my portfolio. Feel free to reach out to discuss your technical challenges.
