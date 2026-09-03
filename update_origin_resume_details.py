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

    # 1. Left Page Headline
    old_headline = """<span class="block text-black/80">I STARTED MAKING</span>
                                                <span class="block text-[var(--blue)] drop-shadow-sm font-black relative w-max">
                                                    CREATIVE STUFF
                                                </span>
                                                <span class="block text-black/80">FOUR YEARS AGO</span>
                                                <span class="block text-black/95">BECAUSE I WANTED</span>
                                                <span class="block text-black/95">TO BUY SOME</span>
                                                
                                                <span class="inline-block mt-1 relative text-[var(--blue)] py-1 px-3 z-30 font-black tracking-normal">
                                                    SNEAKERS
                                                    <!-- Circle drawing around Sneakers (Triggered by GSAP) -->
                                                    <svg class="absolute inset-0 w-full h-full pointer-events-none scale-y-110 scale-x-105" viewBox="0 0 100 40" preserveAspectRatio="none">
                                                        <path id="sneaker-circle-path" class="glowing-circle-path" d="M 5,20 C 5,5 95,5 95,20 C 95,35 5,35 5,20 Z" />
                                                    </svg>
                                                </span> 
                                                <span class="text-black/95">ON MY OWN.</span>"""

    new_headline = """<span class="block text-black/80">I BUILD AUTONOMOUS</span>
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

    content = content.replace(old_headline, new_headline)

    # 2. Left Page Micro Story
    old_micro = """<p class="mb-3">I had no idea what a 'marketing strategy' was in 9th grade. I was just making YouTube thumbnails and taking whatever freelance gigs I could find through Insta & Discord...</p>
                                                <p>I didn't know what a "value proposition" was. I kept making things because I liked seeing them work.</p>"""

    new_micro = """<p class="mb-3">Currently pursuing B.Tech in Computer Science & IoT at Manipal University Jaipur. I specialize in building autonomous multi-agent AI systems, LangGraph state machines, and multi-tenant RAG pipelines...</p>
                                                <p>From orchestrating 3-agent research DAGs in Cascade to hardware-accelerated banking AI in FinTwin, I engineer systems that solve real complex problems.</p>"""

    content = content.replace(old_micro, new_micro)

    # 3. Floating Strategy Annotation
    old_annot = """It started as making things.<br>
                                                <span class="pl-4">Then it became a way of thinking.</span><br>
                                                <span class="text-[12px] md:text-[13px] pl-8">Strategy came later.</span>"""

    new_annot = """Started with full-stack code.<br>
                                                <span class="pl-4">Evolved into multi-agent AI orchestration.</span><br>
                                                <span class="text-[12px] md:text-[13px] pl-8">System design is key.</span>"""

    content = content.replace(old_annot, new_annot)

    # 4. Core Philosophy Card
    old_philo = """<h4 class="font-['Inter'] font-[900] text-[17px] leading-[1.1] mb-1 tracking-tighter text-black uppercase relative z-10">ART WITH A PURPOSE.</h4>
                                            <p class="font-['DM_Sans'] text-[11px] text-black/70 leading-snug relative z-10">I am an artist at heart. I obsess over aesthetics, but I love it even more when my art actually makes people feel something and take action.</p>
                                            
                                            <!-- Handwritten caption -->
                                            <div class="absolute -bottom-6 right-2 font-['Gloria_Hallelujah'] font-medium text-[13px] text-[#222]/90 tracking-tight rotate-[4deg] leading-[1.2]">
                                                beautiful design that actually works.
                                            </div>"""

    new_philo = """<h4 class="font-['Inter'] font-[900] text-[17px] leading-[1.1] mb-1 tracking-tighter text-black uppercase relative z-10">SYSTEMS THAT SCALE.</h4>
                                            <p class="font-['DM_Sans'] text-[11px] text-black/70 leading-snug relative z-10">Computer Science & IoT engineer at MUJ. Driven by multi-agent AI orchestration, BYOK LLM factories, and production-grade software architectures.</p>
                                            
                                            <!-- Handwritten caption -->
                                            <div class="absolute -bottom-6 right-2 font-['Gloria_Hallelujah'] font-medium text-[13px] text-[#222]/90 tracking-tight rotate-[4deg] leading-[1.2]">
                                                code that actually delivers.
                                            </div>"""

    content = content.replace(old_philo, new_philo)

    # 5. Places I've Hustled / Core Projects & Leadership Card
    old_hustle = """<div aria-hidden="true" class="text-[9px] font-bold text-[var(--navy)] tracking-wider mb-2 uppercase opacity-60">// PLACES I'VE HUSTLED AT</div>
                                            <p class="font-bold text-[12px] text-black mb-1">Founding Marketer at RNTL.</p>
                                            <p class="text-black/60 mb-2">Interned at <span class="border-b border-[#222]/30">Grimbyte</span>, <span class="border-b border-[#222]/30">MusicVerse</span>, <span class="border-b border-[#222]/30">Sinskari</span>, <span class="border-b border-[#222]/30">Frost & Sullivan</span> & <span class="border-b border-[#222]/30">Blue Tea</span>.</p>
                                            <p class="text-black/60">Grew an artist's community from scratch to <span class="font-bold text-[var(--navy)]">200K+ followers</span>, and pulled off a wild campus launch for a <span class="font-bold text-[var(--navy)]">Jio Hotstar show</span>.</p>"""

    new_hustle = """<div aria-hidden="true" class="text-[9px] font-bold text-[var(--navy)] tracking-wider mb-2 uppercase opacity-60">// CORE PROJECTS & LEADERSHIP</div>
                                            <p class="font-bold text-[12px] text-black mb-1">Developer & Agentic AI Architect</p>
                                            <p class="text-black/60 mb-2">Built <span class="border-b border-[#222]/30">Cascade</span> (Multi-Agent RAG), <span class="border-b border-[#222]/30">FinTwin</span> (Groq Llama 3.3 70B Agent), <span class="border-b border-[#222]/30">Signal</span> (n8n Workflow), & <span class="border-b border-[#222]/30">GitGravity</span> (60 FPS Physics).</p>
                                            <p class="text-black/60">Curations Lead at <span class="font-bold text-[var(--navy)]">HackX 4.0 & IIC 3.0</span>, former Joint Head at <span class="font-bold text-[var(--navy)]">E-Cell MUJ</span> & Senior Coordinator at <span class="font-bold text-[var(--navy)]">IEEE CS</span>.</p>"""

    content = content.replace(old_hustle, new_hustle)

    # 6. Metrics Stamps Group (₹4.4L+ / 33M+ / DU Rank 1 -> 93% / 67% / MUJ 2028)
    old_stamps = """<!-- Red Stamp (₹4.4L+) -->
                                            <div class="evidence-stamp-red flex-1 p-3 flex flex-col justify-between h-[115px] focus-lift-target">
                                                <div>
                                                    <span class="font-['Bebas_Neue'] text-[32px] block leading-none tracking-tight mb-1">33M+</span>
                                                    <span aria-hidden="true" class="font-['Schoolbell'] font-bold text-[8px] leading-tight block uppercase">Campaign Reach</span>
                                                </div>
                                                <span class="font-['Gloria_Hallelujah'] font-medium text-[9px] text-red-800/80 tracking-tight block text-right mt-1 leading-[1.1]">for flagship brand events.</span>
                                            </div>

                                            <!-- Yellow Dotted Stamp (5+) -->
                                            <div class="evidence-stamp-yellow flex-1 p-3 flex flex-col justify-between h-[115px] focus-lift-target">
                                                <div>
                                                    <span class="font-['Bebas_Neue'] text-[32px] block leading-none tracking-tight mb-1">40+</span>
                                                    <span aria-hidden="true" class="font-['Schoolbell'] font-bold text-[8px] leading-tight block uppercase">Live standup Shows</span>
                                                </div>
                                                <span class="font-['Gloria_Hallelujah'] font-medium text-[8px] text-yellow-800/80 tracking-tight block text-right mt-1 leading-[1.1]">Scaled & executed nationwide in 3 months</span>
                                            </div>

                                            <!-- Blue Stamp (DU Rank 1) -->
                                            <div class="evidence-stamp-blue flex-1 p-3 flex flex-col justify-between h-[115px] focus-lift-target">
                                                <div>
                                                    <span class="font-['Bebas_Neue'] text-[32px] block leading-none tracking-tight mb-1">DU Rank 1</span>
                                                    <span aria-hidden="true" class="font-['Schoolbell'] font-bold text-[8px] leading-tight block uppercase">5 Subjects</span>
                                                </div>
                                                <span class="font-['Gloria_Hallelujah'] font-medium text-[9px] text-[var(--blue)]/80 tracking-tight block text-right mt-1 leading-[1.1]">gotta keep parents happy.</span>
                                            </div>"""

    new_stamps = """<!-- Red Stamp (93% Accuracy) -->
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

    content = content.replace(old_stamps, new_stamps)

    # 7. Blueprint Stamp text
    content = content.replace(
        'bajkamal<br><span aria-hidden="true" class="text-[6px] opacity-80">early phase</span>',
        'dev raikwar<br><span aria-hidden="true" class="text-[6px] opacity-80">cs & iot @ muj</span>'
    )

    # 8. Polaroid Caption text
    old_polaroid_cap = """<div aria-hidden="true" class="font-['Schoolbell'] text-[8px] font-bold text-black/80 uppercase">how it all started.</div>
                                                    <div aria-hidden="true" class="font-['Schoolbell'] text-[7px] text-black/50 leading-tight">initial viral spike.</div>"""
    new_polaroid_cap = """<div aria-hidden="true" class="font-['Schoolbell'] text-[8px] font-bold text-black/80 uppercase">dev kumar raikwar.</div>
                                                    <div aria-hidden="true" class="font-['Schoolbell'] text-[7px] text-black/50 leading-tight">building AI systems @ MUJ.</div>"""
    content = content.replace(old_polaroid_cap, new_polaroid_cap)

    with open(t, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated Origin section details in {t}")

print("All Origin section text updated to Dev Kumar Raikwar's resume facts!")
