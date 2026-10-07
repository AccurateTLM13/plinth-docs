// Collapse the docs menu on small screens. Without JavaScript it stays open.
(function () {
  var details = document.querySelector('[data-nav-details]');
  if (!details) return;
  var query = window.matchMedia('(max-width: 59.99em)');
  function sync() { details.open = !query.matches; }
  sync();
  if (query.addEventListener) query.addEventListener('change', sync);
})();
