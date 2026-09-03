import os
import shutil

desktop_images_dir = "/Users/devkumarraikwar/Desktop/images"

image_mappings = {
    "WhatsApp Image 2026-09-03 at 16.05.39.jpeg": "visual-01.jpeg",
    "WhatsApp Image 2026-09-03 at 16.35.17 (1).jpeg": "visual-02.jpeg",
    "WhatsApp Image 2026-09-03 at 16.35.17 copy2.jpeg": "visual-03.jpeg",
    "WhatsApp Image 2026-09-03 at 16.35.17 copy.jpeg": "visual-04.jpeg"
}

dest_roots = [
    "/Users/devkumarraikwar/portfolio",
    "/Users/devkumarraikwar/Desktop",
    "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio"
]

# Find files flexibly in case of slight spacing differences
all_files = {}
for root, dirs, files in os.walk("/Users/devkumarraikwar/Desktop"):
    for f in files:
        all_files[f.strip()] = os.path.join(root, f)

for src_name, target_name in image_mappings.items():
    found_path = None
    if src_name in all_files:
        found_path = all_files[src_name]
    else:
        # Partial match fallback
        for f, full_path in all_files.items():
            if src_name.split()[0] in f and target_name[-7:-5] in f:
                found_path = full_path
                break
    
    if found_path:
        for dest in dest_roots:
            dest_file = os.path.join(dest, target_name)
            shutil.copy2(found_path, dest_file)
            print(f"Copied {found_path} -> {dest_file}")
    else:
        print(f"Warning: Could not find {src_name} on Desktop!")

print("Image file copies complete!")
