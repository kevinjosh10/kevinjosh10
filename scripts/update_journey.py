import datetime
import os
import re
import urllib.request
import json
import subprocess
import xml.etree.ElementTree as ET

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
  <rect x="10" y="16" width="580" height="30" rx="15" fill="#1e293b" fill-opacity="0.3"/>

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



def fetch_contributions(username="kevinjosh10"):
    """Fetches the last 31 days of contribution data for the user."""
    # 1. Try GraphQL API (GitHub Actions provides GITHUB_TOKEN, or local gh CLI)
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        try:
            token = subprocess.check_output(["gh", "auth", "token"]).decode().strip()
        except Exception:
            token = ""

    query = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays {
                contributionCount
                date
              }
            }
          }
        }
      }
    }
    """
    if token:
        try:
            req = urllib.request.Request(
                "https://api.github.com/graphql",
                data=json.dumps({"query": query, "variables": {"login": username}}).encode(),
                headers={
                    "Authorization": f"Bearer {token}",
                    "User-Agent": "Mozilla/5.0",
                    "Content-Type": "application/json"
                }
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode())
                cal = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]
                days = [d for w in cal["weeks"] for d in w["contributionDays"]]
                if len(days) >= 31:
                    print(f"Successfully fetched {len(days)} days via GitHub GraphQL API")
                    return days[-31:], cal["totalContributions"]
        except Exception as e:
            print(f"GraphQL fetch failed: {e}")

    # 2. Fallback to public contributions API
    try:
        url = f"https://github-contributions-api.jogruber.de/v4/{username}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            contributions = data.get("contributions", [])
            today_str = datetime.date.today().isoformat()
            past = [c for c in contributions if c["date"] <= today_str]
            total = sum(data.get("total", {}).values())
            res = [{"date": c["date"], "contributionCount": c["count"]} for c in past[-31:]]
            if len(res) == 31:
                print("Successfully fetched via public contributions API")
                return res, total
    except Exception as e:
        print(f"Public API fetch failed: {e}")

    return None, 0

def get_nice_y_axis(max_val):
    if max_val <= 0:
        return 10, [0, 2, 4, 6, 8, 10]
    
    raw_step = max_val / 5.0
    magnitude = 10 ** (len(str(int(raw_step))) - 1) if raw_step >= 1 else 1
    norm = raw_step / magnitude
    if norm <= 1.2:
        step = 1 * magnitude
    elif norm <= 2.5:
        step = 2 * magnitude
    elif norm <= 6:
        step = 5 * magnitude
    else:
        step = 10 * magnitude
    
    step = max(1, int(step))
    y_max = int((max_val + step - 1) // step) * step
    if y_max == max_val:
        y_max += step
    
    ticks = list(range(0, y_max + 1, step))
    return y_max, ticks

def generate_activity_svg(days):
    width = 1200
    height = 420
    x_start = 90.0
    x_end = 1150.0
    y_top = 80.0
    y_bottom = 350.0
    chart_h = y_bottom - y_top
    chart_w = x_end - x_start

    n = len(days) # 31
    step_x = chart_w / (n - 1)

    max_count = max(d["contributionCount"] for d in days)
    y_max, ticks = get_nice_y_axis(max_count)

    # Compute points
    points = []
    for i, d in enumerate(days):
        px = x_start + i * step_x
        val = d["contributionCount"]
        py = y_bottom - (val / y_max) * chart_h
        points.append((px, py, val, d["date"]))

    # Grid lines - vertical
    grid_lines_h = []
    for px, _, _, _ in points:
        grid_lines_h.append(f'<line x1="{px:.2f}" x2="{px:.2f}" y1="{y_top}" y2="{y_bottom}" stroke="#1e293b" stroke-width="1" stroke-dasharray="4" class="ct-grid ct-horizontal"/>')

    # Grid lines - horizontal & labels
    grid_lines_v = []
    y_labels = []
    for val in ticks:
        gy = y_bottom - (val / y_max) * chart_h
        grid_lines_v.append(f'<line y1="{gy:.2f}" y2="{gy:.2f}" x1="{x_start}" x2="{x_end}" stroke="#1e293b" stroke-width="1" stroke-dasharray="4" class="ct-grid ct-vertical"/>')
        y_labels.append(f'<text y="{gy + 4.5:.2f}" x="80" fill="#94a3b8" font-family="Segoe UI, Ubuntu, -apple-system, sans-serif" font-size="13" font-weight="500" text-anchor="end" class="ct-label ct-vertical ct-start">{val}</text>')

    # Compute cubic Bezier spline
    k = 0.2
    curve_commands = [f"M{points[0][0]:.2f},{points[0][1]:.2f}"]
    for i in range(n - 1):
        p_prev = points[i - 1] if i > 0 else points[0]
        p_curr = points[i]
        p_next = points[i + 1]
        p_after = points[i + 2] if i + 2 < n else points[i + 1]

        cp1_x = p_curr[0] + k * (p_next[0] - p_prev[0])
        cp1_y = min(y_bottom, max(y_top - 10, p_curr[1] + k * (p_next[1] - p_prev[1])))

        cp2_x = p_next[0] - k * (p_after[0] - p_curr[0])
        cp2_y = min(y_bottom, max(y_top - 10, p_next[1] - k * (p_after[1] - p_curr[1])))

        curve_commands.append(f"C{cp1_x:.2f},{cp1_y:.2f} {cp2_x:.2f},{cp2_y:.2f} {p_next[0]:.2f},{p_next[1]:.2f}")

    spline_d = "".join(curve_commands)
    area_d = f"M{points[0][0]:.2f},{y_bottom} L{points[0][0]:.2f},{points[0][1]:.2f}" + "".join(curve_commands[1:]) + f" L{points[-1][0]:.2f},{y_bottom} Z"

    # Points (bouncing dots)
    point_lines = []
    for px, py, val, _ in points:
        point_lines.append(
            f'<line x1="{px:.2f}" y1="{py:.2f}" x2="{px + 0.01:.2f}" y2="{py:.2f}" stroke="#39ff14" stroke-width="8" stroke-linecap="round" filter="drop-shadow(0 0 5px #39ff14)" class="ct-point" ct:value="{val}">'
            f'<animateTransform attributeName="transform" type="translate" values="0,0; 0,-6; 0,0" dur="2s" repeatCount="indefinite" />'
            f'</line>'
        )

    # X labels
    x_labels = []
    for px, _, _, date_str in points:
        day_num = str(int(date_str.split("-")[2]))
        x_labels.append(f'<text x="{px:.2f}" y="370" fill="#94a3b8" font-family="Segoe UI, Ubuntu, -apple-system, sans-serif" font-size="13" font-weight="500" text-anchor="middle" class="ct-label ct-horizontal ct-end">{day_num}</text>')

    svg = f"""<svg width="1200" height="420" viewBox="0 0 1200 420" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:ct="http://gionkunz.github.com/chartist-js/ct">
<defs>
  <linearGradient id="fadeGradient" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.6" />
    <stop offset="100%" stop-color="#00f2fe" stop-opacity="0.0" />
  </linearGradient>
  <style>
    .header {{
      font: 600 22px 'Segoe UI', Ubuntu, Sans-Serif;
      fill: #94a3b8;
      text-anchor: middle;
    }}
    .ct-label {{
      fill: #94a3b8;
      font-family: 'Segoe UI', Ubuntu, Sans-Serif;
      font-size: 13px;
      line-height: 1;
    }}
    .ct-label.ct-horizontal.ct-end {{
      text-anchor: middle;
    }}
    .ct-label.ct-vertical.ct-start {{
      text-anchor: end;
    }}
    .ct-grid {{
      stroke: #1e293b;
      stroke-width: 1px;
      stroke-dasharray: 4;
    }}
    .ct-line {{
      fill: none;
      stroke: #00f2fe;
      stroke-width: 3.5px;
      stroke-dasharray: 5000;
      stroke-dashoffset: 5000;
      filter: drop-shadow(0 0 6px #00f2fe);
    }}
    .ct-point {{
      stroke: #39ff14;
      stroke-width: 8px;
      stroke-linecap: round;
      filter: drop-shadow(0 0 5px #39ff14);
    }}
    .ct-area {{
      fill: url(#fadeGradient);
      fill-opacity: 1;
    }}
    .ct-axis-title {{
      fill: #94a3b8;
      font-family: 'Segoe UI', Ubuntu, Sans-Serif;
      font-size: 14px;
      font-weight: 600;
    }}
  </style>
</defs>

<!-- Title -->
<text x="600" y="45" fill="#94a3b8" font-family="Segoe UI, Ubuntu, -apple-system, sans-serif" font-size="22" font-weight="600" text-anchor="middle" class="header">Contribution Activity</text>

<!-- Chart container -->
<g class="ct-grids">
  {''.join(grid_lines_h)}
  {''.join(grid_lines_v)}
</g>

<g class="ct-series ct-series-a">
  <path d="{area_d}" fill="url(#fadeGradient)" fill-opacity="1" class="ct-area" />
  <path d="{spline_d}" fill="none" stroke="#00f2fe" stroke-width="3.5" stroke-dasharray="5000" stroke-dashoffset="5000" stroke-linecap="round" stroke-linejoin="round" filter="drop-shadow(0 0 6px #00f2fe)" class="ct-line">
    <animate attributeName="stroke-dashoffset" from="5000" to="0" dur="5s" repeatCount="indefinite" />
    <animate attributeName="opacity" values="0.75;1;0.75" dur="3s" repeatCount="indefinite" />
  </path>
  {''.join(point_lines)}
</g>

<g class="ct-labels">
  {''.join(x_labels)}
  {''.join(y_labels)}
</g>

<!-- Axis titles -->
<text class="ct-axis-title ct-label" x="620" y="400" dominant-baseline="text-after-edge" text-anchor="middle">Days</text>
<text class="ct-axis-title ct-label" x="25" y="215" transform="rotate(-90, 25, 215)" dominant-baseline="hanging" text-anchor="middle">Contributions</text>

</svg>
"""
    return svg

def update_activity_graph():
    """Generates the animated activity graph from real GitHub contribution data."""
    print("Generating animated activity graph...")
    try:
        days, total = fetch_contributions("kevinjosh10")
        if days:
            svg_data = generate_activity_svg(days)
            # Validate XML
            ET.fromstring(svg_data)
            with open('assets/activity.svg', 'w', encoding='utf-8') as f:
                f.write(svg_data)
            print("Successfully generated and validated assets/activity.svg")
        else:
            print("Warning: Could not fetch contribution days; keeping existing activity.svg")
    except Exception as e:
        print(f"Failed to generate animated activity graph: {e}")

def update_streak_stats():
    """Downloads the GitHub streak stats to cache it locally."""
    import time
    print("Caching GitHub streak stats...")
    url = f'https://streak-stats.demolab.com/?user=kevinjosh10&theme=transparent&hide_border=true&ring=00f2fe&fire=39ff14&currStreakNum=39ff14&currStreakLabel=00f2fe&sideNums=e2e8f0&sideLabels=94a3b8&dates=94a3b8&_cache_buster={int(time.time())}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            with open('assets/streak.svg', 'wb') as f:
                f.write(response.read())
        print("Successfully cached assets/streak.svg")
    except Exception as e:
        print(f"Failed to cache streak stats: {e}")

def update_readme_cache_busters(days_passed):
    """Updates the cache buster query parameters in README.md so GitHub Camo reloads daily."""
    try:
        if not os.path.exists("README.md"):
            return
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()

        new_content = re.sub(
            r'src="assets/activity\.svg(\?[^"]*)?"',
            f'src="assets/activity.svg?v=day_{days_passed}"',
            content
        )
        new_content = re.sub(
            r'src="assets/streak\.svg(\?[^"]*)?"',
            f'src="assets/streak.svg?v=day_{days_passed}"',
            new_content
        )

        if new_content != content:
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(new_content)
            print("Successfully updated README.md cache busters")
    except Exception as e:
        print(f"Failed to update README cache buster: {e}")

def main():
    # Use UTC time and convert to IST (UTC +5:30)
    utc_now = datetime.datetime.now(datetime.timezone.utc)
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
    
    # Cache Streak Stats
    update_streak_stats()

    # Update README Cache Busters
    update_readme_cache_busters(days_passed)

if __name__ == "__main__":
    main()
