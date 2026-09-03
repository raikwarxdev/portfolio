import os
import shutil
import re

portfolio_images = "/Users/devkumarraikwar/portfolio/images"
desktop_images = "/Users/devkumarraikwar/Desktop/images"
scratch_images = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/images"

src_image = os.path.join(portfolio_images, "WhatsApp Image 2026-09-02 at 13.53.13.jpeg")
if not os.path.exists(src_image):
    # Fallback to any jpeg in images
    jpegs = [f for f in os.listdir(portfolio_images) if f.endswith(".jpeg") or f.endswith(".jpg")]
    if jpegs:
        src_image = os.path.join(portfolio_images, jpegs[0])

if os.path.exists(src_image):
    for d in [portfolio_images, desktop_images, scratch_images]:
        if os.path.exists(d):
            shutil.copy2(src_image, os.path.join(d, "profile_polaroid.jpeg"))
            print(f"Copied {src_image} -> {os.path.join(d, 'profile_polaroid.jpeg')}")

# Update index.html polaroid img src
targets = [
    "/Users/devkumarraikwar/portfolio/index.html",
    "/Users/devkumarraikwar/Desktop/index.html",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"
]

old_img_src = 'src="https://bajkamal-style-portfolio.me/polaroidimg.PNG"'
new_img_src = 'src="./images/profile_polaroid.jpeg"'

for t in targets:
    if os.path.exists(t):
        with open(t, "r", encoding="utf-8") as f:
            content = f.read()

        if old_img_src in content:
            content = content.replace(old_img_src, new_img_src)
            with open(t, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated polaroid image src in {t}")
        else:
            # Fallback regex search for any polaroid img src
            content = re.sub(r'src="[^"]*polaroidimg[^"]*"', new_img_src, content)
            with open(t, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated polaroid image src via regex in {t}")

print("Polaroid photo setup complete!")
