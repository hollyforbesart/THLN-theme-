/* THLN prototype — progressive enhancement only; every page works without JS. */
(function () {
  var header = document.querySelector('.site-header');
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('primary-nav');

  // Header hairline once the page scrolls
  if (header) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 8); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Mobile menu
  if (toggle && nav) {
    var setOpen = function (open) {
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      nav.classList.toggle('is-open', open);
    };
    toggle.addEventListener('click', function () { setOpen(toggle.getAttribute('aria-expanded') !== 'true'); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) setOpen(false); });
    window.matchMedia('(min-width: 1081px)').addEventListener('change', function () { setOpen(false); });
  }

  // Blog topic filter (in WordPress these become real category archive links)
  var topics = document.querySelectorAll('[data-topic]');
  topics.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var t = btn.getAttribute('data-topic');
      topics.forEach(function (b) { b.setAttribute('aria-pressed', String(b === btn)); });
      document.querySelectorAll('.post-grid .post-card').forEach(function (card) {
        card.hidden = t !== 'all' && card.getAttribute('data-cat') !== t;
      });
    });
  });

  // Article table of contents: highlight current section
  var tocLinks = document.querySelectorAll('.toc a');
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var map = {};
    tocLinks.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          tocLinks.forEach(function (a) { a.classList.remove('is-active'); });
          var l = map[en.target.id]; if (l) l.classList.add('is-active');
        }
      });
    }, { rootMargin: '-20% 0px -70% 0px' });
    Object.keys(map).forEach(function (id) { var el = document.getElementById(id); if (el) io.observe(el); });
  }
  // Contact form: prototype only (WordPress uses a form plugin)
  var form = document.querySelector('.contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var status = form.querySelector('.form-status');
      if (!form.reportValidity()) return;
      status.hidden = false;
      status.textContent = 'Prototype only: this form doesn\'t send yet. In WordPress it will go to Holly\'s inbox.';
    });
  }
})();
