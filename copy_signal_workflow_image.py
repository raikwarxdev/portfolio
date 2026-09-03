import os
import shutil
import re

desktop_dir = "/Users/devkumarraikwar/Desktop"
found_file = None

for root, dirs, files in os.walk(desktop_dir):
    for f in files:
        if "3.37.14" in f or "Screenshot 2026-09-03 at 3.37.14" in f:
            found_file = os.path.join(root, f)
            print(f"Found screenshot file: {found_file}")
            break
    if found_file:
        break

if not found_file:
    # Also check Downloads just in case
    for root, dirs, files in os.walk("/Users/devkumarraikwar/Downloads"):
        for f in files:
            if "3.37.14" in f:
                found_file = os.path.join(root, f)
                print(f"Found screenshot in Downloads: {found_file}")
                break
        if found_file:
            break

dest_dirs = [
    "/Users/devkumarraikwar/portfolio/assets",
    "/Users/devkumarraikwar/Desktop/assets",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/assets"
]

if found_file:
    for d in dest_dirs:
        os.makedirs(d, exist_ok=True)
        dest_path = os.path.join(d, "signal-workflow.png")
        shutil.copy2(found_file, dest_path)
        print(f"Copied {found_file} -> {dest_path}")

print("File copy search complete!")
