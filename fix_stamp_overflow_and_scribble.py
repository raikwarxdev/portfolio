import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

# 1. Update Evidence Stamps (Increased height h-[125px] & adjusted font leading so text NEVER spills outside box)
new_stamps_block = """<!-- METRICS SYSTEM (Clustered Evidence Stamps) -->
                                        <div id="metrics-stamps-group" class="relative md:absolute md:bottom-[5%] md:left-[8%] w-full max-w-[300px] md:max-w-none md:w-[84%] flex justify-between items-start gap-4 z-20">
                                            
                                            <!-- Red Stamp (5 LLM PROVIDERS) -->
                                            <div class="evidence-stamp-red flex-1 p-2.5 md:p-3 flex flex-col justify-between h-[126px] focus-lift-target overflow-hidden">
                                                <div>
                                                    <span class="font-['Bebas_Neue'] text-[30px] md:text-[32px] block leading-none tracking-tight mb-1">5</span>
                                                    <span aria-hidden="true" class="font-['Schoolbell'] font-bold text-[8px] leading-tight block uppercase">LLM PROVIDERS</span>
                                                </div>
                                                <span class="font-['Gloria_Hallelujah'] font-medium text-[8px] md:text-[8.5px] text-red-800/90 tracking-tight block text-right mt-0.5 leading-[1.05]">commitment issues,<br>professionally.</span>
                                            </div>

                                            <!-- Yellow Dotted Stamp (MUJ '28 B.TECH, CS (IOT)) -->
                                            <div class="evidence-stamp-yellow flex-1 p-2.5 md:p-3 flex flex-col justify-between h-[126px] focus-lift-target overflow-hidden">
                                                <div>
                                                    <span class="font-['Bebas_Neue'] text-[30px] md:text-[32px] block leading-none tracking-tight mb-1">MUJ '28</span>
                                                    <span aria-hidden="true" class="font-['Schoolbell'] font-bold text-[8px] leading-tight block uppercase">B.TECH, CS (IOT)</span>
                                                </div>
                                                <span class="font-['Gloria_Hallelujah'] font-medium text-[8px] md:text-[8.5px] text-yellow-800/90 tracking-tight block text-right mt-0.5 leading-[1.05]">IoT because plain CS<br>felt too calm.</span>
                                            </div>

                                            <!-- Blue Stamp (7.2 CGPA) -->
                                            <div class="evidence-stamp-blue flex-1 p-2.5 md:p-3 flex flex-col justify-between h-[126px] focus-lift-target overflow-hidden">
                                                <div>
                                                    <span class="font-['Bebas_Neue'] text-[30px] md:text-[32px] block leading-none tracking-tight mb-1">7.2</span>
                                                    <span aria-hidden="true" class="font-['Schoolbell'] font-bold text-[8px] leading-tight block uppercase">CGPA</span>
                                                </div>
                                                <span class="font-['Gloria_Hallelujah'] font-medium text-[8px] md:text-[8.5px] text-[var(--blue)]/90 tracking-tight block text-right mt-0.5 leading-[1.05]">gotta keep parents<br>happy.</span>
                                            </div>

                                        </div>"""

# 2. Update Scribble note to include "learned a lot here built a lot too" cleanly placed above the card
new_building_block = """<!-- CLUSTER 3: Bottom Left (Experience Typewriter + Stamp) -->
                                        <div id="experience-typewriter" class="relative md:absolute md:top-[44%] xl:top-[48%] md:right-[8%] w-[90%] max-w-[280px] bg-transparent focus-lift-target p-4 font-['Schoolbell'] text-[11px] text-[#222] leading-[1.7] z-20">
                                            <!-- Masking tape holding the block -->
                                            <div class="absolute -top-2 -left-2 w-8 h-4 bg-white/30 transform -rotate-6 shadow-sm"></div>

                                            <div aria-hidden="true" class="text-[9px] font-bold text-[var(--navy)] tracking-wider mb-2 uppercase opacity-60">// WHAT I'VE BEEN BUILDING</div>
                                            <p class="font-bold text-[12px] text-black mb-1.5">Developer & Agentic AI Architect</p>
                                            <p class="text-black/70 mb-2">Built <span class="font-bold text-[var(--navy)]">Cascade, FinTwin, Signal & GitGravity</span> — all shipped live, not just prototyped.</p>
                                            <p class="text-black/70">Also learning DSA — because agents don't ace interviews for me.</p>
                                            
                                            <!-- Red Stamp overlapping the text -->
                                            <div id="verified-stamp" aria-hidden="true" class="absolute bottom-[-15px] right-[10%] border-[2px] border-red-600 text-red-600 font-['Schoolbell'] text-[10px] font-bold uppercase tracking-widest p-1 transform rotate-[-15deg] opacity-70 mix-blend-multiply rounded-sm">
                                                VERIFIED
                                            </div>
                                            
                                            <!-- Scribble note cleanly positioned at top-right with zero overlap -->
                                            <div class="absolute top-[-14%] right-[-24%] xl:right-[-18%] font-['Gloria_Hallelujah'] font-medium text-[10px] md:text-[11px] text-[var(--blue)] tracking-tight rotate-[6deg] w-max leading-[1.15]">
                                                learned a lot<br><span class="pl-2">here</span><br>built a lot<br><span class="pl-2">too</span>
                                            </div>
                                        </div>"""

pattern_stamps = r'<!-- METRICS SYSTEM \(Clustered Evidence Stamps\) -->[\s\S]*?<!-- torn look signature sheet'
pattern_building = r'<!-- CLUSTER 3: Bottom Left \(Experience Typewriter \+ Stamp\) -->[\s\S]*?<!-- METRICS SYSTEM'

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    # Apply building card scribble update
    content = re.sub(pattern_building, new_building_block + "\n\n                                        <!-- METRICS SYSTEM", content, count=1)
    # Apply evidence stamp height & text fit update
    content = re.sub(pattern_stamps, new_stamps_block + "\n\n                                        <!-- torn look signature sheet", content, count=1)

    with open(t, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated stamps & scribble note in {t}")

print("Stamps height adjustment & scribble note update complete!")
