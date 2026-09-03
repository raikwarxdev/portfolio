import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

# 1. Update paragraph text
old_para = """                        <p class="contact-stagger font-['Schoolbell'] text-xl md:text-2xl text-white/65 max-w-md leading-relaxed mt-4">
                            Ready to make a move? Drop an email to discuss<br>
                            internships, collaborations, or just to say hi.
                        </p>"""

new_para = """                        <p class="contact-stagger font-['Schoolbell'] text-xl md:text-2xl text-white/65 max-w-md leading-relaxed mt-4">
                            Ready to make a move? Drop an email to talk projects, discuss internships, collaborations or just to say hi.
                        </p>"""

# 2. Update say hi href
old_say_hi_pattern = r'href="/cdn-cgi/l/email-protection[^"]+"'
new_say_hi = 'href="mailto:dev.1806raikwar21@gmail.com"'

# 3. Update social links row (Instagram -> GitHub -> LinkedIn -> Mail)
new_social_row = """                        <!-- Social Links -->
                        <div class="contact-stagger flex gap-8 mt-4">
                            <a href="https://www.instagram.com/raikwarxdev_18/?hl=en" target="_blank" rel="noopener noreferrer" 
                               class="focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0F35FF] relative text-white/50 font-['Schoolbell'] text-sm md:text-base uppercase tracking-widest hover:text-[var(--blue)] transition-all duration-300 hover:scale-[1.03] group">
                                INSTAGRAM
                                <span class="absolute -bottom-1 left-0 w-0 h-[1px] bg-[var(--blue)] transition-all duration-300 group-hover:w-full"></span>
                                <!-- Optional thin line extension (blueprint feel) -->
                                <span class="absolute top-1/2 -left-3 w-2 h-[1px] bg-white/20 group-hover:bg-[var(--blue)] transition-colors"></span>
                            </a>
                            <a href="https://github.com/raikwarxdev" target="_blank" rel="noopener noreferrer" 
                               class="focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0F35FF] relative text-white/50 font-['Schoolbell'] text-sm md:text-base uppercase tracking-widest hover:text-[var(--blue)] transition-all duration-300 hover:scale-[1.03] group">
                                GITHUB
                                <span class="absolute -bottom-1 left-0 w-0 h-[1px] bg-[var(--blue)] transition-all duration-300 group-hover:w-full"></span>
                                <span class="absolute top-1/2 -left-3 w-2 h-[1px] bg-white/20 group-hover:bg-[var(--blue)] transition-colors"></span>
                            </a>
                            <a href="https://www.linkedin.com/in/dev-kumar-raikwar-x7/" target="_blank" rel="noopener noreferrer" 
                               class="focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0F35FF] relative text-white/50 font-['Schoolbell'] text-sm md:text-base uppercase tracking-widest hover:text-[var(--blue)] transition-all duration-300 hover:scale-[1.03] group">
                                LINKEDIN
                                <span class="absolute -bottom-1 left-0 w-0 h-[1px] bg-[var(--blue)] transition-all duration-300 group-hover:w-full"></span>
                                <span class="absolute top-1/2 -left-3 w-2 h-[1px] bg-white/20 group-hover:bg-[var(--blue)] transition-colors"></span>
                            </a>
                            <a href="mailto:dev.1806raikwar21@gmail.com" class="focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#0F35FF] relative text-white/50 font-['Schoolbell'] text-sm md:text-base uppercase tracking-widest hover:text-[var(--blue)] transition-all duration-300 hover:scale-[1.03] group">
                                MAIL
                                <span class="absolute -bottom-1 left-0 w-0 h-[1px] bg-[var(--blue)] transition-all duration-300 group-hover:w-full"></span>
                                <span class="absolute top-1/2 -left-3 w-2 h-[1px] bg-white/20 group-hover:bg-[var(--blue)] transition-colors"></span>
                            </a>
                        </div>"""

social_row_pattern = r'<!-- Social Links -->[\s\S]*?</div>\s*</div>\s*</section>'

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    # Update paragraph
    if old_para in content:
        content = content.replace(old_para, new_para)
        print(f"Updated contact paragraph in {t}")

    # Update say hi mailto
    content = re.sub(r'<a href="/cdn-cgi/l/email-protection[^"]+"', '<a href="mailto:dev.1806raikwar21@gmail.com"', content)

    # Update social row
    if re.search(social_row_pattern, content):
        content = re.sub(r'<!-- Social Links -->[\s\S]*?(?=</section>)', new_social_row + '\n                ', content, count=1)
        print(f"Updated social links row in {t}")

    with open(t, "w", encoding="utf-8") as f:
        f.write(content)

print("Contact section updates complete!")
