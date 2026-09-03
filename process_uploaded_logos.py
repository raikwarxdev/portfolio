import os
import shutil
import re

brain_dir = "/Users/devkumarraikwar/.gemini/antigravity/brain/4d2ee6b3-6590-4b2c-9024-99929f0c6f18"

targets_dir = [
    "/Users/devkumarraikwar/portfolio/images",
    "/Users/devkumarraikwar/Desktop/images",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/images"
]

for d in targets_dir:
    os.makedirs(d, exist_ok=True)

# Map the exact brain media file IDs to friendly logo names
logo_mapping = {
    "media__1788369906811.png": "logo_claude.png",
    "media__1788369955151.png": "logo_vscode.png",
    "media__1788370028212.png": "logo_antigravity.png",
    "media__1788370083001.png": "logo_cpp.png",
    "media__1788369893347.png": "logo_python.png"
}

for src_name, dest_name in logo_mapping.items():
    src_path = os.path.join(brain_dir, src_name)
    if os.path.exists(src_path):
        for d in targets_dir:
            dest_path = os.path.join(d, dest_name)
            shutil.copy2(src_path, dest_path)
            print(f"Copied {src_name} -> {dest_path}")
    else:
        print(f"Warning: {src_name} not found in brain dir")

# Now build the exact HTML for the 5 draggable stickers using the user's uploaded logo images!
new_stickers_html = """<!-- REAL-LIFE DRAGGABLE STICKERS OVER notebook container -->
                            <!-- Sticker 1: VS CODE Sticker -->
                            <div class="draggable-sticker" style="top: 15%; left: -5%; transform: rotate(-12deg);" id="sticker-vscode">
                                <div class="sticker-matte-base w-18 h-20 flex flex-col justify-center items-center gap-1 p-2 bg-[#181824] border-[3px] border-white shadow-xl rounded-xl overflow-hidden">
                                    <img loading="lazy" src="./images/logo_vscode.png" class="w-10 h-10 object-contain drop-shadow-sm" alt="VS Code" />
                                    <span aria-hidden="true" class="text-[8px] font-extrabold font-['DM_Mono'] text-white tracking-wider text-center leading-none mt-1 uppercase">VS CODE</span>
                                </div>
                            </div>

                            <!-- Sticker 2: CLAUDE AI Sticker -->
                            <div class="draggable-sticker" style="top: -6%; left: 35%; transform: rotate(15deg);" id="sticker-claude">
                                <div class="sticker-matte-base w-24 h-16 p-2 bg-[#FBF7EE] border-[3px] border-white flex items-center justify-center gap-2 shadow-xl rounded-xl overflow-hidden">
                                    <img loading="lazy" src="./images/logo_claude.png" class="w-9 h-9 object-contain drop-shadow-sm" alt="Claude AI" />
                                    <span class="font-['Inter'] font-[900] text-[#D97757] text-xs tracking-widest uppercase">CLAUDE</span>
                                </div>
                            </div>

                            <!-- Sticker 3: PYTHON Sticker -->
                            <div class="draggable-sticker" style="bottom: 12%; left: -6%; transform: rotate(-8deg);" id="sticker-python">
                                <div class="sticker-diecut-round w-20 h-20 flex flex-col items-center justify-center p-2 bg-[#0F172A] border-[3px] border-white shadow-xl rounded-full overflow-hidden">
                                    <img loading="lazy" src="./images/logo_python.png" class="w-10 h-10 object-contain drop-shadow-sm" alt="Python" />
                                    <span aria-hidden="true" class="text-[7px] font-['DM_Mono'] font-bold text-white tracking-wider uppercase mt-0.5">PYTHON</span>
                                </div>
                            </div>

                            <!-- Sticker 4: C++ Sticker -->
                            <div class="draggable-sticker" style="bottom: -10%; left: 45%; transform: rotate(-18deg);" id="sticker-cpp">
                                <div class="sticker-matte-base w-18 h-20 p-2 bg-[#1B2537] border-[3px] border-white flex flex-col items-center justify-between shadow-xl rounded-xl overflow-hidden">
                                    <img loading="lazy" src="./images/logo_cpp.png" class="w-10 h-10 object-contain drop-shadow-sm mt-1" alt="C++" />
                                    <span aria-hidden="true" class="text-[7px] font-['DM_Mono'] font-extrabold text-[#659AD2] tracking-widest uppercase mb-1">C++ LANG</span>
                                </div>
                            </div>

                            <!-- Sticker 5: ANTIGRAVITY AI Sticker -->
                            <div class="draggable-sticker" style="top: 20%; left: 48%; transform: translate(-50%, 0) rotate(4deg);" id="sticker-antigravity">
                                <div class="w-26 h-24 p-2 bg-[#000000] border-[3px] border-white flex flex-col items-center justify-center relative overflow-hidden z-50 shadow-2xl rounded-xl">
                                    <img loading="lazy" src="./images/logo_antigravity.png" class="w-10 h-10 object-contain drop-shadow-sm mb-1" alt="Antigravity AI" />
                                    <span class="font-['Inter'] font-[900] text-xs text-white tracking-widest uppercase">ANTIGRAVITY</span>
                                    <span aria-hidden="true" class="text-[6px] text-[#38BDF8] font-mono font-bold tracking-widest uppercase mt-0.5">AGY ENGINE</span>
                                </div>
                            </div>"""

html_files = [
    "/Users/devkumarraikwar/portfolio/index.html",
    "/Users/devkumarraikwar/Desktop/index.html",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"
]

for hf in html_files:
    if os.path.exists(hf):
        with open(hf, "r", encoding="utf-8") as f:
            content = f.read()

        stickers_pattern = r'<!-- REAL-LIFE DRAGGABLE STICKERS OVER notebook container -->[\s\S]*?<!-- RIGHT PAGE BASE'
        new_block = new_stickers_html + "\n\n                            <!-- RIGHT PAGE BASE"
        content = re.sub(stickers_pattern, new_block, content, count=1)

        with open(hf, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Replaced stickers in {hf}")

print("Uploaded user logo images configured successfully!")
