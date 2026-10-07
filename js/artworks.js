// Loads the artworks from content/obras.json (edited through Pages CMS)
// and builds the oracle carousel cards and the "All Works" grid.

const TEMAS = ['sol', 'magia', 'naturaleza'];

function el(tag, className, attrs = {}) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  Object.entries(attrs).forEach(([k, v]) => node.setAttribute(k, v));
  return node;
}

function img(obra) {
  return el('img', '', { src: obra.foto, alt: obra.titulo || '', loading: 'lazy' });
}

function carouselCard(obra) {
  const card = el('div', 'carousel-card', { 'data-tema': obra.emocion });
  const wrap = el('div', 'carousel-img-wrap');
  wrap.appendChild(img(obra));

  const meta = el('div', 'carousel-meta');
  const titulo = el('p', 'carousel-titulo');
  titulo.textContent = obra.titulo || '';
  const sub = el('p', 'carousel-subtitulo');
  sub.textContent = obra.tecnica || '';
  meta.append(titulo, sub);

  card.append(wrap, meta);
  return card;
}

function galleryItem(obra) {
  const item = el('div', 'fg-item');
  item.dataset.titulo = obra.titulo || '';
  item.dataset.medium = obra.tecnica || '';
  item.dataset.year   = obra.anio || '';
  item.dataset.desc   = obra.descripcion || '';
  item.appendChild(img(obra));
  return item;
}

export async function renderArtworks() {
  const track = document.getElementById('carousel-track');
  const grid  = document.querySelector('#full-gallery .full-gallery-grid');
  if (!track || !grid) return;

  let obras = [];
  try {
    const res = await fetch('content/obras.json', { cache: 'no-cache' });
    const data = await res.json();
    obras = (data.obras || []).filter(o => o && o.foto);
  } catch (err) {
    console.error('Could not load artworks', err);
    return;
  }

  // Carousel: grouped by emotion, keeping the order from the file
  const cards = document.createDocumentFragment();
  TEMAS.forEach(tema => {
    obras.filter(o => o.emocion === tema).forEach(o => cards.appendChild(carouselCard(o)));
  });
  track.appendChild(cards);

  // Full gallery: every artwork
  const items = document.createDocumentFragment();
  obras.forEach(o => items.appendChild(galleryItem(o)));
  grid.appendChild(items);
}
