import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"

images_dir = "/Users/devkumarraikwar/portfolio/images"
image_files = sorted([f for f in os.listdir(images_dir) if f.endswith(('.jpeg', '.jpg', '.png', '.webp'))])
print(f"Found {len(image_files)} image files: {image_files}")

formatted_paths = [f'./images/{img}' for img in image_files]
array_str = "const insomniacImages = " + str(formatted_paths).replace("'", '"') + ";"

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r'const insomniacImages = \[[\s\S]*?\];'
    updated_content, count = re.subn(pattern, array_str, content, count=1)
    if count > 0:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"Updated insomniacImages in {filepath}")
    else:
        print(f"Pattern insomniacImages not found in {filepath}")

update_file(portfolio_html)
update_file(desktop_html)
