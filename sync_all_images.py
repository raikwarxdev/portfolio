import os
import shutil
import re

desktop_images = "/Users/devkumarraikwar/Desktop/images"
portfolio_images = "/Users/devkumarraikwar/portfolio/images"
scratch_images = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/images"

os.makedirs(portfolio_images, exist_ok=True)
os.makedirs(scratch_images, exist_ok=True)

# Copy all images from Desktop/images to portfolio/images and scratch_images
files = [f for f in os.listdir(desktop_images) if f.endswith(('.jpeg', '.jpg', '.png', '.webp'))]
files.sort()

print(f"Found total {len(files)} images in Desktop/images.")

for f in files:
    src = os.path.join(desktop_images, f)
    shutil.copy2(src, os.path.join(portfolio_images, f))
    shutil.copy2(src, os.path.join(scratch_images, f))

print("All images synced across directories!")

formatted_paths = [f'./images/{img}' for img in files]
array_str = "const insomniacImages = " + str(formatted_paths).replace("'", '"') + ";"

targets = [
    "/Users/devkumarraikwar/portfolio/index.html",
    "/Users/devkumarraikwar/Desktop/index.html",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"
]

for t in targets:
    if os.path.exists(t):
        with open(t, "r", encoding="utf-8") as f:
            content = f.read()

        pattern = r'const insomniacImages = \[[\s\S]*?\];'
        updated_content, count = re.subn(pattern, array_str, content, count=1)
        if count > 0:
            with open(t, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"Updated insomniacImages in {t}")

print("All 13 images updated in HTML array!")
