import os
import requests
import re

def fetch_views():
    url = "https://komarev.com/ghpvc/?username=kevinjosh10&style=flat"
    try:
        response = requests.get(url, timeout=5)
        # Find all numbers inside text elements
        matches = re.findall(r'<text[^>]*>([\d,]+)</text>', response.text)
        if matches:
            # Usually the last text element holds the value
            return matches[-1]
    except Exception:
        pass
    return "0"

def generate_svg(views):
    svg_content = f"""<svg width="350" height="100" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <filter id="neonGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <style>
      .label {{ font-family: 'Courier New', monospace; font-size: 14px; fill: #64748b; text-anchor: middle; letter-spacing: 3px; }}
      .count {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 42px; font-weight: 900; fill: #39ff14; text-anchor: middle; filter: url(#neonGlow); letter-spacing: 4px; }}
      .box {{ stroke: #1e293b; stroke-width: 2; fill: #020617; rx: 6px; }}
      .scanline {{ stroke: #39ff14; stroke-width: 1; opacity: 0.1; }}
    </style>
  </defs>

  <rect class="box" x="10" y="10" width="330" height="80" />
  
  <!-- Subtle scanlines for cyberpunk feel -->
  <line class="scanline" x1="10" y1="20" x2="340" y2="20" />
  <line class="scanline" x1="10" y1="30" x2="340" y2="30" />
  <line class="scanline" x1="10" y1="40" x2="340" y2="40" />
  <line class="scanline" x1="10" y1="50" x2="340" y2="50" />
  <line class="scanline" x1="10" y1="60" x2="340" y2="60" />
  <line class="scanline" x1="10" y1="70" x2="340" y2="70" />
  <line class="scanline" x1="10" y1="80" x2="340" y2="80" />

  <text class="label" x="175" y="35">>> SYSTEM.VIEWS</text>
  <text class="count" x="175" y="75">{views}</text>
</svg>
"""
    return svg_content

def main():
    views = fetch_views()
    svg = generate_svg(views)
    os.makedirs("assets", exist_ok=True)
    with open("assets/views.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated Neon Views SVG with count: {views}")

if __name__ == "__main__":
    main()
