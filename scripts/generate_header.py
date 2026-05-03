import os

svg_content = """<svg width="800" height="250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient (Darker stormy sky) -->
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f1624" />
      <stop offset="50%" stop-color="#1a1e36" />
      <stop offset="100%" stop-color="#1e293b" />
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
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>

    <!-- Storm Cloud Gradient -->
    <linearGradient id="stormCloudGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#94a3b8" />
      <stop offset="60%" stop-color="#64748b" />
      <stop offset="100%" stop-color="#475569" />
    </linearGradient>

    <!-- Fog/Mist Gradient -->
    <linearGradient id="mistGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#94a3b8" stop-opacity="0" />
      <stop offset="30%" stop-color="#94a3b8" stop-opacity="0.12" />
      <stop offset="50%" stop-color="#cbd5e1" stop-opacity="0.18" />
      <stop offset="70%" stop-color="#94a3b8" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#94a3b8" stop-opacity="0" />
    </linearGradient>
    <linearGradient id="mistGrad2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#818cf8" stop-opacity="0" />
      <stop offset="40%" stop-color="#818cf8" stop-opacity="0.08" />
      <stop offset="60%" stop-color="#a5b4fc" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#818cf8" stop-opacity="0" />
    </linearGradient>

    <!-- Neon Border Gradient -->
    <linearGradient id="neonBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#06b6d4" />
      <stop offset="50%" stop-color="#8b5cf6" />
      <stop offset="100%" stop-color="#06b6d4" />
    </linearGradient>

    <!-- Lightning Glow Filter -->
    <filter id="lightningGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <!-- Neon Border Glow Filter -->
    <filter id="neonGlow" x="-5%" y="-5%" width="110%" height="110%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <!-- Text Electric Glow Filter -->
    <filter id="electricGlow" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur stdDeviation="6" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <!-- Drop Shadow for Text -->
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.8"/>
    </filter>

    <!-- Storm Cloud Graphic (Darker, puffier) -->
    <g id="stormCloud">
      <circle cx="25" cy="32" r="22" fill="url(#stormCloudGrad)" />
      <circle cx="50" cy="18" r="28" fill="url(#stormCloudGrad)" />
      <circle cx="78" cy="22" r="24" fill="url(#stormCloudGrad)" />
      <circle cx="100" cy="32" r="18" fill="url(#stormCloudGrad)" />
      <rect x="20" y="28" width="85" height="22" rx="10" fill="url(#stormCloudGrad)" />
      <!-- Dark underbelly -->
      <rect x="25" y="38" width="75" height="12" rx="6" fill="#374151" opacity="0.6" />
    </g>

    <style>
      .title { fill: #00f2fe; filter: url(#shadow); font-family: 'Consolas', 'Menlo', 'Monaco', 'Ubuntu Mono', monospace; font-size: 44px; font-weight: 900; text-anchor: middle; letter-spacing: -0.5px; }
      .sub1 { fill: #ffd700; filter: url(#shadow); font-family: 'Consolas', 'Menlo', 'Monaco', 'Ubuntu Mono', monospace; font-size: 24px; font-weight: 700; text-anchor: middle; animation: fadeIn 0.5s ease-out 5s forwards; opacity: 0; letter-spacing: 0.5px; }
      .sub2 { fill: #f7fafc; filter: url(#shadow); font-family: 'Consolas', 'Menlo', 'Monaco', 'Ubuntu Mono', monospace; font-size: 16px; font-style: italic; font-weight: 500; text-anchor: middle; animation: fadeIn 0.5s ease-out 5.4s forwards; opacity: 0; }
      
      @keyframes fadeIn {
        from { opacity: 0; transform: translateY(5px); }
        to { opacity: 1; transform: translateY(0); }
      }

      /* === DECRYPT ANIMATION (5s FAST TWITCHING) === */
      .decryptText { fill: #00f2fe; filter: url(#shadow); font-family: 'Consolas', 'Menlo', 'Monaco', 'Ubuntu Mono', monospace; font-size: 44px; font-weight: 900; text-anchor: middle; letter-spacing: 0px; opacity: 0; }
      .dec1 { animation: cycle 0.7s infinite; animation-delay: 0.0s; }
      .dec2 { animation: cycle 0.7s infinite; animation-delay: 0.1s; }
      .dec3 { animation: cycle 0.7s infinite; animation-delay: 0.2s; }
      .dec4 { animation: cycle 0.7s infinite; animation-delay: 0.3s; }
      .dec5 { animation: cycle 0.7s infinite; animation-delay: 0.4s; }
      .dec6 { animation: cycle 0.7s infinite; animation-delay: 0.5s; }
      .dec7 { animation: cycle 0.7s infinite; animation-delay: 0.6s; }

      @keyframes cycle { 0%, 14.2% { opacity: 1; } 14.3%, 100% { opacity: 0; } }

      .decryptWrapper { animation: hideWrapper 5s forwards; }
      @keyframes hideWrapper { 0%, 99.9% { opacity: 1; } 100% { opacity: 0; } }

      .finalReveal { animation: showFinal 5s forwards; opacity: 0; }
      @keyframes showFinal { 0%, 99.9% { opacity: 0; } 100% { opacity: 1; } }

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

      /* === LIGHTNING FLASH === */
      .lightning { animation: flash 4s ease-in-out infinite; }
      .lightning1 { animation-delay: 0s; }
      .lightning2 { animation-delay: 1.8s; }
      .lightning3 { animation-delay: 3.2s; }
      .lightning4 { animation-delay: 0.6s; }
      .lightning5 { animation-delay: 2.5s; }

      @keyframes flash {
        0%, 100% { opacity: 0; }
        4% { opacity: 1; }
        6% { opacity: 0; }
        8% { opacity: 0.8; }
        10% { opacity: 0; }
      }



      /* === RAIN DROPS FALLING === */
      .rain { animation: fall 1.2s linear infinite; }
      .rain1 { animation-delay: 0s; }
      .rain2 { animation-delay: 0.15s; }
      .rain3 { animation-delay: 0.3s; }
      .rain4 { animation-delay: 0.45s; }
      .rain5 { animation-delay: 0.6s; }
      .rain6 { animation-delay: 0.75s; }
      .rain7 { animation-delay: 0.9s; }
      .rain8 { animation-delay: 1.05s; }
      .rain9 { animation-delay: 0.2s; }
      .rain10 { animation-delay: 0.5s; }
      .rain11 { animation-delay: 0.35s; }
      .rain12 { animation-delay: 0.8s; }
      .rain13 { animation-delay: 0.1s; }
      .rain14 { animation-delay: 0.55s; }
      .rain15 { animation-delay: 0.7s; }
      .rain16 { animation-delay: 0.25s; }

      @keyframes fall {
        0% { transform: translateY(0); opacity: 0.7; }
        80% { opacity: 0.4; }
        100% { transform: translateY(200px); opacity: 0; }
      }

      /* === SKY FLASH (ambient glow during lightning) === */
      .skyFlash { animation: ambientFlash 4s ease-in-out infinite; }
      .skyFlash1 { animation-delay: 0s; }
      .skyFlash2 { animation-delay: 1.8s; }

      @keyframes ambientFlash {
        0%, 100% { opacity: 0; }
        4% { opacity: 0.08; }
        6% { opacity: 0; }
        8% { opacity: 0.05; }
        10% { opacity: 0; }
      }

      /* === DRIFTING FOG/MIST === */
      .mist1 { animation: moveLeft 40s linear infinite; }
      .mist2 { animation: moveLeft 55s linear infinite; }

      /* === NEON BORDER PULSE === */
      .neonBorderRect { animation: borderPulse 4s ease-in-out infinite; }

      @keyframes borderPulse {
        0%, 100% { opacity: 0.4; }
        50% { opacity: 0.9; }
      }

      /* === GLITCH / HACKER TEXT EFFECT (RGB channel split) === */
      .glitchR {
        animation: glitchRight 3s steps(1, end) infinite;
        fill: #ff0040;
        font-family: 'Consolas', 'Menlo', 'Monaco', 'Ubuntu Mono', monospace;
        font-size: 44px;
        font-weight: 900;
        text-anchor: middle;
      }
      .glitchL {
        animation: glitchLeft 3s steps(1, end) infinite;
        fill: #00f2fe;
        font-family: 'Consolas', 'Menlo', 'Monaco', 'Ubuntu Mono', monospace;
        font-size: 44px;
        font-weight: 900;
        text-anchor: middle;
      }

      @keyframes glitchRight {
        0%, 100% { opacity: 0; transform: translateX(0); }
        7% { opacity: 0.7; transform: translateX(3px); }
        8% { opacity: 0.7; transform: translateX(-2px); }
        9% { opacity: 0; transform: translateX(0); }
        32% { opacity: 0; transform: translateX(0); }
        33% { opacity: 0.5; transform: translateX(4px); }
        34% { opacity: 0.6; transform: translateX(-1px); }
        35% { opacity: 0; transform: translateX(0); }
        54% { opacity: 0; transform: translateX(0); }
        55% { opacity: 0.8; transform: translateX(2px); }
        56% { opacity: 0; transform: translateX(0); }
        78% { opacity: 0; transform: translateX(0); }
        79% { opacity: 0.6; transform: translateX(-3px); }
        80% { opacity: 0.5; transform: translateX(2px); }
        81% { opacity: 0; transform: translateX(0); }
      }

      @keyframes glitchLeft {
        0%, 100% { opacity: 0; transform: translateX(0); }
        7% { opacity: 0.5; transform: translateX(-3px); }
        8% { opacity: 0.6; transform: translateX(2px); }
        9% { opacity: 0; transform: translateX(0); }
        32% { opacity: 0; transform: translateX(0); }
        33% { opacity: 0.6; transform: translateX(-4px); }
        34% { opacity: 0.4; transform: translateX(1px); }
        35% { opacity: 0; transform: translateX(0); }
        54% { opacity: 0; transform: translateX(0); }
        55% { opacity: 0.6; transform: translateX(-2px); }
        56% { opacity: 0; transform: translateX(0); }
        78% { opacity: 0; transform: translateX(0); }
        79% { opacity: 0.5; transform: translateX(3px); }
        80% { opacity: 0.7; transform: translateX(-2px); }
        81% { opacity: 0; transform: translateX(0); }
      }
    </style>
  </defs>
  
  <rect width="100%" height="100%" fill="url(#bg)" rx="15px" />
  
  <clipPath id="clipBox">
    <rect width="100%" height="100%" rx="15px" />
  </clipPath>
  
  <g clip-path="url(#clipBox)">
    
    <!-- Ambient Sky Flash (lights up the whole sky during lightning) -->
    <rect width="100%" height="100%" fill="#c4b5fd" class="skyFlash skyFlash1" />
    <rect width="100%" height="100%" fill="#93c5fd" class="skyFlash skyFlash2" />

    <!-- Sweeping Spotlight Beam (Using proven translateX) -->
    <polygon points="100,-50 300,-50 150,300 -50,300" fill="url(#spotlightGrad)" class="spotlight" />

    <!-- === RAIN STREAKS (placed across the whole scene) === -->
    <line x1="80" y1="30" x2="78" y2="50" stroke="#93c5fd" stroke-width="1.5" stroke-linecap="round" opacity="0.5" class="rain rain1" />
    <line x1="155" y1="25" x2="153" y2="45" stroke="#93c5fd" stroke-width="1" stroke-linecap="round" opacity="0.4" class="rain rain2" />
    <line x1="230" y1="35" x2="228" y2="55" stroke="#a5b4fc" stroke-width="1.5" stroke-linecap="round" opacity="0.5" class="rain rain3" />
    <line x1="310" y1="28" x2="308" y2="48" stroke="#93c5fd" stroke-width="1" stroke-linecap="round" opacity="0.35" class="rain rain4" />
    <line x1="385" y1="32" x2="383" y2="52" stroke="#a5b4fc" stroke-width="1.5" stroke-linecap="round" opacity="0.45" class="rain rain5" />
    <line x1="460" y1="26" x2="458" y2="46" stroke="#93c5fd" stroke-width="1" stroke-linecap="round" opacity="0.4" class="rain rain6" />
    <line x1="530" y1="38" x2="528" y2="58" stroke="#a5b4fc" stroke-width="1.5" stroke-linecap="round" opacity="0.5" class="rain rain7" />
    <line x1="600" y1="30" x2="598" y2="50" stroke="#93c5fd" stroke-width="1" stroke-linecap="round" opacity="0.35" class="rain rain8" />
    <line x1="120" y1="40" x2="118" y2="60" stroke="#a5b4fc" stroke-width="1" stroke-linecap="round" opacity="0.3" class="rain rain9" />
    <line x1="270" y1="22" x2="268" y2="42" stroke="#93c5fd" stroke-width="1.5" stroke-linecap="round" opacity="0.45" class="rain rain10" />
    <line x1="350" y1="36" x2="348" y2="56" stroke="#a5b4fc" stroke-width="1" stroke-linecap="round" opacity="0.35" class="rain rain11" />
    <line x1="500" y1="28" x2="498" y2="48" stroke="#93c5fd" stroke-width="1.5" stroke-linecap="round" opacity="0.4" class="rain rain12" />
    <line x1="670" y1="34" x2="668" y2="54" stroke="#a5b4fc" stroke-width="1" stroke-linecap="round" opacity="0.3" class="rain rain13" />
    <line x1="735" y1="30" x2="733" y2="50" stroke="#93c5fd" stroke-width="1.5" stroke-linecap="round" opacity="0.45" class="rain rain14" />
    <line x1="195" y1="42" x2="193" y2="62" stroke="#a5b4fc" stroke-width="1" stroke-linecap="round" opacity="0.35" class="rain rain15" />
    <line x1="425" y1="20" x2="423" y2="40" stroke="#93c5fd" stroke-width="1" stroke-linecap="round" opacity="0.3" class="rain rain16" />

    <!-- Storm Cloud Layers (Darker, moodier) -->
    <g class="clouds" opacity="0.75">
      <use href="#stormCloud" transform="translate(50, -8) scale(0.9)" />
      <use href="#stormCloud" transform="translate(300, 12) scale(1.3)" />
      <use href="#stormCloud" transform="translate(550, -12) scale(0.7)" />
      <use href="#stormCloud" transform="translate(720, 8) scale(1.0)" />
      <use href="#stormCloud" transform="translate(850, -8) scale(0.9)" />
      <use href="#stormCloud" transform="translate(1100, 12) scale(1.3)" />
      <use href="#stormCloud" transform="translate(1350, -12) scale(0.7)" />
      <use href="#stormCloud" transform="translate(1520, 8) scale(1.0)" />
    </g>

    <g class="clouds2" opacity="0.45">
      <use href="#stormCloud" transform="translate(150, 22) scale(1.1)" />
      <use href="#stormCloud" transform="translate(400, -2) scale(0.8)" />
      <use href="#stormCloud" transform="translate(650, 30) scale(1.2)" />
      <use href="#stormCloud" transform="translate(780, 5) scale(0.9)" />
      <use href="#stormCloud" transform="translate(950, 22) scale(1.1)" />
      <use href="#stormCloud" transform="translate(1200, -2) scale(0.8)" />
      <use href="#stormCloud" transform="translate(1450, 30) scale(1.2)" />
      <use href="#stormCloud" transform="translate(1580, 5) scale(0.9)" />
    </g>

    <!-- === LIGHTNING BOLTS (positioned under specific clouds) === -->
    <g class="lightning lightning1">
      <polygon points="355,48 361,62 357,62 365,82 353,66 357,66 351,48" fill="#fbbf24" filter="url(#lightningGlow)" />
    </g>
    <g class="lightning lightning2">
      <polygon points="105,40 110,52 107,52 114,68 103,55 107,55 102,40" fill="#fde68a" filter="url(#lightningGlow)" />
    </g>
    <g class="lightning lightning3">
      <polygon points="585,38 592,56 588,56 598,80 584,60 588,60 582,38" fill="#fbbf24" filter="url(#lightningGlow)" />
      <polygon points="592,56 598,62 596,62 602,72 594,64 596,64 590,56" fill="#fde68a" filter="url(#lightningGlow)" />
    </g>
    <g class="lightning lightning4">
      <polygon points="735,42 739,54 737,54 743,66 733,56 736,56 732,42" fill="#fde68a" filter="url(#lightningGlow)" />
    </g>
    <g class="lightning lightning5">
      <polygon points="255,45 260,58 257,58 264,74 254,60 257,60 252,45" fill="#fbbf24" filter="url(#lightningGlow)" />
    </g>




    <!-- Waves -->
    <path class="wave3" d="M 0 160 Q 100 130 200 160 T 400 160 T 600 160 T 800 160 T 1000 160 T 1200 160 T 1400 160 T 1600 160 L 1600 250 L 0 250 Z" fill="url(#waveGrad3)" opacity="0.4" />
    <path class="wave2" d="M 0 180 Q 100 210 200 180 T 400 180 T 600 180 T 800 180 T 1000 180 T 1200 180 T 1400 180 T 1600 180 L 1600 250 L 0 250 Z" fill="url(#waveGrad2)" opacity="0.6" />
    <path class="wave1" d="M 0 200 Q 100 170 200 200 T 400 200 T 600 200 T 800 200 T 1000 200 T 1200 200 T 1400 200 T 1600 200 L 1600 250 L 0 250 Z" fill="url(#waveGrad1)" opacity="0.8" />
  </g>
  
  <!-- === NEON GLOWING BORDER (replaces boring grey) === -->
  <rect width="99%" height="98%" x="4" y="2" fill="none" stroke="url(#neonBorder)" stroke-width="1.5" rx="15px" filter="url(#neonGlow)" class="neonBorderRect" />
  
  <!-- === HACKER DECRYPT SEQUENCE (5s FAST TWITCHING) === -->
  <g class="decryptWrapper">
    <text x="50%" y="80" class="decryptText dec1">0x8F4B2A9C7D1E5F3A8B1C</text>
    <text x="50%" y="80" class="decryptText dec2">X#9a!z_ Q$m*p! %'bY8x@p</text>
    <text x="50%" y="80" class="decryptText dec3">H@x$9, %Q*p! 0xK#v1nZ2!</text>
    <text x="50%" y="80" class="decryptText dec4">H3!&amp;o, W%rLd_ 1"m k3v1n</text>
    <text x="50%" y="80" class="decryptText dec5">He[lo, W0r]d! I'x K?vin</text>
    <text x="50%" y="80" class="decryptText dec6">Hell0, Wor1d! I'm Kev!n</text>
    <text x="50%" y="80" class="decryptText dec7">Hello, World! I'm Kevin</text>
  </g>

  <g class="finalReveal">
    <!-- === GLITCH GHOST COPIES (RGB split behind main text) === -->
    <text x="50%" y="80" class="glitchR">Hello, World! I'm Kevin 👨‍💻</text>
    <text x="50%" y="80" class="glitchL">Hello, World! I'm Kevin 👨‍💻</text>

    <!-- Base Text -->
    <text x="50%" y="80" class="title">Hello, World! I'm Kevin 👨‍💻</text>
  </g>
  <text x="50%" y="125" class="sub1">I push directly to main.</text>
  <text x="50%" y="155" class="sub2">(Just kidding, I use CI/CD pipelines like a responsible adult 🛠️)</text>

</svg>
"""

os.makedirs("assets", exist_ok=True)
with open("assets/header.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("Generated glitch storm header SVG.")
