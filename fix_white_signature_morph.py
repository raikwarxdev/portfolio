import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

# 1. Update SVG elements so blueprint trace path and glow are WHITE (#ffffff)
old_svg_paths = """<path id="blueprint-trace-path-glow" class="map-line-path" style="stroke: #012CEB; stroke-width: 1.5px; opacity: 0.85; mix-blend-mode: multiply;" stroke-dasharray="4000" stroke-dashoffset="4000" d="M 330,360 C 150,390 60,490 80,570 C 100,650 270,780 380,750 C 490,720 720,300 850,140 C 950,50 1150,50 1250,100 C 1320,130 1250,220 1200,320 C 1150,420 1350,550 1300,680 C 1250,750 1150,680 1075,680 C 1000,680 920,660 850,680 C 800,700 800,730 850,750 C 920,780 980,820 1050,800" />
                                <path id="blueprint-trace-path" class="map-line-path" style="stroke: #012CEB; stroke-width: 3.5px; opacity: 0.2; mix-blend-mode: multiply;" stroke-dasharray="4000" stroke-dashoffset="4000" transform="translate(0.5, 0.5)" d="M 330,360 C 150,390 60,490 80,570 C 100,650 270,780 380,750 C 490,720 720,300 850,140 C 950,50 1150,50 1250,100 C 1320,130 1250,220 1200,320 C 1150,420 1350,550 1300,680 C 1250,750 1150,680 1075,680 C 1000,680 920,660 850,680 C 800,700 800,730 850,750 C 920,780 980,820 1050,800" />"""

new_svg_paths = """<path id="blueprint-trace-path-glow" class="map-line-path" style="stroke: #ffffff; stroke-width: 1.5px; opacity: 0.9; mix-blend-mode: overlay;" stroke-dasharray="4000" stroke-dashoffset="4000" d="M 330,360 C 150,390 60,490 80,570 C 100,650 270,780 380,750 C 490,720 720,300 850,140 C 950,50 1150,50 1250,100 C 1320,130 1250,220 1200,320 C 1150,420 1350,550 1300,680 C 1250,750 1150,680 1075,680 C 1000,680 920,660 850,680 C 800,700 800,730 850,750 C 920,780 980,820 1050,800" />
                                <path id="blueprint-trace-path" class="map-line-path" style="stroke: #ffffff; stroke-width: 3.5px; opacity: 0.85;" stroke-dasharray="4000" stroke-dashoffset="4000" transform="translate(0.5, 0.5)" d="M 330,360 C 150,390 60,490 80,570 C 100,650 270,780 380,750 C 490,720 720,300 850,140 C 950,50 1150,50 1250,100 C 1320,130 1250,220 1200,320 C 1150,420 1350,550 1300,680 C 1250,750 1150,680 1075,680 C 1000,680 920,660 850,680 C 800,700 800,730 850,750 C 920,780 980,820 1050,800" />"""

# 2. Update GSAP morph code for smooth WHITE morph transition
old_morph_logic = r'aboutTl\.to\(morphObj, \{[\s\S]*?\},\s*tMorph\);'

new_morph_logic = """aboutTl.to(morphObj, {
                    progress: 1,
                    duration: 4.5,
                    ease: "power3.inOut",
                    onStart: () => {
                        if (!originalD) originalD = tracePathEl.getAttribute('d');
                        initMorphEngine();
                    },
                    onUpdate: () => {
                        if (!isEngineInit) initMorphEngine();
                        if (!isEngineInit) return;
                        
                        let d = "M ";
                        for(let i=0; i<numPoints; i++) {
                            const curX = sourcePoints[i].x + (targetPoints[i].x - sourcePoints[i].x) * morphObj.progress;
                            const curY = sourcePoints[i].y + (targetPoints[i].y - sourcePoints[i].y) * morphObj.progress;
                            d += `${curX},${curY} `;
                            if(i === 0) d += "L ";
                        }
                        tracePathEl.setAttribute('d', d);

                        // Smoothly blend fill and stroke in WHITE throughout the morph
                        const fillAlpha = Math.max(0, (morphObj.progress - 0.5) * 2);
                        gsap.set(tracePathEl, { 
                            stroke: "#ffffff", 
                            strokeWidth: `${3.5 * (1 - morphObj.progress * 0.7)}px`,
                            fill: `rgba(255, 255, 255, ${fillAlpha})`,
                            opacity: 0.9 + 0.1 * morphObj.progress
                        });
                    },
                    onComplete: () => {
                        // Display exact authentic signature vector path in pure white
                        tracePathEl.setAttribute('d', sigPathEl.getAttribute('d'));
                        gsap.set(tracePathEl, { fill: "#ffffff", stroke: "#ffffff", strokeWidth: "0.5px", opacity: 1 });
                    },
                    onReverseComplete: () => {
                        if (originalD) tracePathEl.setAttribute('d', originalD);
                        gsap.set(tracePathEl, { strokeDasharray: pathLen, strokeDashoffset: 0, fill: "none", stroke: "#ffffff", strokeWidth: "3.5px", opacity: 0.85 });
                    }
                }, tMorph);"""

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    if old_svg_paths in content:
        content = content.replace(old_svg_paths, new_svg_paths)

    content = re.sub(old_morph_logic, new_morph_logic, content, count=1)

    with open(t, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated white signature morph in {t}")

print("Pure white signature morph script execution complete!")
