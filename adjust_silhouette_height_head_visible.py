import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

new_silhouette_html = """<!-- ENLARGED & DEAD-CENTERED HEAD-TO-WAIST HERO BLACK SILHOUETTE (HEAD 100% VISIBLE) -->
                    <div id="dev-hero-silhouette" class="absolute bottom-[2%] left-1/2 -translate-x-1/2 w-[90%] max-w-[720px] h-[82%] max-h-[740px] z-[15] pointer-events-none flex items-end justify-center">
                        <img loading="lazy" src="./images/dev_hero_cutout.png" alt="Dev Silhouette" class="w-full h-full object-contain object-bottom filter brightness-0 contrast-200 opacity-95 drop-shadow-[0_25px_60px_rgba(0,0,0,0.95)] transform translate-x-[3%] scale-100 origin-bottom" />
                    </div>"""

pattern = r'<div id="dev-hero-silhouette"[\s\S]*?</div>'

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(pattern, new_silhouette_html, content, count=1)
    with open(t, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Adjusted silhouette height (head 100% visible) in {t}")

print("Silhouette height adjustment complete!")
