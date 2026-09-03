import os

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

old_block = '<div class="w-full aspect-[4/3.2] bg-[#05080f] flex items-center justify-center overflow-hidden relative shadow-[inset_0_2px_5px_rgba(0,0,0,0.6)] rounded-sm">\n                                                    <img loading="lazy" src="./images/WhatsApp Image 2026-09-03 at 02.21.51.jpeg" alt="Polaroid Memory" class="w-full h-full object-cover object-[center_15%] transition-all duration-500" />\n                                                </div>'

new_block = '<div class="w-full aspect-square bg-[#05080f] flex items-center justify-center overflow-hidden relative shadow-[inset_0_2px_5px_rgba(0,0,0,0.6)] rounded-sm">\n                                                    <img loading="lazy" src="./images/WhatsApp Image 2026-09-03 at 02.21.51.jpeg" alt="Dev Kumar Raikwar (Myself)" class="w-full h-full object-contain object-center p-1 transition-all duration-500" />\n                                                </div>'

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    if old_block in content:
        content = content.replace(old_block, new_block)
        with open(t, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated full face polaroid in {t}")
    else:
        # Replace aspect-[4/3.2] and object-[center_15%]
        content = content.replace("aspect-[4/3.2]", "aspect-square")
        content = content.replace("object-cover object-[center_15%]", "object-contain object-center p-1")
        with open(t, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fallback updated full face polaroid in {t}")

print("Full face polaroid update complete!")
