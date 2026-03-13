---
layout: default
title: "Welcome"
permalink: /en/
lang: en
description: "Solutions & cloud security architect. Fixed-price offers, modernization, security and DevSecOps."
alternate: /
hero_title: "Freelance solutions & cloud security architect in Paris"
hero_subtitle: "Modernization, DevSecOps, and IAM for critical platforms"
---

<div style="display: flex; align-items: center; gap: 2rem; margin-top: 2rem;">
  <img src="{{ site.author.photo | relative_url }}" alt="{{ site.author.name }}" width="140" height="140" loading="lazy" decoding="async" style="width: 140px; height: 140px; border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.1);" />

  <div>
    <h2>{{ site.author.name }}</h2>
    <p><strong>{{ site.author.title_en }} with <span class="exp-years" data-exp-start-year="{{ site.author.experience_start_year }}" data-exp-start-month="{{ site.author.experience_start_month }}">14</span> years of experience</strong></p>
    <p>I modernize, secure, and stabilize critical platforms through fixed-price, packaged offers.</p>
  </div>
</div>

---

## Positioning

- Solutions architect for SMEs, scale-ups, and B2B organizations with security and integration challenges.
- Specialist in legacy migrations, resilience, and DevSecOps industrialization.
- I use AI to accelerate analysis, improve diagnostic reliability, and enhance delivery quality.

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

## Key experience

{% for exp in site.experiences %}
### <i class="fas fa-{{ exp.icon }}"></i> {{ exp.company }} — {{ exp.role_en }} *({{ exp.period_en }})*
- {{ exp.description_en }}
{% for h in exp.highlights_en %}- {{ h }}
{% endfor %}
{% endfor %}

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
