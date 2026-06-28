import os

def generate_typist_svg():
    lines = [
        "Cloud Infrastructure Engineer",
        "AWS Architecture | Serverless",
        "Building Production-Grade Systems",
        "Learning in Public Every Day"
    ]
    
    char_width = 12.2 # Approximate width per char for 22px Consolas
    
    # Total animation duration
    dur_per_line = 4
    total_dur = len(lines) * dur_per_line
    
    svg_content = f"""<svg width="600" height="40" viewBox="0 0 600 40" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Flowing Gradient -->
    <linearGradient id="flowingGradient" x1="0%" y1="0%" x2="200%" y2="0%">
      <stop offset="0%" stop-color="#00f2fe" />
      <stop offset="25%" stop-color="#4facfe" />
      <stop offset="50%" stop-color="#8b5cf6" />
      <stop offset="75%" stop-color="#4facfe" />
      <stop offset="100%" stop-color="#00f2fe" />
      <animate attributeName="x1" values="0%;-100%" dur="3s" repeatCount="indefinite" />
      <animate attributeName="x2" values="200%;100%" dur="3s" repeatCount="indefinite" />
    </linearGradient>

    <style>
      .text {{
        font-family: 'Consolas', 'Menlo', 'Monaco', monospace;
        font-size: 22px;
        font-weight: 700;
        fill: url(#flowingGradient);
        text-anchor: middle;
      }}
      .cursor {{
        fill: #00f2fe;
        font-size: 22px;
        font-family: 'Consolas', 'Menlo', monospace;
        font-weight: 700;
      }}
      
      @keyframes blinkCursor {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}
    </style>
  </defs>

  <g>
"""

    for i, line in enumerate(lines):
        line_width = len(line) * char_width
        start_x = 300 - (line_width / 2)
        
        # Timing
        start_time = i * dur_per_line
        
        t_start = start_time / total_dur
        t_type_end = (start_time + 1.2) / total_dur
        t_hold_end = (start_time + 3.2) / total_dur
        t_erase_end = (start_time + 3.8) / total_dur
        
        times = [0]
        vals = [0]
        opac_times = [0]
        opac_vals = [0]
        
        if t_start > 0:
            times.append(t_start - 0.001)
            vals.append(0)
            times.append(t_start)
            vals.append(0)
            
            opac_times.append(t_start - 0.001)
            opac_vals.append(0)
            opac_times.append(t_start)
            opac_vals.append(1)
        else:
            opac_vals[0] = 1
            
        times.append(t_type_end)
        vals.append(line_width + 10)
        
        times.append(t_hold_end)
        vals.append(line_width + 10)
        
        times.append(t_erase_end)
        vals.append(0)
        
        opac_times.append(t_erase_end)
        opac_vals.append(1)
        
        if t_erase_end < 1:
            times.append(t_erase_end + 0.001)
            vals.append(0)
            times.append(1)
            vals.append(0)
            
            opac_times.append(t_erase_end + 0.001)
            opac_vals.append(0)
            opac_times.append(1)
            opac_vals.append(0)
            
        times_str = ";".join([f"{t:.4f}" for t in times])
        vals_str = ";".join([str(v) for v in vals])
        
        opac_times_str = ";".join([f"{t:.4f}" for t in opac_times])
        opac_vals_str = ";".join([str(v) for v in opac_vals])
        
        svg_content += f"""
    <!-- Group for Line {i}, only visible during its time -->
    <g opacity="0">
      <animate attributeName="opacity" values="{opac_vals_str}" keyTimes="{opac_times_str}" dur="{total_dur}s" repeatCount="indefinite" />
      
      <clipPath id="clip_full_{i}">
        <rect x="{start_x}" y="0" width="0" height="40">
          <animate attributeName="width" 
                   values="{vals_str}" 
                   keyTimes="{times_str}" 
                   dur="{total_dur}s" 
                   repeatCount="indefinite" />
        </rect>
      </clipPath>
      
      <text x="300" y="28" class="text" clip-path="url(#clip_full_{i})">{line}</text>
      
      <!-- Cursor -->
      <text x="{start_x}" y="28" class="cursor" style="animation: blinkCursor 0.8s step-end infinite;">|
        <!-- Move cursor X -->
        <animate attributeName="x" 
                 values="{vals_str}" 
                 keyTimes="{times_str}" 
                 dur="{total_dur}s" 
                 repeatCount="indefinite" additive="sum" />
      </text>
    </g>
"""

    svg_content += """
  </g>
</svg>
"""

    os.makedirs("assets", exist_ok=True)
    with open("assets/typist.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Generated custom typing SVG with flowing gradient.")

if __name__ == "__main__":
    generate_typist_svg()
