import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

new_stickers_html = """<!-- REAL-LIFE DRAGGABLE STICKERS OVER notebook container -->
                            <!-- Sticker 1 -->
                            <div class="draggable-sticker" style="top: 15%; left: -5%; transform: rotate(-12deg);" id="sticker-1">
                                <div class="w-16 h-16 md:w-20 md:h-20 p-2 bg-white/95 border-[3px] border-white shadow-xl rounded-2xl flex items-center justify-center">
                                    <img loading="lazy" src="./images/logo_vscode.png" class="w-full h-full object-contain" alt="Logo" />
                                </div>
                            </div>

                            <!-- Sticker 2 -->
                            <div class="draggable-sticker" style="top: -6%; left: 35%; transform: rotate(15deg);" id="sticker-2">
                                <div class="w-16 h-16 md:w-20 md:h-20 p-2 bg-[#FBF7EE] border-[3px] border-white shadow-xl rounded-2xl flex items-center justify-center">
                                    <img loading="lazy" src="./images/logo_claude.png" class="w-full h-full object-contain" alt="Logo" />
                                </div>
                            </div>

                            <!-- Sticker 3 -->
                            <div class="draggable-sticker" style="bottom: 12%; left: -6%; transform: rotate(-8deg);" id="sticker-3">
                                <div class="w-16 h-16 md:w-20 md:h-20 p-2 bg-[#0F172A] border-[3px] border-white shadow-xl rounded-full flex items-center justify-center">
                                    <img loading="lazy" src="./images/logo_python.png" class="w-full h-full object-contain" alt="Logo" />
                                </div>
                            </div>

                            <!-- Sticker 4 -->
                            <div class="draggable-sticker" style="bottom: -10%; left: 45%; transform: rotate(-18deg);" id="sticker-4">
                                <div class="w-16 h-16 md:w-20 md:h-20 p-2 bg-[#1B2537] border-[3px] border-white shadow-xl rounded-2xl flex items-center justify-center">
                                    <img loading="lazy" src="./images/logo_cpp.png" class="w-full h-full object-contain" alt="Logo" />
                                </div>
                            </div>

                            <!-- Sticker 5 -->
                            <div class="draggable-sticker" style="top: 20%; left: 48%; transform: translate(-50%, 0) rotate(4deg);" id="sticker-5">
                                <div class="w-20 h-20 md:w-24 md:h-24 p-2 bg-[#000000] border-[3px] border-white shadow-2xl rounded-2xl flex items-center justify-center">
                                    <img loading="lazy" src="./images/logo_antigravity.png" class="w-full h-full object-contain" alt="Logo" />
                                </div>
                            </div>"""

html_files = [portfolio_html, desktop_html, scratch_html]

for hf in html_files:
    if os.path.exists(hf):
        with open(hf, "r", encoding="utf-8") as f:
            content = f.read()

        stickers_pattern = r'<!-- REAL-LIFE DRAGGABLE STICKERS OVER notebook container -->[\s\S]*?<!-- RIGHT PAGE BASE'
        new_block = new_stickers_html + "\n\n                            <!-- RIGHT PAGE BASE"
        content = re.sub(stickers_pattern, new_block, content, count=1)

        with open(hf, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated stickers (ONLY LOGOS, NO TEXT) in {hf}")

print("Only-logos sticker update complete!")
