import { getCurrentLang } from './navigation.js';

export function initGallery() {
  const fullGallery = document.getElementById('full-gallery');
  const allWorksBtn = document.getElementById('all-works-open-btn');
  const artworkModal = document.getElementById('artwork-modal');
  const modalImg     = document.getElementById('modal-img');
  const modalTitulo  = document.getElementById('modal-titulo');
  const modalMedium  = document.getElementById('modal-medium');
  const modalYear    = document.getElementById('modal-year');
  const modalDesc    = document.getElementById('modal-desc');
  const modalWaBtn   = document.getElementById('modal-wa-btn');

  // All Works CTA button → open gallery with staggered animation
  if (allWorksBtn && fullGallery) {
    allWorksBtn.addEventListener('click', () => {
      if (!fullGallery.classList.contains('open')) {
        fullGallery.querySelectorAll('.fg-item').forEach((item, i) => {
          item.style.animationDelay = `${i * 38}ms`;
        });
        fullGallery.classList.add('open');
        allWorksBtn.textContent = 'Hide Gallery';
      } else {
        fullGallery.classList.remove('open');
        allWorksBtn.textContent = 'Discover the Collection';
      }
      if (fullGallery.classList.contains('open')) {
        setTimeout(() => fullGallery.scrollIntoView({ behavior: 'smooth', block: 'start' }), 80);
      }
    });
  }

  function openArtworkModal(item) {
    const img    = item.querySelector('img');
    const titulo = item.dataset.titulo;
    modalImg.src        = img.src;
    modalImg.alt        = img.alt;
    modalTitulo.textContent = titulo;
    modalMedium.textContent = item.dataset.medium;
    modalYear.textContent   = item.dataset.year;
    modalDesc.textContent   = item.dataset.desc;
    const msg = encodeURIComponent(`Hi Iza! I'm interested in your artwork "${titulo}". I'd love to know if it's still available.`);
    modalWaBtn.href = `https://wa.me/31610291900?text=${msg}`;
    artworkModal.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeArtworkModal() {
    artworkModal.classList.remove('open');
    document.body.style.overflow = '';
  }

  if (artworkModal) {
    artworkModal.querySelector('.artwork-modal-backdrop').addEventListener('click', closeArtworkModal);
    artworkModal.querySelector('.artwork-modal-close').addEventListener('click', closeArtworkModal);
    document.addEventListener('keydown', e => { if (e.key === 'Escape') closeArtworkModal(); });
  }

  document.querySelectorAll('.fg-item').forEach(item => {
    item.addEventListener('click', () => openArtworkModal(item));
  });
}
