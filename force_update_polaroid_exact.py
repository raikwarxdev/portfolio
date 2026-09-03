import os

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

old_polaroid_html = """                                             <!-- POLAROID EVENT_01 ARTIFACT (Linked to Line) -->
                                             <div id="art-polaroid" class="absolute bottom-[25%] right-[2%] w-full max-w-[165px] bg-[#fdfdfc] p-3 pb-8 shadow-[4px_8px_16px_rgba(0,0,0,0.12),_inset_0_0_1px_rgba(0,0,0,0.1)] transform rotate-[4deg] origin-bottom-left flex flex-col z-20 focus-lift-target pointer-events-auto">
                                                 <div class="absolute -top-2 left-1/2 -translate-x-1/2 w-8 h-3 bg-white/40 border border-white/20 shadow-[0_1px_2px_rgba(0,0,0,0.05)] backdrop-blur-[1px] rotate-[-2deg] opacity-70 z-30" style="mix-blend-mode: multiply;"></div>
                                                 <!-- Polaroid Image -->
                                                 <div class="w-full aspect-[4/3.2] bg-[#05080f] flex items-center justify-center overflow-hidden relative shadow-[inset_0_2px_5px_rgba(0,0,0,0.6)] rounded-sm">
                                                     <img loading="lazy" src="https://bajkamalsingh.me/polaroidimg.PNG" alt="Polaroid Memory" class="w-full h-full object-cover object-[center_15%] transition-all duration-500" />
                                                 </div>
                                                 <!-- Description -->
                                                 <div class="mt-2.5 flex flex-col items-start gap-0.5">
                                                     <div aria-hidden="true" class="font-['Schoolbell'] text-[8px] font-bold text-black/80 uppercase">dev kumar raikwar.</div>
                                                     <div aria-hidden="true" class="font-['Schoolbell'] text-[7px] text-black/50 leading-tight">building AI systems @ MUJ.</div>
                                                 </div>
                                             </div>"""

new_polaroid_html = """                                             <!-- POLAROID EVENT_01 ARTIFACT (Linked to Line) -->
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

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    if old_polaroid_html in content:
        content = content.replace(old_polaroid_html, new_polaroid_html)
        with open(t, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Direct replaced Polaroid in {t}")
    else:
        # Direct string replacement of img src & text
        content = content.replace('src="https://bajkamalsingh.me/polaroidimg.PNG"', 'src="./images/WhatsApp Image 2026-09-03 at 02.21.51.jpeg"')
        content = content.replace('dev kumar raikwar.', 'Dev Kumar Raikwar (Myself)')
        with open(t, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fallback replaced image src & text in {t}")

print("Exact polaroid update script complete!")
