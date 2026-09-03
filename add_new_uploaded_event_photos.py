import os
import shutil
import re

new_brain_files = [
    ("/Users/devkumarraikwar/.gemini/antigravity/brain/4d2ee6b3-6590-4b2c-9024-99929f0c6f18/media__1788434943600.jpg", "visual-20.jpeg"),
    ("/Users/devkumarraikwar/.gemini/antigravity/brain/4d2ee6b3-6590-4b2c-9024-99929f0c6f18/media__1788434946986.jpg", "visual-21.jpeg"),
    ("/Users/devkumarraikwar/.gemini/antigravity/brain/4d2ee6b3-6590-4b2c-9024-99929f0c6f18/media__1788434950703.jpg", "visual-22.jpeg"),
    ("/Users/devkumarraikwar/.gemini/antigravity/brain/4d2ee6b3-6590-4b2c-9024-99929f0c6f18/media__1788434953329.jpg", "visual-23.jpeg"),
]

dest_roots = [
    "/Users/devkumarraikwar/portfolio",
    "/Users/devkumarraikwar/Desktop",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio"
]

for src_path, target_name in new_brain_files:
    if os.path.exists(src_path):
        for dest in dest_roots:
            dest_file = os.path.join(dest, target_name)
            shutil.copy2(src_path, dest_file)
            print(f"Copied {src_path} -> {dest_file}")
    else:
        print(f"Error: {src_path} not found!")

# Now append visual-20.jpeg through visual-23.jpeg to insomniacImages in index.html
targets = [
    "/Users/devkumarraikwar/portfolio/index.html",
    "/Users/devkumarraikwar/Desktop/index.html",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"
]

new_entries = ['"./visual-20.jpeg"', '"./visual-21.jpeg"', '"./visual-22.jpeg"', '"./visual-23.jpeg"']

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the current array closing bracket
    match = re.search(r'const insomniacImages = \[([\s\S]*?)\];', content)
    if match:
        arr_body = match.group(1).strip()
        # Parse array elements
        items = [x.strip() for x in arr_body.split(",") if x.strip()]
        for ne in new_entries:
            if ne not in items:
                items.append(ne)

        new_array_str = f'const insomniacImages = [{", ".join(items)}];'
        content = re.sub(r'const insomniacImages = \[[\s\S]*?\];', new_array_str, content, count=1)

        with open(t, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated insomniacImages (total {len(items)} images) in {t}")

print("New uploaded event photos addition complete!")
