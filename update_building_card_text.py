import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

new_building_block = """<!-- CLUSTER 3: Bottom Left (Experience Typewriter + Stamp) -->
                                        <div id="experience-typewriter" class="relative md:absolute md:top-[44%] xl:top-[48%] md:right-[8%] w-[90%] max-w-[280px] bg-transparent focus-lift-target p-4 font-['Schoolbell'] text-[11px] text-[#222] leading-[1.7] z-20">
                                            <!-- Masking tape holding the block -->
                                            <div class="absolute -top-2 -left-2 w-8 h-4 bg-white/30 transform -rotate-6 shadow-sm"></div>

                                            <div aria-hidden="true" class="text-[9px] font-bold text-[var(--navy)] tracking-wider mb-2 uppercase opacity-60">// WHAT I'VE BEEN BUILDING</div>
                                            <p class="font-bold text-[12px] text-black mb-1">Executive Committee, Curations at HackX 4.0.</p>
                                            <p class="text-black/60 mb-2">Also Curations at <span class="border-b border-[#222]/30">IIC 3.0</span>. Previously <span class="border-b border-[#222]/30">E-Cell MUJ</span> & <span class="border-b border-[#222]/30">IEEE Computer Society, MUJ</span>.</p>
                                            <p class="text-black/60">Built <span class="font-bold text-[var(--navy)]">Cascade, FinTwin, Signal & GitGravity</span> — all shipped live, not just prototyped.<br>Also learning DSA — because agents don't ace interviews for me.</p>
                                            
                                            <!-- Red Stamp overlapping the text -->
                                            <div id="verified-stamp" aria-hidden="true" class="absolute bottom-[-15px] right-[10%] border-[2px] border-red-600 text-red-600 font-['Schoolbell'] text-[10px] font-bold uppercase tracking-widest p-1 transform rotate-[-15deg] opacity-70 mix-blend-multiply rounded-sm">
                                                VERIFIED
                                            </div>
                                            
                                            <!-- Scribble note -->
                                            <div class="absolute top-[20%] right-[-25%] xl:right-[-8%] font-['Gloria_Hallelujah'] font-medium text-[13px] text-[var(--blue)] tracking-tight rotate-[10deg] w-max leading-[1.2]">
                                                learned a lot<br><span class="pl-2">here</span><br>built a lot<br><span class="pl-2">too</span>
                                            </div>
                                        </div>"""

pattern = r'<!-- CLUSTER 3: Bottom Left \(Experience Typewriter \+ Stamp\) -->[\s\S]*?<!-- METRICS SYSTEM'

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(pattern, new_building_block + "\n\n                                        <!-- METRICS SYSTEM", content, count=1)
    with open(t, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated building block in {t}")

print("Building block text replacement complete!")
