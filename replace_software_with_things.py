import os

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

find_text = "SOFTWARE"
replace_text = "THINGS"

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    if find_text in content:
        content = content.replace(find_text, replace_text)
        with open(t, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Replaced '{find_text}' -> '{replace_text}' in {t}")
    else:
        print(f"Text '{find_text}' not found in {t}")

print("Word replacement complete!")
