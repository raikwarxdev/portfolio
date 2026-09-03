import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

# 1. 100% Real, Defensible Resume Data
new_stack_data = '''        const stackData = [
            {
                company: 'HackX 4.0', desc: "Manipal University Jaipur's Flagship Hackathon & Innovation Platform", duration: '2024 – Present', role: 'Executive Committee — Curations',
                points: [
                    'Served on the Executive Committee for the <strong class="text-current underline decoration-2 underline-offset-2">Curations department</strong> at HackX 4.0.',
                    'Curated technical problem statements, hackathon tracks, and competition judging criteria.'
                ],
                stats: [{ num: 'PRESENT', label: 'Tenure' }, { num: 'CURATIONS', label: 'Department' }, { num: 'HACKX 4.0', label: 'Event' }]
            },
            {
                company: 'IIC 3.0 (International Innovation Challenge)', desc: 'Global Entrepreneurship & Innovation Summit at Manipal University Jaipur', duration: '2024 – Present', role: 'Executive Committee — Curations',
                points: [
                    'Served on the Executive Committee handling <strong class="text-current underline decoration-2 underline-offset-2">Curations</strong> for International Innovation Challenge 3.0.',
                    'Handled pitch screening guidelines, innovation tracks, and competition structures.'
                ],
                stats: [{ num: 'PRESENT', label: 'Tenure' }, { num: 'CURATIONS', label: 'Department' }, { num: 'IIC 3.0', label: 'Summit' }]
            },
            {
                company: 'E-Cell, Manipal University Jaipur', desc: 'Campus Entrepreneurship Cell & Incubator Ecosystem at MUJ', duration: '2023 – 2024', role: 'Joint Head — Curations',
                points: [
                    'Served as <strong class="text-current underline decoration-2 underline-offset-2">Joint Head of the Curations department</strong> at E-Cell MUJ.',
                    'Curated speaker sessions, entrepreneurship workshops, and campus startup summits.'
                ],
                stats: [{ num: '2023-24', label: 'Tenure' }, { num: 'JOINT HEAD', label: 'Role' }, { num: 'CURATIONS', label: 'Department' }]
            },
            {
                company: 'IEEE Computer Society, MUJ', desc: 'Premier Technical Society Chapter at Manipal University Jaipur', duration: '2023 – 2024', role: 'Senior Coordinator — Promotions',
                points: [
                    'Served as <strong class="text-current underline decoration-2 underline-offset-2">Senior Coordinator for Promotions</strong> at IEEE Computer Society MUJ.',
                    'Managed promotional campaigns, social media announcements, and event publicity.'
                ],
                stats: [{ num: '2023-24', label: 'Tenure' }, { num: 'SR. COORD', label: 'Role' }, { num: 'PROMOTIONS', label: 'Department' }]
            }
        ];'''

# 2. Fix CSS & JS for #stack-cursor-label so it hides completely when card is open
cursor_hide_css = """
        /* Hide stack cursor label when card is expanded so it never blocks text */
        .stack-card.card-is-open #stack-cursor-label,
        .stack-card:hover .card-expand #stack-cursor-label,
        .card-expand #stack-cursor-label {
            display: none !important;
            opacity: 0 !important;
        }
"""

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if os.path.exists(t):
        with open(t, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace stackData
        pattern_stack = r'const stackData = \[[\s\S]*?\];'
        content, c1 = re.subn(pattern_stack, new_stack_data, content, count=1)

        # Hide cursor label when card is open in updateStack JS logic
        # In updateStack: add class 'card-is-open' when open, remove when closed
        js_open_fix = "if(isOpen) {\n                    el.classList.add('card-is-open');\n                    if (stackCursorLabel) stackCursorLabel.classList.remove('visible');"
        if "if(isOpen) {" in content and "el.classList.add('card-is-open');" not in content:
            content = content.replace("if(isOpen) {", js_open_fix, 1)

        with open(t, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {t}")

print("Clean defensible details & cursor label fix applied!")
