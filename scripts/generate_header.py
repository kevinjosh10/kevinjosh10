import os

svg_content = """<svg width="800" height="250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a202c;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#2d3748;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#38B2AC;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#4299E1;stop-opacity:1" />
    </linearGradient>
    <style>
      .title { fill: url(#glow); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 42px; font-weight: 800; text-anchor: middle; }
      .sub1 { fill: #f7fafc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 22px; font-weight: 600; text-anchor: middle; opacity: 0.95; }
      .sub2 { fill: #a0aec0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 16px; font-style: italic; text-anchor: middle; opacity: 0.8; }
      .border { fill: none; stroke: url(#glow); stroke-width: 2; rx: 15px; }
    </style>
  </defs>
  
  <rect width="100%" height="100%" fill="url(#bg)" rx="15px" />
  <rect width="99%" height="98%" x="4" y="2" class="border" />
  
  <text x="50%" y="90" class="title">Hello, World! I'm Kevin 👨‍💻</text>
  <text x="50%" y="145" class="sub1">I push directly to main.</text>
  <text x="50%" y="180" class="sub2">(Just kidding, I use CI/CD pipelines like a responsible adult 🛠️)</text>
</svg>
"""

os.makedirs("assets", exist_ok=True)
with open("assets/header.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
    
print("Generated custom 3-line header SVG.")
