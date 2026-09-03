import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

old_desc_block = """<!-- Description -->
                                                <div class="mt-2.5 flex flex-col items-start gap-0.5">
                                                    <div aria-hidden="true" class="font-['Schoolbell'] text-[8px] font-bold text-black/80 uppercase">Dev Kumar Raikwar (Myself)</div>
                                                    <div aria-hidden="true" class="font-['Schoolbell'] text-[7px] text-black/50 leading-tight">building AI systems @ MUJ.</div>
                                                </div>"""

new_desc_block = """<!-- Description -->
                                                <div class="mt-2.5 flex flex-col items-center justify-center w-full">
                                                    <div aria-hidden="true" class="font-['Schoolbell'] text-[10px] md:text-[11px] font-bold text-black/90 uppercase text-center leading-snug">Dev Kumar Raikwar (Myself)</div>
                                                </div>"""

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    if old_desc_block in content:
        content = content.replace(old_desc_block, new_desc_block)
        with open(t, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated polaroid description in {t}")
    else:
        # Fallback regex search
        pattern = r'<!-- Description -->[\s\S]*?building AI systems @ MUJ\.</div>\s*</div>'
        content = re.sub(pattern, new_desc_block, content, count=1)
        with open(t, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fallback updated polaroid description in {t}")

print("Polaroid caption update complete!")
