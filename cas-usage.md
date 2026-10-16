---
layout: default
title: "Cas d'usage"
permalink: /cas-usage
lang: fr
description: "Cas d'usage de modernisation cloud, sécurité IAM, DevSecOps, intégration et benchmark de performance (Java, GraalVM, Spring Boot, Quarkus, Go, Rust, C, C++)."
alternate: /en/use-cases
hero_title: "Cas d'usage : modernisation, sécurité et intégration"
hero_subtitle: "Exemples concrets orientés résultats : architecture, sécurité, performance"
---

Quatre exemples concrets. Ouvrez celui qui vous intéresse.

<details class="uc" id="benchmark" open markdown="1">
<summary>Choisir une pile technique par la mesure <span class="uc-tag">Benchmark · 6 langages · 3 frameworks Java</span></summary>

Pour un service transactionnel critique, quel langage, quel framework, quel accès à la base ? Plutôt que d'en débattre, je l'ai mesuré, à travail strictement égal : mêmes requêtes SQL, même ordre, mêmes ressources pour chaque version. Les résultats sont présentés en indices relatifs ; voici la méthode et quelques extraits.

**La méthode en bref :** 6 langages, 3 frameworks Java, 3 techniques d'accès aux données · plus de 300 mesures retenues, des dizaines de millions d'opérations · plus de 150 contrôles automatiques, dont une vérification d'intégrité des données à la fin de chaque mesure : toute mesure qui échoue est rejetée · rapport produit automatiquement depuis les résultats.

**Extrait : un service d'entrée HTTP réécrit en 8 versions.** Indice 100 = Java sans framework sur la JVM. Mémoire, calcul et démarrage : plus bas = mieux. Capacité : plus haut = mieux.

<div class="bench-charts">
<div class="bench-chart" role="img" aria-label="Mémoire au pic par version">
<p class="bench-title">Mémoire au pic<span>indice, plus court = mieux</span></p>
<div class="bench-row"><span class="bench-label">C</span><span class="bench-track"><span class="bench-bar" style="width:10%"></span></span><span class="bench-val">10</span></div>
<div class="bench-row"><span class="bench-label">C++</span><span class="bench-track"><span class="bench-bar" style="width:10%"></span></span><span class="bench-val">10</span></div>
<div class="bench-row"><span class="bench-label">Rust</span><span class="bench-track"><span class="bench-bar" style="width:20%"></span></span><span class="bench-val">20</span></div>
<div class="bench-row"><span class="bench-label">Go</span><span class="bench-track"><span class="bench-bar" style="width:30%"></span></span><span class="bench-val">30</span></div>
<div class="bench-row"><span class="bench-label">Java natif (GraalVM)</span><span class="bench-track"><span class="bench-bar" style="width:40%"></span></span><span class="bench-val">40</span></div>
<div class="bench-row"><span class="bench-label">Quarkus (JVM)</span><span class="bench-track"><span class="bench-bar" style="width:90%"></span></span><span class="bench-val">90</span></div>
<div class="bench-row"><span class="bench-label">Java (JVM)</span><span class="bench-track"><span class="bench-bar" style="width:100%"></span></span><span class="bench-val">100</span></div>
<div class="bench-row"><span class="bench-label">Spring Boot</span><span class="bench-track"><span class="bench-bar" style="width:100%"></span></span><span class="bench-val">100</span></div>
</div>
<div class="bench-chart" role="img" aria-label="Calcul par opération, trois mesures par version">
<p class="bench-title">Calcul par opération, une mesure = un point<span>indice, plus à gauche = mieux ; points serrés = résultat stable</span></p>
<div class="bench-row"><span class="bench-label">C++</span><span class="bench-track bench-dots"><span class="bench-dot" style="left:22.5%"></span><span class="bench-dot" style="left:25.0%"></span><span class="bench-dot" style="left:22.5%"></span></span><span class="bench-val">45</span></div>
<div class="bench-row"><span class="bench-label">C</span><span class="bench-track bench-dots"><span class="bench-dot" style="left:25.0%"></span><span class="bench-dot" style="left:25.0%"></span><span class="bench-dot" style="left:25.0%"></span></span><span class="bench-val">50</span></div>
<div class="bench-row"><span class="bench-label">Rust</span><span class="bench-track bench-dots"><span class="bench-dot" style="left:47.5%"></span><span class="bench-dot" style="left:45.0%"></span><span class="bench-dot" style="left:45.0%"></span></span><span class="bench-val">90</span></div>
<div class="bench-row"><span class="bench-label">Java natif (GraalVM)</span><span class="bench-track bench-dots"><span class="bench-dot" style="left:47.5%"></span><span class="bench-dot" style="left:47.5%"></span><span class="bench-dot" style="left:47.5%"></span></span><span class="bench-val">95</span></div>
<div class="bench-row"><span class="bench-label">Java (JVM)</span><span class="bench-track bench-dots"><span class="bench-dot" style="left:50.0%"></span><span class="bench-dot" style="left:50.0%"></span><span class="bench-dot" style="left:55.0%"></span></span><span class="bench-val">100</span></div>
<div class="bench-row"><span class="bench-label">Go</span><span class="bench-track bench-dots"><span class="bench-dot" style="left:60.0%"></span><span class="bench-dot" style="left:62.5%"></span><span class="bench-dot" style="left:60.0%"></span></span><span class="bench-val">120</span></div>
<div class="bench-row"><span class="bench-label">Spring Boot</span><span class="bench-track bench-dots"><span class="bench-dot" style="left:85.0%"></span><span class="bench-dot" style="left:70.0%"></span><span class="bench-dot" style="left:55.0%"></span></span><span class="bench-val">140</span></div>
<div class="bench-row"><span class="bench-label">Quarkus (JVM)</span><span class="bench-track bench-dots"><span class="bench-dot" style="left:95.0%"></span><span class="bench-dot" style="left:92.5%"></span><span class="bench-dot" style="left:95.0%"></span></span><span class="bench-val">190</span></div>
<div class="bench-row"><span></span><span class="bench-axis"><span style="left:0%">0</span><span style="left:25%">50</span><span style="left:50%">100</span><span style="left:75%">150</span><span style="left:100%">200</span></span><span></span></div>
</div>
</div>

| Version | Mémoire au pic | Calcul par opération | Capacité | Démarrage |
|---|---|---|---|---|
| Java (JVM, sans framework) | 100 | 100 | 100 | 100 |
| Java natif (GraalVM) | 40 | 95 | 120 | 40 |
| Spring Boot | 100 | 140 | 110 | 335 |
| Quarkus (JVM) | 90 | 190 | 90 | 165 |
| Go | 30 | 120 | 140 | 40 |
| Rust | 20 | 90 | 120 | 15 |
| C | 10 | 50 | 140 | 80 |
| C++ | 10 | 45 | 140 | 40 |

**Extrait : un service transactionnel en 6 langages.** Indice 100 = Java sur la JVM.

<div class="bench-charts">
<div class="bench-chart" role="img" aria-label="Débit en local et avec le réseau par langage">
<p class="bench-title">Service transactionnel : le réseau efface presque le langage<span>opérations par seconde, indice, plus long = mieux</span></p>
<div class="bench-row"><span class="bench-label">Java (JVM)</span><span class="bench-track"><span class="bench-bar" style="width:69%"></span><span class="bench-bar alt" style="width:69%"></span></span><span class="bench-val" style="line-height:13px;font-size:0.8rem">100<br>100</span></div>
<div class="bench-row"><span class="bench-label">Java natif (GraalVM)</span><span class="bench-track"><span class="bench-bar" style="width:86%"></span><span class="bench-bar alt" style="width:69%"></span></span><span class="bench-val" style="line-height:13px;font-size:0.8rem">125<br>100</span></div>
<div class="bench-row"><span class="bench-label">Go</span><span class="bench-track"><span class="bench-bar" style="width:100%"></span><span class="bench-bar alt" style="width:72%"></span></span><span class="bench-val" style="line-height:13px;font-size:0.8rem">145<br>105</span></div>
<div class="bench-row"><span class="bench-label">Rust</span><span class="bench-track"><span class="bench-bar" style="width:100%"></span><span class="bench-bar alt" style="width:72%"></span></span><span class="bench-val" style="line-height:13px;font-size:0.8rem">145<br>105</span></div>
<div class="bench-row"><span class="bench-label">C</span><span class="bench-track"><span class="bench-bar" style="width:100%"></span><span class="bench-bar alt" style="width:72%"></span></span><span class="bench-val" style="line-height:13px;font-size:0.8rem">145<br>105</span></div>
<div class="bench-row"><span class="bench-label">C++</span><span class="bench-track"><span class="bench-bar" style="width:97%"></span><span class="bench-bar alt" style="width:76%"></span></span><span class="bench-val" style="line-height:13px;font-size:0.8rem">140<br>110</span></div>
<p class="bench-legend"><i style="background:#3498db;margin-left:0"></i>base sur la même machine<i style="background:#a9cfee"></i>base à distance (latence réaliste)</p>
</div>
</div>

**Ce que les mesures montrent :**

- Avec GraalVM, le même code Java compilé en natif consomme moins de la moitié de la mémoire, sans aucune modification.
- Sur un service transactionnel, Go, Rust, C et C++ font environ 40 % de mieux que Java en local. Avec une latence réseau réaliste vers la base, l'écart tombe sous 10 % : le réseau efface presque le langage.
- Le levier le plus rentable n'est pas le langage : diviser par deux les échanges avec la base fait gagner environ 70 % en local, et double le nombre d'opérations par seconde avec le réseau.
- Spring Boot est le moins régulier d'une mesure à l'autre ; Java natif, C et Quarkus donnent des résultats très stables.
- JPA traite environ 30 % d'opérations en moins que JDBC ou jOOQ quand la base est à distance.
- Près de la saturation, le ramasse-miettes ZGC tient des temps de réponse (p99) environ 5 fois plus bas que G1, pour environ 15 % de calcul en plus.

Le rapport complet (méthode, graphiques, limites) se présente en rendez-vous.

</details>

{% for usecase in site.use_cases %}
<details class="uc" id="{{ usecase.title | slugify: "latin" }}" markdown="1">
<summary>{{ usecase.title }}</summary>

**Contexte** : {{ usecase.context }}

**Approche** :
{% for item in usecase.approach %}
- {{ item }}
{% endfor %}

**Résultats** :
{% for item in usecase.results %}
- {{ item }}
{% endfor %}

</details>
{% endfor %}

## Besoin d'un cas similaire ?

Parlons-en : [me contacter]({{ "/contact" | relative_url }}).

<script>
(function () {
  function openTarget() {
    var id = decodeURIComponent(location.hash.slice(1));
    var d = id && document.getElementById(id);
    if (d && d.tagName === "DETAILS") { d.open = true; d.scrollIntoView(); }
  }
  window.addEventListener("hashchange", openTarget);
  openTarget();
})();
</script>
