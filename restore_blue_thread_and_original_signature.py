import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

# 1. Restore BLUE blueprint thread colors for storytelling journey
old_svg_paths = """<path id="blueprint-trace-path-glow" class="map-line-path" style="stroke: #ffffff; stroke-width: 1.5px; opacity: 0.9; mix-blend-mode: overlay;" stroke-dasharray="4000" stroke-dashoffset="4000" d="M 330,360 C 150,390 60,490 80,570 C 100,650 270,780 380,750 C 490,720 720,300 850,140 C 950,50 1150,50 1250,100 C 1320,130 1250,220 1200,320 C 1150,420 1350,550 1300,680 C 1250,750 1150,680 1075,680 C 1000,680 920,660 850,680 C 800,700 800,730 850,750 C 920,780 980,820 1050,800" />
                                <path id="blueprint-trace-path" class="map-line-path" style="stroke: #ffffff; stroke-width: 3.5px; opacity: 0.85;" stroke-dasharray="4000" stroke-dashoffset="4000" transform="translate(0.5, 0.5)" d="M 330,360 C 150,390 60,490 80,570 C 100,650 270,780 380,750 C 490,720 720,300 850,140 C 950,50 1150,50 1250,100 C 1320,130 1250,220 1200,320 C 1150,420 1350,550 1300,680 C 1250,750 1150,680 1075,680 C 1000,680 920,660 850,680 C 800,700 800,730 850,750 C 920,780 980,820 1050,800" />"""

new_svg_paths = """<path id="blueprint-trace-path-glow" class="map-line-path" style="stroke: #012CEB; stroke-width: 1.5px; opacity: 0.85; mix-blend-mode: multiply;" stroke-dasharray="4000" stroke-dashoffset="4000" d="M 330,360 C 150,390 60,490 80,570 C 100,650 270,780 380,750 C 490,720 720,300 850,140 C 950,50 1150,50 1250,100 C 1320,130 1250,220 1200,320 C 1150,420 1350,550 1300,680 C 1250,750 1150,680 1075,680 C 1000,680 920,660 850,680 C 800,700 800,730 850,750 C 920,780 980,820 1050,800" />
                                <path id="blueprint-trace-path" class="map-line-path" style="stroke: #012CEB; stroke-width: 3.5px; opacity: 0.85; mix-blend-mode: multiply;" stroke-dasharray="4000" stroke-dashoffset="4000" transform="translate(0.5, 0.5)" d="M 330,360 C 150,390 60,490 80,570 C 100,650 270,780 380,750 C 490,720 720,300 850,140 C 950,50 1150,50 1250,100 C 1320,130 1250,220 1200,320 C 1150,420 1350,550 1300,680 C 1250,750 1150,680 1075,680 C 1000,680 920,660 850,680 C 800,700 800,730 850,750 C 920,780 980,820 1050,800" />"""

# 2. Update signature element to display exact original vector path in pure white (#ffffff)
old_sig_tag = r'<path id="signature-source-path" style="display:none;" d="([^"]*)" />'
new_sig_tag = r'<path id="signature-source-path" class="opacity-0 transition-opacity duration-700" style="display:inline-block; fill:#ffffff; stroke:#ffffff; stroke-width:0.5px;" d="\1" />'

# 3. Update GSAP logic: thread is BLUE during journey, turns WHITE at closing, and reveals original signature natively with ZERO morph distortion!
old_gsap_morph_section = r'// PHASE 4: THE SIGNATURE MORPH[\s\S]*?// PHASE 5: THE EPILOGUE'

new_gsap_morph_section = """// PHASE 4: CLOSING & ORIGINAL SIGNATURE REVEAL (T = 30.5s)
            // -------------------------------------------------------------------------
            const tMorph = 30.5;
            const sigPathEl = document.getElementById('signature-source-path');

            if (tracePathEl && sigPathEl) {
                // Thread turns WHITE at closing
                aboutTl.to(tracePathEl, { 
                    stroke: "#ffffff", 
                    strokeWidth: "2.5px", 
                    opacity: 0.9,
                    duration: 1.0, 
                    ease: "power2.out" 
                }, tMorph);

                // Reveal exact, 100% unaltered original white signature natively
                aboutTl.to(sigPathEl, { 
                    opacity: 1, 
                    duration: 1.5, 
                    ease: "power2.out" 
                }, tMorph + 0.5);
            }

            // PHASE 5: THE EPILOGUE"""

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    if old_svg_paths in content:
        content = content.replace(old_svg_paths, new_svg_paths)

    content = re.sub(old_sig_tag, new_sig_tag, content, count=1)
    content = re.sub(old_gsap_morph_section, new_gsap_morph_section, content, count=1)

    with open(t, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated storytelling thread & original signature in {t}")

print("Blue thread + original signature update complete!")
