const TRANSLATIONS = {
  en: {
    'nav-explore':      'Explore',
    'nav-workshops':    'Workshops',
    'hero-sub':         'Endlessly creating',
    'manifesto-1':      'For me, art is',
    'manifesto-2':      'stopping time —',
    'manifesto-3':      'a way to listen to nature,',
    'manifesto-4':      'to <span class="frase-gold">magic</span>, to the quiet voice',
    'manifesto-5':      'that lives inside.',
    'about-desc':       'I believe art begins with intuition. Painting is my way of slowing down, reconnecting with nature and expressing what words often can\'t.',
    'oracle-question':  'How are you feeling today?',
    'oracle-sub':       'Choose the emotion that resonates with you and discover artworks inspired by that feeling.',
    'oracle-sun':       'Sun',
    'oracle-magic':     'Magic',
    'oracle-nature':    'Nature',
    'discover-btn':     '↑ Discover another feeling',
    'all-works-label':  'Continue exploring.',
    'all-works-heading':'Every painting begins<br>with a feeling.',
    'all-works-sub':    'Acrylics, watercolors, mandalas and portraits — each piece born from a feeling, a moment, an impulse to create.',
    'all-works-btn':    'Discover the Collection',
    'gallery-title':    'All Works',
    'modal-wa-btn':     'I\'m interested',
    'bridge-1':         'Art is personal.',
    'bridge-2':         'But it\'s even more powerful',
    'bridge-3':         'when it\'s shared.',
    'ws-hero-label':    'Painting Together',
    'ws-heading-1':     'Creative',
    'ws-heading-2':     'Experiences',
    'ws-subhead':       'More than learning how to paint, these workshops create space to slow down, reconnect with yourself and enjoy making something with your own hands. Every session is different because every group brings its own energy.',
    'ws-card-1-title':  'No experience needed',
    'ws-card-1-desc':   'Come exactly as you are.',
    'ws-card-2-title':  'Everything is provided',
    'ws-card-2-desc':   'Just bring your curiosity.',
    'ws-card-3-title':  'Hosted anywhere',
    'ws-card-3-desc':   'Hostels · Cafés · Retreats · Creative Spaces',
    'ws-note-1':        'No one knew each other at the beginning.',
    'ws-note-2':        'Two hours later, everyone was smiling.',
    'ws-note-3':        'No experience. Just curiosity.',
    'ws-note-4':        'Every stroke tells something you didn\'t plan.',
    'ws-note-5':        'The mess is part of it.',
    'ws-quote':         'Art brings<br><span class="ws-quote-people">people</span> together.',
    'ws-cta-h1':        'Interested in an artwork?',
    'ws-cta-btn1':      'Ask about an artwork',
    'ws-cta-h2':        'Want to host a workshop?',
    'ws-cta-btn2':      'Let\'s create together',
    'footer-tagline':   'Thank you for visiting my world.',
  },
  es: {
    'nav-explore':      'Explorar',
    'nav-workshops':    'Talleres',
    'hero-sub':         'Creando sin parar',
    'manifesto-1':      'Para mí, el arte es',
    'manifesto-2':      'detener el tiempo —',
    'manifesto-3':      'una forma de escuchar la naturaleza,',
    'manifesto-4':      'a la <span class="frase-gold">magia</span>, a esa voz silenciosa',
    'manifesto-5':      'que vive dentro.',
    'about-desc':       'Creo que el arte comienza con la intuición. Pintar es mi forma de desacelerar, reconectarme con la naturaleza y expresar lo que las palabras a veces no pueden.',
    'oracle-question':  '¿Cómo te sientes hoy?',
    'oracle-sub':       'Elige la emoción que más resuena contigo y descubre obras inspiradas en ese sentimiento.',
    'oracle-sun':       'Sol',
    'oracle-magic':     'Magia',
    'oracle-nature':    'Naturaleza',
    'discover-btn':     '↑ Descubre otro sentimiento',
    'all-works-label':  'Sigue explorando.',
    'all-works-heading':'Cada pintura comienza<br>con un sentimiento.',
    'all-works-sub':    'Acrílicos, acuarelas, mandalas y retratos — cada obra nace de un sentimiento, un momento, un impulso de crear.',
    'all-works-btn':    'Descubre la Colección',
    'gallery-title':    'Todas las Obras',
    'modal-wa-btn':     'Me interesa',
    'bridge-1':         'El arte es personal.',
    'bridge-2':         'Pero es aún más poderoso',
    'bridge-3':         'cuando se comparte.',
    'ws-hero-label':    'Pintando Juntos',
    'ws-heading-1':     'Experiencias',
    'ws-heading-2':     'Creativas',
    'ws-subhead':       'Más que aprender a pintar, estos talleres crean un espacio para desacelerar, reconectarte contigo mismo y disfrutar de hacer algo con tus propias manos. Cada sesión es diferente porque cada grupo trae su propia energía.',
    'ws-card-1-title':  'Sin experiencia previa',
    'ws-card-1-desc':   'Ven exactamente como eres.',
    'ws-card-2-title':  'Todo está incluido',
    'ws-card-2-desc':   'Solo trae tu curiosidad.',
    'ws-card-3-title':  'En cualquier lugar',
    'ws-card-3-desc':   'Hostels · Cafés · Retiros · Espacios Creativos',
    'ws-note-1':        'Al principio nadie se conocía.',
    'ws-note-2':        'Dos horas después, todos sonreían.',
    'ws-note-3':        'Sin experiencia. Solo curiosidad.',
    'ws-note-4':        'Cada trazo cuenta algo que no planeaste.',
    'ws-note-5':        'El desorden es parte de todo.',
    'ws-quote':         'El arte une<br>a las <span class="ws-quote-people">personas</span>.',
    'ws-cta-h1':        '¿Te interesa una obra?',
    'ws-cta-btn1':      'Pregunta por una obra',
    'ws-cta-h2':        '¿Quieres organizar un taller?',
    'ws-cta-btn2':      'Creemos juntos',
    'footer-tagline':   'Gracias por visitar mi mundo.',
  }
};

let currentLang = localStorage.getItem('iza-lang') || 'en';

export function getCurrentLang() {
  return currentLang;
}

export function setLang(lang) {
  currentLang = lang;
  localStorage.setItem('iza-lang', lang);
  const t = TRANSLATIONS[lang];
  document.documentElement.lang = lang;

  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.dataset.i18n;
    if (t[key] !== undefined) el.innerHTML = t[key];
  });

  // Update oracle button data-label for carousel theme label
  document.querySelectorAll('.oracle-icon-btn').forEach(btn => {
    btn.dataset.label = lang === 'es' ? btn.dataset.labelEs : btn.dataset.label.replace(btn.dataset.labelEs || '', '') || btn.querySelector('.oracle-label').textContent;
  });

  // Update WhatsApp hrefs for CTA buttons
  const waArtwork = lang === 'es'
    ? 'https://wa.me/31610291900?text=Hola%20Iza!%20Vi%20tu%20trabajo%20y%20una%20de%20tus%20pinturas%20me%20llegó%20al%20alma.%20Me%20gustaría%20saber%20más.'
    : 'https://wa.me/31610291900?text=Hi%20Iza!%20I%20came%20across%20your%20work%20and%20one%20of%20your%20paintings%20really%20resonated%20with%20me.%20I%27d%20love%20to%20know%20more%20about%20it.';
  const waWorkshop = lang === 'es'
    ? 'https://wa.me/31610291900?text=Hola%20Iza!%20Me%20interesa%20organizar%20un%20taller%20de%20pintura.%20Me%20encantaría%20crear%20algo%20especial%20para%20mi%20comunidad.'
    : 'https://wa.me/31610291900?text=Hi%20Iza!%20I%27m%20interested%20in%20hosting%20a%20painting%20workshop.%20I%27d%20love%20to%20create%20something%20special%20for%20my%20community.';
  const b1 = document.getElementById('ws-cta-btn1');
  const b2 = document.getElementById('ws-cta-btn2');
  if (b1) b1.href = waArtwork;
  if (b2) b2.href = waWorkshop;

  // Update toggle buttons label (show the OTHER language)
  const nextLang = lang === 'en' ? 'ES' : 'EN';
  document.querySelectorAll('.lang-toggle').forEach(b => b.textContent = nextLang);
}

export function initCursor() {
  const cursor = document.getElementById('cursor');
  let cursorTicking = false, mouseX = -100, mouseY = -100;
  document.addEventListener('mousemove', e => {
    mouseX = e.clientX; mouseY = e.clientY;
    if (!cursorTicking) {
      requestAnimationFrame(() => {
        cursor.style.transform = `translate3d(${mouseX - 6}px,${mouseY - 6}px,0)`;
        cursorTicking = false;
      });
      cursorTicking = true;
    }
  }, { passive: true });
}

export function initProgress() {
  const progressBarEl = document.getElementById('progress');
  let scrollTicking = false;
  window.addEventListener('scroll', () => {
    if (!scrollTicking) {
      requestAnimationFrame(() => {
        const sy = window.scrollY;
        const total = document.body.scrollHeight - window.innerHeight;
        progressBarEl.style.width = (sy / total * 100) + '%';
        scrollTicking = false;
      });
      scrollTicking = true;
    }
  }, { passive: true });
}

export function initHamburger() {
  const hamburger = document.getElementById('nav-hamburger');
  const mobileMenu = document.getElementById('nav-mobile-menu');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      const isOpen = hamburger.classList.toggle('open');
      if (isOpen) {
        mobileMenu.classList.add('open');
        requestAnimationFrame(() => mobileMenu.classList.add('visible'));
      } else {
        mobileMenu.classList.remove('visible');
        setTimeout(() => mobileMenu.classList.remove('open'), 400);
      }
    });
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('open');
        mobileMenu.classList.remove('visible');
        setTimeout(() => mobileMenu.classList.remove('open'), 400);
      });
    });
  }
}

export function initLang() {
  setLang(currentLang);
  document.querySelectorAll('.lang-toggle').forEach(btn => {
    btn.addEventListener('click', () => setLang(currentLang === 'en' ? 'es' : 'en'));
  });
}
