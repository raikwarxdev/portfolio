import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

old_cursive = '<div id="frag-origin-cursive" class="absolute top-[1%] left-[4%] font-[\'Gloria_Hallelujah\'] font-medium text-[15px] text-[var(--blue)] -rotate-3 focus-lift-target z-20 leading-[1.2]">'
new_cursive = '<div id="frag-origin-cursive" class="absolute top-[-3%] left-[4%] font-[\'Gloria_Hallelujah\'] font-medium text-[14px] md:text-[15px] text-[var(--blue)] -rotate-3 focus-lift-target z-20 leading-[1.2]">'

old_headline_div = '<div id="origin-headline" class="absolute top-[4%] left-[4%] w-[90%] font-[\'Inter\'] font-[900] text-[2.1vw] lg:text-[26px] xl:text-[24px] text-[var(--navy)] leading-[1.04] uppercase tracking-[-0.04em] focus-lift-target z-20">'
new_headline_div = '<div id="origin-headline" class="absolute top-[7%] left-[4%] w-[90%] font-[\'Inter\'] font-[900] text-[2.1vw] lg:text-[26px] xl:text-[24px] text-[var(--navy)] leading-[1.04] uppercase tracking-[-0.04em] focus-lift-target z-20">'

old_micro_div = '<div id="origin-micro-story" aria-hidden="true" class="absolute top-[52%] xl:top-[54%] left-[4%] w-[72%] font-[\'Schoolbell\'] text-[10px] md:text-[11px] text-[#222]/90 leading-[1.6] focus-lift-target z-20">'
new_micro_div = '<div id="origin-micro-story" aria-hidden="true" class="absolute top-[55%] xl:top-[57%] left-[4%] w-[72%] font-[\'Schoolbell\'] text-[10px] md:text-[11px] text-[#222]/90 leading-[1.6] focus-lift-target z-20">'

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    if old_cursive in content:
        content = content.replace(old_cursive, new_cursive)
    else:
        content = re.sub(r'<div id="frag-origin-cursive" class="[^"]+">', new_cursive, content, count=1)

    if old_headline_div in content:
        content = content.replace(old_headline_div, new_headline_div)
    else:
        content = re.sub(r'<div id="origin-headline" class="[^"]+">', new_headline_div, content, count=1)

    if old_micro_div in content:
        content = content.replace(old_micro_div, new_micro_div)
    else:
        content = re.sub(r'<div id="origin-micro-story" [^>]+>', new_micro_div, content, count=1)

    with open(t, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed cursive overlap in {t}")

print("Cursive overlap fix applied across all HTML files!")
