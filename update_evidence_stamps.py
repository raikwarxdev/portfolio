import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

new_stamps_block = """<!-- METRICS SYSTEM (Clustered Evidence Stamps) -->
                                        <div id="metrics-stamps-group" class="relative md:absolute md:bottom-[6%] md:left-[8%] w-full max-w-[300px] md:max-w-none md:w-[84%] flex justify-between items-start gap-4 z-20">
                                            
                                            <!-- Red Stamp (5 LLM PROVIDERS) -->
                                            <div class="evidence-stamp-red flex-1 p-3 flex flex-col justify-between h-[115px] focus-lift-target">
                                                <div>
                                                    <span class="font-['Bebas_Neue'] text-[32px] block leading-none tracking-tight mb-1">5</span>
                                                    <span aria-hidden="true" class="font-['Schoolbell'] font-bold text-[8px] leading-tight block uppercase">LLM PROVIDERS</span>
                                                </div>
                                                <span class="font-['Gloria_Hallelujah'] font-medium text-[9px] text-red-800/80 tracking-tight block text-right mt-1 leading-[1.1]">commitment issues, professionally.</span>
                                            </div>

                                            <!-- Yellow Dotted Stamp (MUJ '28 B.TECH, CS (IOT)) -->
                                            <div class="evidence-stamp-yellow flex-1 p-3 flex flex-col justify-between h-[115px] focus-lift-target">
                                                <div>
                                                    <span class="font-['Bebas_Neue'] text-[32px] block leading-none tracking-tight mb-1">MUJ '28</span>
                                                    <span aria-hidden="true" class="font-['Schoolbell'] font-bold text-[8px] leading-tight block uppercase">B.TECH, CS (IOT)</span>
                                                </div>
                                                <span class="font-['Gloria_Hallelujah'] font-medium text-[8px] text-yellow-800/80 tracking-tight block text-right mt-1 leading-[1.1]">IoT because plain CS felt too calm.</span>
                                            </div>

                                            <!-- Blue Stamp (7.2 CGPA) -->
                                            <div class="evidence-stamp-blue flex-1 p-3 flex flex-col justify-between h-[115px] focus-lift-target">
                                                <div>
                                                    <span class="font-['Bebas_Neue'] text-[32px] block leading-none tracking-tight mb-1">7.2</span>
                                                    <span aria-hidden="true" class="font-['Schoolbell'] font-bold text-[8px] leading-tight block uppercase">CGPA</span>
                                                </div>
                                                <span class="font-['Gloria_Hallelujah'] font-medium text-[9px] text-[var(--blue)]/80 tracking-tight block text-right mt-1 leading-[1.1]">gotta keep parents happy.</span>
                                            </div>

                                        </div>"""

pattern = r'<!-- METRICS SYSTEM \(Clustered Evidence Stamps\) -->[\s\S]*?<!-- torn look signature sheet'

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = re.sub(pattern, new_stamps_block + "\n\n                                        <!-- torn look signature sheet", content, count=1)
    with open(t, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated Evidence Stamps in {t}")

print("Evidence Stamps text replacements complete!")
