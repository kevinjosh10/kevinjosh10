import datetime
import os

START_DATE = datetime.date(2026, 3, 1) 
TOTAL_DAYS = 1000

def generate_svg(days_passed, total_days):
    percent = min(1.0, max(0.0, days_passed / total_days))
    percent_to_go = 100.0 - (percent * 100)
    bar_width_pct = percent * 100
    # Pixel width for clipping (based on 600px total, 10px padding each side)
    bar_px = bar_width_pct / 100 * 580

    svg_content = f"""<svg width="600" height="80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Base gradient for the bar -->
    <linearGradient id="waveGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0d9488"/>
      <stop offset="35%" stop-color="#06b6d4"/>
      <stop offset="70%" stop-color="#6366f1"/>
      <stop offset="100%" stop-color="#a855f7"/>
    </linearGradient>

    <!-- Shimmer gradient -->
    <linearGradient id="shimmer" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="45%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.35" />
      <stop offset="55%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>

    <!-- Glow filter -->
    <filter id="glowFilter" x="-10%" y="-50%" width="120%" height="200%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>

    <!-- Clip the bar area -->
    <clipPath id="barClip">
      <rect x="10" y="18" width="{bar_px:.1f}" height="34" rx="17"/>
    </clipPath>

    <style>
      /* Background track */
      .track {{ fill: #1e293b; }}

      /* Wave layers */
      .wave1 {{ fill: url(#waveGrad); opacity: 0.9; }}
      .wave2 {{ fill: url(#waveGrad); opacity: 0.45; }}
      .wave3 {{ fill: url(#waveGrad); opacity: 0.25; }}

      /* Wave animation — continuous horizontal scroll */
      @keyframes drift1 {{
        0%   {{ transform: translateX(0); }}
        100% {{ transform: translateX(-600px); }}
      }}
      @keyframes drift2 {{
        0%   {{ transform: translateX(0); }}
        100% {{ transform: translateX(-600px); }}
      }}
      @keyframes drift3 {{
        0%   {{ transform: translateX(0); }}
        100% {{ transform: translateX(-600px); }}
      }}

      .wave1 {{ animation: drift1 4s linear infinite; }}
      .wave2 {{ animation: drift2 5.5s linear infinite; }}
      .wave3 {{ animation: drift3 7s linear infinite; }}

      /* Shimmer sweep */
      .shimmer {{
        fill: url(#shimmer);
        animation: sweep 2.5s ease-in-out infinite;
      }}
      @keyframes sweep {{
        0%   {{ transform: translateX(-600px); }}
        100% {{ transform: translateX(600px); }}
      }}

      /* Floating bubbles */
      .b1 {{ fill: #ffffff; opacity: 0.6; animation: rise 3s ease-in infinite; }}
      .b2 {{ fill: #ffffff; opacity: 0.6; animation: rise 3.5s ease-in 0.7s infinite; }}
      .b3 {{ fill: #ffffff; opacity: 0.6; animation: rise 2.8s ease-in 1.4s infinite; }}
      .b4 {{ fill: #ffffff; opacity: 0.6; animation: rise 3.2s ease-in 2.1s infinite; }}
      .b5 {{ fill: #ffffff; opacity: 0.6; animation: rise 4s ease-in 0.3s infinite; }}

      @keyframes rise {{
        0%   {{ opacity: 0; transform: translateY(0); }}
        30%  {{ opacity: 0.7; }}
        100% {{ opacity: 0; transform: translateY(-28px); }}
      }}

      /* Pulsing outer glow on the bar edge */
      .edgeGlow {{
        fill: none;
        stroke: #6366f1;
        stroke-width: 2;
        opacity: 0.5;
        animation: pulseGlow 2s ease-in-out infinite alternate;
      }}
      @keyframes pulseGlow {{
        0%   {{ opacity: 0.25; stroke-width: 1.5; }}
        100% {{ opacity: 0.7; stroke-width: 3; }}
      }}

      /* Text */
      .label {{
        fill: #e2e8f0;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 13px;
        font-weight: 600;
        dominant-baseline: middle;
        text-anchor: middle;
      }}
      .pct {{
        fill: #f8fafc;
        font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 11px;
        font-weight: 700;
        dominant-baseline: middle;
      }}
    </style>
  </defs>

  <!-- ===== Background Track ===== -->
  <rect class="track" x="10" y="18" width="580" height="34" rx="17"/>

  <!-- ===== Clipped Wave Fill ===== -->
  <g clip-path="url(#barClip)" filter="url(#glowFilter)">
    <!-- Wave layer 1 (fastest, most opaque) -->
    <path class="wave1" d="
      M0 30 Q25 22,50 30 T100 30 T150 30 T200 30 T250 30 T300 30 T350 30 T400 30 T450 30 T500 30 T550 30 T600 30
      Q625 22,650 30 T700 30 T750 30 T800 30 T850 30 T900 30 T950 30 T1000 30 T1050 30 T1100 30 T1150 30 T1200 30
      V55 H0 Z"/>
    <!-- Wave layer 2 -->
    <path class="wave2" d="
      M0 33 Q30 26,60 33 T120 33 T180 33 T240 33 T300 33 T360 33 T420 33 T480 33 T540 33 T600 33
      Q630 26,660 33 T720 33 T780 33 T840 33 T900 33 T960 33 T1020 33 T1080 33 T1140 33 T1200 33
      V55 H0 Z"/>
    <!-- Wave layer 3 (slowest, most transparent) -->
    <path class="wave3" d="
      M0 36 Q35 28,70 36 T140 36 T210 36 T280 36 T350 36 T420 36 T490 36 T560 36 T630 36
      Q665 28,700 36 T770 36 T840 36 T910 36 T980 36 T1050 36 T1120 36 T1190 36 T1260 36
      V55 H0 Z"/>

    <!-- Shimmer overlay -->
    <rect class="shimmer" x="0" y="18" width="600" height="34"/>

    <!-- Floating bubbles -->
    <circle class="b1" cx="{bar_px * 0.2:.0f}" cy="42" r="2"/>
    <circle class="b2" cx="{bar_px * 0.4:.0f}" cy="40" r="1.5"/>
    <circle class="b3" cx="{bar_px * 0.6:.0f}" cy="44" r="2.5"/>
    <circle class="b4" cx="{bar_px * 0.8:.0f}" cy="38" r="1.8"/>
    <circle class="b5" cx="{bar_px * 0.9:.0f}" cy="43" r="2"/>
  </g>

  <!-- ===== Edge Glow Outline ===== -->
  <rect class="edgeGlow" x="10" y="18" width="{bar_px:.1f}" height="34" rx="17"/>

  <!-- ===== Percentage Badge ===== -->
  <rect x="{min(10 + bar_px - 1, 560):.0f}" y="5" width="36" height="16" rx="8" fill="#6366f1" opacity="0.85"/>
  <text class="pct" x="{min(10 + bar_px + 17, 578):.0f}" y="14" text-anchor="middle">{bar_width_pct:.1f}%</text>

  <!-- ===== Main Label ===== -->
  <text class="label" x="300" y="68">Day {days_passed} / {total_days}  •  {percent_to_go:.1f}% remaining  🚀</text>
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
