---
layout: default
title: "Use cases"
permalink: /en/use-cases
lang: en
description: "Use cases for cloud modernization, IAM security, DevSecOps, integration and performance benchmarking (Java, GraalVM, Spring Boot, Quarkus, Go, Rust, C, C++)."
alternate: /cas-usage
hero_title: "Use cases: modernization, security and integration"
hero_subtitle: "Concrete examples with measurable outcomes"
---

Four concrete examples. Open the one that interests you.

<details class="uc" id="benchmark" open markdown="1">
<summary>Choosing a tech stack by measuring it <span class="uc-tag">Benchmark · 6 languages · 3 Java frameworks</span></summary>

For a critical transactional service, which language, which framework, which database access? Instead of debating it, I measured it, with strictly equal work: same SQL queries, same order, same resources for every version. Results are shown as relative indices; here are the method and a few excerpts.

**The method in short:** 6 languages, 3 Java frameworks, 3 data access techniques · over 300 retained measurements, tens of millions of operations · over 150 automated checks, including a data integrity verification at the end of each measurement: any measurement that fails is rejected · report produced automatically from the results.

**Excerpt: an HTTP entry service rewritten in 8 versions.** Index 100 = Java without a framework on the JVM. Memory, compute and startup: lower is better. Capacity: higher is better.

<div class="bench-charts">
<div class="bench-chart" role="img" aria-label="Peak memory per version">
<p class="bench-title">Peak memory<span>index, shorter is better</span></p>
<div class="bench-row"><span class="bench-label">C</span><span class="bench-track"><span class="bench-bar" style="width:10%"></span></span><span class="bench-val">10</span></div>
<div class="bench-row"><span class="bench-label">C++</span><span class="bench-track"><span class="bench-bar" style="width:10%"></span></span><span class="bench-val">10</span></div>
<div class="bench-row"><span class="bench-label">Rust</span><span class="bench-track"><span class="bench-bar" style="width:20%"></span></span><span class="bench-val">20</span></div>
<div class="bench-row"><span class="bench-label">Go</span><span class="bench-track"><span class="bench-bar" style="width:30%"></span></span><span class="bench-val">30</span></div>
<div class="bench-row"><span class="bench-label">Native Java (GraalVM)</span><span class="bench-track"><span class="bench-bar" style="width:40%"></span></span><span class="bench-val">40</span></div>
<div class="bench-row"><span class="bench-label">Quarkus (JVM)</span><span class="bench-track"><span class="bench-bar" style="width:90%"></span></span><span class="bench-val">90</span></div>
<div class="bench-row"><span class="bench-label">Java (JVM)</span><span class="bench-track"><span class="bench-bar" style="width:100%"></span></span><span class="bench-val">100</span></div>
<div class="bench-row"><span class="bench-label">Spring Boot</span><span class="bench-track"><span class="bench-bar" style="width:100%"></span></span><span class="bench-val">100</span></div>
</div>
<div class="bench-chart" role="img" aria-label="Compute per operation, three measurements per version">
<p class="bench-title">Compute per operation, one measurement = one dot<span>index, further left is better; tight dots = stable result</span></p>
<div class="bench-row"><span class="bench-label">C++</span><span class="bench-track bench-dots"><span class="bench-dot" style="left:22.5%"></span><span class="bench-dot" style="left:25.0%"></span><span class="bench-dot" style="left:22.5%"></span></span><span class="bench-val">45</span></div>
<div class="bench-row"><span class="bench-label">C</span><span class="bench-track bench-dots"><span class="bench-dot" style="left:25.0%"></span><span class="bench-dot" style="left:25.0%"></span><span class="bench-dot" style="left:25.0%"></span></span><span class="bench-val">50</span></div>
<div class="bench-row"><span class="bench-label">Rust</span><span class="bench-track bench-dots"><span class="bench-dot" style="left:47.5%"></span><span class="bench-dot" style="left:45.0%"></span><span class="bench-dot" style="left:45.0%"></span></span><span class="bench-val">90</span></div>
<div class="bench-row"><span class="bench-label">Native Java (GraalVM)</span><span class="bench-track bench-dots"><span class="bench-dot" style="left:47.5%"></span><span class="bench-dot" style="left:47.5%"></span><span class="bench-dot" style="left:47.5%"></span></span><span class="bench-val">95</span></div>
<div class="bench-row"><span class="bench-label">Java (JVM)</span><span class="bench-track bench-dots"><span class="bench-dot" style="left:50.0%"></span><span class="bench-dot" style="left:50.0%"></span><span class="bench-dot" style="left:55.0%"></span></span><span class="bench-val">100</span></div>
<div class="bench-row"><span class="bench-label">Go</span><span class="bench-track bench-dots"><span class="bench-dot" style="left:60.0%"></span><span class="bench-dot" style="left:62.5%"></span><span class="bench-dot" style="left:60.0%"></span></span><span class="bench-val">120</span></div>
<div class="bench-row"><span class="bench-label">Spring Boot</span><span class="bench-track bench-dots"><span class="bench-dot" style="left:85.0%"></span><span class="bench-dot" style="left:70.0%"></span><span class="bench-dot" style="left:55.0%"></span></span><span class="bench-val">140</span></div>
<div class="bench-row"><span class="bench-label">Quarkus (JVM)</span><span class="bench-track bench-dots"><span class="bench-dot" style="left:95.0%"></span><span class="bench-dot" style="left:92.5%"></span><span class="bench-dot" style="left:95.0%"></span></span><span class="bench-val">190</span></div>
<div class="bench-row"><span></span><span class="bench-axis"><span style="left:0%">0</span><span style="left:25%">50</span><span style="left:50%">100</span><span style="left:75%">150</span><span style="left:100%">200</span></span><span></span></div>
</div>
</div>

| Version | Peak memory | Compute per operation | Capacity | Startup |
|---|---|---|---|---|
| Java (JVM, no framework) | 100 | 100 | 100 | 100 |
| Native Java (GraalVM) | 40 | 95 | 120 | 40 |
| Spring Boot | 100 | 140 | 110 | 335 |
| Quarkus (JVM) | 90 | 190 | 90 | 165 |
| Go | 30 | 120 | 140 | 40 |
| Rust | 20 | 90 | 120 | 15 |
| C | 10 | 50 | 140 | 80 |
| C++ | 10 | 45 | 140 | 40 |

**Excerpt: a transactional service in 6 languages.** Index 100 = Java on the JVM.

<div class="bench-charts">
<div class="bench-chart" role="img" aria-label="Throughput locally and over the network per language">
<p class="bench-title">Transactional service: the network almost erases the language<span>operations per second, index, longer is better</span></p>
<div class="bench-row"><span class="bench-label">Java (JVM)</span><span class="bench-track"><span class="bench-bar" style="width:69%"></span><span class="bench-bar alt" style="width:69%"></span></span><span class="bench-val" style="line-height:13px;font-size:0.8rem">100<br>100</span></div>
<div class="bench-row"><span class="bench-label">Native Java (GraalVM)</span><span class="bench-track"><span class="bench-bar" style="width:86%"></span><span class="bench-bar alt" style="width:69%"></span></span><span class="bench-val" style="line-height:13px;font-size:0.8rem">125<br>100</span></div>
<div class="bench-row"><span class="bench-label">Go</span><span class="bench-track"><span class="bench-bar" style="width:100%"></span><span class="bench-bar alt" style="width:72%"></span></span><span class="bench-val" style="line-height:13px;font-size:0.8rem">145<br>105</span></div>
<div class="bench-row"><span class="bench-label">Rust</span><span class="bench-track"><span class="bench-bar" style="width:100%"></span><span class="bench-bar alt" style="width:72%"></span></span><span class="bench-val" style="line-height:13px;font-size:0.8rem">145<br>105</span></div>
<div class="bench-row"><span class="bench-label">C</span><span class="bench-track"><span class="bench-bar" style="width:100%"></span><span class="bench-bar alt" style="width:72%"></span></span><span class="bench-val" style="line-height:13px;font-size:0.8rem">145<br>105</span></div>
<div class="bench-row"><span class="bench-label">C++</span><span class="bench-track"><span class="bench-bar" style="width:97%"></span><span class="bench-bar alt" style="width:76%"></span></span><span class="bench-val" style="line-height:13px;font-size:0.8rem">140<br>110</span></div>
<p class="bench-legend"><i style="background:#3498db;margin-left:0"></i>database on the same machine<i style="background:#a9cfee"></i>remote database (realistic latency)</p>
</div>
</div>

**What the measurements show:**

- With GraalVM, the same Java code compiled to native uses less than half the memory, with no modification at all.
- On a transactional service, Go, Rust, C and C++ do about 40% better than Java locally. With realistic network latency to the database, the gap drops below 10%: the network almost erases the language.
- The most profitable lever is not the language: halving the exchanges with the database gains about 70% locally, and doubles the operations per second over the network.
- Spring Boot is the least consistent from one measurement to the next; native Java, C and Quarkus give very stable results.
- JPA handles about 30% fewer operations than JDBC or jOOQ when the database is remote.
- Near saturation, the ZGC garbage collector keeps response times (p99) about 5 times lower than G1, for about 15% more compute.

The full report (method, charts, limits) is presented in a call.

</details>

{% for usecase in site.use_cases %}
<details class="uc" id="{{ usecase.title_en | slugify: "latin" }}" markdown="1">
<summary>{{ usecase.title_en }}</summary>

**Context**: {{ usecase.context_en }}

**Approach**:
{% for item in usecase.approach_en %}
- {{ item }}
{% endfor %}

**Outcomes**:
{% for item in usecase.results_en %}
- {{ item }}
{% endfor %}

</details>
{% endfor %}

## Need a similar case?

Let's talk: [contact me]({{ "/en/contact" | relative_url }}).

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
