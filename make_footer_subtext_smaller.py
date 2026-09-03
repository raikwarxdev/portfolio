import os

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

old_line = '<span class="font-[\'Gloria_Hallelujah\'] text-4xl md:text-[50px] text-[var(--blue)] leading-none transform -rotate-[2deg] mt-1 md:mt-2">(thanks for scrolling this far)</span>'
new_line = '<span class="font-[\'Gloria_Hallelujah\'] text-lg md:text-2xl text-[var(--blue)] leading-none transform -rotate-[2deg] mt-1 md:mt-2 opacity-90">(thanks for scrolling this far)</span>'

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    if old_line in content:
        content = content.replace(old_line, new_line)
        with open(t, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated footer signature subtext font size in {t}")
    else:
        print(f"Warning: line not found in {t}")

print("Footer subtext font size reduction complete!")
