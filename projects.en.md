---
layout: default
title: "Projects"
permalink: /en/projects
lang: en
description: "Recent projects and client missions focused on modernization, security and integration."
alternate: /projects
hero_title: "Cloud modernization and security projects"
hero_subtitle: "Finance, insurance, SaaS and B2B platforms"
---

## Latest experience (excerpts)

{% for exp in site.experiences %}
### {% if exp.logo %}<img src="{{ exp.logo | relative_url }}" alt="{{ exp.company }}" width="28" height="28" style="vertical-align: middle; margin-right: 0.4rem; border-radius: 4px;"/>{% endif %}{{ exp.company }} — {{ exp.role_en }} ({{ exp.period_en }})
- {{ exp.description_en }}
{% for h in exp.highlights_en %}- {{ h }}
{% endfor %}
{% endfor %}

---

## Clients & missions

| Client | Sector | Mission type |
|---|---|---|
{% for project in site.projects %}| {{ project.client }} | {{ project.sector_en }} | {{ project.mission_en }} |
{% endfor %}
