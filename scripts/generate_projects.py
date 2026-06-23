import os

def generate_projects_svg():
    projects = [
        {
            "title": "S3 Backup Tool",
            "link": "https://github.com/kevinjosh10/s3-backup-tool",
            "desc": [
                "Resilient CLI utility for metadata-",
                "based incremental synchronization,",
                "encryption, and lifecycle automation."
            ],
            "tags": ["Python", "AWS S3", "Boto3", "CLI"],
            "color": "#00f2fe", # Cyan
            "x": 20, "y": 20
        },
        {
            "title": "CloudMorph",
            "link": "https://github.com/kevinjosh10/CloudMorph",
            "desc": [
                "Serverless file intelligence platform",
                "handling secure cross-origin uploads",
                "and pre-signed URLs via Lambda."
            ],
            "tags": ["Lambda", "API Gtwy", "S3", "Python"],
            "color": "#39ff14", # Green
            "x": 410, "y": 20
        },
        {
            "title": "Cryptexa",
            "link": "https://github.com/kevinjosh10/Cryptexa",
            "desc": [
                "Full-stack student community hub for",
                "resource sharing &amp; real-time forums.",
                "Built with a decoupled serverless backend."
            ],
            "tags": ["React", "Node.js", "Serverless"],
            "color": "#ff007f", # Pink
            "x": 20, "y": 230
        },
        {
            "title": "AWS Static Website",
            "link": "https://github.com/kevinjosh10/aws-static-website",
            "desc": [
                "Serverless web hosting architecture",
                "using Amazon S3, CloudFront CDN, and",
                "Route 53 for low-latency delivery."
            ],
            "tags": ["AWS S3", "CloudFront", "Route 53"],
            "color": "#ff9900", # AWS Orange
            "x": 410, "y": 230
        },
        {
            "title": "CloudTrain Studio",
            "link": "https://github.com/kevinjosh10/CloudTrain",
            "desc": [
                "End-to-end serverless MLOps platform",
                "to manage machine learning projects",
                "and event-driven training pipelines."
            ],
            "tags": ["SQS", "Lambda", "S3", "Firebase"],
            "color": "#ffd700", # Bright Yellow
            "x": 20, "y": 440
        },
        {
            "title": "GitWrapped",
            "link": "https://github.com/kevinjosh10/GitWrapped",
            "desc": [
                "Highly animated cinematic 'Spotify",
                "Wrapped' style experience generated",
                "entirely from raw GitHub statistics."
            ],
            "tags": ["React", "Framer Motion", "API"],
            "color": "#8b5cf6", # Purple
            "x": 410, "y": 440
        }
    ]

    cards_html = ""
    for idx, p in enumerate(projects):
        # Generate description text elements
        desc_html = ""
        for i, line in enumerate(p["desc"]):
            desc_html += f'<text x="{p["x"] + 25}" y="{p["y"] + 80 + (i*22)}" class="desc">{line}</text>\n'
            
        # Generate tags
        tags_html = ""
        tag_x = p["x"] + 25
        for tag in p["tags"]:
            tag_width = len(tag) * 8 + 16
            tags_html += f'''
            <rect x="{tag_x}" y="{p["y"] + 155}" width="{tag_width}" height="24" rx="12" fill="{p["color"]}" fill-opacity="0.15" stroke="{p["color"]}" stroke-width="1" />
            <text x="{tag_x + tag_width/2}" y="{p["y"] + 171}" class="tag" fill="{p["color"]}">{tag}</text>
            '''
            tag_x += tag_width + 10

        cards_html += f'''
        <!-- Card: {p["title"]} -->
        <g class="card" style="animation-delay: {idx * 0.15}s">
            <rect x="{p["x"]}" y="{p["y"]}" width="370" height="200" rx="12" class="card-bg" />
            <!-- Neon top border highlight -->
            <path d="M {p["x"]} {p["y"]+12} Q {p["x"]} {p["y"]} {p["x"]+12} {p["y"]} L {p["x"]+358} {p["y"]} Q {p["x"]+370} {p["y"]} {p["x"]+370} {p["y"]+12}" stroke="{p["color"]}" stroke-width="3" fill="none" class="card-highlight" />
            
            <!-- Icon/Folder -->
            <svg x="{p["x"] + 25}" y="{p["y"] + 25}" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="{p["color"]}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path>
            </svg>
            
            <text x="{p["x"] + 60}" y="{p["y"] + 43}" class="title" fill="{p["color"]}">{p["title"]}</text>
            
            {desc_html}
            {tags_html}
        </g>
        '''

    svg_content = f"""<svg width="800" height="660" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .card {{
        cursor: pointer;
        transition: transform 0.3s ease;
        animation: floatUp 0.8s ease-out forwards;
        opacity: 0;
        transform-origin: center;
      }}
      .card:hover {{
        transform: translateY(-5px);
      }}
      .card:hover .card-bg {{
        fill: #1e293b;
        stroke: #475569;
      }}
      .card-bg {{
        fill: #0f172a;
        stroke: #1e293b;
        stroke-width: 2;
        transition: all 0.3s ease;
      }}
      .title {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 18px;
        font-weight: 700;
        letter-spacing: 0.5px;
      }}
      .desc {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 14px;
        fill: #94a3b8;
      }}
      .tag {{
        font-family: 'Courier New', Courier, monospace;
        font-size: 12px;
        font-weight: bold;
        text-anchor: middle;
      }}
      
      @keyframes floatUp {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}
    </style>
  </defs>

  <!-- Background container -->
  <rect width="100%" height="100%" fill="transparent" />

  {cards_html}

</svg>
"""
    os.makedirs("assets", exist_ok=True)
    with open("assets/projects.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Generated Animated Projects SVG.")

if __name__ == "__main__":
    generate_projects_svg()
