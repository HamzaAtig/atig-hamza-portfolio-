/* Consentement et mesure d'audience. Fichier identique sur les trois sites
   (portfolio, AgentForge, Aegis Defend) : le modifier ici, puis le recopier.

   Règles CNIL appliquées :
   - aucun cookie de mesure tant que le visiteur n'a pas accepté
     (GA4 tourne en Consent Mode v2 « refusé » par défaut, voir gtag-init) ;
   - « Refuser » aussi visible et aussi simple que « Accepter » ;
   - choix conservé 6 mois, modifiable à tout moment (lien [data-cc-open]).

   Clarity et LinkedIn Insight ne se chargent qu'après accord, et seulement
   si leur identifiant est renseigné sur la balise <script> :
   data-clarity="..." data-linkedin="..." */
(function () {
  "use strict";

  var me = document.currentScript;
  var CLARITY = (me && me.dataset.clarity) || "";
  var LINKEDIN = (me && me.dataset.linkedin) || "";
  var KEY = "cc-choice-v1";
  var MAX_AGE = 182 * 864e5;
  var en = (document.documentElement.lang || "fr").slice(0, 2) === "en";

  function track(name, params) {
    if (typeof window.gtag === "function") window.gtag("event", name, params || {});
  }

  /* ── Choix mémorisé ── */
  function readChoice() {
    try {
      var c = JSON.parse(localStorage.getItem(KEY));
      if (c && (c.v === "granted" || c.v === "denied") && Date.now() - c.t < MAX_AGE) return c.v;
    } catch (e) {}
    return null;
  }
  function saveChoice(v) {
    try { localStorage.setItem(KEY, JSON.stringify({ v: v, t: Date.now() })); } catch (e) {}
  }

  /* ── Outils optionnels, chargés seulement après accord ── */
  var extrasLoaded = false;
  function loadExtras() {
    if (extrasLoaded) return;
    extrasLoaded = true;
    if (CLARITY) {
      (function (c, l, a, r, i, t, y) {
        c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
        t = l.createElement(r); t.async = 1; t.src = "https://www.clarity.ms/tag/" + i;
        y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
      })(window, document, "clarity", "script", CLARITY);
      window.clarity("consent");
    }
    if (LINKEDIN) {
      window._linkedin_partner_id = LINKEDIN;
      window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
      window._linkedin_data_partner_ids.push(LINKEDIN);
      if (!window.lintrk) {
        window.lintrk = function (a, b) { window.lintrk.q.push([a, b]); };
        window.lintrk.q = [];
      }
      var s = document.createElement("script");
      s.async = true;
      s.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
      document.head.appendChild(s);
    }
  }

  function clearCookies() {
    var host = location.hostname;
    var domains = ["", host, "." + host, "." + host.split(".").slice(-2).join(".")];
    document.cookie.split(";").forEach(function (c) {
      var name = c.split("=")[0].trim();
      if (!/^(_ga|_gid|_clck|_clsk|li_|lms_|AnalyticsSyncHistory|UserMatchHistory)/.test(name)) return;
      domains.forEach(function (d) {
        document.cookie = name + "=; Max-Age=0; path=/" + (d ? "; domain=" + d : "");
      });
    });
  }

  function apply(v) {
    if (typeof window.gtag === "function") {
      window.gtag("consent", "update", { analytics_storage: v });
    }
    if (v === "granted") loadExtras();
  }

  /* ── Bandeau ── */
  var style = document.createElement("style");
  style.textContent =
    ".cc-banner{position:fixed;left:16px;right:16px;bottom:16px;z-index:9999;max-width:760px;margin:0 auto;" +
    "background:var(--cc-bg,#fff);color:var(--cc-fg,#222);border:1px solid var(--cc-border,#ddd);border-radius:10px;" +
    "padding:14px 16px;box-shadow:0 8px 30px rgba(0,0,0,.25);display:flex;gap:14px;align-items:center;flex-wrap:wrap;" +
    "font-family:inherit;font-size:14px;line-height:1.5}" +
    ".cc-banner[hidden]{display:none}" +
    ".cc-text{flex:1 1 320px;margin:0}" +
    ".cc-actions{display:flex;gap:8px;flex:0 0 auto}" +
    ".cc-btn{cursor:pointer;border-radius:6px;padding:8px 18px;font:inherit;font-weight:600;" +
    "border:1px solid var(--cc-accent,#3498db);background:var(--cc-accent,#3498db);color:var(--cc-accent-fg,#fff)}" +
    ".cc-btn:hover{filter:brightness(1.08)}";
  document.head.appendChild(style);

  var tools = ["Google Analytics"];
  if (CLARITY) tools.push("Microsoft Clarity");
  if (LINKEDIN) tools.push("LinkedIn");
  var list = tools.join(", ");

  var banner = document.createElement("div");
  banner.className = "cc-banner";
  banner.hidden = true;
  banner.setAttribute("role", "dialog");
  banner.setAttribute("aria-label", en ? "Cookie consent" : "Consentement aux cookies");
  banner.innerHTML =
    '<p class="cc-text">' +
    (en
      ? "Audience measurement: this site uses " + list + " to understand how it is used. No cookie is set without your consent. You can change your mind at any time via the “Cookies” link at the bottom of the page."
      : "Mesure d'audience : ce site utilise " + list + " pour comprendre comment il est consulté. Aucun cookie n'est déposé sans votre accord. Vous pouvez changer d'avis à tout moment via le lien « Cookies » en bas de page.") +
    "</p>" +
    '<div class="cc-actions">' +
    '<button type="button" class="cc-btn" data-cc="denied">' + (en ? "Decline" : "Refuser") + "</button>" +
    '<button type="button" class="cc-btn" data-cc="granted">' + (en ? "Accept" : "Accepter") + "</button>" +
    "</div>";

  function show() { banner.hidden = false; }

  banner.addEventListener("click", function (e) {
    var btn = e.target.closest("[data-cc]");
    if (!btn) return;
    var v = btn.getAttribute("data-cc");
    var previous = readChoice();
    saveChoice(v);
    banner.hidden = true;
    track("consent_choice", { choice: v });
    if (v === "denied") {
      clearCookies();
      apply("denied");
      if (previous === "granted" && extrasLoaded) location.reload();
    } else {
      apply("granted");
    }
  });

  function init() {
    document.body.appendChild(banner);
    var choice = readChoice();
    if (choice) apply(choice);
    else show();

    document.addEventListener("click", function (e) {
      var open = e.target.closest("[data-cc-open]");
      if (open) { e.preventDefault(); show(); return; }

      var a = e.target.closest("a[href]");
      if (!a) return;
      var href = a.getAttribute("href");
      var where = whereIs(a);

      if (/calendly\.com/.test(href)) {
        track("book_call_click", { link_location: where });
      } else if (a.matches("a.lang-switch, .lang-switch a")) {
        track("lang_switch", { to_lang: en ? "fr" : "en" });
      } else if (/^mailto:/.test(href)) {
        track("email_click", { link_location: where });
      } else if (/linkedin\.com/.test(href)) {
        track("linkedin_click", { link_location: where });
      } else if (a.host && a.host !== location.host) {
        var target =
          /aegis-defend/.test(href) ? "aegis-defend" :
          /agentforge/.test(href) ? "agentforge" :
          /atig-hamza-portfolio-/.test(href) ? "portfolio" : "";
        if (target) track("cross_site_click", { target_site: target, link_location: where });
      }
    });

    /* Sections réellement atteintes, une fois par page */
    if ("IntersectionObserver" in window) {
      var seen = {};
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en_) {
          if (!en_.isIntersecting || seen[en_.target.id]) return;
          seen[en_.target.id] = true;
          track("section_view", { section_id: en_.target.id });
          io.unobserve(en_.target);
        });
      }, { rootMargin: "0px 0px -40% 0px" });
      document.querySelectorAll("section[id], main h2[id]").forEach(function (el) { io.observe(el); });
    }

    /* Lecture vidéo YouTube : le clic dans l'iframe fait perdre le focus à la page */
    var played = {};
    window.addEventListener("blur", function () {
      setTimeout(function () {
        var f = document.activeElement;
        if (!f || f.tagName !== "IFRAME" || !/youtube/.test(f.src)) return;
        var id = (f.src.match(/embed\/([\w-]+)/) || [])[1] || "unknown";
        if (played[id]) return;
        played[id] = true;
        track("video_play", { video_id: id, link_location: whereIs(f) });
      }, 0);
    });
  }

  function whereIs(el) {
    var sec = el.closest("section[id]");
    if (sec) return sec.id;
    if (el.closest("footer")) return "footer";
    if (el.closest("nav, .topnav")) return "nav";
    if (el.closest("header, .hero")) return "hero";
    return "page";
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
