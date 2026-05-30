import os
import requests
import textwrap

def fetch_quote():
    # Use ZenQuotes API for high-quality motivational quotes
    url = "https://zenquotes.io/api/random"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            quote = data[0].get("q", "The only way to do great work is to love what you do.")
            author = data[0].get("a", "Steve Jobs")
            return f'"{quote}"\n— {author}'
    except Exception:
        pass
    
    # Safe fallback quote
    return '"The future belongs to those who learn more skills and combine them in creative ways."\n— Robert Greene'

def generate_svg(quote_text):
    # Wrap text to fit inside the SVG beautifully
    lines = textwrap.wrap(quote_text, width=45)
    
    base_height = 80
    line_height = 25
    total_height = base_height + (len(lines) * line_height)
    
    svg_lines = ""
    y_pos = 60
    for line in lines:
        # Check if line is the author (starts with mdash or hyphen)
        if line.startswith("—") or line.startswith("-"):
            svg_lines += f'<text x="50%" y="{y_pos}" class="author">{line}</text>\n'
        else:
            svg_lines += f'<text x="50%" y="{y_pos}" class="text">{line}</text>\n'
        y_pos += line_height
        
    svg_content = f"""<svg width="500" height="{total_height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#2d3748;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#1a202c;stop-opacity:1" />
    </linearGradient>
    <style>
      .title {{ fill: #63b3ed; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 18px; font-weight: bold; text-anchor: middle; }}
      .text {{ fill: #e2e8f0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 15px; font-style: italic; text-anchor: middle; }}
      .author {{ fill: #a0aec0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 14px; font-weight: bold; text-anchor: middle; }}
      .border {{ fill: none; stroke: #4a5568; stroke-width: 2; rx: 12px; }}
    </style>
  </defs>
  
  <rect width="100%" height="100%" fill="transparent" rx="12px" />
  
  <text x="50%" y="30" class="title">✨ Motivational Quote of the Day</text>
  
  {svg_lines}
</svg>
"""
    return svg_content

def main():
    quote = fetch_quote()
    svg = generate_svg(quote)
    
    os.makedirs("assets", exist_ok=True)
    with open("assets/quote.svg", "w", encoding="utf-8") as f:
        f.write(svg)
        
    # Remove old joke if exists
    if os.path.exists("assets/joke.svg"):
        try:
            os.remove("assets/joke.svg")
        except:
            pass
        
    print("Generated Motivational Quote SVG.")

if __name__ == "__main__":
    main()
