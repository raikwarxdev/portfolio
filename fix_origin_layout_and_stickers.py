import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

# 1. Headline & Micro Story Layout Fix (Zero Overlap)
old_headline_div = '<div id="origin-headline" class="absolute top-[6%] left-[4%] w-[90%] font-[\'Inter\'] font-[900] text-[2.8vw] lg:text-[38px] xl:text-[34px] text-[var(--navy)] leading-[1.08] uppercase tracking-[-0.04em] focus-lift-target z-20">'
new_headline_div = '<div id="origin-headline" class="absolute top-[4%] left-[4%] w-[90%] font-[\'Inter\'] font-[900] text-[2.1vw] lg:text-[26px] xl:text-[24px] text-[var(--navy)] leading-[1.04] uppercase tracking-[-0.04em] focus-lift-target z-20">'

old_micro_div = '<div id="origin-micro-story" aria-hidden="true" class="absolute top-[42%] xl:top-[48%] left-[4%] w-[65%] font-[\'Schoolbell\'] text-[10px] md:text-[11px] text-[#222]/85 leading-relaxed focus-lift-target z-20">'
new_micro_div = '<div id="origin-micro-story" aria-hidden="true" class="absolute top-[52%] xl:top-[54%] left-[4%] w-[72%] font-[\'Schoolbell\'] text-[10px] md:text-[11px] text-[#222]/90 leading-[1.6] focus-lift-target z-20">'

# 2. Modern AI & Dev Stickers (VS Code, Claude, Antigravity, LangGraph, Docker)
new_stickers_html = """<!-- REAL-LIFE DRAGGABLE STICKERS OVER notebook container -->
                            <!-- Sticker 1: VS CODE Sticker -->
                            <div class="draggable-sticker" style="top: 15%; left: -5%; transform: rotate(-12deg);" id="sticker-vscode">
                                <div class="sticker-matte-base w-16 h-20 flex flex-col justify-center items-center gap-1 p-2 bg-[#181824] border-[3px] border-white shadow-lg">
                                    <svg class="w-9 h-9 text-[#007ACC]" viewBox="0 0 24 24" fill="currentColor">
                                        <path d="M23.15 2.587L18.21.21a1.494 1.494 0 0 0-1.705.29l-9.46 8.63-4.12-3.128a.999.999 0 0 0-1.276.057L.327 7.261a1 1 0 0 0-.032 1.488l3.6 3.42-3.6 3.42a1 1 0 0 0 .032 1.488l1.322 1.201a.999.999 0 0 0 1.276.057l4.12-3.128 9.46 8.63a1.492 1.492 0 0 0 1.705.29l4.94-2.377A1.5 1.5 0 0 0 24 20.358V3.629a1.5 1.5 0 0 0-.85-1.042zm-5.15 15.543l-6.705-5.98 6.705-5.98v11.96z"/>
                                    </svg>
                                    <span aria-hidden="true" class="text-[8px] font-extrabold font-['DM_Mono'] text-white tracking-wider text-center leading-none mt-1 uppercase">VS CODE</span>
                                </div>
                            </div>

                            <!-- Sticker 2: CLAUDE AI Sticker -->
                            <div class="draggable-sticker" style="top: -6%; left: 35%; transform: rotate(15deg);" id="sticker-claude">
                                <div class="sticker-matte-base w-24 h-14 p-2 bg-[#D97757] border-[3px] border-white flex items-center justify-center gap-2 shadow-lg">
                                    <svg class="w-8 h-8 text-white shrink-0" viewBox="0 0 24 24" fill="currentColor">
                                        <path d="M12 2L14.5 9.5L22 12L14.5 14.5L12 22L9.5 14.5L2 12L9.5 9.5L12 2Z"/>
                                    </svg>
                                    <span class="font-['Inter'] font-[900] text-white text-xs tracking-widest uppercase">CLAUDE</span>
                                </div>
                            </div>

                            <!-- Sticker 3: LANGGRAPH Sticker -->
                            <div class="draggable-sticker" style="bottom: 12%; left: -6%; transform: rotate(-8deg);" id="sticker-langgraph">
                                <div class="sticker-diecut-round w-20 h-20 flex flex-col items-center justify-center p-2 bg-[#0F172A] border-[3px] border-white shadow-lg">
                                    <svg class="w-8 h-8 text-[#38BDF8] mb-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                        <circle cx="6" cy="6" r="3"/><circle cx="18" cy="6" r="3"/><circle cx="12" cy="18" r="3"/>
                                        <path d="M8.5 7.5L15.5 7.5M7.5 8.5L10.5 15.5M16.5 8.5L13.5 15.5"/>
                                    </svg>
                                    <span aria-hidden="true" class="text-[7px] font-['DM_Mono'] font-bold text-white tracking-wider uppercase">LANGGRAPH</span>
                                </div>
                            </div>

                            <!-- Sticker 4: DOCKER Sticker -->
                            <div class="draggable-sticker" style="bottom: -10%; left: 45%; transform: rotate(-18deg);" id="sticker-docker">
                                <div class="sticker-matte-base w-16 h-20 p-2 bg-[#0DB7ED] border-[3px] border-white flex flex-col items-center justify-between shadow-lg">
                                    <svg class="w-10 h-10 text-white mt-1" viewBox="0 0 24 24" fill="currentColor">
                                        <path d="M13.983 11.078h2.119v-1.97h-2.119v1.97zm-2.754 0h2.118v-1.97h-2.118v1.97zm-2.755 0h2.118v-1.97H8.474v1.97zm-2.754 0h2.118v-1.97H5.72v1.97zm8.263-2.61h2.119V6.498h-2.119v1.97zm-2.754 0h2.118V6.498h-2.118v1.97zm-2.755 0h2.118V6.498H8.474v1.97zm5.509-2.61h2.119V1.918h-2.119v1.94zm0 0"/>
                                    </svg>
                                    <span aria-hidden="true" class="text-[7px] font-['DM_Mono'] font-extrabold text-white tracking-widest uppercase mb-1">DOCKER</span>
                                </div>
                            </div>

                            <!-- Sticker 5: ANTIGRAVITY AI Sticker -->
                            <div class="draggable-sticker" style="top: 20%; left: 48%; transform: translate(-50%, 0) rotate(4deg);" id="sticker-antigravity">
                                <div class="w-26 h-24 p-2 bg.gradient-to-br bg-[#051024] border-[3px] border-[var(--blue)] flex flex-col items-center justify-center relative overflow-hidden z-50 shadow-xl" style="border-radius: 6px;">
                                    <svg class="w-8 h-8 text-[var(--blue)] mb-1" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                                        <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
                                    </svg>
                                    <span class="font-['Inter'] font-[900] text-xs text-white tracking-widest uppercase">ANTIGRAVITY</span>
                                    <span aria-hidden="true" class="text-[6px] text-[#4a7fff] font-mono font-bold tracking-widest uppercase mt-0.5">AGY ENGINE</span>
                                </div>
                            </div>"""

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Headline & Micro story layout divs
    if old_headline_div in content:
        content = content.replace(old_headline_div, new_headline_div)
    else:
        content = re.sub(r'<div id="origin-headline" class="[^"]+">', new_headline_div, content, count=1)

    if old_micro_div in content:
        content = content.replace(old_micro_div, new_micro_div)
    else:
        content = re.sub(r'<div id="origin-micro-story" [^>]+>', new_micro_div, content, count=1)

    # 2. Replace old stickers HTML block
    stickers_pattern = r'<!-- REAL-LIFE DRAGGABLE STICKERS OVER notebook container -->[\s\S]*?<!-- RIGHT PAGE BASE'
    new_block = new_stickers_html + "\n\n                            <!-- RIGHT PAGE BASE"
    content = re.sub(stickers_pattern, new_block, content, count=1)

    with open(t, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated layout & stickers in {t}")

print("All Origin layout fixes and VS Code, Claude, Antigravity sticker replacements applied!")
