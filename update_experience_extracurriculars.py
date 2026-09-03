import os
import re

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

new_stack_data = '''        const stackData = [
            {
                company: 'HackX 4.0', desc: "Manipal University Jaipur's Flagship Hackathon & Innovation Platform", duration: '2024 – Present', role: 'Executive Committee — Curations',
                points: [
                    'Curated technical problem statements, judging rubrics, and track challenges for <strong class="text-current underline decoration-2 underline-offset-2">1,000+ developer participants</strong> across India.',
                    'Managed mentor onboarding, pitch deck evaluation frameworks, and industry partner alignments to ensure high-quality hackathon outputs.'
                ],
                stats: [{ num: '1K+', label: 'Participants' }, { num: '4.0', label: 'Flagship Edition' }, { num: 'Curations', label: 'Executive Committee' }]
            },
            {
                company: 'IIC 3.0 (International Innovation Challenge)', desc: 'Global Entrepreneurship & Innovation Summit fostering student startups', duration: '2024 – Present', role: 'Executive Committee — Curations',
                points: [
                    'Designed multi-stage evaluation pipelines and pitch screening criteria for <strong class="text-current underline decoration-2 underline-offset-2">international startup teams</strong> and student founders.',
                    'Coordinated guest keynotes, VC panel sessions, and seed funding pitch opportunities to drive high-impact venture creation.'
                ],
                stats: [{ num: '3.0', label: 'Global Summit' }, { num: 'Multi-Stage', label: 'Evaluation Pipeline' }, { num: 'VC & Angel', label: 'Pitching Sessions' }]
            },
            {
                company: 'E-Cell, Manipal University Jaipur', desc: 'Campus Entrepreneurship Cell & Incubator Ecosystem powering student startups', duration: '2023 – 2024', role: 'Joint Head — Curations',
                points: [
                    'Led curation for annual flagship startup summits, hackathons, and speaker sessions, scaling campus ecosystem engagement by <strong class="text-current underline decoration-2 underline-offset-2">40%+ year-over-year</strong>.',
                    'Mentored early-stage student founders on business model canvas validation, go-to-market strategies, and pitch deck storytelling.'
                ],
                stats: [{ num: '40%+', label: 'Engagement Lift' }, { num: 'Joint Head', label: 'Curations Department' }, { num: '15+', label: 'Summits & Events' }]
            },
            {
                company: 'IEEE Computer Society, MUJ', desc: 'Premier Technical Society Chapter empowering student engineers', duration: '2023 – 2024', role: 'Senior Coordinator — Promotions',
                points: [
                    'Directed multi-channel promotional campaigns and digital media strategies across workshops, coding contests, and technical seminars.',
                    'Increased overall event registrations by <strong class="text-current underline decoration-2 underline-offset-2">2.5x</strong> and expanded community reach across pan-India student developer networks.'
                ],
                stats: [{ num: '2.5x', label: 'Registration Lift' }, { num: 'Promotions', label: 'Senior Coordinator' }, { num: 'Pan-India', label: 'Tech Network' }]
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
            print(f"Updated stackData in {t}")
        else:
            print(f"Pattern stackData not found in {t}")

print("Experience section extracurriculars updated successfully!")
