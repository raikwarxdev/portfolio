import os

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

find_text = '"If I ever write a book on how I see creativity,<br>it will have infinite pages.<br>And I\'ll still be figuring it out."'
replace_text = '"If I ever write a README for myself,<br>the \'Known Issues\' section will be the longest part.<br>And I\'ll still be figuring it out."'

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
        print(f"Updated epilogue-quote text in {t}")
    else:
        print(f"Find text not found in {t}")

print("Epilogue quote update complete!")
