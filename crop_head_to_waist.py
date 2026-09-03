import os
import shutil
from PIL import Image
import re

brain_src = "/Users/devkumarraikwar/.gemini/antigravity/brain/4d2ee6b3-6590-4b2c-9024-99929f0c6f18/media__1788383876894.png"

dest_dirs = [
    "/Users/devkumarraikwar/portfolio/images",
    "/Users/devkumarraikwar/Desktop/images",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/images"
]

if os.path.exists(brain_src):
    im = Image.open(brain_src).convert("RGBA")
    w, h = im.size
    print(f"Original image size: {w}x{h}")

    # The person's bounding box:
    # Head is near y=0, hoodie waist ends at around 62% of height
    # Let's crop from y=0 to y=int(h * 0.63)
    crop_box = (0, 0, w, int(h * 0.63))
    cropped_im = im.crop(crop_box)

    # Trim any outer white or transparent padding around the cropped upper body
    bbox = cropped_im.getbbox()
    if bbox:
        cropped_im = cropped_im.crop(bbox)

    print(f"Cropped head-to-waist image size: {cropped_im.size}")

    for d in dest_dirs:
        os.makedirs(d, exist_ok=True)
        dest_file = os.path.join(d, "dev_hero_cutout.png")
        cropped_im.save(dest_file)
        print(f"Saved head-to-waist cutout to {dest_file}")

# Update HTML styling to render this head-to-waist silhouette LARGE, CLEAN, & DEAD-CENTERED
new_silhouette_html = """<!-- ENLARGED & DEAD-CENTERED HEAD-TO-WAIST HERO BLACK SILHOUETTE -->
                    <div id="dev-hero-silhouette" class="absolute bottom-0 left-1/2 -translate-x-1/2 w-[110%] max-w-[950px] h-[95%] max-h-[950px] z-[15] pointer-events-none flex items-end justify-center">
                        <img loading="lazy" src="./images/dev_hero_cutout.png" alt="Dev Silhouette" class="w-full h-full object-contain object-bottom filter brightness-0 contrast-200 opacity-95 drop-shadow-[0_30px_70px_rgba(0,0,0,0.95)] transform translate-x-[4%] scale-110 md:scale-125 origin-bottom" />
                    </div>"""

pattern = r'<div id="dev-hero-silhouette"[\s\S]*?</div>'

targets = [
    "/Users/devkumarraikwar/portfolio/index.html",
    "/Users/devkumarraikwar/Desktop/index.html",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"
]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(pattern, new_silhouette_html, content, count=1)
    with open(t, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated head-to-waist silhouette in {t}")

print("Head-to-waist silhouette crop & styling complete!")
