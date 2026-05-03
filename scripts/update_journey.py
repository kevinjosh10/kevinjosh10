import datetime
import os

START_DATE = datetime.date(2026, 3, 1) 
TOTAL_DAYS = 1000

def generate_svg(days_passed, total_days):
    percent = min(1.0, max(0.0, days_passed / total_days))
    percent_to_go = 100.0 - (percent * 100)
    percent_str = f"{percent*100:.1f}"
    
    # SVG Template with CSS animation
    svg_content = f"""<svg width="600" height="60" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#38B2AC;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#4299E1;stop-opacity:1" />
    </linearGradient>
    <style>
      .bg {{ fill: #1a202c; rx: 15px; }}
      .bar {{ fill: url(#glow); rx: 15px; animation: fillBar 1.5s ease-out forwards; }}
      .text {{ fill: #f7fafc; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 15px; font-weight: bold; dominant-baseline: middle; text-anchor: middle; }}
      @keyframes fillBar {{
        from {{ width: 0; }}
        to {{ width: {percent * 100}%; }}
      }}
    </style>
  </defs>
  <!-- Background Bar -->
  <rect class="bg" width="100%" height="30" y="15" />
  <!-- Animated Progress Bar -->
  <rect class="bar" height="30" y="15" />
  <!-- Text Overlay -->
  <text class="text" x="50%" y="32">Day {days_passed} of {total_days} — Just {percent_to_go:.1f}% to go! 🚀</text>
</svg>
"""
    return svg_content

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

if __name__ == "__main__":
    main()
