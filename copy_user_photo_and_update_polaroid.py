import os
import shutil
import re

src_file = "/Users/devkumarraikwar/Desktop/images/WhatsApp Image 2026-09-03 at 02.21.51.jpeg"

dest_dirs = [
    "/Users/devkumarraikwar/portfolio/images",
    "/Users/devkumarraikwar/Desktop/images",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/images"
]

if os.path.exists(src_file):
    for d in dest_dirs:
        os.makedirs(d, exist_ok=True)
        target1 = os.path.join(d, "WhatsApp Image 2026-09-03 at 02.21.51.jpeg")
        target2 = os.path.join(d, "dev_polaroid_photo.jpeg")
        if os.path.abspath(src_file) != os.path.abspath(target1):
            shutil.copy2(src_file, target1)
        if os.path.abspath(src_file) != os.path.abspath(target2):
            shutil.copy2(src_file, target2)
        print(f"Verified photo in {d}")

new_polaroid_block = """<!-- POLAROID EVENT_01 ARTIFACT (Linked to Line) -->
                                            <div id="art-polaroid" class="absolute bottom-[25%] right-[2%] w-full max-w-[165px] bg-[#fdfdfc] p-3 pb-8 shadow-[4px_8px_16px_rgba(0,0,0,0.12),_inset_0_0_1px_rgba(0,0,0,0.1)] transform rotate-[4deg] origin-bottom-left flex flex-col z-20 focus-lift-target pointer-events-auto">
                                                <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-8 h-3 bg-white/40 border border-white/20 shadow-[0_1px_2px_rgba(0,0,0,0.05)] backdrop-blur-[1px] rotate-[-2deg] opacity-70 z-30" style="mix-blend-mode: multiply;"></div>
                                                <!-- Polaroid Image -->
                                                <div class="w-full aspect-[4/3.2] bg-[#05080f] flex items-center justify-center overflow-hidden relative shadow-[inset_0_2px_5px_rgba(0,0,0,0.6)] rounded-sm">
                                                    <img loading="lazy" src="./images/WhatsApp Image 2026-09-03 at 02.21.51.jpeg" alt="Dev Kumar Raikwar (Myself)" class="w-full h-full object-cover object-center transition-all duration-500" />
                                                </div>
                                                <!-- Description -->
                                                <div class="mt-2.5 flex flex-col items-start gap-0.5">
                                                    <div aria-hidden="true" class="font-['Schoolbell'] text-[8px] font-bold text-black/80 uppercase">Dev Kumar Raikwar (Myself)</div>
                                                    <div aria-hidden="true" class="font-['Schoolbell'] text-[7px] text-black/50 leading-tight">building AI systems @ MUJ.</div>
                                                </div>
                                            </div>"""

pattern = r'<!-- POLAROID EVENT_01 ARTIFACT \(Linked to Line\) -->[\s\S]*?</div>\s*</div>\s*<!-- CLUSTER 3'

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

    # Replace polaroid element
    new_content = re.sub(pattern, new_polaroid_block + "\n\n                                        <!-- CLUSTER 3", content, count=1)
    with open(t, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated Polaroid card in {t}")

print("Polaroid image update complete!")
