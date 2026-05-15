# Portfolio Template - Jekyll

Un template de portfolio professionnel moderne, bilingue (FR/EN), optimise pour le SEO et entierement personnalisable via un fichier de configuration.

## Demo

[Voir le site en ligne](https://hamzaatig.github.io/atig-hamza-portfolio-/)

## Fonctionnalites

- **Bilingue** : Support FR/EN avec switch de langue
- **Dark Mode** : Theme clair/sombre avec persistance
- **SEO Optimise** : Schema.org, Open Graph, sitemap, meta tags
- **Responsive** : Mobile-first, adaptatif tous ecrans
- **Performance** : CSS externe, lazy loading images
- **Accessible** : Focus states, reduced motion support
- **Animations** : Fade-in, hover effects, transitions fluides
- **Configurable** : Toutes les donnees dans `_config.yml`

## Installation rapide

### Prerequis

- Ruby >= 2.7
- Bundler (`gem install bundler`)

### Etapes

```bash
# 1. Cloner le repo
git clone https://github.com/votre-username/portfolio-template.git
cd portfolio-template

# 2. Installer les dependances
bundle install

# 3. Personnaliser _config.yml (voir section suivante)

# 4. Lancer en local
bundle exec jekyll serve

# 5. Ouvrir http://localhost:4000
```

## Personnalisation

### 1. Informations personnelles

Editez `_config.yml` :

```yaml
author:
  name: "Votre Nom"
  title: "Votre Titre FR"
  title_en: "Your Title EN"
  email: "votre@email.com"
  location: "Votre Ville, Pays"
  photo: "/assets/img/votre-photo.jpg"
  experience_start_year: 2015  # Annee de debut de carriere
```

### 2. Liens sociaux

```yaml
social:
  linkedin: "https://www.linkedin.com/in/votre-profil/"
  github: "https://github.com/votre-username"
  twitter: ""  # Laisser vide si non utilise
```

### 3. Offres / Services

```yaml
offers:
  - name: "Nom de l'offre FR"
    name_en: "Offer Name EN"
    duration: "X jours/semaines"
    duration_en: "X days/weeks"
    description: "Description FR..."
    description_en: "Description EN..."
    deliverables: "Liste des livrables FR"
    deliverables_en: "Deliverables list EN"
```

### 4. Experiences

```yaml
experiences:
  - company: "Nom Entreprise"
    role: "Votre Role FR"
    role_en: "Your Role EN"
    period: "2022 - 2024"
    period_en: "2022 - 2024"
    icon: "building"  # Icone Font Awesome (sans 'fa-')
    description: "Description FR"
    description_en: "Description EN"
    highlights:
      - "Point cle 1 FR"
      - "Point cle 2 FR"
    highlights_en:
      - "Key point 1 EN"
      - "Key point 2 EN"
```

### 5. Competences

```yaml
skills:
  expert:
    - "Competence expert 1"
    - "Competence expert 2"
  expert_en:
    - "Expert skill 1"
    - "Expert skill 2"
  standard:
    - "Competence standard 1"  # Meme en FR et EN generalement
```

### 6. Formation & Certifications

```yaml
education:
  - year: "2020"
    degree: "Diplome FR"
    degree_en: "Degree EN"
    school: "Ecole FR"
    school_en: "School EN"

certifications:
  - name: "Nom Certification"
    description: "Description FR"
    description_en: "Description EN"
```

### 7. Photo de profil

Remplacez le fichier :
```
assets/img/votre-photo.jpg
```

Format recommande : 400x400px, JPG optimise

### 8. CV PDF

Placez vos CV dans :
```
assets/cv/cv-votre-nom-fr.pdf
assets/cv/cv-votre-nom-en.pdf
```

Puis mettez a jour les liens dans `about.md`, `about.en.md`, `contact.md`, `contact.en.md`.

### 9. Favicon

Remplacez `favicon.ico` a la racine.

### 10. Google Analytics

```yaml
google_analytics: "G-XXXXXXXXXX"  # Ou vide pour desactiver
```

## Structure des fichiers

```
.
├── _config.yml          # Configuration principale (A MODIFIER)
├── _layouts/
│   └── default.html     # Template principal
├── assets/
│   ├── css/
│   │   └── style.css    # Styles CSS
│   ├── cv/              # CV PDF
│   └── img/             # Images (photo profil)
├── index.md             # Page d'accueil FR
├── index.en.md          # Page d'accueil EN
├── about.md             # A propos FR
├── about.en.md          # A propos EN
├── strategie.md         # Offres FR
├── strategie.en.md      # Offres EN
├── cas-usage.md         # Cas d'usage FR
├── use-cases.en.md      # Cas d'usage EN
├── projects.md          # Projets FR
├── projects.en.md       # Projets EN
├── contact.md           # Contact FR
├── contact.en.md        # Contact EN
└── 404.html             # Page 404
```

## Deploiement

### GitHub Pages

1. Pushez le code sur GitHub
2. Allez dans Settings > Pages
3. Source: `main` branch, `/ (root)`
4. Le site sera disponible sur `https://username.github.io/repo-name/`

### Netlify / Vercel

1. Connectez votre repo
2. Build command: `bundle exec jekyll build`
3. Publish directory: `_site`

## Personnalisation avancee

### Couleurs

Editez les variables CSS dans `assets/css/style.css` :

```css
:root {
  --accent: #3498db;        /* Couleur principale */
  --cta-bg: #3498db;        /* Bouton CTA */
  --badge-expert: #2c3e50;  /* Badges expert */
  /* ... */
}
```

### Layout

Modifiez `_layouts/default.html` pour :
- Changer la structure de navigation
- Modifier le hero banner
- Ajuster le footer

### Ajouter une page

1. Creez `nouvelle-page.md` et `nouvelle-page.en.md`
2. Ajoutez le front matter :
```yaml
---
layout: default
title: "Titre"
permalink: /nouvelle-page
lang: fr
alternate: /en/new-page
---
```
3. Ajoutez le lien dans le menu (`_layouts/default.html`)

## Technologies

- [Jekyll](https://jekyllrb.com/) - Generateur de site statique
- [GitHub Pages](https://pages.github.com/) - Hebergement
- [Font Awesome](https://fontawesome.com/) - Icones
- [Google Fonts](https://fonts.google.com/) - Typographie (Roboto)

## Licence

MIT License - Libre d'utilisation et modification.

## Credits

Template cree par [Hamza Atig](https://www.linkedin.com/in/hamza-atig-88760559/)

---

## Support

Pour toute question : ouvrez une issue sur GitHub.
