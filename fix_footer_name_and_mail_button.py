import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

# 1. Footer name replacement
old_footer_name = """                    <div class="flex flex-col items-start md:items-end md:text-right">
                        <span class="font-['Gloria_Hallelujah'] text-4xl md:text-[50px] text-[var(--navy)] leading-none transform -rotate-[2deg]">Bajkamal Singh</span>
                        <span class="font-['Gloria_Hallelujah'] text-4xl md:text-[50px] text-[var(--blue)] leading-none transform -rotate-[2deg] mt-1 md:mt-2">(Baaz)</span>
                    </div>"""

new_footer_name = """                    <div class="flex flex-col items-start md:items-end md:text-right">
                        <span class="font-['Gloria_Hallelujah'] text-4xl md:text-[50px] text-[var(--navy)] leading-none transform -rotate-[2deg]">Dev Kumar Raikwar</span>
                        <span class="font-['Gloria_Hallelujah'] text-4xl md:text-[50px] text-[var(--blue)] leading-none transform -rotate-[2deg] mt-1 md:mt-2">(Myself)</span>
                    </div>"""

# 2. Bulletproof Mail handler function (copies email to clipboard + opens mailto)
mail_helper_js = """
    function handleMailClick(e) {
        const email = 'dev.1806raikwar21@gmail.com';
        navigator.clipboard.writeText(email).then(() => {
            const toast = document.createElement('div');
            toast.innerText = 'Copied ' + email + ' to clipboard!';
            toast.style.cssText = 'position:fixed;bottom:30px;right:30px;background:#0F35FF;color:#fff;padding:12px 24px;border-radius:8px;font-family:sans-serif;font-weight:bold;z-index:99999;box-shadow:0 10px 25px rgba(0,0,0,0.3);transition:all 0.3s;';
            document.body.appendChild(toast);
            setTimeout(() => { toast.style.opacity = '0'; setTimeout(() => toast.remove(), 300); }, 3000);
        }).catch(err => console.log(err));
        window.location.href = 'mailto:' + email;
    }
"""

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    # Update Footer Name
    if old_footer_name in content:
        content = content.replace(old_footer_name, new_footer_name)
        print(f"Updated footer name in {t}")

    # Ensure all mailto links use onclick="handleMailClick(event); return false;" or bulletproof helper
    content = content.replace(
        'href="mailto:dev.1806raikwar21@gmail.com"',
        'href="mailto:dev.1806raikwar21@gmail.com" onclick="handleMailClick(event)"'
    )

    # Insert handleMailClick JS if not already present
    if 'function handleMailClick' not in content:
        content = content.replace('</body>', f'<script>{mail_helper_js}</script>\n</body>')
        print(f"Added handleMailClick helper in {t}")

    with open(t, "w", encoding="utf-8") as f:
        f.write(content)

print("Footer name & mail button fix complete!")
