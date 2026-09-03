import os
import shutil
import re

src_dir = "/Users/devkumarraikwar/Desktop/images"

mapping = {
    "WhatsApp Image 2026-09-03 at 16.05.39.jpeg": "visual-01.jpeg",
    "WhatsApp Image 2026-09-03 at 16.35.17 (1).jpeg": "visual-02.jpeg",
    "WhatsApp Image 2026-09-03 at 16.35.17 copy 2.jpeg": "visual-03.jpeg",
    "WhatsApp Image 2026-09-03 at 16.35.17 copy.jpeg": "visual-04.jpeg"
}

dest_roots = [
    "/Users/devkumarraikwar/portfolio",
    "/Users/devkumarraikwar/Desktop",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio"
]

for src_name, target_name in mapping.items():
    src_file = os.path.join(src_dir, src_name)
    if os.path.exists(src_file):
        for dest in dest_roots:
            dest_file = os.path.join(dest, target_name)
            shutil.copy2(src_file, dest_file)
            print(f"Copied {src_file} -> {dest_file}")
    else:
        print(f"Error: {src_file} not found!")

# Now update index.html insomniacImages array
targets = [
    "/Users/devkumarraikwar/portfolio/index.html",
    "/Users/devkumarraikwar/Desktop/index.html",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"
]

new_array_code = 'const insomniacImages = ["visual-01.jpeg", "visual-02.jpeg", "visual-03.jpeg", "visual-04.jpeg"];'

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
        print(f"Updated insomniacImages array in {t}")
    else:
        print(f"Warning: insomniacImages array pattern not found in {t}")

print("Exact visual image copies & array update complete!")
