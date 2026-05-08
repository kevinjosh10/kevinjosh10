import datetime
import os
import re
import urllib.request

START_DATE = datetime.date(2026, 3, 1) 
TOTAL_DAYS = 1000

def generate_svg(days_passed, total_days):
    """Generate an animated progress SVG using SMIL animations (GitHub-safe).
    
    GitHub's SVG sanitizer strips CSS <style> blocks and @keyframes.
    SMIL animations (<animate>, <animateTransform>) are preserved and
    render correctly when embedded in GitHub READMEs.
    """
    percent = min(1.0, max(0.0, days_passed / total_days))
    percent_to_go = 100.0 - (percent * 100)
    bar_width_pct = percent * 100
    # Pixel width for the filled portion (600px total, 10px padding each side)
    bar_px = max(bar_width_pct / 100 * 580, 2)
    # Badge position
    badge_x = min(10 + bar_px - 18, 550)
    badge_text_x = badge_x + 18

    svg_content = f"""<svg width="600" height="75" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <!-- Bar gradient: teal → cyan → indigo → purple -->
    <linearGradient id="g1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0d9488"/>
      <stop offset="30%" stop-color="#06b6d4"/>
      <stop offset="65%" stop-color="#6366f1"/>
      <stop offset="100%" stop-color="#a855f7"/>
    </linearGradient>
    <!-- Shimmer highlight -->
    <linearGradient id="sh" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/>
      <stop offset="0.4" stop-color="#fff" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#fff" stop-opacity="0.4"/>
      <stop offset="0.6" stop-color="#fff" stop-opacity="0"/>
      <stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <!-- Soft glow filter -->
    <filter id="gf"><feGaussianBlur stdDeviation="2.5"/></filter>
    <!-- Clip to filled area -->
    <clipPath id="cp"><rect x="10" y="16" width="{bar_px:.1f}" height="30" rx="15"/></clipPath>
  </defs>

  <!-- ========== BACKGROUND TRACK ========== -->
  <rect x="10" y="16" width="580" height="30" rx="15" fill="#1e293b"/>

  <!-- ========== GLOW LAYER (behind bar) ========== -->
  <rect x="10" y="16" width="{bar_px:.1f}" height="30" rx="15" fill="url(#g1)" filter="url(#gf)" opacity="0.5">
    <animate attributeName="opacity" values="0.35;0.6;0.35" dur="3s" repeatCount="indefinite"/>
  </rect>

  <!-- ========== WAVE FILL (clipped) ========== -->
  <g clip-path="url(#cp)">
    <!-- Wave 1 — fast drift -->
    <path fill="url(#g1)" opacity="0.9"
      d="M0,28 Q15,20 30,28 T60,28 T90,28 T120,28 T150,28 T180,28 T210,28 T240,28 T270,28 T300,28 T330,28 T360,28 T390,28 T420,28 T450,28 T480,28 T510,28 T540,28 T570,28 T600,28 T630,28 T660,28 T690,28 T720,28 T750,28 T780,28 T810,28 T840,28 T870,28 T900,28 T930,28 T960,28 T990,28 T1020,28 T1050,28 T1080,28 T1110,28 T1140,28 T1170,28 T1200,28 V50 H0 Z">
      <animateTransform attributeName="transform" type="translate" values="0,0;-600,0" dur="4s" repeatCount="indefinite"/>
    </path>
    <!-- Wave 2 — medium drift -->
    <path fill="url(#g1)" opacity="0.4"
      d="M0,32 Q20,24 40,32 T80,32 T120,32 T160,32 T200,32 T240,32 T280,32 T320,32 T360,32 T400,32 T440,32 T480,32 T520,32 T560,32 T600,32 T640,32 T680,32 T720,32 T760,32 T800,32 T840,32 T880,32 T920,32 T960,32 T1000,32 T1040,32 T1080,32 T1120,32 T1160,32 T1200,32 V50 H0 Z">
      <animateTransform attributeName="transform" type="translate" values="0,0;-600,0" dur="6s" repeatCount="indefinite"/>
    </path>
    <!-- Wave 3 — slow drift -->
    <path fill="url(#g1)" opacity="0.2"
      d="M0,35 Q25,26 50,35 T100,35 T150,35 T200,35 T250,35 T300,35 T350,35 T400,35 T450,35 T500,35 T550,35 T600,35 T650,35 T700,35 T750,35 T800,35 T850,35 T900,35 T950,35 T1000,35 T1050,35 T1100,35 T1150,35 T1200,35 V50 H0 Z">
      <animateTransform attributeName="transform" type="translate" values="0,0;-600,0" dur="8s" repeatCount="indefinite"/>
    </path>

    <!-- Shimmer sweep -->
    <rect x="-600" y="16" width="600" height="30" fill="url(#sh)">
      <animateTransform attributeName="transform" type="translate" values="0,0;1200,0" dur="3s" repeatCount="indefinite"/>
    </rect>

    <!-- Bubbles rising -->
    <circle cx="{max(bar_px*0.25,15):.0f}" cy="40" r="2" fill="#fff" opacity="0">
      <animate attributeName="cy" values="40;14" dur="2.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;0.7;0" dur="2.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="{max(bar_px*0.5,20):.0f}" cy="42" r="1.5" fill="#fff" opacity="0">
      <animate attributeName="cy" values="42;16" dur="3s" begin="0.8s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;0.6;0" dur="3s" begin="0.8s" repeatCount="indefinite"/>
    </circle>
    <circle cx="{max(bar_px*0.75,25):.0f}" cy="38" r="2.2" fill="#fff" opacity="0">
      <animate attributeName="cy" values="38;12" dur="3.5s" begin="1.6s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;0.65;0" dur="3.5s" begin="1.6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="{max(bar_px*0.9,30):.0f}" cy="41" r="1.8" fill="#fff" opacity="0">
      <animate attributeName="cy" values="41;15" dur="2.8s" begin="2.2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0;0.55;0" dur="2.8s" begin="2.2s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- ========== PULSING EDGE GLOW ========== -->
  <rect x="10" y="16" width="{bar_px:.1f}" height="30" rx="15" fill="none" stroke="#818cf8" stroke-width="1.5">
    <animate attributeName="stroke-opacity" values="0.2;0.7;0.2" dur="2s" repeatCount="indefinite"/>
    <animate attributeName="stroke-width" values="1;2.5;1" dur="2s" repeatCount="indefinite"/>
  </rect>

  <!-- ========== LABEL ========== -->
  <text x="300" y="65" fill="#94a3b8" font-family="Segoe UI,Roboto,Helvetica,Arial,sans-serif" font-size="13" font-weight="600" text-anchor="middle">Day {days_passed} / {total_days}  ·  {percent_to_go:.1f}% remaining  🚀</text>
</svg>
"""
    return svg_content



def update_activity_graph():
    """Downloads the activity graph and injects SMIL animations for GitHub rendering."""
    print("Generating animated activity graph...")
    url = 'https://github-readme-activity-graph.vercel.app/graph?username=kevinjosh10&theme=redical&hide_border=true&area=true&custom_title=Contribution%20Activity'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            svg_data = response.read().decode('utf-8')

        # Add <defs> for the moving gradient
        defs = """<defs>
          <linearGradient id="movingGradient" x1="0%" y1="0%" x2="200%" y2="0%">
            <stop offset="0%" stop-color="#fe428e" stop-opacity="0.1"/>
            <stop offset="25%" stop-color="#ff9eb5" stop-opacity="0.6"/>
            <stop offset="50%" stop-color="#fe428e" stop-opacity="0.1"/>
            <stop offset="75%" stop-color="#ff9eb5" stop-opacity="0.6"/>
            <stop offset="100%" stop-color="#fe428e" stop-opacity="0.1"/>
            <animate attributeName="x1" values="0%; -200%" dur="4s" repeatCount="indefinite" />
            <animate attributeName="x2" values="200%; 0%" dur="4s" repeatCount="indefinite" />
          </linearGradient>
        </defs>"""
        
        # Inject defs right after <svg ...>
        svg_data = re.sub(r'(<svg[^>]*>)', r'\1\n' + defs, svg_data, count=1)

        # Line animation - continuous drawing trace and pulse
        svg_data = re.sub(
            r'(<path[^>]*class="ct-line"[^>]*)></path>',
            r'\1><animate attributeName="stroke-dashoffset" from="5000" to="0" dur="5s" repeatCount="indefinite" /><animate attributeName="opacity" values="0.7;1;0.7" dur="3s" repeatCount="indefinite" /></path>',
            svg_data
        )
        
        # Area animation - moving gradient fill!
        svg_data = re.sub(
            r'(<path[^>]*class="ct-area"[^>]*)></path>',
            r'\1 style="fill: url(#movingGradient) !important;" opacity="1"></path>',
            svg_data
        )

        # Point animation - continuous bouncing and fading
        svg_data = re.sub(
            r'(<line[^>]*class="ct-point"[^>]*)></line>',
            r'\1><animateTransform attributeName="transform" type="translate" values="0,0; 0,-6; 0,0" dur="2s" repeatCount="indefinite" /></line>',
            svg_data
        )

        with open('assets/activity.svg', 'w', encoding='utf-8') as f:
            f.write(svg_data)
        print("Successfully generated assets/activity.svg")
    except Exception as e:
        print(f"Failed to generate animated activity graph: {e}")

def main():
    # Use UTC time and convert to IST (UTC +5:30)
    utc_now = datetime.datetime.utcnow()
    ist_now = utc_now + datetime.timedelta(hours=5, minutes=30)
    today = ist_now.date()
    
    days_passed = (today - START_DATE).days
    days_passed = max(0, min(days_passed, TOTAL_DAYS))
    
    svg = generate_svg(days_passed, TOTAL_DAYS)
    
    # Ensure assets directory exists
    os.makedirs("assets", exist_ok=True)
    
    with open("assets/progress.svg", "w", encoding="utf-8") as f:
        f.write(svg)
        
    print(f"Generated animated progress SVG for Day {days_passed}")
    
    # Generate Animated Activity Graph
    update_activity_graph()

if __name__ == "__main__":
    main()
