import os
import re

targets = [
    "/Users/devkumarraikwar/portfolio/index.html",
    "/Users/devkumarraikwar/Desktop/index.html",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"
]

# Set exact local paths so the canvas/cursor trail gallery loads visual-01 to 04 directly from project root!
new_array_code = 'const insomniacImages = ["./visual-01.jpeg", "./visual-02.jpeg", "./visual-03.jpeg", "./visual-04.jpeg"];'

pattern = r'const insomniacImages = \[[\s\S]*?\];'

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    if re.search(pattern, content):
        content = re.sub(pattern, new_array_code, content, count=1)
        with open(t, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated insomniacImages to local paths in {t}")

print("Local image path fix complete!")
