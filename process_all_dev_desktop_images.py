import os
import shutil
import re

desktop_images_dir = "/Users/devkumarraikwar/Desktop/images"

dest_roots = [
    "/Users/devkumarraikwar/portfolio",
    "/Users/devkumarraikwar/Desktop",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio"
]

# Find all dev WhatsApp / photo files in Desktop/images
dev_photos = []
if os.path.exists(desktop_images_dir):
    for f in sorted(os.listdir(desktop_images_dir)):
        if f.startswith("WhatsApp Image") or f.endswith(".jpeg") or f.endswith(".jpg") or f.endswith(".png"):
            # Exclude logo files and silhouette files
            if not any(k in f for k in ["logo_", "dev_hero_cutout", "dev_polaroid_photo", "removebg", "Screenshot"]):
                dev_photos.append(f)

print(f"Found {len(dev_photos)} Dev photos in Desktop/images: {dev_photos}")

# Copy them to project roots as visual-01.jpeg, visual-02.jpeg, etc.
copied_filenames = []
for idx, p_name in enumerate(dev_photos, 1):
    src_path = os.path.join(desktop_images_dir, p_name)
    target_name = f"visual-{idx:02d}.jpeg"
    copied_filenames.append(f"./{target_name}")

    for dest in dest_roots:
        dest_file = os.path.join(dest, target_name)
        shutil.copy2(src_path, dest_file)

print(f"Copied {len(copied_filenames)} dev photos to project roots: {copied_filenames}")

# Now update insomniacImages in index.html to contain ONLY dev's photos
new_array_json = str(copied_filenames).replace("'", '"')
new_array_code = f"const insomniacImages = {new_array_json};"

pattern = r'const insomniacImages = \[[\s\S]*?\];'

targets = [
    "/Users/devkumarraikwar/portfolio/index.html",
    "/Users/devkumarraikwar/Desktop/index.html",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"
]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    if re.search(pattern, content):
        content = re.sub(pattern, new_array_code, content, count=1)
        with open(t, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated insomniacImages to ONLY Dev's desktop photos in {t}")

print("All Dev Desktop photos setup complete!")
