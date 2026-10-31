(function () {
  // #region agent log
  function dbg(hypothesisId, location, message, data) {
    fetch('http://127.0.0.1:7850/ingest/8dbf0039-6c7e-44d2-abd0-e5edbb27f7a8', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'X-Debug-Session-Id': 'a6a44b' },
      body: JSON.stringify({
        sessionId: 'a6a44b',
        runId: 'audit1',
        hypothesisId: hypothesisId,
        location: location,
        message: message,
        data: data || {},
        timestamp: Date.now()
      })
    }).catch(function () {});
  }
  window.addEventListener('error', function (e) {
    dbg('A', 'site.js:window.error', 'uncaught_error', {
      msg: String(e.message || ''),
      src: String(e.filename || ''),
      line: e.lineno || 0
    });
  });
  window.addEventListener('unhandledrejection', function (e) {
    dbg('A', 'site.js:unhandledrejection', 'promise_rejection', {
      reason: String((e.reason && e.reason.message) || e.reason || '')
    });
  });
  // #endregion

  var nav = document.getElementById("nav");
  var menuBtn = document.getElementById("menuBtn");
  var mobile = document.getElementById("mobile");
  var forceLight = document.body.classList.contains("nav-light");

  // #region agent log
  dbg('C', 'site.js:dom', 'critical_dom', {
    hasNav: !!nav,
    hasMenuBtn: !!menuBtn,
    hasMobile: !!mobile,
    forceLight: forceLight,
    path: String(location.pathname || location.href),
    protocol: location.protocol
  });
  var cssLink = document.querySelector('link[rel="stylesheet"][href*="site.css"]');
  var logoImg = document.querySelector('.brand img');
  function checkRes(label, el, hyp) {
    if (!el) {
      dbg(hyp, 'site.js:res', label + '_missing_el', {});
      return;
    }
    if (el.tagName === 'LINK') {
      try {
        var sheet = el.sheet;
        dbg(hyp, 'site.js:res', label + '_css', { loaded: !!sheet, href: el.href || '' });
      } catch (err) {
        dbg(hyp, 'site.js:res', label + '_css_blocked', { err: String(err.message || err) });
      }
    }
    if (el.tagName === 'IMG') {
      dbg(hyp, 'site.js:res', label + '_img', {
        complete: el.complete,
        naturalWidth: el.naturalWidth || 0,
        src: el.currentSrc || el.src || ''
      });
    }
  }
  checkRes('css', cssLink, 'B');
  checkRes('logo', logoImg, 'B');
  var broken = [];
  document.querySelectorAll('a[href]').forEach(function (a) {
    var h = a.getAttribute('href') || '';
    if (!h || h.charAt(0) === '#' || /^https?:/i.test(h) || /^mailto:/i.test(h)) return;
    if (h === './' || h === '../' || /\/$/.test(h)) broken.push(h);
  });
  dbg('E', 'site.js:links', 'folder_style_hrefs', { count: broken.length, samples: broken.slice(0, 8) });
  // #endregion

  function onScroll() {
    if (!nav) return;
    if (forceLight) {
      nav.classList.add("on-light");
      return;
    }
    nav.classList.toggle("is-solid", window.scrollY > 40);
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (menuBtn && mobile) {
    menuBtn.addEventListener("click", function () {
      menuBtn.classList.toggle("active");
      mobile.classList.toggle("open");
      // #region agent log
      dbg('C', 'site.js:menu', 'menu_toggle', { open: mobile.classList.contains('open') });
      // #endregion
    });
    mobile.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        menuBtn.classList.remove("active");
        mobile.classList.remove("open");
      });
    });
  }

  var els = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) e.target.classList.add("in");
      });
    }, { threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add("in"); });
  }

  // #region agent log
  dbg('D', 'site.js:reveal', 'reveal_setup', {
    count: els.length,
    hasIO: 'IntersectionObserver' in window
  });
  // #endregion

  var sampleHiAudio = null;

  function playHiAudio() {
    try {
      if (!sampleHiAudio) {
        sampleHiAudio = new Audio("assets/sample-hi.mp3");
      }
      sampleHiAudio.pause();
      sampleHiAudio.currentTime = 0;
      var p = sampleHiAudio.play();
      if (p && typeof p.then === "function") {
        p.then(function () {
          // #region agent log
          dbg('H1', 'site.js:playSample', 'hi_audio_ok', { src: sampleHiAudio.currentSrc || sampleHiAudio.src });
          // #endregion
        }).catch(function (err) {
          // #region agent log
          dbg('H1', 'site.js:playSample', 'hi_audio_fail', { err: String(err && err.message || err) });
          // #endregion
          speakWithTts("hi");
        });
      }
      return true;
    } catch (err) {
      // #region agent log
      dbg('H1', 'site.js:playSample', 'hi_audio_throw', { err: String(err && err.message || err) });
      // #endregion
      return false;
    }
  }

  function speakWithTts(lang) {
    if (!("speechSynthesis" in window)) return;
    var voices = window.speechSynthesis.getVoices() || [];
    var want = lang === "hi" ? "hi" : "en";
    var match = null;
    for (var i = 0; i < voices.length; i++) {
      var vl = (voices[i].lang || "").toLowerCase();
      if (vl.indexOf(want) === 0) { match = voices[i]; break; }
    }
    // #region agent log
    dbg('H1', 'site.js:playSample', 'tts_voices', {
      lang: lang,
      voiceCount: voices.length,
      picked: match ? (match.name + "|" + match.lang) : null,
      langs: voices.slice(0, 12).map(function (v) { return v.lang; })
    });
    // #endregion
    window.speechSynthesis.cancel();
    var u = new SpeechSynthesisUtterance();
    if (lang === "hi" && !match) {
      // No Hindi system voice — romanized en-IN so sample still audibly plays
      u.lang = "en-IN";
      u.text = "Do sau pachaas rupaye praapt hue";
      for (var j = 0; j < voices.length; j++) {
        if ((voices[j].lang || "").toLowerCase().indexOf("en-in") === 0) {
          match = voices[j];
          break;
        }
      }
    } else {
      u.lang = lang === "hi" ? "hi-IN" : "en-IN";
      u.text = lang === "hi" ? "दो सौ पचास रुपये प्राप्त हुए" : "Two hundred fifty rupees received";
    }
    if (match) u.voice = match;
    u.rate = 0.95;
    u.onstart = function () {
      // #region agent log
      dbg('H1', 'site.js:playSample', 'tts_start', { lang: u.lang });
      // #endregion
    };
    u.onerror = function (e) {
      // #region agent log
      dbg('H1', 'site.js:playSample', 'tts_error', { error: String(e.error || '') });
      // #endregion
    };
    window.setTimeout(function () {
      window.speechSynthesis.speak(u);
    }, 40);
  }

  // Chrome loads voices async
  if ("speechSynthesis" in window) {
    window.speechSynthesis.getVoices();
    window.speechSynthesis.addEventListener("voiceschanged", function () {
      window.speechSynthesis.getVoices();
    });
  }

  window.playSample = function (lang) {
    // #region agent log
    dbg('D', 'site.js:playSample', 'play_clicked', {
      lang: lang,
      hasSpeech: 'speechSynthesis' in window,
      runId: 'post-fix'
    });
    // #endregion
    if (lang === "hi") {
      if (playHiAudio()) return;
    }
    speakWithTts(lang || "en");
  };

  // #region agent log
  dbg('A', 'site.js:boot', 'boot_ok', { t: Date.now() });
  // #endregion
})();
