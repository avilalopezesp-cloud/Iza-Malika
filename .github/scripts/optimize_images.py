# Shrinks heavy artwork photos (e.g. straight from a phone) so the site stays fast.
# Keeps filename and format; fixes phone rotation. Light images are left untouched.
import sys
from pathlib import Path
from PIL import Image, ImageOps

MAX_SIDE = 1600
MAX_BYTES = 700 * 1024
EXTS = {'.jpg', '.jpeg', '.png', '.webp'}

def optimize(path: Path) -> bool:
    if path.suffix.lower() not in EXTS or path.stat().st_size <= MAX_BYTES:
        return False
    before = path.stat().st_size
    with Image.open(path) as im:
        im = ImageOps.exif_transpose(im)
        im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
        ext = path.suffix.lower()
        if ext in ('.jpg', '.jpeg'):
            im.convert('RGB').save(path, 'JPEG', quality=82, optimize=True, progressive=True)
        elif ext == '.webp':
            im.save(path, 'WEBP', quality=82)
        else:
            im.save(path, 'PNG', optimize=True)
    print(f'{path}: {before // 1024} KB -> {path.stat().st_size // 1024} KB')
    return True

if __name__ == '__main__':
    folder = Path(sys.argv[1] if len(sys.argv) > 1 else 'images/obras')
    changed = [p for p in sorted(folder.iterdir()) if p.is_file() and optimize(p)]
    print(f'{len(changed)} image(s) optimized')
