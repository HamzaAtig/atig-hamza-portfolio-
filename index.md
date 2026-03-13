---
layout: default
title: "Bienvenue sur mon portfolio"
description: "Architecte solutions & securite cloud. Offres forfaitaires, modernisation, securite et DevSecOps."
alternate: /en/
hero_title: "Architecte solutions & securite cloud freelance a Paris"
hero_subtitle: "Modernisation, DevSecOps et IAM pour plateformes critiques"
---

<div style="display: flex; align-items: center; gap: 2rem; margin-top: 2rem;">
  <img src="{{ site.author.photo | relative_url }}" alt="{{ site.author.name }}" width="140" height="140" loading="lazy" decoding="async" style="width: 140px; height: 140px; border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.1);" />

  <div>
    <h2>{{ site.author.name }}</h2>
    <p><strong>{{ site.author.title }} avec <span class="exp-years" data-exp-start-year="{{ site.author.experience_start_year }}" data-exp-start-month="{{ site.author.experience_start_month }}">14</span> ans d'experience</strong></p>
    <p>Je modernise, securise et fiabilise les plateformes critiques avec des offres packagees au forfait.</p>
  </div>
</div>

---

## Positionnement

- Architecte solutions pour PME, scale-ups et acteurs B2B avec enjeux de securite et d'integration.
- Specialiste des migrations legacy, de la resilience et de l'industrialisation DevSecOps.
- J'utilise l'IA pour accelerer l'analyse, fiabiliser les diagnostics et ameliorer la qualite des livrables.

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

Pour plus de details: [voir la strategie]({{ "/strategie" | relative_url }}).

---

## Experiences cles

{% for exp in site.experiences %}
### <i class="fas fa-{{ exp.icon }}"></i> {{ exp.company }} — {{ exp.role }} *({{ exp.period }})*
- {{ exp.description }}
{% for h in exp.highlights %}- {{ h }}
{% endfor %}
{% endfor %}

---

## Expertises cles

<div class="skills expert">
{% for skill in site.skills.expert %}  <span>{{ skill }}</span>
{% endfor %}</div>

---

## Competences standards

<div class="skills standard">
{% for skill in site.skills.standard %}  <span>{{ skill }}</span>
{% endfor %}</div>

---

## Me contacter

- **Email** : {{ site.author.email }}
{% if site.social.linkedin %}- [LinkedIn]({{ site.social.linkedin }}){% endif %}
