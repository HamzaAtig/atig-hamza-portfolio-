---
layout: default
title: "About"
permalink: /en/about
lang: en
description: "Solutions & cloud security architect. Modernization, IAM, integration, and platform reliability."
alternate: /about
hero_title: "Solutions & cloud security architect (freelance)"
hero_subtitle: "<span class=\"exp-years\" data-exp-start-year=\"2011\" data-exp-start-month=\"7\">14</span> years of experience in modernization and reliability"
---

<div style="display: flex; align-items: center; gap: 2rem; margin-top: 2rem;">
  <img src="{{ site.author.photo | relative_url }}" alt="{{ site.author.name }}" width="140" height="140" loading="lazy" decoding="async" style="width: 140px; height: 140px; border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.1);" />

  <div>
    <h2>About me</h2>
    <p>{{ site.author.title_en }} with <span class="exp-years" data-exp-start-year="{{ site.author.experience_start_year }}" data-exp-start-month="{{ site.author.experience_start_month }}">14</span> years of experience, working on critical platforms where performance, resilience, and compliance are key.</p>
    <p>My role: stabilize operations, secure data flows, and design realistic modernization paths without service disruption.</p>
  </div>
</div>

---

## What I deliver

- **Pragmatic modernization**: legacy to cloud-ready architectures, decoupling, industrialization.
- **Security & IAM**: SSO/OAuth2, OWASP hardening, access governance.
- **Integration & interoperability**: API design, event-driven, B2B mediation.
- **Observability & reliability**: metrics, logs, alerting, SLOs, stabilization plans.

---

## AI for quality

I use AI to accelerate analysis, improve diagnostic reliability, and enhance delivery quality.
AI is an accelerator, not a substitute: every recommendation is technically validated and adapted to the context.

---

## My approach

- Rapid, fact-based diagnosis
- Architecture blueprint and quick-win prioritization
- Phased delivery with operational handover

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

## Download my CV

<div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1rem;">
  <a href="{{ '/assets/cv/cv-hamza-atig-en.pdf' | relative_url }}" target="_blank" style="display: inline-block; padding: 0.6rem 1.2rem; background: #3498db; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 500;">CV English (PDF)</a>
  <a href="{{ '/assets/cv/cv-hamza-atig-fr.pdf' | relative_url }}" target="_blank" style="display: inline-block; padding: 0.6rem 1.2rem; background: #2c3e50; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 500;">CV Francais (PDF)</a>
</div>

---

Thanks for visiting my portfolio. Feel free to reach out to discuss your technical challenges.
