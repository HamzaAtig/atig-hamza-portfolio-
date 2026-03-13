---
layout: default
title: "Projets"
permalink: /projects
description: "Projets recents et missions par client, orientes modernisation, securite et integration."
alternate: /en/projects
hero_title: "Projets de modernisation et securite cloud"
hero_subtitle: "Finance, assurance, SaaS et plateformes B2B"
---

## Dernieres experiences (extraits)

{% for exp in site.experiences limit:5 %}
### {{ exp.company }} — {{ exp.role }} ({{ exp.period }})
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
