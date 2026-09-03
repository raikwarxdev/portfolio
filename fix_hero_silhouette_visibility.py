import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

# Enhanced Hero Blue Backdrop Spotlight + Black Silhouette Layering (z-35 behind text z-40)
old_hero_markup = """                <!-- 1. HERO -->
                <section id="hero" class="h-screen w-full relative overflow-hidden flex flex-col justify-center items-center border-b-grid bg-[#01040a] cursor-none" style="transform-style: preserve-3d; perspective: 1200px;">
                    <div id="hero-bg-target" class="absolute inset-0 w-full h-full will-change-transform flex items-center justify-center scale-105">
                        <div id="intro-thumb-container" class="absolute inset-0 w-full h-full will-change-transform">
                            <video src="https://bajkamalsingh.me/1778536504558493.mp4" id="intro-vid" class="w-full h-full object-cover block pointer-events-none opacity-40 mix-blend-screen" style="object-position: 50% 50%;" muted loop playsinline autoplay></video>
                            <div id="intro-thumb-lighting" class="absolute inset-0 w-full h-full mix-blend-multiply pointer-events-none z-[5]" style="background: radial-gradient(circle at center, rgba(244,239,230,0) 0%, rgba(5,16,36,0.7) 100%);"></div>
                        </div>
                    </div>
                    <div id="hero-lighting" class="absolute inset-0 w-full h-full pointer-events-none opacity-0 mix-blend-multiply z-10 will-change-[background]" style="background: radial-gradient(circle 1100px at 50% 50%, rgba(244, 239, 230, 0) 0%, rgba(5, 16, 36, 0.65) 100%);"></div>
                    <!-- HERO BLACK SILHOUETTE CUTOUT -->
                    <div id="dev-hero-silhouette" class="absolute bottom-0 left-1/2 -translate-x-1/2 w-[90%] max-w-[700px] h-[90%] max-h-[800px] z-[12] pointer-events-none flex items-end justify-center">
                        <img loading="lazy" src="./images/dev_hero_cutout.png" alt="Dev Silhouette" class="w-full h-full object-contain object-bottom filter brightness-0 contrast-200 opacity-90 drop-shadow-[0_25px_60px_rgba(0,0,0,0.95)]" />
                    </div>"""

new_hero_markup = """                <!-- 1. HERO -->
                <section id="hero" class="h-screen w-full relative overflow-hidden flex flex-col justify-center items-center border-b-grid bg-[#020b24] cursor-none" style="transform-style: preserve-3d; perspective: 1200px;">
                    <!-- BLUE RADIAL SPOTLIGHT BACKDROP (Matches Reference Image) -->
                    <div class="absolute inset-0 w-full h-full pointer-events-none z-[2]" style="background: radial-gradient(circle at 50% 50%, #0F35FF 0%, #020817 75%); opacity: 0.95;"></div>

                    <div id="hero-bg-target" class="absolute inset-0 w-full h-full will-change-transform flex items-center justify-center scale-105 z-[3]">
                        <div id="intro-thumb-container" class="absolute inset-0 w-full h-full will-change-transform">
                            <video src="https://bajkamalsingh.me/1778536504558493.mp4" id="intro-vid" class="w-full h-full object-cover block pointer-events-none opacity-25 mix-blend-overlay" style="object-position: 50% 50%;" muted loop playsinline autoplay></video>
                        </div>
                    </div>
                    <div id="hero-lighting" class="absolute inset-0 w-full h-full pointer-events-none opacity-0 mix-blend-multiply z-10 will-change-[background]" style="background: radial-gradient(circle 1100px at 50% 50%, rgba(244, 239, 230, 0) 0%, rgba(5, 16, 36, 0.65) 100%);"></div>
                    
                    <!-- HERO BLACK SILHOUETTE CUTOUT OF DEV (High-Contrast Black on Blue Glow) -->
                    <div id="dev-hero-silhouette" class="absolute bottom-0 left-1/2 -translate-x-1/2 w-[85%] max-w-[620px] h-[88%] max-h-[820px] z-[15] pointer-events-none flex items-end justify-center">
                        <img loading="lazy" src="./images/dev_hero_cutout.png" alt="Dev Silhouette" class="w-full h-full object-contain object-bottom filter brightness-0 contrast-200 opacity-95 drop-shadow-[0_20px_50px_rgba(0,0,0,0.95)]" />
                    </div>"""

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern match existing hero section opening
    hero_pattern = r'<!-- 1\. HERO -->[\s\S]*?<!-- HERO BLACK SILHOUETTE CUTOUT -->[\s\S]*?</div>'
    new_content = re.sub(hero_pattern, new_hero_markup, content, count=1)

    with open(t, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated hero silhouette visibility in {t}")

print("Hero silhouette visibility fix complete!")
