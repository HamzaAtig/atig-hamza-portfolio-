---
layout: default
title: "Contact — Reservez un diagnostic gratuit (30 min) | Hamza Atig"
permalink: /contact
description: "Reservez un creneau gratuit (30 min) avec Hamza Atig, architecte solutions, securite cloud et IA agentique freelance a Paris. Calendly, email ou LinkedIn. Reponse 24-48h."
keywords: "contact architecte freelance Paris, reserver diagnostic gratuit, Calendly Hamza Atig, mission forfaitaire, IA agentique, securite cloud"
alternate: /en/contact
hero_title: "Contact architecte solutions, securite cloud & IA agentique"
hero_subtitle: "Paris - missions forfaitaires et pilotes IA"
---

## Contactez-moi

Vous avez un projet de modernisation, un audit de securite a mener ou un besoin d'architecture technique ? Parlons-en.

### Reserver un creneau

{% if site.social.calendly %}
<div style="margin: 1rem 0 1.5rem 0;">
  <a href="{{ site.social.calendly }}" target="_blank" rel="noopener" style="display: inline-block; padding: 0.7rem 1.4rem; background: #3498db; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 600;">📅 Reserver un diagnostic gratuit (30 min)</a>
</div>
{% endif %}

### Prendre contact

- **Email** : [{{ site.author.email }}](mailto:{{ site.author.email }})
{% if site.social.linkedin %}- **LinkedIn** : [Mon profil]({{ site.social.linkedin }}){% endif %}
{% if site.social.github %}- **GitHub** : [{{ site.social.github }}]({{ site.social.github }}){% endif %}

---

### Ce que je propose

| Type de mission | Duree indicative |
|-----------------|------------------|
{% for offer in site.offers %}| {{ offer.name }} | {{ offer.duration }} |
{% endfor %}| Accompagnement au sprint | Sur mesure |

---

### Disponibilite

Base a **{{ site.author.location }}**, j'interviens en presentiel ou en remote selon vos besoins.

Reponse sous **24-48h** pour toute demande de contact.

---

### Telecharger mon CV

<div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1rem;">
  <a href="{{ '/assets/cv/cv-hamza-atig-fr.pdf' | relative_url }}" target="_blank" style="display: inline-block; padding: 0.6rem 1.2rem; background: #2c3e50; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 500;">CV Francais (PDF)</a>
  <a href="{{ '/assets/cv/cv-hamza-atig-en.pdf' | relative_url }}" target="_blank" style="display: inline-block; padding: 0.6rem 1.2rem; background: #3498db; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 500;">CV English (PDF)</a>
</div>
