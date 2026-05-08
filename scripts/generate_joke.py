import os
import requests
import textwrap

def fetch_joke():
    # Enforcing strict SFW filters using JokeAPI
    url = "https://v2.jokeapi.dev/joke/Programming,Miscellaneous?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if not data.get("error"):
            return data.get("joke", "Why do programmers prefer dark mode?\nBecause light attracts bugs!")
    except Exception:
        pass
    
    # Safe fallback joke
    return "Why do programmers prefer dark mode?\nBecause light attracts bugs!"

def generate_svg(joke_text):
    # Wrap text to fit inside the SVG beautifully
    lines = textwrap.wrap(joke_text, width=45)
    
    base_height = 80
    line_height = 25
    total_height = base_height + (len(lines) * line_height)
    
    svg_lines = ""
    y_pos = 60
    for line in lines:
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
      .text {{ fill: #e2e8f0; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 15px; text-anchor: middle; }}
      .border {{ fill: none; stroke: #4a5568; stroke-width: 2; rx: 12px; }}
    </style>
  </defs>
  
  <rect width="100%" height="100%" fill="transparent" rx="12px" />
  
  <text x="50%" y="30" class="title">💻 Dev Joke of the Day</text>
  
  {svg_lines}
</svg>
"""
    return svg_content

def main():
    joke = fetch_joke()
    svg = generate_svg(joke)
    
    os.makedirs("assets", exist_ok=True)
    with open("assets/joke.svg", "w", encoding="utf-8") as f:
        f.write(svg)
        
    print("Generated 100% SFW Dev Joke of the Day SVG.")

if __name__ == "__main__":
    main()
