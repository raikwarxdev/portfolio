import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

old_morph_code = """                aboutTl.to(morphObj, {
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
                    },
                    onReverseComplete: () => {
                        // Atomically restore the original route path + dash state so the
                        // map-route shape never flashes while strokeDasharray is still "none"
                        if (originalD) tracePathEl.setAttribute('d', originalD);
                        gsap.set(tracePathEl, { strokeDasharray: pathLen, strokeDashoffset: 0 });
                    }
                }, tMorph);"""

new_morph_code = """                aboutTl.to(morphObj, {
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
                        
                        if (morphObj.progress >= 0.96) {
                            // Snap to full sharp vector signature at end of morph
                            tracePathEl.setAttribute('d', sigPathEl.getAttribute('d'));
                            gsap.set(tracePathEl, { fill: "#f6f3eb", stroke: "#f6f3eb", strokeWidth: "0.5px", opacity: 0.95 });
                        } else {
                            let d = "M ";
                            for(let i=0; i<numPoints; i++) {
                                const curX = sourcePoints[i].x + (targetPoints[i].x - sourcePoints[i].x) * morphObj.progress;
                                const curY = sourcePoints[i].y + (targetPoints[i].y - sourcePoints[i].y) * morphObj.progress;
                                d += `${curX},${curY} `;
                                if(i === 0) d += "L ";
                            }
                            tracePathEl.setAttribute('d', d);
                            gsap.set(tracePathEl, { fill: "none", stroke: "#012CEB", strokeWidth: "3.5px" });
                        }
                    },
                    onComplete: () => {
                        tracePathEl.setAttribute('d', sigPathEl.getAttribute('d'));
                        gsap.set(tracePathEl, { fill: "#f6f3eb", stroke: "#f6f3eb", strokeWidth: "0.5px", opacity: 0.95 });
                    },
                    onReverseComplete: () => {
                        if (originalD) tracePathEl.setAttribute('d', originalD);
                        gsap.set(tracePathEl, { strokeDasharray: pathLen, strokeDashoffset: 0, fill: "none", stroke: "#012CEB", strokeWidth: "3.5px", opacity: 0.2 });
                    }
                }, tMorph);"""

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    if old_morph_code in content:
        content = content.replace(old_morph_code, new_morph_code)
        with open(t, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated morph code in {t}")
    else:
        print(f"Old morph code pattern not found in {t}")

print("Signature morph clarity update complete!")
