# Iza Malika — Handoff Checklist

**Project:** Iza Malika Portfolio Website  
**Developer:** Sebastián Ávila  
**Version:** 1.0 · July 2026

---

## Before Handing Off

- [x] All pages render correctly in Chrome, Safari, and Firefox
- [x] Mobile layout tested at 375px (iPhone) and 768px (iPad)
- [x] All animations work on first load and after page refresh
- [x] Language toggle (EN ↔ ES) works and persists on reload
- [x] Oracle buttons open correct themed carousels
- [x] Carousel swipe works on touch devices
- [x] All artwork images load (no broken images)
- [x] Lightbox opens and closes correctly
- [x] WhatsApp buttons contain the correct phone number
- [x] WhatsApp message language matches the site language
- [x] Full gallery opens and all images load
- [x] Workshop section scroll animations trigger correctly
- [x] Footer loads correctly on all screen sizes
- [x] No JavaScript errors in the browser console
- [x] Page title and meta description are set correctly

---

## Content Review (Client to Confirm)

- [ ] All artwork titles are spelled correctly
- [ ] All artwork dimensions and mediums are accurate
- [ ] About section bio text is final
- [ ] Workshop cards (3 items) — titles and descriptions are accurate
- [ ] Oracle button labels (Sun / Magic / Nature) match Iza's vision
- [ ] Footer tagline text is approved
- [ ] Instagram handle (`iza.groot`) is correct
- [ ] WhatsApp number (`+31 610 291 900`) is correct and active
- [ ] All Spanish translations reviewed by a native speaker

---

## Before Going Live

- [ ] Choose a hosting platform (GitHub Pages recommended — free)
- [ ] Register a custom domain if desired (e.g. `izamalika.com`)
- [ ] Upload all project files to the hosting platform
- [ ] Test the live URL in an incognito/private browser window
- [ ] Test on a real mobile phone (not just browser emulation)
- [ ] Confirm all images load on the live URL (not just locally)
- [ ] Add the site to Google Search Console (optional, improves SEO)
- [ ] Submit sitemap to Google (optional)

---

## After Going Live

- [ ] Share the live URL with Iza for final approval
- [ ] Test WhatsApp buttons from the live URL (not local)
- [ ] Test language toggle on the live URL
- [ ] Bookmark the live URL for future reference
- [ ] Save a copy of the project folder as a backup

---

## How to Make Future Edits

### Editing text

1. Open `index.html` in a text editor (VS Code recommended)
2. Search (`Cmd+F`) for the text you want to change
3. If the text has a `data-i18n` attribute, also update `js/navigation.js`
4. Save and refresh the browser

### Replacing an artwork image

1. Name your new image exactly the same as the one you're replacing
2. Place it in `images/obras/`
3. The website will automatically use the new image

### Adding a new artwork

See Section 5 of `README.md` for step-by-step instructions.

### Changing the WhatsApp number

Search for `31610291900` in these 3 files and replace:
- `index.html`
- `js/navigation.js`
- `js/gallery.js`

### Testing changes locally

You need a local server (not just opening the file in a browser).  
Run this in Terminal:
```bash
cd /path/to/Iza.Malika
python3 -m http.server 3456
```
Then open `http://localhost:3456` in your browser.

---

## Files Delivered

| File | Description |
|---|---|
| `index.html` | Main website file |
| `css/style.css` | Global styles |
| `css/components.css` | UI components |
| `css/animations.css` | Animations and scroll reveals |
| `css/responsive.css` | Mobile breakpoints |
| `js/main.js` | JS entry point |
| `js/navigation.js` | Nav, language system, translations |
| `js/hero.js` | Canvas animation |
| `js/oracle.js` | Oracle + carousel |
| `js/gallery.js` | Gallery + lightbox |
| `js/workshop.js` | Workshop animations |
| `js/utils.js` | Shared utilities |
| `images/` | All artwork and workshop photos |
| `delivery/README.md` | Full technical documentation |
| `delivery/design-tokens.json` | All design values in JSON format |
| `delivery/Iza_Malika_Brand_Guidelines.pdf` | Brand identity guide |
| `delivery/HANDOFF-CHECKLIST.md` | This file |

---

## Support

For questions about the website, contact:  
**Sebastián Ávila** · avilalopezesp@gmail.com
