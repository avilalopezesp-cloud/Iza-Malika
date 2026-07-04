import { onVisible } from './utils.js';

export function initWorkshop() {
  // Manifesto reveal
  onVisible(document.querySelector('#manifesto .frase-inner'), el => el.classList.add('visible'), 0.25);

  // About reveal
  const aboutImg  = document.querySelector('.about-img-wrap');
  const aboutText = document.querySelector('.about-text');
  if (aboutImg) {
    onVisible(aboutImg, () => {
      aboutImg.classList.add('visible');
      aboutText && aboutText.classList.add('visible');
    }, 0.15);
  }

  // Bridge quote reveal
  onVisible(document.getElementById('ws-bridge'), el => el.classList.add('bridge-in'), 0.3);

  // Workshops: title + text reveal
  onVisible(document.querySelector('#workshops .ws-heading'), el => {
    document.getElementById('workshops').classList.add('ws-text-in');
  }, 0.15);

  // Workshops: cards stagger
  document.querySelectorAll('.ws-card').forEach((card, i) => {
    card.style.transitionDelay = (i * 0.16) + 's';
    new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('ws-card-in');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.2 }).observe(card);
  });

  // Workshop hero parallax
  (function() {
    const heroImg = document.querySelector('.ws-hero img');
    if (!heroImg) return;
    function onScroll() {
      const rect = heroImg.closest('.ws-hero').getBoundingClientRect();
      if (rect.bottom > 0 && rect.top < window.innerHeight) {
        heroImg.style.transform = `translateY(${-rect.top * 0.22}px)`;
      }
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  })();

  // Workshops: quote & CTA reveal
  onVisible(document.querySelector('.ws-quote-wrap'), el => el.classList.add('ws-quote-in'), 0.3);
  onVisible(document.querySelector('.ws-cta-block'), el => el.classList.add('ws-cta-in'), 0.2);

  // Footer reveal
  onVisible(document.querySelector('footer'), el => el.classList.add('footer-in'), 0.2);
}
