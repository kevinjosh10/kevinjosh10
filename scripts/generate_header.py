import os
import random

def generate_header():
    # Isometric Cube Generator
    def iso_cube(x, y, size, color_top, color_left, color_right, delay):
        # x, y is the top vertex of the cube
        w = size * 0.866 # sqrt(3)/2
        h = size * 0.5
        
        top = f"M {x} {y} L {x+w} {y+h} L {x} {y+size} L {x-w} {y+h} Z"
        left = f"M {x-w} {y+h} L {x} {y+size} L {x} {y+size+size} L {x-w} {y+h+size} Z"
        right = f"M {x+w} {y+h} L {x} {y+size} L {x} {y+size+size} L {x+w} {y+h+size} Z"
        
        return f'''
        <g class="float-node" style="animation-delay: {delay}s">
            <path d="{top}" fill="{color_top}" stroke="#0f172a" stroke-width="1" />
            <path d="{left}" fill="{color_left}" stroke="#0f172a" stroke-width="1" />
            <path d="{right}" fill="{color_right}" stroke="#0f172a" stroke-width="1" />
        </g>
        '''

    # Generate a background mesh of data lines
    mesh_lines = ""
    for i in range(15):
        y = 20 + i * 15
        delay = i * 0.2
        mesh_lines += f'<line x1="0" y1="{y}" x2="800" y2="{y}" class="grid-line" style="animation-delay: {delay}s" />\n'
    for i in range(25):
        x = 20 + i * 35
        delay = i * 0.15
        mesh_lines += f'<line x1="{x}" y1="0" x2="{x}" y2="200" class="grid-line" style="animation-delay: {delay}s" />\n'

    # Generate animated data packets on the grid
    packets = ""
    for i in range(10):
        path_y = 20 + random.randint(1, 13) * 15
        dur = random.uniform(3, 6)
        delay = random.uniform(0, 4)
        packets += f'<circle cx="-10" cy="{path_y}" r="1.5" class="packet"><animate attributeName="cx" from="-10" to="810" dur="{dur}s" begin="{delay}s" repeatCount="indefinite" /></circle>\n'

    # Generate the Isometric Data Core Cluster
    # Center X: 650, Y: 50
    # Center cube (Core)
    cluster = iso_cube(650, 60, 30, "#ffb703", "#fb8500", "#e85d04", 0)
    # Surrounding smaller nodes
    cluster += iso_cube(650 - 30*0.866, 60 - 30*0.5, 15, "#8ecae6", "#219ebc", "#023047", 0.5)
    cluster += iso_cube(650 + 30*0.866, 60 + 30*0.5, 15, "#8ecae6", "#219ebc", "#023047", 1.2)
    cluster += iso_cube(650 + 35*0.866, 60 - 15*0.5, 20, "#00f2fe", "#00c6ff", "#00a8cc", 0.8)
    cluster += iso_cube(650 - 20*0.866, 60 + 40*0.5, 18, "#00f2fe", "#00c6ff", "#00a8cc", 1.5)
    
    # Connecting neon beams between the isometric nodes
    # Core (650, 60+30) to left node (650-26, 60-15+15)
    beams = '''
    <path d="M 650 90 L 624 60" class="neon-beam" />
    <path d="M 650 90 L 676 120" class="neon-beam" />
    <path d="M 650 90 L 680 75" class="neon-beam" />
    <path d="M 650 90 L 632 100" class="neon-beam" />
    '''

    svg = f'''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .bg-rect {{
        fill: #0f172a;
      }}
      .grid-line {{
        stroke: #1e293b;
        stroke-width: 1;
        opacity: 0.5;
        stroke-dasharray: 4 4;
      }}
      .packet {{
        fill: #00f2fe;
        filter: drop-shadow(0 0 3px #00f2fe);
      }}
      .float-node {{
        animation: floatNode 4s ease-in-out infinite alternate;
        filter: drop-shadow(0 0 10px rgba(251, 133, 0, 0.4));
      }}
      @keyframes floatNode {{
        0% {{ transform: translateY(0px); }}
        100% {{ transform: translateY(-8px); }}
      }}
      .neon-beam {{
        fill: none;
        stroke: #00f2fe;
        stroke-width: 1.5;
        stroke-dasharray: 5 15;
        animation: beamFlow 20s linear infinite;
        opacity: 0.6;
        filter: drop-shadow(0 0 4px #00f2fe);
      }}
      @keyframes beamFlow {{
        to {{ stroke-dashoffset: -100; }}
      }}
      .title-text {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        font-size: 38px;
        font-weight: 800;
        fill: #ffffff;
        filter: drop-shadow(0 0 8px rgba(0, 242, 254, 0.6));
      }}
      .title-accent {{
        fill: #ffb703;
      }}
      .subtext {{
        font-family: "Courier New", Courier, monospace;
        font-size: 14px;
        fill: #94a3b8;
      }}
      .subtext-accent {{
        fill: #ffb703;
      }}
      .cursor {{
        fill: #00f2fe;
        animation: blink 1s step-end infinite;
      }}
      @keyframes blink {{
        50% {{ opacity: 0; }}
      }}
      .glow-border {{
        fill: none;
        stroke: #00f2fe;
        stroke-width: 2;
        opacity: 0.3;
        rx: 12px;
      }}
      .float-cloud {{
        animation: floatCloud 10s ease-in-out infinite alternate;
      }}
      .float-cloud2 {{
        animation: floatCloud 15s ease-in-out infinite alternate-reverse;
      }}
      @keyframes floatCloud {{
        0% {{ transform: translateY(0px) translateX(0px); }}
        100% {{ transform: translateY(-10px) translateX(20px); }}
      }}
    </style>
  </defs>

  <!-- Background -->
  <rect width="100%" height="100%" rx="12" class="bg-rect" />
  
  <!-- Geometric Clouds -->
  <g class="float-cloud" opacity="0.15" stroke="#00f2fe" stroke-width="2" fill="none" transform="translate(300, 20)">
    <path d="M 120,60 A 20,20 0 0,1 150,45 A 30,30 0 0,1 200,55 A 20,20 0 0,1 210,85 L 120,85 A 15,15 0 0,1 120,60 Z" />
  </g>
  <g class="float-cloud2" opacity="0.1" stroke="#ffb703" stroke-width="2" fill="none" transform="translate(60, -10) scale(0.7)">
    <path d="M 120,60 A 20,20 0 0,1 150,45 A 30,30 0 0,1 200,55 A 20,20 0 0,1 210,85 L 120,85 A 15,15 0 0,1 120,60 Z" />
  </g>
  
  <!-- Subtle Grid -->
  {mesh_lines}
  
  <!-- Data Packets -->
  {packets}

  <!-- Isometric Cloud Core -->
  <g id="cloud-core">
    {beams}
    {cluster}
  </g>

  <!-- Typography -->
  <text x="50" y="100" class="title-text">Hello, World! I'm <tspan class="title-accent">Kevin</tspan><tspan class="cursor">_</tspan></text>
  <text x="50" y="135" class="subtext">&gt; I push directly to main... just kidding, I use <tspan class="subtext-accent">CI/CD pipelines</tspan> like a responsible adult.</text>

  <!-- Border -->
  <rect x="2" y="2" width="796" height="196" class="glow-border" />
</svg>'''

    os.makedirs('assets', exist_ok=True)
    with open('assets/header.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("Generated unique Cloud Architecture Header SVG.")

if __name__ == "__main__":
    generate_header()
