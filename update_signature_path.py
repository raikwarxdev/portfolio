import os
import re

txt_path = "/Users/devkumarraikwar/Downloads/dev_raikwar_signature_path.txt"

with open(txt_path, "r", encoding="utf-8") as f:
    signature_d = f.read().strip()

print(f"Loaded signature path data ({len(signature_d)} chars)")

targets = [
    "/Users/devkumarraikwar/portfolio/index.html",
    "/Users/devkumarraikwar/Desktop/index.html",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"
]

pattern = r'<path id="signature-source-path" style="display:none;" d="[^"]*" />'
replacement = f'<path id="signature-source-path" style="display:none;" d="{signature_d}" />'

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    new_content, count = re.subn(pattern, replacement, content, count=1)
    if count > 0:
        with open(t, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated signature-source-path in {t}")
    else:
        print(f"Pattern signature-source-path not found in {t}")

print("Signature path update complete!")
