"""Quick helper: reads header.svg and wraps it into generate_header.py"""
with open("assets/header.svg", "r", encoding="utf-8") as f:
    svg = f.read()

script = 'import os\n\nsvg_content = """' + svg + '"""\n\nos.makedirs("assets", exist_ok=True)\nwith open("assets/header.svg", "w", encoding="utf-8") as f:\n    f.write(svg_content)\n\nprint("Generated glitch storm header SVG.")\n'

with open("scripts/generate_header.py", "w", encoding="utf-8") as f:
    f.write(script)

print("Synced generate_header.py with current header.svg")
