import { initCursor, initProgress, initHamburger, initLang } from './navigation.js';
import { initHero } from './hero.js';
import { renderArtworks } from './artworks.js';
import { initOracle } from './oracle.js';
import { initGallery } from './gallery.js';
import { initWorkshop } from './workshop.js';

initCursor();
initProgress();
initHamburger();
initLang();
initHero();

// Artworks come from content/obras.json — build them before wiring up carousel + gallery
await renderArtworks();

initOracle();
initGallery();
initWorkshop();
