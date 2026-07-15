# Iza Malika — Website Documentation

**Version:** 1.0  
**Delivered:** July 2026  
**Developer:** Sebastián Ávila · avilalopezesp@gmail.com

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Project Structure](#2-project-structure)
3. [Technologies Used](#3-technologies-used)
4. [How to Edit Text](#4-how-to-edit-text)
5. [How to Replace Images](#5-how-to-replace-images)
6. [Languages (EN / ES)](#6-languages-en--es)
7. [How to Deploy](#7-how-to-deploy)
8. [File Organization](#8-file-organization)
9. [Common Tasks](#9-common-tasks)
10. [Design System Quick Reference](#10-design-system-quick-reference)

---

## 1. Project Overview

A single-page portfolio website for Iza Malika, a painter based in Granada, Spain.  
Built with pure HTML, CSS, and vanilla JavaScript — no frameworks, no build tools required.

**Live features:**
- Animated hero with spiral canvas painting
- Interactive emotional oracle (Sun / Magic / Nature) opening themed carousels
- Gallery-wall carousel with swipe support
- Full artwork grid with lightbox + WhatsApp inquiry
- Workshop section with editorial photo mosaic
- Bilingual: English / Spanish (persists via localStorage)
- Custom cursor, scroll progress bar, entrance animations

---

## 2. Project Structure

```
Iza.Malika/
├── index.html              ← Main HTML file (page structure only)
│
├── css/
│   ├── style.css           ← Global styles: variables, nav, hero, about, footer
│   ├── components.css      ← Components: oracle, carousel, gallery, workshops, buttons
│   ├── animations.css      ← All @keyframes and scroll-reveal state classes
│   └── responsive.css      ← All @media queries (mobile breakpoints)
│
├── js/
│   ├── main.js             ← Entry point: imports and calls all module inits
│   ├── utils.js            ← Shared helper: onVisible() for scroll animations
│   ├── navigation.js       ← Cursor, progress bar, hamburger menu, i18n system
│   ├── hero.js             ← Canvas spiral animation + scroll parallax
│   ├── oracle.js           ← Oracle buttons, carousel logic, touch/swipe
│   ├── gallery.js          ← Full gallery open/close, lightbox, WhatsApp links
│   └── workshop.js         ← All scroll-reveal animations for workshop section
│
└── images/
    ├── iza.jpg             ← Portrait photo (About section)
    ├── hero-spiral.webp    ← Hero background painting
    ├── favicon.ico         ← Browser tab icon
    ├── favicon.png         ← Browser tab icon (PNG)
    ├── obras/              ← All artwork images
    │   ├── sol-montana.jpg
    │   ├── mandala-sol.jpg
    │   └── ... (16 artworks total)
    └── workshops/
        ├── ws-2.jpg
        ├── ws-3.jpg
        └── ... (workshop photos)
```

---

## 3. Technologies Used

| Technology | Purpose | Notes |
|---|---|---|
| HTML5 | Page structure | Semantic, accessible markup |
| CSS3 | Styling + animations | Custom properties, Grid, Flexbox |
| Vanilla JS (ES Modules) | Interactivity | No frameworks, no dependencies |
| Google Fonts | Typography | Cormorant Garamond 300/400 |
| IntersectionObserver API | Scroll animations | Native browser API |
| Canvas API | Hero spiral animation | Drawn with requestAnimationFrame |
| localStorage | Language preference | Persists EN/ES choice |

**No npm. No webpack. No build step required.**  
Open `index.html` directly in a browser or serve from any static host.

---

## 4. How to Edit Text

### Option A: Edit directly in `index.html`

All visible text is in `index.html`. Open it in any text editor (VS Code, Notepad++, etc.)

**Important:** The site is bilingual. Most text appears in TWO places:
1. The HTML (default English text, shown on load)
2. The `TRANSLATIONS` object in `js/navigation.js` (both EN and ES values)

**You must update both places** when editing text that appears in both languages.

### Finding text in the HTML

Search (`Ctrl+F` / `Cmd+F`) for the text you want to change. Elements with `data-i18n` attributes are translatable:

```html
<!-- Example: oracle question -->
<p class="oracle-question" data-i18n="oracle-question">How are you feeling today?</p>
```

### Finding text in the translations file

Open `js/navigation.js` and search for the `data-i18n` key (e.g. `oracle-question`):

```js
const TRANSLATIONS = {
  en: {
    'oracle-question': 'How are you feeling today?',
    ...
  },
  es: {
    'oracle-question': '¿Cómo te sientes hoy?',
    ...
  }
};
```

Update both `en` and `es` values.

### Translatable text keys reference

| Key | Location | EN Default |
|---|---|---|
| `nav-explore` | Navigation | Explore |
| `nav-workshops` | Navigation | Workshops |
| `hero-sub` | Hero tagline | Endlessly creating |
| `oracle-question` | Oracle section | How are you feeling today? |
| `oracle-sub` | Oracle section | Choose the emotion... |
| `oracle-sun/magic/nature` | Oracle buttons | Sun / Magic / Nature |
| `discover-btn` | Carousel | ↑ Discover another feeling |
| `all-works-label` | Portfolio section | Continue exploring. |
| `all-works-heading` | Portfolio section | Every painting begins... |
| `all-works-btn` | Portfolio button | Discover the Collection |
| `gallery-title` | Gallery header | All Works |
| `modal-wa-btn` | Lightbox button | I'm interested |
| `bridge-1/2/3` | Bridge quote | Art is personal... |
| `ws-hero-label` | Workshop hero | Painting Together |
| `ws-heading-1/2` | Workshop title | Creative / Experiences |
| `ws-subhead` | Workshop description | More than learning... |
| `ws-card-1/2/3-title/desc` | Feature cards | No experience needed / ... |
| `ws-note-1 through 5` | Photo captions | No one knew each other... |
| `ws-quote` | Workshop quote | Art brings people together. |
| `ws-cta-h1/h2` | CTA headings | Interested in an artwork? |
| `ws-cta-btn1/btn2` | CTA buttons | Ask about an artwork |
| `footer-tagline` | Footer | Thank you for visiting... |

### Text NOT in the i18n system (English only)

- Manifesto quote (lines in `#manifesto` section)
- About section bio text
- Artwork titles and descriptions (in `data-titulo`, `data-desc` attributes on `.fg-item`)
- Footer name, copyright, credits

---

## 5. How to Replace Images

### Artwork images (`images/obras/`)

1. Name your new image the **same filename** as the one you're replacing
2. Use **JPG format**, recommended size: **800×1000px minimum** (4:5 ratio)
3. Replace the file — the website will automatically use it

**Artwork filenames:**
```
sol-montana.jpg      mandala-sol.jpg      flor-dorada.jpg
mandala-blanca.jpg   flamenco.jpg         luna-mistica.jpg
mandala-purpura.jpg  mujer-viento.jpg     mandala-lavanda.jpg
luna-mujer.jpg       diosa-acuarela.jpg   plantas-verdes.jpg
silueta-hojas.jpg    botanica.jpg         cuerpo-flores.jpg
bailarina-verde.jpg  retrato-femenino.jpg
```

### To add a new artwork

1. Add the image file to `images/obras/`
2. Add a carousel card in `index.html` (copy an existing one):
```html
<div class="carousel-card" data-tema="sol">
  <div class="carousel-img-wrap">
    <img src="images/obras/YOUR-FILE.jpg" alt="Artwork Title" loading="lazy" />
  </div>
  <div class="carousel-meta">
    <p class="carousel-titulo">Artwork Title</p>
    <p class="carousel-subtitulo">Acrylic · 50×40 cm</p>
  </div>
</div>
```
3. Add a gallery item in `index.html` (copy an existing one):
```html
<div class="fg-item"
  data-titulo="Artwork Title"
  data-medium="Acrylic on canvas"
  data-year="2025"
  data-desc="Description of the piece...">
  <img src="images/obras/YOUR-FILE.jpg" alt="Artwork Title" loading="lazy" />
</div>
```

### Portrait photo (`images/iza.jpg`)

Replace with same filename. Recommended: **3:4 ratio**, min 600×800px.

### Workshop photos (`images/workshops/`)

Files are named `ws-2.jpg` through `ws-8.jpg`. Replace with same filenames.  
Used sizes: hero is full-width (shoot landscape), editorial is portrait.

---

## 6. Languages (EN / ES)

The site defaults to **English**. The user's language choice is saved in the browser and remembered on next visit.

### To change the default language

In `js/navigation.js`, find this line:

```js
let currentLang = localStorage.getItem('iza-lang') || 'en';
```

Change `'en'` to `'es'` to default to Spanish.

### To add or change a translation

Open `js/navigation.js`. Find the `TRANSLATIONS` object:

```js
const TRANSLATIONS = {
  en: {
    'key': 'English text',
  },
  es: {
    'key': 'Texto en español',
  }
};
```

Update both `en` and `es` values for the key you want to change.

### WhatsApp message translations

Also in `js/navigation.js`, in the `setLang()` function, find:

```js
const waArtwork = lang === 'es'
  ? 'https://wa.me/31610291900?text=Hola%20Iza!...'
  : 'https://wa.me/31610291900?text=Hi%20Iza!...';
```

Update these URLs to change the pre-filled WhatsApp messages.

---

## 7. How to Deploy

### GitHub Pages (recommended — free)

1. Create a GitHub account at github.com if you don't have one
2. Create a new repository (e.g. `iza-malika`)
3. Upload all project files (drag and drop in GitHub's web interface, or use Git)
4. Go to **Settings → Pages**
5. Under "Source", select **Deploy from a branch** → **main** → **/ (root)**
6. Click Save — your site will be live at `https://yourusername.github.io/iza-malika`

**Important:** Keep the folder structure intact. All paths in the code are relative.

### Custom domain (e.g. izamalika.com)

1. Deploy to GitHub Pages first
2. In your domain registrar (GoDaddy, Namecheap, etc.), add these DNS records:
   ```
   A     @     185.199.108.153
   A     @     185.199.109.153
   A     @     185.199.110.153
   A     @     185.199.111.153
   CNAME www   yourusername.github.io
   ```
3. In GitHub Pages settings, enter your custom domain
4. Enable "Enforce HTTPS"

### Local development (testing changes)

You need a local server (not `file://`) because ES modules require HTTP.

**Option 1 — Python (no install needed):**
```bash
cd /path/to/Iza.Malika
python3 -m http.server 3456
# Open: http://localhost:3456
```

**Option 2 — Node.js:**
```bash
npx serve -l 3456 .
```

**Option 3 — VS Code:**  
Install the "Live Server" extension → right-click `index.html` → "Open with Live Server"

---

## 8. File Organization

### Current structure (post-refactor)

```
Iza.Malika/
├── index.html          Pure HTML — no CSS, no JS inline
├── css/                4 focused CSS files
├── js/                 7 ES module files, one responsibility each
├── images/             All visual assets
└── delivery/           This documentation package
```

### Recommended future additions

```
Iza.Malika/
├── ... (existing files)
└── assets/
    ├── images/         Move images/ here when restructuring
    ├── icons/          SVG icons, favicon files
    ├── fonts/          Self-hosted fonts (optional)
    └── videos/         Any future video content
```

---

## 9. Common Tasks

### Change the WhatsApp number

Search for `31610291900` across all files and replace with the new number (international format, no +).

Files affected: `index.html`, `js/navigation.js`, `js/gallery.js`

### Add a new oracle theme (e.g. "Fire")

1. Add a button in `index.html`:
```html
<button class="oracle-icon-btn" data-tema="fuego" data-color="#F0E8E0" data-label="Fire" data-label-es="Fuego">
  <span class="oracle-emoji">🔥</span>
  <span class="oracle-label" data-i18n="oracle-fire">Fire</span>
</button>
```
2. Add translations in `js/navigation.js` for `'oracle-fire'`
3. Add carousel cards with `data-tema="fuego"` in `index.html`

### Change the hero spiral colors

Open `js/hero.js`. Find the color arrays in the `initHero()` function and update the hex values.

### Adjust animation speed

Open `css/animations.css`. All transition durations are at the top of each block.  
The main spring easing is: `cubic-bezier(0.16, 1, 0.3, 1)` — keep this for consistency.

### Update the page title / SEO

In `index.html`, `<head>` section:
```html
<title>Iza Malika — Painter · Granada</title>
```

---

## 10. Design System Quick Reference

### Colors
```css
--cream:  #F5EDE0   /* Background */
--rose:   #C4687A   /* Accent */
--gold:   #C9A84C   /* Details */
--green:  #4A7C59   /* Nature accent */
--night:  #1C1C2E   /* Dark sections */
--ink:    #2A2018   /* Text & UI */
```

### Typography
- **Font:** Cormorant Garamond (Google Fonts)
- **Weights:** 300 (default), 400 (emphasis), italic variants
- **Display:** `clamp(3rem, 8vw, 6.5rem)`
- **Heading:** `clamp(2.4rem, 6.5vw, 5rem)`
- **Body:** `clamp(1rem, 1.8vw, 1.3rem)`
- **Label:** `0.72rem – 0.95rem`, uppercase, tracked

### Breakpoints
- Mobile: `max-width: 640px`
- Tablet: `max-width: 700px`
- Modal: `max-width: 600px`

---

*Crafted with care by Sebastián Ávila · July 2026*
