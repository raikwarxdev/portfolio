import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

# Replacement for Signal's link section + workflow diagram embed
old_signal_links_block = """                    <div class="mt-12 flex gap-4 flex-wrap align-center">
                        <a href="#" target="_blank" rel="noopener" class="brutal-tag" style="text-decoration:none; cursor: pointer; color: #F4EFE6; border-color: rgba(255,255,255,0.2);">Live Demo ↗</a>
                        <a href="https://github.com/raikwarxdev/Signal-AI" target="_blank" rel="noopener" class="brutal-tag" style="text-decoration:none; cursor: pointer; color: #F4EFE6; border-color: rgba(255,255,255,0.2);">GitHub ↗</a>
                    </div>"""

new_signal_workflow_block = """                    <div class="brutal-overline mt-12 mb-4 w-max reveal-text" style="color: #FF2E93;">Workflow Diagram</div>
                    <div class="reveal-blur" style="margin-bottom: 3rem; border: 2px solid rgba(255,255,255,0.2); overflow: hidden; border-radius: 8px;">
                        <img src="assets/signal-workflow.png" alt="Signal n8n workflow diagram" style="width: 100%; display: block;">
                    </div>

                    <div class="brutal-overline mt-4 mb-4 w-max reveal-text" style="color: #FF2E93;">Links</div>
                    <div class="mt-4 flex gap-4 flex-wrap align-center">
                        <a href="assets/signal-workflow.png" target="_blank" rel="noopener" class="brutal-tag" style="text-decoration:none; cursor: pointer; color: #F4EFE6; border-color: rgba(255,255,255,0.2);">Workflow Diagram ↗</a>
                        <a href="https://github.com/raikwarxdev/Signal-AI" target="_blank" rel="noopener" class="brutal-tag" style="text-decoration:none; cursor: pointer; color: #F4EFE6; border-color: rgba(255,255,255,0.2);">GitHub ↗</a>
                    </div>"""

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    if old_signal_links_block in content:
        content = content.replace(old_signal_links_block, new_signal_workflow_block, 1)
        with open(t, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated Signal workflow diagram and links in {t}")
    else:
        print(f"Warning: Old Signal links block not found in {t}")

print("Signal workflow diagram embed complete!")
