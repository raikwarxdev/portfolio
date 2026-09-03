import os

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

find_text = "(Myself)"
replace_text = "(thanks for scrolling this far)"

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
        print(f"Replaced footer signature text in {t}")
    else:
        print(f"Text not found in {t}")

print("Footer signature text replacement complete!")
