---
layout: default
title: "Contact — Book a free diagnostic call (30 min) | Hamza Atig"
permalink: /en/contact
lang: en
description: "Book a free 30-min call with Hamza Atig, freelance solutions, cloud security and agentic AI architect in Paris. Calendly, email or LinkedIn. Response within 24-48h."
keywords: "contact freelance architect Paris, book free diagnostic call, Calendly Hamza Atig, fixed-price mission, agentic AI, cloud security"
alternate: /contact
hero_title: "Contact solutions, cloud security & agentic AI architect"
hero_subtitle: "Paris - fixed-price missions and AI pilots"
---

## Contact me

Have a modernization project, a security audit to conduct, or a technical architecture need? Let's talk.

### Book a slot

{% if site.social.calendly %}
<div style="margin: 1rem 0 1.5rem 0;">
  <a href="{{ site.social.calendly }}" target="_blank" rel="noopener" style="display: inline-block; padding: 0.7rem 1.4rem; background: #3498db; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 600;">📅 Book a free diagnostic call (30 min)</a>
</div>
{% endif %}

### Get in touch

- **Email**: [{{ site.author.email }}](mailto:{{ site.author.email }})
{% if site.social.linkedin %}- **LinkedIn**: [My profile]({{ site.social.linkedin }}){% endif %}
{% if site.social.github %}- **GitHub**: [{{ site.social.github }}]({{ site.social.github }}){% endif %}

---

### What I offer

| Mission type | Indicative duration |
|--------------|---------------------|
{% for offer in site.offers %}| {{ offer.name_en }} | {{ offer.duration_en }} |
{% endfor %}| Sprint support | Custom |

---

### Availability

Based in **{{ site.author.location }}**, I work on-site or remotely depending on your needs.

Response within **24-48h** for any inquiry.

---

### Download my CV

<div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1rem;">
  <a href="{{ '/assets/cv/cv-hamza-atig-en.pdf' | relative_url }}" target="_blank" style="display: inline-block; padding: 0.6rem 1.2rem; background: #3498db; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 500;">CV English (PDF)</a>
  <a href="{{ '/assets/cv/cv-hamza-atig-fr.pdf' | relative_url }}" target="_blank" style="display: inline-block; padding: 0.6rem 1.2rem; background: #2c3e50; color: #fff; text-decoration: none; border-radius: 6px; font-weight: 500;">CV Francais (PDF)</a>
</div>
