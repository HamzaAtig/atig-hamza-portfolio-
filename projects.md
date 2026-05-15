---
layout: default
title: "Projets"
permalink: /projects
description: "Projets récents et missions par client, orientés modernisation, sécurité et intégration."
alternate: /en/projects
hero_title: "Projets de modernisation et sécurité cloud"
hero_subtitle: "Finance, assurance, SaaS et plateformes B2B"
---

## Dernières expériences (extraits)

{% for exp in site.experiences %}
### {% if exp.logo %}<img src="{{ exp.logo | relative_url }}" alt="{{ exp.company }}" width="28" height="28" style="vertical-align: middle; margin-right: 0.4rem; border-radius: 4px;"/>{% endif %}{{ exp.company }} — {{ exp.role }} ({{ exp.period }})
- {{ exp.description }}
{% for h in exp.highlights %}- {{ h }}
{% endfor %}
{% endfor %}

---

## Clients & missions

| Client | Secteur | Type de mission |
|---|---|---|
{% for project in site.projects %}| {{ project.client }} | {{ project.sector }} | {{ project.mission }} |
{% endfor %}
