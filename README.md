# 🌐 Portfolio – Hamza Atig

Bienvenue sur mon portfolio personnel, réalisé avec **Jekyll** et hébergé via **GitHub Pages**. Ce site présente mon parcours, mes expériences clés, mes compétences techniques, ainsi qu’un lien vers mon CV.

🔗 **Accès en ligne :** [https://hamzaatig.github.io/atig-hamza-portfolio-/](https://hamzaatig.github.io/atig-hamza-portfolio-/)

---

## ✨ Présentation

Je suis **Hamza Atig**, architecte solutions & sécurité cloud avec 14 ans d'expérience. Passionné par la conception d’architectures robustes, la performance applicative et l’optimisation continue, j’ai construit ce site pour centraliser et partager :

- Mon parcours professionnel
- Mes expertises technologiques
- Mon CV au format PDF
- Mes coordonnées

---

## 🛠️ Stack technique

- [x] **Jekyll** (site statique)
- [x] **GitHub Pages** pour l’hébergement gratuit
- [x] HTML/CSS custom (avec dégradé, responsive & effet burger menu)
- [x] Markdown enrichi avec icônes et emojis
- [x] Version mobile responsive
- [x] Page 404 personnalisée 😄

---

## 📁 Arborescence

```bash
.
├── _layouts/             # Templates HTML (default.html)
├── _posts/               # Articles de blog (facultatif)
├── assets/               # Fichiers statiques (ex: CV PDF)
├── index.md              # Page d'accueil
├── about.md              # À propos
├── contact.md            # Contact
├── projects.md           # Projets
├── 404.html              # Page 404 personnalisée
├── _config.yml           # Configuration Jekyll
```

---

## ⚙️ Choix techniques & déploiement

### 🔧 Stack choisie

| Élément                  | Choix                             | Raison principale |
|--------------------------|------------------------------------|--------------------|
| **Générateur de site**   | [Jekyll](https://jekyllrb.com)     | Léger, statique, intégration native avec GitHub Pages |
| **Thème**                | Custom (à partir de Minima)        | Plus de liberté sur le design & structure |
| **Langages**             | Markdown, HTML, CSS                | Markdown pour le contenu, HTML/CSS pour le style avancé |
| **Fonts & Icônes**       | [Google Fonts – Roboto](https://fonts.google.com/specimen/Roboto), [Font Awesome](https://fontawesome.com) | Typographie moderne et icônes stylées |
| **Responsive**           | CSS Media Queries + Burger Menu    | Navigation fluide sur mobile/tablette |
| **Animation / Design**   | Dégradé de fond, `hero banner`     | Moderne & clair sans images lourdes |

---

### 🚀 Déploiement GitHub Pages

- Le dépôt est **public** pour permettre le **déploiement automatique via GitHub Pages**.
- Le site est généré à partir de la branche `main`, racine `/`.
- Une fois le code modifié en local, le déploiement se fait automatiquement après `git push`.

#### 🧪 Développement local :
- Utilisation de `bundle exec jekyll serve` pour prévisualiser le site.
- Les fichiers `.md` sont transformés en `.html` par Jekyll.

---

### 🧩 Pages personnalisées

| Page              | Rôle                                  |
|-------------------|----------------------------------------|
| `index.md`        | Accueil avec présentation, expériences |
| `about.md`        | Bio plus complète (à propos)           |
| `projects.md`     | Section projets                        |
| `strategie.md`    | Offres & stratégie                     |
| `contact.md`      | Infos de contact + LinkedIn/email      |
| `404.html`        | Page d’erreur fun & stylée 😄          |

---

## 🚀 Déploiement local

```bash
# Installer les dépendances Ruby (nécessite Ruby + Bundler)
bundle install

# Lancer le serveur local
bundle exec jekyll serve

# Accéder au site
http://localhost:4000
```

---

## 🔍 SEO et Référencement

Le site est optimisé pour les moteurs de recherche grâce aux éléments suivants :

- **`jekyll-seo-tag`** : Génère automatiquement les balises meta utiles (titre, description, OpenGraph, etc.)
- **`jekyll-sitemap`** : Génère un fichier `sitemap.xml` listant toutes les pages à indexer
- **Structure sémantique** : Titres hiérarchisés (`h1`, `h2`, etc.), contenu bien structuré
- **URL propres** hébergées via **GitHub Pages**
- **Accessibilité publique** à l’adresse suivante :  
  👉 [https://hamzaatig.github.io/atig-hamza-portfolio-/](https://hamzaatig.github.io/atig-hamza-portfolio-/)

✅ Bonne syntaxe PowerShell (Windows)
```
$env:JEKYLL_ENV="production"; bundle exec jekyll build
```

---

## 📄 Licence

Ce projet est open-source sous licence **GPL-3.0**.

---

## 🙌 Remerciements

Merci à [Jekyll](https://jekyllrb.com) et [GitHub Pages](https://pages.github.com) pour cette stack simple, efficace et 100 % gratuite 💙

---

> ✉️ Pour toute question, n’hésitez pas à me contacter via [hamza.atig@gmail.com](mailto:hamza.atig@gmail.com)
