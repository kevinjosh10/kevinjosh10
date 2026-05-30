import os

def generate_skills_svg():
    lines = [
        "kevin@aws:~$ ./init_cloud_infrastructure.sh",
        "[ OK ] Booting KevinOS v1.0.0...",
        "[ OK ] Initializing AWS Architecture...",
        "[ OK ] Loading Python 3.10 Runtime...",
        "[ OK ] Compiling C/C++ Core Binaries...",
        "[ OK ] Mounting Docker Containers & Kubernetes Pods...",
        "[ OK ] Starting Java Virtual Machine...",
        "[ OK ] Establishing Git & GitHub Actions CI/CD pipelines...",
        "[ OK ] Configuring Bash Environment & Linux Kernel...",
        "[ OK ] Connecting Firebase & JS Front-end Services...",
        "[ OK ] All systems operational. Ready to build.",
        "kevin@aws:~$ _"
    ]
    
    # Timing configuration
    delay = 0.5
    interval = 0.6
    
    svg_texts = ""
    y_pos = 45
    
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            # Cursor blink for the last line
            css_class = f"line l{i} blink"
        elif line.startswith("kevin@aws:~$"):
            css_class = f"line l{i} prompt"
        else:
            css_class = f"line l{i}"
            
        # Add color highlighting for specific words
        if line.startswith("[ OK ]"):
            # Split out the [ OK ] part
            rest = line[6:]
            line_html = f'<tspan class="ok">[ OK ]</tspan>{rest}'
        else:
            line_html = line
            
        svg_texts += f'    <text x="20" y="{y_pos}" class="{css_class}">{line_html}</text>\n'
        y_pos += 25

    # Generate CSS delays
    css_delays = ""
    current_delay = delay
    for i in range(len(lines)):
        css_delays += f"    .l{i} {{ animation-delay: {current_delay:.1f}s; }}\n"
        if i == 0 or i == len(lines) - 2:
            current_delay += 1.0 # Pause longer after command and before prompt
        else:
            current_delay += interval
            
    svg_content = f"""<svg width="800" height="360" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .bg {{ fill: #0f172a; rx: 10px; }}
      .topbar {{ fill: #1e293b; }}
      .btn-red {{ fill: #ef4444; }}
      .btn-yellow {{ fill: #eab308; }}
      .btn-green {{ fill: #22c55e; }}
      
      .line {{
        font-family: 'Courier New', Courier, monospace;
        font-size: 15px;
        fill: #94a3b8;
        opacity: 0;
        animation: type 0.1s forwards;
      }}
      .prompt {{ fill: #00f2fe; font-weight: bold; }}
      .ok {{ fill: #39ff14; font-weight: bold; }}
      
      @keyframes type {{
        to {{ opacity: 1; }}
      }}
      
      .blink {{
        animation: type 0.1s forwards, blinkCursor 1s step-end infinite {current_delay:.1f}s !important;
      }}
      @keyframes blinkCursor {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}
      
{css_delays}
    </style>
  </defs>

  <!-- Terminal Window -->
  <rect width="100%" height="100%" class="bg" />
  
  <!-- Top Bar -->
  <path d="M 0 10 Q 0 0 10 0 L 790 0 Q 800 0 800 10 L 800 25 L 0 25 Z" class="topbar" />
  
  <!-- Window Buttons -->
  <circle cx="20" cy="12.5" r="5" class="btn-red" />
  <circle cx="40" cy="12.5" r="5" class="btn-yellow" />
  <circle cx="60" cy="12.5" r="5" class="btn-green" />
  
  <!-- Terminal Title -->
  <text x="400" y="17" font-family="-apple-system, sans-serif" font-size="12" fill="#64748b" text-anchor="middle">kevin@aws: ~/skills</text>

  <!-- Content -->
  <g transform="translate(0, 10)">
{svg_texts}  </g>
</svg>
"""

    os.makedirs("assets", exist_ok=True)
    with open("assets/skills.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Generated Terminal Skills SVG.")

if __name__ == "__main__":
    generate_skills_svg()
