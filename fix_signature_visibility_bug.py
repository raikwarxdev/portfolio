import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Remove CSS transition-opacity duration-700 class from signature-source-path and enforce opacity:0 in style
    old_svg_path = 'id="signature-source-path" class="opacity-0 transition-opacity duration-700" style="display:inline-block; fill:#ffffff; stroke:#ffffff; stroke-width:0.5px;"'
    new_svg_path = 'id="signature-source-path" class="opacity-0" style="display:inline-block; fill:#ffffff; stroke:#ffffff; stroke-width:0.5px; opacity:0;"'

    if old_svg_path in content:
        content = content.replace(old_svg_path, new_svg_path)
        print(f"Updated SVG path element in {t}")

    # 2. Add explicit GSAP set at t=0.0 in aboutTl to force opacity:0 when Origin is open
    old_gsap_start = "aboutTl.to('#notebook-container', { \n                opacity: 1, \n                duration: 0.8, ease: \"power2.out\" \n            }, 0.0);"
    new_gsap_start = "aboutTl.set('#signature-source-path', { opacity: 0 }, 0.0);\n            aboutTl.to('#notebook-container', { \n                opacity: 1, \n                duration: 0.8, ease: \"power2.out\" \n            }, 0.0);"

    if old_gsap_start in content:
        content = content.replace(old_gsap_start, new_gsap_start)
        print(f"Added GSAP opacity reset at t=0 in {t}")
    else:
        # Fallback regex search for GSAP timeline start
        content = re.sub(
            r"(aboutTl\.to\('#notebook-container',\s*\{\s*opacity:\s*1,)",
            r"aboutTl.set('#signature-source-path', { opacity: 0 }, 0.0);\n            \1",
            content,
            count=1
        )
        print(f"Regex added GSAP opacity reset in {t}")

    with open(t, "w", encoding="utf-8") as f:
        f.write(content)

print("Signature visibility bug fix complete!")
