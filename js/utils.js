/**
 * Calls fn(element) once when el enters the viewport.
 * @param {Element} el
 * @param {Function} fn
 * @param {number} threshold 0–1
 */
export function onVisible(el, fn, threshold = 0.15) {
  if (!el) return;
  new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        fn(entry.target);
        obs.unobserve(entry.target);
      }
    });
  }, { threshold }).observe(el);
}
