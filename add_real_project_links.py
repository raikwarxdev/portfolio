import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

# Define the exact link blocks for each project
cascade_links = """                    <div class="mt-12 flex gap-4 flex-wrap align-center">
                        <a href="https://cascade-855w.vercel.app/" target="_blank" rel="noopener" class="brutal-tag" style="text-decoration:none; cursor: pointer;">Live Demo ↗</a>
                        <a href="https://github.com/raikwarxdev/Cascade" target="_blank" rel="noopener" class="brutal-tag" style="text-decoration:none; cursor: pointer;">GitHub ↗</a>
                    </div>"""

fintwin_links = """                    <div class="mt-12 flex gap-4 flex-wrap align-center">
                        <a href="https://fin-twin-delta.vercel.app/" target="_blank" rel="noopener" class="brutal-tag" style="text-decoration:none; cursor: pointer;">Live Demo ↗</a>
                        <a href="https://github.com/raikwarxdev/FinTwin" target="_blank" rel="noopener" class="brutal-tag" style="text-decoration:none; cursor: pointer;">GitHub ↗</a>
                    </div>"""

signal_links = """                    <div class="mt-12 flex gap-4 flex-wrap align-center">
                        <a href="#" target="_blank" rel="noopener" class="brutal-tag" style="text-decoration:none; cursor: pointer; color: #F4EFE6; border-color: rgba(255,255,255,0.2);">Live Demo ↗</a>
                        <a href="https://github.com/raikwarxdev/Signal-AI" target="_blank" rel="noopener" class="brutal-tag" style="text-decoration:none; cursor: pointer; color: #F4EFE6; border-color: rgba(255,255,255,0.2);">GitHub ↗</a>
                    </div>"""

gitgravity_links = """                    <div class="mt-12 flex gap-4 flex-wrap align-center">
                        <a href="https://git-gravity-six.vercel.app/" target="_blank" rel="noopener" class="brutal-tag" style="text-decoration:none; cursor: pointer;">Live Demo ↗</a>
                        <a href="https://github.com/raikwarxdev/GitGravity" target="_blank" rel="noopener" class="brutal-tag" style="text-decoration:none; cursor: pointer;">GitHub ↗</a>
                    </div>"""

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    # If project link blocks already exist in the file, replace them block by block
    # 1. Cascade
    if 'href="https://cascade-855w.vercel.app/"' not in content:
        # Find stats grid end in Cascade block
        cascade_target = '<div class="brutal-stat-card"><div class="brutal-stat-big">Docker</div><div class="brutal-stat-label">Vercel + Railway Live</div></div>\n                    </div>'
        if cascade_target in content:
            content = content.replace(cascade_target, cascade_target + '\n\n' + cascade_links, 1)
            print(f"Added Cascade links in {t}")

    # 2. FinTwin
    if 'href="https://fin-twin-delta.vercel.app/"' not in content:
        fintwin_target = '<div class="brutal-stat-card"><div class="brutal-stat-big">100%</div><div class="brutal-stat-label">Tool Usage Accuracy</div></div>\n                    </div>'
        if fintwin_target in content:
            content = content.replace(fintwin_target, fintwin_target + '\n\n' + fintwin_links, 1)
            print(f"Added FinTwin links in {t}")

    # 3. Signal
    if 'href="https://github.com/raikwarxdev/Signal-AI"' not in content:
        signal_target = '<div class="brutal-stat-card"><div class="brutal-stat-big" style="color: #FF2E93;">3 DRAFTS</div><div class="brutal-stat-label" style="color: #8b92a5;">Per Execution</div></div>\n                    </div>'
        if signal_target in content:
            content = content.replace(signal_target, signal_target + '\n\n' + signal_links, 1)
            print(f"Added Signal links in {t}")

    # 4. GitGravity
    if 'href="https://git-gravity-six.vercel.app/"' not in content:
        gitgravity_target = '<div class="brutal-stat-card"><div class="brutal-stat-big">GraphQL</div><div class="brutal-stat-label">Optimized Pipeline</div></div>\n                    </div>'
        if gitgravity_target in content:
            content = content.replace(gitgravity_target, gitgravity_target + '\n\n' + gitgravity_links, 1)
            print(f"Added GitGravity links in {t}")

    with open(t, "w", encoding="utf-8") as f:
        f.write(content)

print("Real project links update complete!")
