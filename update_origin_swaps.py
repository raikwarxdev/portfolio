import os

portfolio_html = "/Users/devkumarraikwar/portfolio/index.html"
desktop_html = "/Users/devkumarraikwar/Desktop/index.html"
scratch_html = "/Users/devkumarraikwar/.gemini/antigravity/scratch/bajkamal-style-portfolio/index.html"

replacements = [
    ("AI AGENTS", "SOFTWARE"),
    ("HALLUCINATE.", "BREAK."),
    (
        "I didn't start with LangGraph or RAG pipelines. I started with basic web projects in first year, just trying to make things that worked end-to-end.",
        "I didn't start with any one stack. I started with basic web projects in first year, just trying to make things that worked end-to-end — frontend, backend, whatever it took."
    ),
    (
        "Somewhere along the way I got hooked on LLMs and multi-agent systems — and kept building bigger, weirder things because I liked seeing them actually run.",
        "Somewhere along the way I started picking up whatever a project needed — APIs, databases, deployment, AI when it made sense — and kept building bigger, weirder things because I liked seeing them actually run."
    ),
    ("Developer & Agentic AI Architect", "Full-Stack Developer")
]

targets = [portfolio_html, desktop_html, scratch_html]

for t in targets:
    if not os.path.exists(t):
        continue
    with open(t, "r", encoding="utf-8") as f:
        content = f.read()

    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            print(f"Replaced '{old[:30]}...' -> '{new[:30]}...' in {t}")
        else:
            print(f"Warning: '{old[:30]}...' not found in {t}")

    with open(t, "w", encoding="utf-8") as f:
        f.write(content)

print("Origin section text swaps complete!")
