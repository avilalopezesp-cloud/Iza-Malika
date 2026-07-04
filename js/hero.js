export function initHero() {
  // ── Hero canvas (scroll-driven brush reveal) ─────────────────
  (function () {
    const canvas = document.getElementById('hero-canvas');
    const ctx    = canvas.getContext('2d');
    const RES    = 600;
    canvas.width = canvas.height = RES;
    const heroScrollEl = document.getElementById('hero-scroll');
    let loadedImg = null, lastProgress = -1;
    const rng = (function() {
      let s = 0xDEADBEEF;
      return () => { s ^= s << 13; s ^= s >> 17; s ^= s << 5; return (s >>> 0) / 0xFFFFFFFF; };
    })();
    const N = 90, STROKES = [];
    for (let i = 0; i < N; i++) {
      const t = i / N, eased = Math.pow(t, 0.65);
      const angle = eased * Math.PI * 9, radius = eased * RES * 0.46;
      const cx = RES/2 + Math.cos(angle) * radius;
      const cy = RES/2 + Math.sin(angle) * radius;
      const tangentAngle = angle + Math.PI/2 + (rng()-0.5) * 0.9;
      const sizeT = 0.3 + eased * 0.7;
      STROKES.push({ cx, cy, rx:(50+rng()*55)*sizeT, ry:(10+rng()*10)*sizeT, rot:tangentAngle, blur:7+rng()*8 });
    }
    const COVER = [
      { cx:RES*.5, cy:RES*.5, rx:RES*.55, ry:RES*.55, rot:0,   blur:22 },
      { cx:RES*.3, cy:RES*.2, rx:RES*.38, ry:RES*.15, rot:.4,  blur:18 },
      { cx:RES*.7, cy:RES*.2, rx:RES*.38, ry:RES*.15, rot:-.4, blur:18 },
      { cx:RES*.2, cy:RES*.7, rx:RES*.35, ry:RES*.14, rot:.6,  blur:18 },
      { cx:RES*.8, cy:RES*.7, rx:RES*.35, ry:RES*.14, rot:-.6, blur:18 },
      { cx:RES*.5, cy:RES*.1, rx:RES*.45, ry:RES*.12, rot:.1,  blur:18 },
      { cx:RES*.5, cy:RES*.9, rx:RES*.45, ry:RES*.12, rot:-.1, blur:18 },
    ];
    function drawReveal(progress) {
      if (!loadedImg) return;
      if (Math.abs(progress - lastProgress) < 0.003) return;
      lastProgress = progress;
      ctx.clearRect(0, 0, RES, RES);
      const exactCount = Math.max(0.04, progress) * N;
      const fullCount  = Math.floor(exactCount);
      const frac = exactCount - fullCount;
      for (let i = 0; i <= fullCount && i < N; i++) {
        const s = STROKES[i], alpha = (i === fullCount) ? frac : 1;
        ctx.save(); ctx.filter = `blur(${s.blur}px)`; ctx.globalAlpha = alpha;
        ctx.translate(s.cx, s.cy); ctx.rotate(s.rot);
        ctx.fillStyle = '#000'; ctx.beginPath();
        ctx.ellipse(0,0,s.rx,s.ry,0,0,Math.PI*2); ctx.fill(); ctx.restore();
      }
      if (progress > 0.85) {
        const ca = Math.min(1, (progress-0.85)/0.15);
        for (const s of COVER) {
          ctx.save(); ctx.filter=`blur(${s.blur}px)`; ctx.globalAlpha=ca*0.85;
          ctx.translate(s.cx,s.cy); ctx.rotate(s.rot);
          ctx.fillStyle='#000'; ctx.beginPath();
          ctx.ellipse(0,0,s.rx,s.ry,0,0,Math.PI*2); ctx.fill(); ctx.restore();
        }
      }
      ctx.globalAlpha = 1;
      ctx.globalCompositeOperation = 'source-in';
      ctx.drawImage(loadedImg, 0, 0, RES, RES);
      ctx.globalCompositeOperation = 'source-over';
    }
    function getProgress() {
      const trackH = heroScrollEl.offsetHeight - window.innerHeight;
      return Math.max(0, Math.min(1, window.scrollY / trackH));
    }
    const scrollHint = document.querySelector('.hero-scroll-hint');
    window.addEventListener('scroll', () => {
      requestAnimationFrame(() => {
        const p = getProgress();
        drawReveal(p);
        if (scrollHint) scrollHint.style.opacity = Math.max(0, 1 - p * 8);
      });
    }, { passive: true });
    const img = new Image();
    img.onload = () => { loadedImg = img; drawReveal(getProgress() || 0.01); };
    img.src = 'images/hero-spiral.webp';
  })();
}
