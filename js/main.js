// West Paws — small, dependency-free helpers
(function () {
  // Mobile menu
  var t = document.querySelector('.nav-toggle'), n = document.querySelector('.nav');
  if (t && n) t.addEventListener('click', function () {
    var o = n.classList.toggle('open'); t.setAttribute('aria-expanded', o);
  });

  // Case filters
  var f = document.querySelectorAll('.filters button');
  f.forEach(function (b) {
    b.addEventListener('click', function () {
      f.forEach(function (x) { x.classList.remove('on'); }); b.classList.add('on');
      var k = b.getAttribute('data-f');
      document.querySelectorAll('#case-grid .case').forEach(function (c) {
        c.hidden = !(k === 'all' || c.getAttribute('data-cat') === k);
      });
    });
  });

  // Highlight today's hours
  var d = new Date().getDay(); // 0 = Sunday
  var idx = d === 0 ? 6 : d - 1;
  var row = document.querySelector('.hours tr[data-day="' + idx + '"]');
  if (row) row.classList.add('today');

  // Conversion tracking for Meta Pixel / GA4 (no-op until those tags are enabled)
  document.addEventListener('click', function (e) {
    var a = e.target.closest('[data-track]'); if (!a) return;
    var kind = a.getAttribute('data-track');
    try { if (window.fbq) fbq('track', 'Contact', { method: kind }); } catch (_) {}
    try { if (window.gtag) gtag('event', 'contact_click', { method: kind, page: location.pathname }); } catch (_) {}
  });
})();
