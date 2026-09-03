import os

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

replacements = [
    ("Bajkamal Singh AKA Baaz", "Dev Kumar Raikwar"),
    ("SRCC '27", "MUJ '28"),
    ('baa<span style="display: inline-block; transform: translateY(-17px);">z</span>', 'De<span style="display: inline-block; transform: translateY(-17px);">v</span>'),
    ('>Designer<', '>Copy-Pasting Stack Overflow<'),
    ('>Artist Manager<', '>Actually Understanding It<'),
    ('>Creative Director<', '>Still Googling Errors<')
]

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            print(f"Replaced '{old}' -> '{new}' in {t}")
        else:
            print(f"Warning: '{old}' not found in {t}")

    with open(t, "w", encoding="utf-8") as f:
        f.write(content)

print("Hero section exact text replacements complete!")
