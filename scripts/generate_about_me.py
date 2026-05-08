import os

def generate_about_me_svg():
    svg_content = """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Glowing text filter -->
    <filter id="glowCyan" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <style>
      /* Clean, modern, bright typography */
      .main-title {
        fill: #00f2fe;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 34px;
        font-weight: 800;
        text-anchor: middle;
        letter-spacing: 0.5px;
        opacity: 0;
        animation: fadeUp 1s ease-out forwards 0.5s;
      }
      
      .sub-title {
        fill: #a5b4fc;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 20px;
        font-weight: 600;
        text-anchor: middle;
        opacity: 0;
        animation: fadeUp 1s ease-out forwards 1.2s;
      }
      
      .tagline {
        fill: #f8fafc;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 16px;
        font-weight: 400;
        font-style: italic;
        text-anchor: middle;
        opacity: 0;
        animation: fadeUp 1s ease-out forwards 1.9s;
      }
      
      @keyframes fadeUp {
        0% { opacity: 0; transform: translateY(15px); }
        100% { opacity: 1; transform: translateY(0); }
      }
    </style>
  </defs>

  <rect width="100%" height="100%" fill="transparent" />

  <!-- Clean, Centered Presentation -->
  <g transform="translate(400, 0)">
    <text x="0" y="70" class="main-title" filter="url(#glowCyan)">Architecting Scalable Cloud Systems.</text>
    <text x="0" y="115" class="sub-title">1st-Year CS Student • AWS • Serverless • Python</text>
    <text x="0" y="155" class="tagline">On a 1000-Day Journey to master backend engineering—fueled by code and caffeine ☕</text>
  </g>
</svg>
"""

    os.makedirs("assets", exist_ok=True)
    with open("assets/about_me.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Generated Clean Animated About Me SVG.")

if __name__ == "__main__":
    generate_about_me_svg()
