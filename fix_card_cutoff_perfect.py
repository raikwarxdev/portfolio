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

    # 1. Increase pushAmount to 480 (desktop) / 540 (mobile) so expanded card text is NEVER cut off
    content = content.replace(
        "const pushAmount = window.innerWidth > 768 ? 320 : 380;",
        "const pushAmount = window.innerWidth > 768 ? 480 : 540;"
    )

    # 2. Fix mouseover listener for stackCursorLabel so it never shows when any card is open
    old_mouseover = "if (card && !stackLabelVisible) {"
    new_mouseover = "if (card && !stackLabelVisible && stackOpenIdx === -1) {"
    content = content.replace(old_mouseover, new_mouseover)

    # 3. Ensure updateStack hides stackCursorLabel when open
    old_is_open = "if(isOpen) {\n                    el.classList.add('card-is-open');\n                    if (stackCursorLabel) stackCursorLabel.classList.remove('visible');"
    new_is_open = "if(isOpen) {\n                    el.classList.add('card-is-open');\n                    stackLabelVisible = false;\n                    if (stackCursorLabel) { stackCursorLabel.classList.remove('visible'); stackCursorLabel.style.opacity = '0'; }"
    content = content.replace(old_is_open, new_is_open)

    with open(t, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated card expansion & cursor hide logic in {t}")

print("All card cutoff & cursor overlap fixes applied successfully!")
