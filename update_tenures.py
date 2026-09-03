import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

new_stack_data = '''        const stackData = [
            {
                company: 'HackX 4.0', desc: "Manipal University Jaipur's Flagship Hackathon & Innovation Platform", duration: '2026', role: 'Executive Committee — Curations',
                points: [
                    'Served on the Executive Committee for the <strong class="text-current underline decoration-2 underline-offset-2">Curations department</strong> at HackX 4.0.',
                    'Curated technical problem statements, hackathon tracks, and competition judging criteria.'
                ],
                stats: [{ num: '2026', label: 'Tenure' }, { num: 'CURATIONS', label: 'Department' }, { num: 'HACKX 4.0', label: 'Event' }]
            },
            {
                company: 'IIC 3.0 (International Innovation Challenge)', desc: 'Global Entrepreneurship & Innovation Summit at Manipal University Jaipur', duration: '2026', role: 'Executive Committee — Curations',
                points: [
                    'Served on the Executive Committee handling <strong class="text-current underline decoration-2 underline-offset-2">Curations</strong> for International Innovation Challenge 3.0.',
                    'Handled pitch screening guidelines, innovation tracks, and competition structures.'
                ],
                stats: [{ num: '2026', label: 'Tenure' }, { num: 'CURATIONS', label: 'Department' }, { num: 'IIC 3.0', label: 'Summit' }]
            },
            {
                company: 'E-Cell, Manipal University Jaipur', desc: 'Campus Entrepreneurship Cell & Incubator Ecosystem at MUJ', duration: '2025 – 2026', role: 'Joint Head — Curations',
                points: [
                    'Served as <strong class="text-current underline decoration-2 underline-offset-2">Joint Head of the Curations department</strong> at E-Cell MUJ.',
                    'Curated speaker sessions, entrepreneurship workshops, and campus startup summits.'
                ],
                stats: [{ num: '2025-26', label: 'Tenure' }, { num: 'JOINT HEAD', label: 'Role' }, { num: 'CURATIONS', label: 'Department' }]
            },
            {
                company: 'IEEE Computer Society, MUJ', desc: 'Premier Technical Society Chapter at Manipal University Jaipur', duration: '2025 – 2026', role: 'Senior Coordinator — Promotions',
                points: [
                    'Served as <strong class="text-current underline decoration-2 underline-offset-2">Senior Coordinator for Promotions</strong> at IEEE Computer Society MUJ.',
                    'Managed promotional campaigns, social media announcements, and event publicity.'
                ],
                stats: [{ num: '2025-26', label: 'Tenure' }, { num: 'SR. COORD', label: 'Role' }, { num: 'PROMOTIONS', label: 'Department' }]
            }
        ];'''

pattern = r'const stackData = \[[\s\S]*?\];'

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if os.path.exists(t):
        with open(t, "r", encoding="utf-8") as f:
            content = f.read()

        updated_content, count = re.subn(pattern, new_stack_data, content, count=1)
        if count > 0:
            with open(t, "w", encoding="utf-8") as f:
                f.write(updated_content)
            print(f"Updated stackData tenures in {t}")

print("All Experience section tenures updated successfully!")
