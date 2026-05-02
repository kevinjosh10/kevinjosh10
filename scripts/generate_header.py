import os

svg_content = """<svg width="800" height="250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="200%" y2="200%">
      <stop offset="0%" stop-color="#1a202c">
        <animate attributeName="stop-color" values="#1a202c; #2b6cb0; #2c7a7b; #1a202c" dur="10s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="#2d3748">
        <animate attributeName="stop-color" values="#2d3748; #1a202c; #2b6cb0; #2d3748" dur="10s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#2c7a7b">
        <animate attributeName="stop-color" values="#2c7a7b; #2d3748; #1a202c; #2c7a7b" dur="10s" repeatCount="indefinite" />
      </stop>
    </linearGradient>
    <linearGradient id="glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#63b3ed" />
      <stop offset="100%" stop-color="#4fd1c5" />
    </linearGradient>
    <style>
      .title { fill: url(#glow); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 42px; font-weight: 800; text-anchor: middle; animation: fadeIn 1s ease-out; }
      .sub1 { fill: #f7fafc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 22px; font-weight: 600; text-anchor: middle; opacity: 0.95; animation: fadeIn 1.5s ease-out; }
      .sub2 { fill: #e2e8f0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 16px; font-style: italic; text-anchor: middle; opacity: 0.9; animation: fadeIn 2s ease-out; }
      .border { fill: none; stroke: url(#glow); stroke-width: 2; rx: 15px; }
      @keyframes fadeIn {
        from { opacity: 0; transform: translateY(5px); }
        to { opacity: 1; transform: translateY(0); }
      }
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
    
print("Generated custom 3-line header SVG with animated gradient.")
