---
layout: default
title: "Contact — Réservez un diagnostic gratuit (30 min) | Hamza Atig"
permalink: /contact
description: "Réservez un créneau gratuit (30 min) avec Hamza Atig, architecte solutions, sécurité cloud et IA agentique freelance à Paris. Calendly, email ou LinkedIn. Réponse 24-48h."
keywords: "contact architecte freelance Paris, réserver diagnostic gratuit, Calendly Hamza Atig, mission forfaitaire, IA agentique, sécurité cloud"
alternate: /en/contact
hero_title: "Contact architecte solutions, sécurité cloud & IA agentique"
hero_subtitle: "Paris — missions forfaitaires et pilotes IA"
---

## Contactez-moi

Vous avez un projet de modernisation, un audit de sécurité à mener ou un besoin d'architecture technique ? Parlons-en.

### Réserver un créneau

{% if site.social.calendly %}
<div style="margin: 1rem 0 1.5rem 0;">
  <a href="{{ site.social.calendly }}" target="_blank" rel="noopener" style="display: inline-block; padding: 0.7rem 1.4rem; background: #3498db; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 600;">📅 Réserver un diagnostic gratuit (30 min)</a>
</div>
{% endif %}

### Prendre contact

- **Email** : [{{ site.author.email }}](mailto:{{ site.author.email }})
{% if site.social.linkedin %}- **LinkedIn** : [Mon profil]({{ site.social.linkedin }}){% endif %}
{% if site.social.github %}- **GitHub** : [{{ site.social.github }}]({{ site.social.github }}){% endif %}

---

### Ce que je propose

| Type de mission | Durée indicative |
|-----------------|------------------|
{% for offer in site.offers %}| {{ offer.name }} | {{ offer.duration }} |
{% endfor %}| Accompagnement au sprint | Sur mesure |

---

### Disponibilité

Basé à **{{ site.author.location }}**, j'interviens en présentiel ou en remote selon vos besoins.

Réponse sous **24-48h** pour toute demande de contact.

---

### Télécharger mon CV

<div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1rem;">
  <a href="{{ '/assets/cv/cv-hamza-atig-fr.pdf' | relative_url }}" target="_blank" style="display: inline-block; padding: 0.6rem 1.2rem; background: #2c3e50; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 500;">CV Français (PDF)</a>
  <a href="{{ '/assets/cv/cv-hamza-atig-en.pdf' | relative_url }}" target="_blank" style="display: inline-block; padding: 0.6rem 1.2rem; background: #2c3e50; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 500;">CV English (PDF)</a>
</div>
