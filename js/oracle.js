import { onVisible } from './utils.js';

export function initOracle() {
  const carouselSection   = document.getElementById('carousel-section');
  const carouselCounter   = document.getElementById('carousel-counter');
  const carouselThemeLbl  = document.getElementById('carousel-theme-label');
  const prevBtn           = document.getElementById('carousel-prev');
  const nextBtn           = document.getElementById('carousel-next');
  const oracleEl          = document.getElementById('oracle');
  const intuitionEl       = document.querySelector('.oracle-intuition');

  let activeCards = [], currentIdx = 0;

  function animateCounter(current, total) {
    if (!carouselCounter) return;
    carouselCounter.style.transition = 'none';
    carouselCounter.style.opacity = '0';
    carouselCounter.style.transform = 'translateY(6px)';
    requestAnimationFrame(() => {
      carouselCounter.textContent = `${current} / ${total}`;
      carouselCounter.style.transition = 'opacity 0.4s ease, transform 0.4s cubic-bezier(0.16,1,0.3,1)';
      carouselCounter.style.opacity = '1';
      carouselCounter.style.transform = 'translateY(0)';
    });
  }

  function positionCards(instant) {
    // Hide all cards not in activeCards
    document.querySelectorAll('.carousel-card').forEach(c => {
      if (!activeCards.includes(c)) {
        c.style.transition = 'none';
        c.style.opacity = '0';
        c.style.transform = 'translateX(300%) scale(0.75)';
        c.style.pointerEvents = 'none';
        c.style.zIndex = '0';
        c.removeAttribute('data-active');
      }
    });

    activeCards.forEach((card, i) => {
      const off = i - currentIdx;
      const abs = Math.abs(off);
      const sign = off >= 0 ? 1 : -1;
      card.style.transition = instant ? 'none' : 'transform 0.85s cubic-bezier(0.25,1,0.5,1), opacity 0.7s ease';

      if (abs === 0) {
        card.style.opacity = '1';
        card.style.transform = 'translateX(0) scale(1)';
        card.style.zIndex = '10';
        card.style.pointerEvents = 'auto';
        card.setAttribute('data-active', '');
      } else if (abs === 1) {
        card.style.opacity = '0.48';
        card.style.transform = `translateX(${sign * 82}%) scale(0.85)`;
        card.style.zIndex = '6';
        card.style.pointerEvents = 'none';
        card.removeAttribute('data-active');
      } else if (abs === 2) {
        card.style.opacity = '0.2';
        card.style.transform = `translateX(${sign * 155}%) scale(0.73)`;
        card.style.zIndex = '3';
        card.style.pointerEvents = 'none';
        card.removeAttribute('data-active');
      } else {
        card.style.opacity = '0';
        card.style.transform = `translateX(${sign * 300}%) scale(0.65)`;
        card.style.zIndex = '0';
        card.style.pointerEvents = 'none';
        card.removeAttribute('data-active');
      }
    });

    if (instant) {
      requestAnimationFrame(() => activeCards.forEach(c => { c.style.transition = ''; }));
    }
  }

  function showCard(idx) {
    if (!activeCards.length) return;
    currentIdx = ((idx % activeCards.length) + activeCards.length) % activeCards.length;
    positionCards(false);
    animateCounter(currentIdx + 1, activeCards.length);
  }

  prevBtn && prevBtn.addEventListener('click', () => showCard(currentIdx - 1));
  nextBtn && nextBtn.addEventListener('click', () => showCard(currentIdx + 1));

  // Touch swipe
  let touchStartX = 0;
  const track = document.getElementById('carousel-track');
  if (track) {
    track.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; }, { passive: true });
    track.addEventListener('touchend', e => {
      const dx = e.changedTouches[0].clientX - touchStartX;
      if (Math.abs(dx) > 45) showCard(dx < 0 ? currentIdx + 1 : currentIdx - 1);
    }, { passive: true });
  }

  // Oracle icon click
  document.querySelectorAll('.oracle-icon-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const tema  = btn.dataset.tema;
      const color = btn.dataset.color;
      const label = btn.dataset.label || tema;

      document.querySelectorAll('.oracle-icon-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      activeCards = Array.from(document.querySelectorAll(`.carousel-card[data-tema="${tema}"]`));
      currentIdx = 0;

      positionCards(true);
      animateCounter(1, activeCards.length);

      if (carouselThemeLbl) carouselThemeLbl.textContent = label.toUpperCase();
      if (carouselSection) {
        carouselSection.style.backgroundColor = color;
        carouselSection.classList.add('active');
      }

      requestAnimationFrame(() => carouselSection.scrollIntoView({ behavior: 'smooth', block: 'start' }));
    });
  });

  // Discover another feeling — scroll back to oracle
  const discoverBtn = document.getElementById('discover-btn');
  if (discoverBtn) {
    discoverBtn.addEventListener('click', () => {
      document.getElementById('oracle').scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  }

  // Oracle reveal → expand → bloom
  onVisible(oracleEl, el => {
    el.classList.add('visible');
    setTimeout(() => el.classList.add('expanded'), 900);
    // Preload full gallery images in background
    document.querySelectorAll('#full-gallery .fg-item img').forEach(img => {
      const pre = new Image(); pre.src = img.src;
    });
  }, 0.25);

  if (intuitionEl) {
    intuitionEl.addEventListener('mouseenter', () => oracleEl && oracleEl.classList.add('expanded'));
  }

  // All Works CTA entrance + border animation
  const allWorksCta = document.getElementById('all-works-cta');
  const allWorksBtn = document.getElementById('all-works-open-btn');
  if (allWorksCta) {
    onVisible(allWorksCta, (el) => {
      el.classList.add('aw-in');
      setTimeout(() => allWorksBtn && allWorksBtn.classList.add('border-drawn'), 800);
    }, 0.25);
  }
}
