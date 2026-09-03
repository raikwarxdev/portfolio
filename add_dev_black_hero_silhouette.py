import os
import shutil
import re

brain_src = "/Users/devkumarraikwar/.gemini/antigravity/brain/4d2ee6b3-6590-4b2c-9024-99929f0c6f18/media__1788383876894.png"

dest_dirs = [
    "/Users/devkumarraikwar/portfolio/images",
    "/Users/devkumarraikwar/Desktop/images",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/images"
]

if os.path.exists(brain_src):
    for d in dest_dirs:
        os.makedirs(d, exist_ok=True)
        dest_path = os.path.join(d, "dev_hero_cutout.png")
        shutil.copy2(brain_src, dest_path)
        print(f"Copied cutout image to {dest_path}")

silhouette_html = """<!-- HERO BLACK SILHOUETTE CUTOUT -->
                    <div id="dev-hero-silhouette" class="absolute bottom-0 left-1/2 -translate-x-1/2 w-[90%] max-w-[700px] h-[90%] max-h-[800px] z-[12] pointer-events-none flex items-end justify-center">
                        <img loading="lazy" src="./images/dev_hero_cutout.png" alt="Dev Silhouette" class="w-full h-full object-contain object-bottom filter brightness-0 contrast-200 opacity-90 drop-shadow-[0_25px_60px_rgba(0,0,0,0.95)]" />
                    </div>"""

targets = [
    "/Users/devkumarraikwar/portfolio/index.html",
    "/Users/devkumarraikwar/Desktop/index.html",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"
]

pattern = r'(<div id="hero-lighting" [^>]+></div>)'

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    if 'id="dev-hero-silhouette"' not in content:
        content = re.sub(pattern, r'\1\n                    ' + silhouette_html, content, count=1)
        with open(t, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Added black silhouette element in {t}")
    else:
        print(f"Silhouette element already exists in {t}")

print("Hero black silhouette setup complete!")
