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

    # 1. Headline (big blue drop-shadow block)
    old_h1 = """<span class="block text-black/80">I BUILD AUTONOMOUS</span>
                                                <span class="block text-[var(--blue)] drop-shadow-sm font-black relative w-max">
                                                    MULTI-AGENT AI
                                                </span>
                                                <span class="block text-black/80">SYSTEMS & PLATFORMS</span>
                                                <span class="block text-black/95">BECAUSE I BELIEVE</span>
                                                <span class="block text-black/95">THE FUTURE OF CODE IS</span>
                                                
                                                <span class="inline-block mt-1 relative text-[var(--blue)] py-1 px-3 z-30 font-black tracking-normal">
                                                    AGENTIC
                                                    <!-- Circle drawing around Sneakers (Triggered by GSAP) -->
                                                    <svg class="absolute inset-0 w-full h-full pointer-events-none scale-y-110 scale-x-105" viewBox="0 0 100 40" preserveAspectRatio="none">
                                                        <path id="sneaker-circle-path" class="glowing-circle-path" d="M 5,20 C 5,5 95,5 95,20 C 95,35 5,35 5,20 Z" />
                                                    </svg>
                                                </span> 
                                                <span class="text-black/95">& SCALABLE.</span>"""

    new_h1 = """<span class="block text-black/80">I STARTED BUILDING</span>
                                                <span class="block text-[var(--blue)] drop-shadow-sm font-black relative w-max">
                                                    AI AGENTS
                                                </span>
                                                <span class="block text-black/80">AT 2 AM</span>
                                                <span class="block text-black/95">BECAUSE I WANTED</span>
                                                <span class="block text-black/95">SOMETHING THAT</span>
                                                <span class="block text-black/95">DOESN'T</span>
                                                
                                                <span class="inline-block mt-1 relative text-[var(--blue)] py-1 px-3 z-30 font-black tracking-normal">
                                                    HALLUCINATE.
                                                    <!-- Circle drawing around Sneakers (Triggered by GSAP) -->
                                                    <svg class="absolute inset-0 w-full h-full pointer-events-none scale-y-110 scale-x-105" viewBox="0 0 100 40" preserveAspectRatio="none">
                                                        <path id="sneaker-circle-path" class="glowing-circle-path" d="M 5,20 C 5,5 95,5 95,20 C 95,35 5,35 5,20 Z" />
                                                    </svg>
                                                </span>"""

    content = content.replace(old_h1, new_h1)

    # 2. Micro-story paragraphs
    old_micro = """<p class="mb-3">Currently pursuing B.Tech in Computer Science & IoT at Manipal University Jaipur. I specialize in building autonomous multi-agent AI systems, LangGraph state machines, and multi-tenant RAG pipelines...</p>
                                                <p>From orchestrating 3-agent research DAGs in Cascade to hardware-accelerated banking AI in FinTwin, I engineer systems that solve real complex problems.</p>"""

    new_micro = """<p class="mb-3">I didn't start with LangGraph or RAG pipelines. I started with basic web projects in first year, just trying to make things that worked end-to-end.</p>
                                                <p>Somewhere along the way I got hooked on LLMs and multi-agent systems — and kept building bigger, weirder things because I liked seeing them actually run.</p>"""

    content = content.replace(old_micro, new_micro)

    # 3. Floating annotation
    old_annot = """Started with full-stack code.<br>
                                                <span class="pl-4">Evolved into multi-agent AI orchestration.</span><br>
                                                <span class="text-[12px] md:text-[13px] pl-8">System design is key.</span>"""

    new_annot = """It started as tutorials.<br>
                                                <span class="pl-4">Then it became real projects.</span><br>
                                                <span class="text-[12px] md:text-[13px] pl-8">Agents came later.</span>"""

    content = content.replace(old_annot, new_annot)

    # 4. "CORE PHILOSOPHY" card
    old_philo = """<h4 class="font-['Inter'] font-[900] text-[17px] leading-[1.1] mb-1 tracking-tighter text-black uppercase relative z-10">SYSTEMS THAT SCALE.</h4>
                                            <p class="font-['DM_Sans'] text-[11px] text-black/70 leading-snug relative z-10">Computer Science & IoT engineer at MUJ. Driven by multi-agent AI orchestration, BYOK LLM factories, and production-grade software architectures.</p>
                                            
                                            <!-- Handwritten caption -->
                                            <div class="absolute -bottom-6 right-2 font-['Gloria_Hallelujah'] font-medium text-[13px] text-[#222]/90 tracking-tight rotate-[4deg] leading-[1.2]">
                                                code that actually delivers.
                                            </div>"""

    new_philo = """<h4 class="font-['Inter'] font-[900] text-[17px] leading-[1.1] mb-1 tracking-tighter text-black uppercase relative z-10">IF IT'S NOT LIVE, IT'S NOT DONE.</h4>
                                            <p class="font-['DM_Sans'] text-[11px] text-black/70 leading-snug relative z-10">Tutorials that dead-end at localhost don't count. If someone else can't actually use it, it's not shipped.</p>
                                            
                                            <!-- Handwritten caption -->
                                            <div class="absolute -bottom-6 right-2 font-['Gloria_Hallelujah'] font-medium text-[13px] text-[#222]/90 tracking-tight rotate-[4deg] leading-[1.2]">
                                                no localhost heroes.
                                            </div>"""

    content = content.replace(old_philo, new_philo)

    # 5. "PLACES I'VE HUSTLED AT" block
    old_hustle = """<div aria-hidden="true" class="text-[9px] font-bold text-[var(--navy)] tracking-wider mb-2 uppercase opacity-60">// CORE PROJECTS & LEADERSHIP</div>
                                            <p class="font-bold text-[12px] text-black mb-1">Developer & Agentic AI Architect</p>
                                            <p class="text-black/60 mb-2">Built <span class="border-b border-[#222]/30">Cascade</span> (Multi-Agent RAG), <span class="border-b border-[#222]/30">FinTwin</span> (Groq Llama 3.3 70B Agent), <span class="border-b border-[#222]/30">Signal</span> (n8n Workflow), & <span class="border-b border-[#222]/30">GitGravity</span> (60 FPS Physics).</p>
                                            <p class="text-black/60">Curations Lead at <span class="font-bold text-[var(--navy)]">HackX 4.0 & IIC 3.0</span>, former Joint Head at <span class="font-bold text-[var(--navy)]">E-Cell MUJ</span> & Senior Coordinator at <span class="font-bold text-[var(--navy)]">IEEE CS</span>.</p>
                                            
                                            <!-- Red Stamp overlapping the text -->
                                            <div id="verified-stamp" aria-hidden="true" class="absolute bottom-[-15px] right-[10%] border-[2px] border-red-600 text-red-600 font-['Schoolbell'] text-[10px] font-bold uppercase tracking-widest p-1 transform rotate-[-15deg] opacity-70 mix-blend-multiply rounded-sm">
                                                VERIFIED
                                            </div>
                                            
                                            <!-- Scribble note -->
                                            <div class="absolute top-[20%] right-[-25%] xl:right-[-8%] font-['Gloria_Hallelujah'] font-medium text-[13px] text-[var(--blue)] tracking-tight rotate-[10deg] w-max leading-[1.2]">
                                                learned a lot<br><span class="pl-2">here</span>
                                            </div>"""

    new_hustle = """<div aria-hidden="true" class="text-[9px] font-bold text-[var(--navy)] tracking-wider mb-2 uppercase opacity-60">// WHAT I'VE BEEN BUILDING</div>
                                            <p class="font-bold text-[12px] text-black mb-1">Executive Committee, Curations at HackX 4.0.</p>
                                            <p class="text-black/60 mb-2">Also Curations at <span class="border-b border-[#222]/30">IIC 3.0</span>. Previously <span class="border-b border-[#222]/30">E-Cell MUJ</span> & <span class="border-b border-[#222]/30">IEEE Computer Society, MUJ</span>.</p>
                                            <p class="text-black/60">Built <span class="font-bold text-[var(--navy)]">Cascade, FinTwin, Signal & GitGravity</span> — all shipped live, not just prototyped.</p>
                                            
                                            <!-- Red Stamp overlapping the text -->
                                            <div id="verified-stamp" aria-hidden="true" class="absolute bottom-[-15px] right-[10%] border-[2px] border-red-600 text-red-600 font-['Schoolbell'] text-[10px] font-bold uppercase tracking-widest p-1 transform rotate-[-15deg] opacity-70 mix-blend-multiply rounded-sm">
                                                VERIFIED
                                            </div>
                                            
                                            <!-- Scribble note -->
                                            <div class="absolute top-[20%] right-[-25%] xl:right-[-8%] font-['Gloria_Hallelujah'] font-medium text-[13px] text-[var(--blue)] tracking-tight rotate-[10deg] w-max leading-[1.2]">
                                                built a lot<br><span class="pl-2">here</span>
                                            </div>"""

    content = content.replace(old_hustle, new_hustle)

    # 6. Right page archival tag
    old_tag = """<div aria-hidden="true" class="text-[7px] font-['Schoolbell'] text-black/40 font-bold tracking-widest uppercase mb-1">IN 3 MONTHS</div>
                                                
                                                <!-- Stamped text -->
                                                <h4 class="font-['Bebas_Autumn'] font-['Bebas_Neue'] text-[46px] text-[#A62B2B] leading-none transform -rotate-[2deg] opacity-90 mix-blend-multiply mt-1" style="text-shadow: 0px 0px 1px rgba(166,43,43,0.3);">186M+</h4>
                                                
                                                <!-- Divider -->
                                                <div class="w-[85%] h-[1px] bg-black/10 my-2 border-b border-white/30 relative z-10"></div>
                                                
                                                <p aria-hidden="true" class="font-['Schoolbell'] text-[9px] uppercase tracking-[0.1em] text-black/70 font-bold leading-tight relative z-10">VIEWS DRIVEN</p>
                                            </div>
                                            
                                            <!-- Hand-drawn Arrow & Note -->
                                            <div class="absolute top-full mt-3 -left-16 font-['Gloria_Hallelujah'] font-medium text-[8px] text-[var(--blue)] tracking-tight -rotate-[5deg] opacity-90 leading-[1.5] text-left" style="letter-spacing: -0.01em;">
                                                <svg class="absolute -right-5 -top-1 w-8 h-8 opacity-90 mix-blend-multiply" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 18 C12 16 16 11 18 5 M13 7 L18 5 L19 11" stroke-linejoin="round"/></svg>
                                                crazy what happens<br>when you just make<br>weirdly creative stuff.
                                            </div>"""

    new_tag = """<div aria-hidden="true" class="text-[7px] font-['Schoolbell'] text-black/40 font-bold tracking-widest uppercase mb-1">SINCE MARCH 2025</div>
                                                
                                                <!-- Stamped text -->
                                                <h4 class="font-['Bebas_Autumn'] font-['Bebas_Neue'] text-[46px] text-[#A62B2B] leading-none transform -rotate-[2deg] opacity-90 mix-blend-multiply mt-1" style="text-shadow: 0px 0px 1px rgba(166,43,43,0.3);">93%</h4>
                                                
                                                <!-- Divider -->
                                                <div class="w-[85%] h-[1px] bg-black/10 my-2 border-b border-white/30 relative z-10"></div>
                                                
                                                <p aria-hidden="true" class="font-['Schoolbell'] text-[9px] uppercase tracking-[0.1em] text-black/70 font-bold leading-tight relative z-10">AGENT ACCURACY</p>
                                            </div>
                                            
                                            <!-- Hand-drawn Arrow & Note -->
                                            <div class="absolute top-full mt-3 -left-16 font-['Gloria_Hallelujah'] font-medium text-[8px] text-[var(--blue)] tracking-tight -rotate-[5deg] opacity-90 leading-[1.5] text-left" style="letter-spacing: -0.01em;">
                                                <svg class="absolute -right-5 -top-1 w-8 h-8 opacity-90 mix-blend-multiply" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 18 C12 16 16 11 18 5 M13 7 L18 5 L19 11" stroke-linejoin="round"/></svg>
                                                crazy what happens<br>when you give an LLM<br>too much autonomy.
                                            </div>"""

    content = content.replace(old_tag, new_tag)

    # 7. Evidence stamps
    old_stamps = """<!-- Red Stamp (93% Accuracy) -->
                                            <div class="evidence-stamp-red flex-1 p-3 flex flex-col justify-between h-[115px] focus-lift-target">
                                                <div>
                                                    <span class="font-['Bebas_Neue'] text-[32px] block leading-none tracking-tight mb-1">93%</span>
                                                    <span aria-hidden="true" class="font-['Schoolbell'] font-bold text-[8px] leading-tight block uppercase">Product-Fit Accuracy</span>
                                                </div>
                                                <span class="font-['Gloria_Hallelujah'] font-medium text-[9px] text-red-800/80 tracking-tight block text-right mt-1 leading-[1.1]">validated on FinTwin AI engine.</span>
                                            </div>

                                            <!-- Yellow Dotted Stamp (67% Speedup) -->
                                            <div class="evidence-stamp-yellow flex-1 p-3 flex flex-col justify-between h-[115px] focus-lift-target">
                                                <div>
                                                    <span class="font-['Bebas_Neue'] text-[32px] block leading-none tracking-tight mb-1">67%</span>
                                                    <span aria-hidden="true" class="font-['Schoolbell'] font-bold text-[8px] leading-tight block uppercase">Speed Acceleration</span>
                                                </div>
                                                <span class="font-['Gloria_Hallelujah'] font-medium text-[8px] text-yellow-800/80 tracking-tight block text-right mt-1 leading-[1.1]">achieved in Cascade & GitGravity.</span>
                                            </div>

                                            <!-- Blue Stamp (MUJ 2028) -->
                                            <div class="evidence-stamp-blue flex-1 p-3 flex flex-col justify-between h-[115px] focus-lift-target">
                                                <div>
                                                    <span class="font-['Bebas_Neue'] text-[32px] block leading-none tracking-tight mb-1">MUJ 2028</span>
                                                    <span aria-hidden="true" class="font-['Schoolbell'] font-bold text-[8px] leading-tight block uppercase">CS & IoT Engineering</span>
                                                </div>
                                                <span class="font-['Gloria_Hallelujah'] font-medium text-[9px] text-[var(--blue)]/80 tracking-tight block text-right mt-1 leading-[1.1]">building the next gen of AI.</span>
                                            </div>"""

    new_stamps = """<!-- Red Stamp (500+ Profiles Processed) -->
                                            <div class="evidence-stamp-red flex-1 p-3 flex flex-col justify-between h-[115px] focus-lift-target">
                                                <div>
                                                    <span class="font-['Bebas_Neue'] text-[32px] block leading-none tracking-tight mb-1">500+</span>
                                                    <span aria-hidden="true" class="font-['Schoolbell'] font-bold text-[8px] leading-tight block uppercase">Profiles Processed</span>
                                                </div>
                                                <span class="font-['Gloria_Hallelujah'] font-medium text-[9px] text-red-800/80 tracking-tight block text-right mt-1 leading-[1.1]">real-time, end to end (FinTwin).</span>
                                            </div>

                                            <!-- Yellow Dotted Stamp (1,296 Unique Card Combos) -->
                                            <div class="evidence-stamp-yellow flex-1 p-3 flex flex-col justify-between h-[115px] focus-lift-target">
                                                <div>
                                                    <span class="font-['Bebas_Neue'] text-[32px] block leading-none tracking-tight mb-1">1,296</span>
                                                    <span aria-hidden="true" class="font-['Schoolbell'] font-bold text-[8px] leading-tight block uppercase">Unique Card Combos</span>
                                                </div>
                                                <span class="font-['Gloria_Hallelujah'] font-medium text-[8px] text-yellow-800/80 tracking-tight block text-right mt-1 leading-[1.1]">procedural system, GitGravity.</span>
                                            </div>

                                            <!-- Blue Stamp (7.2 CGPA) -->
                                            <div class="evidence-stamp-blue flex-1 p-3 flex flex-col justify-between h-[115px] focus-lift-target">
                                                <div>
                                                    <span class="font-['Bebas_Neue'] text-[32px] block leading-none tracking-tight mb-1">7.2</span>
                                                    <span aria-hidden="true" class="font-['Schoolbell'] font-bold text-[8px] leading-tight block uppercase">CGPA</span>
                                                </div>
                                                <span class="font-['Gloria_Hallelujah'] font-medium text-[9px] text-[var(--blue)]/80 tracking-tight block text-right mt-1 leading-[1.1]">gotta keep parents happy.</span>
                                            </div>"""

    content = content.replace(old_stamps, new_stamps)

    # 8. PS footnote
    old_ps = """<p><span class="font-bold">PS//</span> The goal is simple: find artists and brands making incredible things, and help them grow using our respective arts.</p>"""
    new_ps = """<p><span class="font-bold">PS//</span> The goal is simple: agents that do the boring part so I don't have to.</p>"""
    content = content.replace(old_ps, new_ps)

    with open(t, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated exact requested Origin items in {t}")

print("All requested Origin section text replacements applied perfectly!")
