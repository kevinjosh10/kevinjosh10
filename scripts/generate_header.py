import os

svg_content = """<svg width="800" height="250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1a202c" />
      <stop offset="100%" stop-color="#2d3748" />
    </linearGradient>

    <!-- Wave Gradients -->
    <linearGradient id="waveGrad1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#f6d365;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#fda085;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="waveGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#84fab0;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#8fd3f4;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="waveGrad3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#a18cd1;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#fbc2eb;stop-opacity:1" />
    </linearGradient>

    <!-- Sweeping Spotlight Beam Gradient -->
    <linearGradient id="spotlightGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>

    <!-- Drop Shadow for Text -->
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.8"/>
    </filter>

    <!-- Cloud Graphic -->
    <g id="cloud" fill="#ffffff">
      <circle cx="30" cy="30" r="20" />
      <circle cx="50" cy="20" r="25" />
      <circle cx="70" cy="25" r="20" />
      <circle cx="90" cy="35" r="15" />
      <rect x="30" y="25" width="60" height="25" rx="10" />
    </g>

    <!-- Sparkle Graphic -->
    <g id="sparkle" fill="#ffffff">
      <path d="M 0,-12 L 2,-2 L 12,0 L 2,2 L 0,12 L -2,2 L -12,0 L -2,-2 Z" />
    </g>

    <style>
      .title { fill: #00f2fe; filter: url(#shadow); font-family: 'Inter', system-ui, -apple-system, sans-serif; font-size: 44px; font-weight: 900; text-anchor: middle; animation: fadeIn 1s ease-out; letter-spacing: -0.5px; }
      .sub1 { fill: #ffd700; filter: url(#shadow); font-family: 'Inter', system-ui, -apple-system, sans-serif; font-size: 24px; font-weight: 700; text-anchor: middle; animation: fadeIn 1.5s ease-out; letter-spacing: 0.5px; }
      .sub2 { fill: #f7fafc; filter: url(#shadow); font-family: 'Inter', system-ui, -apple-system, sans-serif; font-size: 16px; font-style: italic; font-weight: 500; text-anchor: middle; animation: fadeIn 2s ease-out; }
      
      @keyframes fadeIn {
        from { opacity: 0; transform: translateY(5px); }
        to { opacity: 1; transform: translateY(0); }
      }

      /* PROVEN: Infinite moving animations using ONLY translateX */
      .wave1 { animation: moveLeft 12s linear infinite; }
      .wave2 { animation: moveLeft 8s linear infinite; }
      .wave3 { animation: moveLeft 15s linear infinite; }
      .clouds { animation: moveLeft 30s linear infinite; }
      .clouds2 { animation: moveLeft 45s linear infinite; }

      @keyframes moveLeft {
        0% { transform: translateX(0); }
        100% { transform: translateX(-800px); }
      }

      /* Spotlight Beam Sweeping Left to Right */
      .spotlight {
        animation: sweepLight 5s linear infinite;
      }
      @keyframes sweepLight {
        0% { transform: translateX(-600px); }
        100% { transform: translateX(1000px); }
      }

      /* Sparkle Twinkle Animation (ONLY OPACITY, NO TRANSFORM TO AVOID SAFARI 0,0 BUG) */
      .sp { animation: twinkle 3s ease-in-out infinite; }
      .sp1 { animation-delay: 0s; }
      .sp2 { animation-delay: 0.7s; }
      .sp3 { animation-delay: 1.4s; }
      .sp4 { animation-delay: 2.1s; }
      .sp5 { animation-delay: 2.8s; }
      
      @keyframes twinkle {
        0%, 100% { opacity: 0; }
        50% { opacity: 0.9; }
      }
    </style>
  </defs>
  
  <rect width="100%" height="100%" fill="url(#bg)" rx="15px" />
  
  <clipPath id="clipBox">
    <rect width="100%" height="100%" rx="15px" />
  </clipPath>
  
  <g clip-path="url(#clipBox)">
    
    <!-- Sweeping Spotlight Beam (Using proven translateX) -->
    <!-- The beam is slanted physically by drawing the polygon so we don't need CSS skew/rotate -->
    <polygon points="100,-50 300,-50 150,300 -50,300" fill="url(#spotlightGrad)" class="spotlight" />

    <!-- Cloud Layers -->
    <g class="clouds" opacity="0.6">
      <use href="#cloud" transform="translate(50, -5) scale(0.8)" />
      <use href="#cloud" transform="translate(300, 20) scale(1.2)" />
      <use href="#cloud" transform="translate(550, -10) scale(0.6)" />
      <use href="#cloud" transform="translate(720, 15) scale(0.9)" />
      <use href="#cloud" transform="translate(850, -5) scale(0.8)" />
      <use href="#cloud" transform="translate(1100, 20) scale(1.2)" />
      <use href="#cloud" transform="translate(1350, -10) scale(0.6)" />
      <use href="#cloud" transform="translate(1520, 15) scale(0.9)" />
    </g>

    <g class="clouds2" opacity="0.3">
      <use href="#cloud" transform="translate(150, 30) scale(1.0)" />
      <use href="#cloud" transform="translate(400, 5) scale(0.7)" />
      <use href="#cloud" transform="translate(650, 40) scale(1.1)" />
      <use href="#cloud" transform="translate(780, 10) scale(0.8)" />
      <use href="#cloud" transform="translate(950, 30) scale(1.0)" />
      <use href="#cloud" transform="translate(1200, 5) scale(0.7)" />
      <use href="#cloud" transform="translate(1450, 40) scale(1.1)" />
      <use href="#cloud" transform="translate(1580, 10) scale(0.8)" />
    </g>

    <!-- Waves -->
    <path class="wave3" d="M 0 160 Q 100 130 200 160 T 400 160 T 600 160 T 800 160 T 1000 160 T 1200 160 T 1400 160 T 1600 160 L 1600 250 L 0 250 Z" fill="url(#waveGrad3)" opacity="0.4" />
    <path class="wave2" d="M 0 180 Q 100 210 200 180 T 400 180 T 600 180 T 800 180 T 1000 180 T 1200 180 T 1400 180 T 1600 180 L 1600 250 L 0 250 Z" fill="url(#waveGrad2)" opacity="0.6" />
    <path class="wave1" d="M 0 200 Q 100 170 200 200 T 400 200 T 600 200 T 800 200 T 1000 200 T 1200 200 T 1400 200 T 1600 200 L 1600 250 L 0 250 Z" fill="url(#waveGrad1)" opacity="0.8" />
  </g>
  
  <rect width="99%" height="98%" x="4" y="2" fill="none" stroke="#4a5568" stroke-width="1" rx="15px" />
  
  <!-- Physical Sparkles Placed Using Attributes (NOT CSS TRANSFORM) -->
  <use href="#sparkle" x="180" y="50" class="sp sp1" />
  <use href="#sparkle" x="630" y="60" class="sp sp2" />
  <use href="#sparkle" x="240" y="115" class="sp sp3" />
  <use href="#sparkle" x="580" y="110" class="sp sp4" />
  <use href="#sparkle" x="400" y="30" class="sp sp5" />

  <!-- Base Text -->
  <text x="50%" y="80" class="title">Hello, World! I'm Kevin 👨‍💻</text>
  <text x="50%" y="125" class="sub1">I push directly to main.</text>
  <text x="50%" y="155" class="sub2">(Just kidding, I use CI/CD pipelines like a responsible adult 🛠️)</text>

</svg>
"""

os.makedirs("assets", exist_ok=True)
with open("assets/header.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
    
print("Generated custom header SVG with guaranteed bulletproof animations.")
