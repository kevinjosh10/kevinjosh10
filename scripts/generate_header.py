import os

svg_content = """<svg width="800" height="250" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient (Darker stormy sky) -->
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f1624" />
      <stop offset="50%" stop-color="#1a1e36" />
      <stop offset="100%" stop-color="#1e293b" />
    </linearGradient>

    <!-- =============================================
         REALISTIC OCEAN WATER GRADIENTS
         Deep navy depths → dark teal → surface cyan
         ============================================= -->

    <!-- Deepest water layer (ocean floor visible through water) -->
    <linearGradient id="waterDeep" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%"  stop-color="#0c4a6e" stop-opacity="0.95" />
      <stop offset="50%" stop-color="#082f49" stop-opacity="0.98" />
      <stop offset="100%" stop-color="#0a1628" stop-opacity="1"   />
    </linearGradient>

    <!-- Mid-depth water -->
    <linearGradient id="waterMid" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%"  stop-color="#155e75" stop-opacity="0.7"  />
      <stop offset="40%" stop-color="#0e7490" stop-opacity="0.8"  />
      <stop offset="100%" stop-color="#0c4a6e" stop-opacity="0.9" />
    </linearGradient>

    <!-- Surface water (catches sky light) -->
    <linearGradient id="waterSurface" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%"  stop-color="#22d3ee" stop-opacity="0.35" />
      <stop offset="30%" stop-color="#06b6d4" stop-opacity="0.45" />
      <stop offset="100%" stop-color="#0891b2" stop-opacity="0.55" />
    </linearGradient>

    <!-- Foam / whitecap highlight -->
    <linearGradient id="waterFoam" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%"  stop-color="#e0f2fe" stop-opacity="0.6"  />
      <stop offset="30%" stop-color="#bae6fd" stop-opacity="0.35" />
      <stop offset="100%" stop-color="#7dd3fc" stop-opacity="0"   />
    </linearGradient>

    <!-- Surface shimmer (light reflection) -->
    <linearGradient id="waterShimmer" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"  stop-color="#ffffff" stop-opacity="0"    />
      <stop offset="15%" stop-color="#ffffff" stop-opacity="0.08" />
      <stop offset="30%" stop-color="#ffffff" stop-opacity="0"    />
      <stop offset="45%" stop-color="#ffffff" stop-opacity="0.12" />
      <stop offset="60%" stop-color="#ffffff" stop-opacity="0"    />
      <stop offset="75%" stop-color="#ffffff" stop-opacity="0.06" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"   />
    </linearGradient>

    <!-- Soft radial highlight for foam particles -->
    <radialGradient id="foamDot">
      <stop offset="0%"  stop-color="#ffffff" stop-opacity="0.7"  />
      <stop offset="40%" stop-color="#e0f2fe" stop-opacity="0.35" />
      <stop offset="100%" stop-color="#bae6fd" stop-opacity="0"   />
    </radialGradient>

    <!-- Sweeping Spotlight Beam Gradient -->
    <linearGradient id="spotlightGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>

    <!-- =============================================
         SOFT-EDGE CLOUD GRADIENTS (GitHub-safe)
         Each puff uses a radial gradient that fades
         to fully transparent at the edge — no blur
         filters needed. This is the ONLY reliable
         technique for soft clouds on GitHub.
         ============================================= -->

    <!-- Bright puff (upper cloud highlights - muted for storm) -->
    <radialGradient id="puffBright">
      <stop offset="0%"  stop-color="#94a3b8" stop-opacity="1" />
      <stop offset="70%" stop-color="#64748b" stop-opacity="0.95"  />
      <stop offset="90%" stop-color="#475569" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#334155" stop-opacity="0"   />
    </radialGradient>

    <!-- Mid-tone puff (main body - dark slate) -->
    <radialGradient id="puffMid">
      <stop offset="0%"  stop-color="#475569" stop-opacity="1"  />
      <stop offset="75%" stop-color="#334155" stop-opacity="0.95"  />
      <stop offset="95%" stop-color="#1e293b" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#0f172a" stop-opacity="0"   />
    </radialGradient>

    <!-- Dark puff (underbelly / shadow) -->
    <radialGradient id="puffDark">
      <stop offset="0%"  stop-color="#1e293b" stop-opacity="1" />
      <stop offset="75%" stop-color="#0f172a" stop-opacity="0.95" />
      <stop offset="95%" stop-color="#020617" stop-opacity="0.6"  />
      <stop offset="100%" stop-color="#000000" stop-opacity="0"   />
    </radialGradient>

    <!-- Very dark core (deepest shadow) -->
    <radialGradient id="puffDeep">
      <stop offset="0%"  stop-color="#0f172a" stop-opacity="1"  />
      <stop offset="80%" stop-color="#020617" stop-opacity="0.9"  />
      <stop offset="100%" stop-color="#000000" stop-opacity="0"   />
    </radialGradient>

    <!-- White highlight (top-lit puff - very muted) -->
    <radialGradient id="puffWhite">
      <stop offset="0%"  stop-color="#cbd5e1" stop-opacity="0.8" />
      <stop offset="60%" stop-color="#94a3b8" stop-opacity="0.6" />
      <stop offset="90%" stop-color="#64748b" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#475569" stop-opacity="0"   />
    </radialGradient>

    <!-- Subtle wisp (very faint atmosphere) -->
    <radialGradient id="puffWisp">
      <stop offset="0%"  stop-color="#64748b" stop-opacity="0.5"  />
      <stop offset="70%" stop-color="#475569" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#334155" stop-opacity="0"   />
    </radialGradient>
    
    <!-- =============================================
         HEAVY RAIN PATTERN
         ============================================= -->
    <pattern id="rainPattern" x="0" y="0" width="200" height="200" patternUnits="userSpaceOnUse">
      <line x1="20" y1="0" x2="5" y2="30" stroke="#93c5fd" stroke-width="1.5" opacity="0.5" stroke-linecap="round" />
      <line x1="80" y1="50" x2="65" y2="80" stroke="#7dd3fc" stroke-width="1" opacity="0.3" stroke-linecap="round" />
      <line x1="140" y1="20" x2="125" y2="50" stroke="#a5b4fc" stroke-width="2" opacity="0.6" stroke-linecap="round" />
      <line x1="190" y1="120" x2="175" y2="150" stroke="#93c5fd" stroke-width="1.5" opacity="0.4" stroke-linecap="round" />
      <line x1="40" y1="150" x2="25" y2="180" stroke="#7dd3fc" stroke-width="1" opacity="0.4" stroke-linecap="round" />
      <line x1="110" y1="90" x2="95" y2="120" stroke="#a5b4fc" stroke-width="1.5" opacity="0.5" stroke-linecap="round" />
      <line x1="160" y1="170" x2="145" y2="200" stroke="#93c5fd" stroke-width="1" opacity="0.35" stroke-linecap="round" />
      <line x1="60" y1="110" x2="45" y2="140" stroke="#a5b4fc" stroke-width="2" opacity="0.55" stroke-linecap="round" />
    </pattern>

    <!-- =============================================
         CLOUD TYPE A: LARGE CUMULONIMBUS
         Built from ~25 overlapping soft ellipses.
         Bright top, dark underbelly, wispy edges.
         ============================================= -->
    <g id="stormCloud">
      <!-- === ATMOSPHERIC HAZE (outermost layer) === -->
      <ellipse cx="70" cy="35" rx="85" ry="40" fill="url(#puffWisp)" opacity="0.5" />
      <ellipse cx="60" cy="40" rx="90" ry="35" fill="url(#puffWisp)" opacity="0.35" />

      <!-- === DARK UNDERBELLY (bottom layer) === -->
      <ellipse cx="40" cy="52" rx="38" ry="14" fill="url(#puffDeep)" opacity="0.9" />
      <ellipse cx="70" cy="55" rx="45" ry="16" fill="url(#puffDeep)" opacity="0.85" />
      <ellipse cx="100" cy="52" rx="35" ry="13" fill="url(#puffDeep)" opacity="0.8" />
      <ellipse cx="55" cy="50" rx="50" ry="12" fill="url(#puffDark)" opacity="0.7" />
      <ellipse cx="85" cy="48" rx="42" ry="14" fill="url(#puffDark)" opacity="0.65" />

      <!-- === MAIN BODY (mid layer — bulk of the cloud) === -->
      <ellipse cx="30" cy="40" rx="28" ry="18" fill="url(#puffMid)" opacity="0.85" />
      <ellipse cx="55" cy="35" rx="32" ry="22" fill="url(#puffMid)" opacity="0.9" />
      <ellipse cx="80" cy="32" rx="30" ry="20" fill="url(#puffMid)" opacity="0.85" />
      <ellipse cx="105" cy="38" rx="26" ry="16" fill="url(#puffMid)" opacity="0.8" />
      <ellipse cx="45" cy="42" rx="35" ry="16" fill="url(#puffMid)" opacity="0.7" />
      <ellipse cx="90" cy="42" rx="32" ry="15" fill="url(#puffMid)" opacity="0.65" />

      <!-- === UPPER PUFFS (bright tops catch light) === -->
      <ellipse cx="35" cy="28" rx="22" ry="15" fill="url(#puffBright)" opacity="0.9" />
      <ellipse cx="58" cy="22" rx="26" ry="17" fill="url(#puffBright)" opacity="0.95" />
      <ellipse cx="82" cy="20" rx="24" ry="16" fill="url(#puffBright)" opacity="0.9" />
      <ellipse cx="100" cy="26" rx="20" ry="13" fill="url(#puffBright)" opacity="0.8" />
      <ellipse cx="48" cy="26" rx="18" ry="12" fill="url(#puffBright)" opacity="0.7" />
      <ellipse cx="72" cy="24" rx="20" ry="14" fill="url(#puffBright)" opacity="0.75" />

      <!-- === WHITE HIGHLIGHTS (light catches top edges) === -->
      <ellipse cx="50" cy="16" rx="16" ry="10" fill="url(#puffWhite)" opacity="0.9" />
      <ellipse cx="72" cy="14" rx="14" ry="9"  fill="url(#puffWhite)" opacity="0.85" />
      <ellipse cx="38" cy="20" rx="12" ry="8"  fill="url(#puffWhite)" opacity="0.7" />
      <ellipse cx="90" cy="18" rx="13" ry="8"  fill="url(#puffWhite)" opacity="0.65" />

      <!-- === WISPY EDGES (feathered dissolve into sky) === -->
      <ellipse cx="8"   cy="44" rx="16" ry="10" fill="url(#puffWisp)" opacity="0.6" />
      <ellipse cx="125" cy="40" rx="14" ry="10" fill="url(#puffWisp)" opacity="0.5" />
      <ellipse cx="15"  cy="36" rx="12" ry="8"  fill="url(#puffWisp)" opacity="0.4" />
      <ellipse cx="118" cy="34" rx="11" ry="7"  fill="url(#puffWisp)" opacity="0.35" />
    </g>

    <!-- =============================================
         CLOUD TYPE B: MEDIUM STORM CLOUD
         ============================================= -->
    <g id="stormCloudB">
      <!-- Haze -->
      <ellipse cx="52" cy="30" rx="62" ry="30" fill="url(#puffWisp)" opacity="0.4" />
      <!-- Dark base -->
      <ellipse cx="35" cy="44" rx="30" ry="11" fill="url(#puffDeep)" opacity="0.8" />
      <ellipse cx="60" cy="46" rx="35" ry="12" fill="url(#puffDeep)" opacity="0.75" />
      <ellipse cx="80" cy="44" rx="25" ry="10" fill="url(#puffDark)" opacity="0.7" />
      <!-- Body -->
      <ellipse cx="30" cy="34" rx="24" ry="15" fill="url(#puffMid)" opacity="0.85" />
      <ellipse cx="55" cy="30" rx="28" ry="18" fill="url(#puffMid)" opacity="0.9" />
      <ellipse cx="78" cy="32" rx="22" ry="14" fill="url(#puffMid)" opacity="0.8" />
      <ellipse cx="42" cy="36" rx="26" ry="13" fill="url(#puffMid)" opacity="0.65" />
      <!-- Bright tops -->
      <ellipse cx="38" cy="22" rx="18" ry="12" fill="url(#puffBright)" opacity="0.9" />
      <ellipse cx="58" cy="18" rx="20" ry="14" fill="url(#puffBright)" opacity="0.95" />
      <ellipse cx="76" cy="22" rx="16" ry="11" fill="url(#puffBright)" opacity="0.8" />
      <!-- Highlights -->
      <ellipse cx="50" cy="12" rx="12" ry="8"  fill="url(#puffWhite)" opacity="0.85" />
      <ellipse cx="66" cy="14" rx="10" ry="7"  fill="url(#puffWhite)" opacity="0.7" />
      <!-- Wispy edges -->
      <ellipse cx="8"  cy="38" rx="12" ry="8"  fill="url(#puffWisp)" opacity="0.5" />
      <ellipse cx="96" cy="36" rx="10" ry="7"  fill="url(#puffWisp)" opacity="0.4" />
    </g>

    <!-- =============================================
         CLOUD TYPE C: SMALL WISPY CLOUD
         ============================================= -->
    <g id="stormCloudC">
      <!-- Haze -->
      <ellipse cx="35" cy="24" rx="42" ry="20" fill="url(#puffWisp)" opacity="0.35" />
      <!-- Dark base -->
      <ellipse cx="30" cy="34" rx="24" ry="8"  fill="url(#puffDark)" opacity="0.65" />
      <ellipse cx="50" cy="32" rx="20" ry="7"  fill="url(#puffDark)" opacity="0.55" />
      <!-- Body -->
      <ellipse cx="25" cy="26" rx="18" ry="11" fill="url(#puffMid)" opacity="0.8" />
      <ellipse cx="45" cy="24" rx="20" ry="12" fill="url(#puffMid)" opacity="0.85" />
      <ellipse cx="60" cy="26" rx="14" ry="10" fill="url(#puffMid)" opacity="0.7" />
      <!-- Bright tops -->
      <ellipse cx="32" cy="18" rx="14" ry="9"  fill="url(#puffBright)" opacity="0.85" />
      <ellipse cx="48" cy="16" rx="16" ry="10" fill="url(#puffBright)" opacity="0.9" />
      <!-- Highlights -->
      <ellipse cx="42" cy="12" rx="10" ry="6"  fill="url(#puffWhite)" opacity="0.75" />
      <!-- Wisps -->
      <ellipse cx="6"  cy="28" rx="10" ry="6"  fill="url(#puffWisp)" opacity="0.45" />
      <ellipse cx="70" cy="26" rx="8"  ry="5"  fill="url(#puffWisp)" opacity="0.35" />
    </g>

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

    <!-- =============================================
         MARINE LIFE SVG DEFINITIONS
         ============================================= -->

    <!-- Shark Dorsal Fin (Realistic swept-back curve with water wake) -->
    <g id="sharkFin">
      <!-- Trailing wake -->
      <ellipse cx="45" cy="20" rx="15" ry="3" fill="#bae6fd" opacity="0.4" />
      <ellipse cx="35" cy="20" rx="10" ry="2" fill="#e0f2fe" opacity="0.5" />
      <!-- Main fin -->
      <path d="M0,20 C10,10 15,-15 25,-20 C27,-21 30,-19 28,-15 C25,-5 20,10 40,20 Z" fill="#1e293b" />
      <!-- Light edge (trailing edge) -->
      <path d="M25,-20 C27,-21 30,-19 28,-15 C25,-5 20,10 40,20 C30,10 27,-10 25,-20 Z" fill="#334155" opacity="0.7" />
      <!-- Dark shadow side (leading edge/base) -->
      <path d="M0,20 C10,10 15,-15 25,-20 C23,-15 15,5 10,20 Z" fill="#0f172a" opacity="0.6" />
      <!-- Bow wave (front push) -->
      <ellipse cx="-5" cy="20" rx="8" ry="2" fill="#e0f2fe" opacity="0.6" />
      <path d="M-10,20 Q-5,16 5,20" fill="none" stroke="#f8fafc" stroke-width="1.5" opacity="0.5" />
    </g>

    <linearGradient id="skyBlueGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7dd3fc">
        <animate attributeName="stop-color" values="#7dd3fc;#0ea5e9;#00f2fe;#7dd3fc" dur="4s" repeatCount="indefinite" />
      </stop>
      <stop offset="50%" stop-color="#0ea5e9">
        <animate attributeName="stop-color" values="#0ea5e9;#00f2fe;#7dd3fc;#0ea5e9" dur="4s" repeatCount="indefinite" />
      </stop>
      <stop offset="100%" stop-color="#00f2fe">
        <animate attributeName="stop-color" values="#00f2fe;#7dd3fc;#0ea5e9;#00f2fe" dur="4s" repeatCount="indefinite" />
      </stop>
    </linearGradient>
    <style>
      .title { fill: url(#skyBlueGradient); font-family: 'Consolas', 'Menlo', 'Monaco', 'Ubuntu Mono', monospace; font-size: 44px; font-weight: 900; text-anchor: middle; letter-spacing: -0.5px; animation: neonFlow 3s ease-in-out infinite alternate; }
      @keyframes neonFlow {
        0% { filter: drop-shadow(0 0 8px rgba(14,165,233,0.5)); opacity: 0.9; }
        100% { filter: drop-shadow(0 0 15px rgba(0,242,254,1)) drop-shadow(0 0 30px rgba(14,165,233,0.8)); opacity: 1; }
      }
      .sub1 { fill: #ffd700; filter: url(#shadow); font-family: 'Consolas', 'Menlo', 'Monaco', 'Ubuntu Mono', monospace; font-size: 24px; font-weight: 700; text-anchor: middle; animation: fadeIn 0.5s ease-out 5s forwards; opacity: 0; letter-spacing: 0.5px; }
      .sub2 { fill: #f7fafc; filter: url(#shadow); font-family: 'Consolas', 'Menlo', 'Monaco', 'Ubuntu Mono', monospace; font-size: 16px; font-style: italic; font-weight: 500; text-anchor: middle; animation: fadeIn 0.5s ease-out 5.4s forwards; opacity: 0; }
      
      @keyframes fadeIn {
        from { opacity: 0; transform: translateY(5px); }
        to { opacity: 1; transform: translateY(0); }
      }

      /* === DECRYPT ANIMATION (5s FAST TWITCHING) === */
            .decryptText { fill: url(#skyBlueGradient); filter: drop-shadow(0 0 5px rgba(0,242,254,0.8)); font-family: 'Consolas', 'Menlo', 'Monaco', 'Ubuntu Mono', monospace; font-size: 44px; font-weight: 900; text-anchor: middle; letter-spacing: 0px; opacity: 0; }
      .dec1 { animation: cycle 3.0s infinite; animation-delay: 0.00s; }
      .dec2 { animation: cycle 3.0s infinite; animation-delay: 0.10s; }
      .dec3 { animation: cycle 3.0s infinite; animation-delay: 0.20s; }
      .dec4 { animation: cycle 3.0s infinite; animation-delay: 0.30s; }
      .dec5 { animation: cycle 3.0s infinite; animation-delay: 0.40s; }
      .dec6 { animation: cycle 3.0s infinite; animation-delay: 0.50s; }
      .dec7 { animation: cycle 3.0s infinite; animation-delay: 0.60s; }
      .dec8 { animation: cycle 3.0s infinite; animation-delay: 0.70s; }
      .dec9 { animation: cycle 3.0s infinite; animation-delay: 0.80s; }
      .dec10 { animation: cycle 3.0s infinite; animation-delay: 0.90s; }
      .dec11 { animation: cycle 3.0s infinite; animation-delay: 1.00s; }
      .dec12 { animation: cycle 3.0s infinite; animation-delay: 1.10s; }
      .dec13 { animation: cycle 3.0s infinite; animation-delay: 1.20s; }
      .dec14 { animation: cycle 3.0s infinite; animation-delay: 1.30s; }
      .dec15 { animation: cycle 3.0s infinite; animation-delay: 1.40s; }
      .dec16 { animation: cycle 3.0s infinite; animation-delay: 1.50s; }
      .dec17 { animation: cycle 3.0s infinite; animation-delay: 1.60s; }
      .dec18 { animation: cycle 3.0s infinite; animation-delay: 1.70s; }
      .dec19 { animation: cycle 3.0s infinite; animation-delay: 1.80s; }
      .dec20 { animation: cycle 3.0s infinite; animation-delay: 1.90s; }
      .dec21 { animation: cycle 3.0s infinite; animation-delay: 2.00s; }
      .dec22 { animation: cycle 3.0s infinite; animation-delay: 2.10s; }
      .dec23 { animation: cycle 3.0s infinite; animation-delay: 2.20s; }
      .dec24 { animation: cycle 3.0s infinite; animation-delay: 2.30s; }
      .dec25 { animation: cycle 3.0s infinite; animation-delay: 2.40s; }
      .dec26 { animation: cycle 3.0s infinite; animation-delay: 2.50s; }
      .dec27 { animation: cycle 3.0s infinite; animation-delay: 2.60s; }
      .dec28 { animation: cycle 3.0s infinite; animation-delay: 2.70s; }
      .dec29 { animation: cycle 3.0s infinite; animation-delay: 2.80s; }
      .dec30 { animation: cycle 3.0s infinite; animation-delay: 2.90s; }

      @keyframes cycle { 0%, 3.3% { opacity: 1; } 3.4%, 100% { opacity: 0; } }

      .decryptWrapper { animation: hideWrapper 3s forwards; }
      @keyframes hideWrapper { 0%, 99.9% { opacity: 1; } 100% { opacity: 0; } }

      .finalReveal { animation: showFinal 3s forwards; opacity: 0; }
      @keyframes showFinal { 0%, 99.9% { opacity: 0; } 100% { opacity: 1; } }

      /* PROVEN: Infinite moving animations using ONLY translateX */
      /* Realistic water wave layers at different speeds (parallax depth) */
      .waterBase  { animation: moveLeft 25s linear infinite; }
      .waterMid1  { animation: moveLeft 18s linear infinite; }
      .waterMid2  { animation: moveLeft 14s linear infinite; }
      .waterSurf1 { animation: moveLeft 10s linear infinite; }
      .waterSurf2 { animation: moveLeft 8s linear infinite; }
      .waterFoam1 { animation: moveLeft 7s linear infinite; }
      .waterFoam2 { animation: moveLeft 9s linear infinite; }
      .waterShim  { animation: moveLeft 20s linear infinite; }
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



      /* === HEAVY RAIN FALLING === */
      .heavyRain1 { animation: fallRain 0.6s linear infinite; }
      .heavyRain2 { animation: fallRain 0.8s linear infinite; }
      .heavyRain3 { animation: fallRain 1.1s linear infinite; }

      @keyframes fallRain {
        0% { transform: translateY(-200px); }
        100% { transform: translateY(0px); }
      }

      /* === RAIN SPLASHES ON WATER === */
      .splashCircle {
        animation: ripple 0.6s linear infinite;
      }
      .del0 { animation-delay: 0.0s; }
      .del1 { animation-delay: 0.1s; }
      .del2 { animation-delay: 0.2s; }
      .del3 { animation-delay: 0.3s; }
      .del4 { animation-delay: 0.4s; }
      .del5 { animation-delay: 0.5s; }

      @keyframes ripple {
        0% { transform: scale(0.2); opacity: 0.8; }
        100% { transform: scale(2.5); opacity: 0; }
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

      /* === HOVER EASTER EGG === */
      .easterEgg {
        opacity: 0;
        fill: #f8fafc;
        font-size: 22px;
        font-family: monospace;
        font-weight: bold;
        text-anchor: middle;
        transition: opacity 0.5s ease;
        pointer-events: none;
        filter: drop-shadow(0px 0px 8px #93c5fd);
      }
      svg:hover .easterEgg {
        opacity: 1;
      }
      svg:hover .lightning {
        animation-duration: 0.6s !important;
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

      /* =============================================
         SHARK FIN ANIMATIONS (Slow Surface Patrol)
         Fins stay on the surface, moving slowly, and
         smoothly turn around at the edges.
         ============================================= */

      .sharkFin1 {
        animation: finPatrol1 30s linear infinite;
        transform-origin: 20px 20px;
      }
      @keyframes finPatrol1 {
        /* Swim left: Start at x=430 */
        0%   { transform: translate(430px, 191px) scaleX(1); opacity: 0.9; }
        45%  { transform: translate(150px, 191px) scaleX(1); opacity: 0.9; }
        /* Turn around */
        50%  { transform: translate(130px, 191px) scaleX(-1); opacity: 0.9; }
        /* Swim right */
        95%  { transform: translate(410px, 191px) scaleX(-1); opacity: 0.9; }
        /* Turn around */
        100% { transform: translate(430px, 191px) scaleX(1); opacity: 0.9; }
      }

      .sharkFin2 {
        animation: finPatrol2 36s linear infinite;
        animation-delay: -12s;
        transform-origin: 20px 20px;
      }
      @keyframes finPatrol2 {
        /* Swim left: Start at x=700 */
        0%   { transform: translate(700px, 194px) scaleX(1); opacity: 0.85; }
        45%  { transform: translate(300px, 194px) scaleX(1); opacity: 0.85; }
        /* Turn around */
        50%  { transform: translate(280px, 194px) scaleX(-1); opacity: 0.85; }
        /* Swim right */
        95%  { transform: translate(680px, 194px) scaleX(-1); opacity: 0.85; }
        /* Turn around */
        100% { transform: translate(700px, 194px) scaleX(1); opacity: 0.85; }
      }

      .sharkFin3 {
        animation: finPatrol3 26s linear infinite;
        animation-delay: -5s;
        transform-origin: 20px 20px;
      }
      @keyframes finPatrol3 {
        /* Swim left: Start at x=850 (far right) */
        0%   { transform: translate(850px, 196px) scale(0.85, 0.85); opacity: 0.8; }
        45%  { transform: translate(450px, 196px) scale(0.85, 0.85); opacity: 0.8; }
        /* Turn around */
        50%  { transform: translate(430px, 196px) scale(-0.85, 0.85); opacity: 0.8; }
        /* Swim right */
        95%  { transform: translate(830px, 196px) scale(-0.85, 0.85); opacity: 0.8; }
        /* Turn around */
        100% { transform: translate(850px, 196px) scale(0.85, 0.85); opacity: 0.8; }
      }

      .sharkFin4 {
        animation: finPatrol4 42s linear infinite;
        animation-delay: -20s;
        transform-origin: 20px 20px;
      }
      @keyframes finPatrol4 {
        /* Swim left: Start at x=350 */
        0%   { transform: translate(350px, 189px) scale(0.7, 0.7); opacity: 0.7; }
        45%  { transform: translate(-50px, 189px) scale(0.7, 0.7); opacity: 0.7; }
        /* Turn around */
        50%  { transform: translate(-70px, 189px) scale(-0.7, 0.7); opacity: 0.7; }
        /* Swim right */
        95%  { transform: translate(330px, 189px) scale(-0.7, 0.7); opacity: 0.7; }
        /* Turn around */
        100% { transform: translate(350px, 189px) scale(0.7, 0.7); opacity: 0.7; }
      }

      /* === GLITCH / HACKER TEXT EFFECT (RGB channel split) === */
      .glitchR {
        animation: glitchRight 3s steps(1, end) infinite;
        fill: url(#skyBlueGradient);
        font-family: 'Consolas', 'Menlo', 'Monaco', 'Ubuntu Mono', monospace;
        font-size: 44px;
        font-weight: 900;
        text-anchor: middle;
        filter: drop-shadow(0 0 5px rgba(0,242,254,0.8));
      }
      .glitchL {
        animation: glitchLeft 3s steps(1, end) infinite;
        fill: url(#skyBlueGradient);
        font-family: 'Consolas', 'Menlo', 'Monaco', 'Ubuntu Mono', monospace;
        font-size: 44px;
        font-weight: 900;
        text-anchor: middle;
        filter: drop-shadow(0 0 5px rgba(14,165,233,0.8));
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
      .neonServer { 
        animation: neonServerPulse 3s ease-in-out infinite;
        transform-origin: center;
      }
      .neonBlink1 { animation: blinkLED 1s infinite alternate; }
      .neonBlink2 { animation: blinkLED 1.5s infinite alternate; animation-delay: 0.3s; }
      .neonBlink3 { animation: blinkLED 0.8s infinite alternate; animation-delay: 0.7s; }
      @keyframes blinkLED { 0% { opacity: 0.3; } 100% { opacity: 1; } }
      @keyframes neonServerPulse {
        0%, 100% { filter: drop-shadow(0 0 2px #00f2fe) brightness(1); }
        50% { filter: drop-shadow(0 0 8px #00f2fe) brightness(1.2); }
      }
    </style>
  </defs>
  
  <rect width="100%" height="100%" fill="transparent" rx="15px" />
  
  <clipPath id="clipBox">
    <rect width="100%" height="100%" rx="15px" />
  </clipPath>
  
  <g clip-path="url(#clipBox)">
    
    <!-- Ambient Sky Flash (lights up the whole sky during lightning) -->
    <rect width="100%" height="100%" fill="#c4b5fd" class="skyFlash skyFlash1" />
    <rect width="100%" height="100%" fill="#93c5fd" class="skyFlash skyFlash2" />

    <!-- Sweeping Spotlight Beam (Using proven translateX) -->
    <polygon points="100,-50 300,-50 150,300 -50,300" fill="url(#spotlightGrad)" class="spotlight" />

    <!-- === HEAVY RAIN STREAKS (Endless looping layers) === -->
    <rect x="-100" y="-200" width="1000" height="600" fill="url(#rainPattern)" class="heavyRain1" />
    <rect x="-150" y="-300" width="1000" height="600" fill="url(#rainPattern)" class="heavyRain2" opacity="0.8" />
    <rect x="-50" y="-250" width="1000" height="600" fill="url(#rainPattern)" class="heavyRain3" opacity="0.6" />

    <!-- === REALISTIC STORM CLOUD LAYERS === -->
    <!-- Back layer: distant, softer, slower (clouds2 class) -->
    <g class="clouds2" opacity="0.75">
      <use href="#stormCloudC" transform="translate(100, 18) scale(1.4)" />
      <use href="#stormCloudB" transform="translate(350, 8) scale(1.0)" />
      <use href="#stormCloudC" transform="translate(580, 25) scale(1.6)" />
      <use href="#stormCloudB" transform="translate(750, 2) scale(0.9)" />
      <use href="#stormCloudC" transform="translate(900, 18) scale(1.4)" />
      <use href="#stormCloudB" transform="translate(1150, 8) scale(1.0)" />
      <use href="#stormCloudC" transform="translate(1380, 25) scale(1.6)" />
      <use href="#stormCloudB" transform="translate(1550, 2) scale(0.9)" />
    </g>

    <!-- Front layer: larger, closer, more detailed (clouds class) -->
    <g class="clouds" opacity="1.0">
      <use href="#stormCloud" transform="translate(30, -10) scale(1.0)" />
      <use href="#stormCloudB" transform="translate(220, 5) scale(1.1)" />
      <use href="#stormCloud" transform="translate(380, -5) scale(1.3)" />
      <use href="#stormCloudC" transform="translate(560, -15) scale(1.5)" />
      <use href="#stormCloud" transform="translate(680, 0) scale(0.9)" />
      <use href="#stormCloud" transform="translate(830, -10) scale(1.0)" />
      <use href="#stormCloudB" transform="translate(1020, 5) scale(1.1)" />
      <use href="#stormCloud" transform="translate(1180, -5) scale(1.3)" />
      <use href="#stormCloudC" transform="translate(1360, -15) scale(1.5)" />
      <use href="#stormCloud" transform="translate(1480, 0) scale(0.9)" />
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




    <!-- =============================================
         REALISTIC OCEAN WATER
         7 layers creating depth: base → mid → surface → foam → shimmer
         Each layer has organic curves, different speeds, and overlapping
         translucency to simulate light refracting through water.
         ============================================= -->

    <!-- LAYER 1: Deep ocean base (slowest, darkest — the "floor") -->
    <path class="waterBase" d="M0,185 C40,178 80,192 120,185 C160,178 200,195 240,188 C280,181 320,193 360,186 C400,179 440,194 480,187 C520,180 560,192 600,185 C640,178 680,194 720,187 C760,180 800,192 840,185 C880,178 920,194 960,187 C1000,180 1040,192 1080,185 C1120,178 1160,194 1200,187 C1240,180 1280,193 1320,186 C1360,179 1400,194 1440,187 C1480,180 1520,192 1560,185 L1600,185 L1600,260 L0,260 Z" fill="url(#waterDeep)" />

    <!-- LAYER 2: Mid-depth water 1 (subtle undulation) -->
    <path class="waterMid1" d="M0,195 C50,188 90,202 140,195 C190,188 230,205 280,198 C330,191 370,204 420,197 C470,190 510,206 560,199 C610,192 650,205 700,198 C750,191 790,206 840,199 C890,192 930,205 980,198 C1030,191 1070,206 1120,199 C1170,192 1210,205 1260,198 C1310,191 1350,206 1400,199 C1450,192 1490,205 1540,198 L1600,198 L1600,260 L0,260 Z" fill="url(#waterMid)" opacity="0.85" />

    <!-- LAYER 3: Mid-depth water 2 (counter-rhythm for natural feel) -->
    <path class="waterMid2" d="M0,200 C35,206 75,194 110,200 C145,206 185,193 220,199 C255,205 295,193 330,199 C365,205 405,192 440,198 C475,204 515,193 550,199 C585,205 625,192 660,198 C695,204 735,193 770,199 C805,205 845,192 880,198 C915,204 955,193 990,199 C1025,205 1065,192 1100,198 C1135,204 1175,193 1210,199 C1245,205 1285,192 1320,198 C1355,204 1395,193 1430,199 C1465,205 1505,192 1540,198 L1600,198 L1600,260 L0,260 Z" fill="url(#waterMid)" opacity="0.6" />

    <!-- LAYER 4: Surface water 1 (brighter, catches reflected sky) -->
    <path class="waterSurf1" d="M0,208 C30,202 60,214 100,208 C140,202 170,216 210,210 C250,204 280,215 320,209 C360,203 390,216 430,210 C470,204 500,215 540,209 C580,203 610,216 650,210 C690,204 720,215 760,209 C800,203 830,216 870,210 C910,204 940,215 980,209 C1020,203 1050,216 1090,210 C1130,204 1160,215 1200,209 C1240,203 1270,216 1310,210 C1350,204 1380,215 1420,209 C1460,203 1490,216 1530,210 L1600,210 L1600,260 L0,260 Z" fill="url(#waterSurface)" opacity="0.9" />

    <!-- LAYER 5: Surface water 2 (fastest visible ripples) -->
    <path class="waterSurf2" d="M0,215 C25,210 50,220 80,215 C110,210 135,222 165,217 C195,212 220,222 250,217 C280,212 305,223 335,218 C365,213 390,222 420,217 C450,212 475,223 505,218 C535,213 560,222 590,217 C620,212 645,223 675,218 C705,213 730,222 760,217 C790,212 815,223 845,218 C875,213 900,222 930,217 C960,212 985,223 1015,218 C1045,213 1070,222 1100,217 C1130,212 1155,223 1185,218 C1215,213 1240,222 1270,217 C1300,212 1325,223 1355,218 C1385,213 1410,222 1440,217 C1470,212 1495,223 1525,218 L1600,218 L1600,260 L0,260 Z" fill="url(#waterSurface)" opacity="0.5" />

    <!-- LAYER 6: Foam / whitecap crests (thin bright lines on wave peaks) -->
    <path class="waterFoam1" d="M0,206 C20,203 40,208 65,205 C90,202 110,210 140,207 C170,204 190,211 220,208 C250,205 270,212 300,209 C330,206 350,212 380,209 C410,206 430,213 460,210 C490,207 510,213 540,210 C570,207 590,213 620,210 C650,207 670,213 700,210 C730,207 750,214 780,211 C810,208 830,214 860,211 C890,208 910,214 940,211 C970,208 990,214 1020,211 C1050,208 1070,214 1100,211 C1130,208 1150,214 1180,211 C1210,208 1230,214 1260,211 C1290,208 1310,215 1340,212 C1370,209 1390,214 1420,211 C1450,208 1470,214 1500,211 C1530,208 1550,214 1580,211 L1600,211 L1600,216 L0,216 Z" fill="url(#waterFoam)" opacity="0.7" />

    <path class="waterFoam2" d="M0,212 C15,209 35,215 55,212 C75,209 95,216 120,213 C145,210 165,217 190,214 C215,211 235,217 260,214 C285,211 305,218 330,215 C355,212 375,218 400,215 C425,212 445,219 470,216 C495,213 515,219 540,216 C565,213 585,219 610,216 C635,213 655,220 680,217 C705,214 725,220 750,217 C775,214 795,220 820,217 C845,214 865,220 890,217 C915,214 935,221 960,218 C985,215 1005,221 1030,218 C1055,215 1075,221 1100,218 C1125,215 1145,221 1170,218 C1195,215 1215,222 1240,219 C1265,216 1285,222 1310,219 C1335,216 1355,222 1380,219 C1405,216 1425,222 1450,219 C1475,216 1495,222 1520,219 C1545,216 1565,222 1590,219 L1600,219 L1600,222 L0,222 Z" fill="url(#waterFoam)" opacity="0.45" />

    <!-- LAYER 7: Surface shimmer (scattered light reflections) -->
    <rect class="waterShim" x="0" y="200" width="1600" height="25" fill="url(#waterShimmer)" opacity="0.4" />

    <!-- Foam particle dots (scattered across wave surface) -->
    <ellipse cx="120" cy="210" rx="4" ry="2" fill="url(#foamDot)" opacity="0.6" />
    <ellipse cx="280" cy="212" rx="3" ry="1.5" fill="url(#foamDot)" opacity="0.5" />
    <ellipse cx="390" cy="208" rx="5" ry="2" fill="url(#foamDot)" opacity="0.55" />
    <ellipse cx="510" cy="214" rx="3" ry="1.5" fill="url(#foamDot)" opacity="0.45" />
    <ellipse cx="620" cy="209" rx="4" ry="2" fill="url(#foamDot)" opacity="0.5" />
    <ellipse cx="740" cy="213" rx="3" ry="1.5" fill="url(#foamDot)" opacity="0.4" />
    <ellipse cx="180" cy="215" rx="2" ry="1" fill="url(#foamDot)" opacity="0.35" />
    <ellipse cx="450" cy="211" rx="3" ry="1.5" fill="url(#foamDot)" opacity="0.5" />
    <ellipse cx="580" cy="216" rx="2" ry="1" fill="url(#foamDot)" opacity="0.3" />
    <ellipse cx="700" cy="210" rx="4" ry="2" fill="url(#foamDot)" opacity="0.45" />

    <!-- === RAIN SPLASHES ON WATER SURFACE === -->
    <g class="splashes" opacity="0.6">
      <g transform="translate(40, 205)"><ellipse class="splashCircle del0" cx="0" cy="0" rx="3" ry="1" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(150, 212)"><ellipse class="splashCircle del3" cx="0" cy="0" rx="4" ry="1.5" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(280, 208)"><ellipse class="splashCircle del1" cx="0" cy="0" rx="3" ry="1" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(390, 215)"><ellipse class="splashCircle del4" cx="0" cy="0" rx="2" ry="0.5" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(510, 206)"><ellipse class="splashCircle del2" cx="0" cy="0" rx="3" ry="1" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(640, 218)"><ellipse class="splashCircle del5" cx="0" cy="0" rx="3" ry="1" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(750, 210)"><ellipse class="splashCircle del0" cx="0" cy="0" rx="4" ry="1.5" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(85, 216)"><ellipse class="splashCircle del3" cx="0" cy="0" rx="3" ry="1" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(220, 207)"><ellipse class="splashCircle del1" cx="0" cy="0" rx="3" ry="1" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(330, 214)"><ellipse class="splashCircle del4" cx="0" cy="0" rx="4" ry="1.5" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(460, 205)"><ellipse class="splashCircle del2" cx="0" cy="0" rx="3" ry="1" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(580, 211)"><ellipse class="splashCircle del5" cx="0" cy="0" rx="2" ry="0.5" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(710, 217)"><ellipse class="splashCircle del0" cx="0" cy="0" rx="4" ry="1.5" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(190, 209)"><ellipse class="splashCircle del2" cx="0" cy="0" rx="3" ry="1" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(410, 213)"><ellipse class="splashCircle del4" cx="0" cy="0" rx="3" ry="1" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(540, 208)"><ellipse class="splashCircle del1" cx="0" cy="0" rx="2" ry="0.5" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(680, 206)"><ellipse class="splashCircle del5" cx="0" cy="0" rx="4" ry="1.5" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
      <g transform="translate(780, 215)"><ellipse class="splashCircle del3" cx="0" cy="0" rx="3" ry="1" fill="none" stroke="#e0f2fe" stroke-width="0.8"/></g>
    </g>

    <!-- =============================================
         MARINE LIFE: SHARK FINS
         Placed between water layers for depth.
         ============================================= -->

    <!-- Shark Fin 1: Patrols left side -->
    <g class="sharkFin1">
      <use href="#sharkFin" />
    </g>

    <!-- Shark Fin 2: Patrols right side -->
    <g class="sharkFin2">
      <use href="#sharkFin" />
    </g>

    <!-- Shark Fin 3: Far right, slightly smaller -->
    <g class="sharkFin3">
      <use href="#sharkFin" />
    </g>

    <!-- Shark Fin 4: Deep background left, very slow and small -->
    <g class="sharkFin4">
      <use href="#sharkFin" />
    </g>

  </g>
  
  <!-- === NEON GLOWING BORDER (replaces boring grey) === -->
  <rect width="99%" height="98%" x="4" y="2" fill="none" stroke="url(#neonBorder)" stroke-width="1.5" rx="15px" filter="url(#neonGlow)" class="neonBorderRect" />
  
  <!-- === HACKER DECRYPT SEQUENCE (3s RANDOM SHUFFLE) === -->
  <g class="decryptWrapper">
    <text x="50%" y="80" class="decryptText dec1">?x?t=ju)&*_!;@HY&Zp9-|r</text>
    <text x="50%" y="80" class="decryptText dec2">}1U[}AjHdku<tv>i];:!sch</text>
    <text x="50%" y="80" class="decryptText dec3">Mmgfr3OXzr1+KGX-C^NHtTE</text>
    <text x="50%" y="80" class="decryptText dec4">i5(&VY=x_S?#>YMu^I1qH2C</text>
    <text x="50%" y="80" class="decryptText dec5">>i3@2X>?8tKctZUB:YzBm*;</text>
    <text x="50%" y="80" class="decryptText dec6">SufMPXdpS#fD+#{DX;ox]z,</text>
    <text x="50%" y="80" class="decryptText dec7">_}%bzY%[+X5(_0|NcUIK-9Z</text>
    <text x="50%" y="80" class="decryptText dec8">18Z_mk.g?wDKETMy]OuADow</text>
    <text x="50%" y="80" class="decryptText dec9">y-*$t3oCtJE-JpC?U8uJ}W6</text>
    <text x="50%" y="80" class="decryptText dec10">&v_dA*NY}(2:qoe;Nka1&Tr</text>
    <text x="50%" y="80" class="decryptText dec11">:CNM}Zq-fd1BZ;hF+j&OQ<<</text>
    <text x="50%" y="80" class="decryptText dec12">zG[02]<vOwr#D-X+=Rf0$Zj</text>
    <text x="50%" y="80" class="decryptText dec13">3=9&vzv<N#t:p9a4WB|Wfm}</text>
    <text x="50%" y="80" class="decryptText dec14">}qN]x1Q{-s8o)27}/V4KZ(#</text>
    <text x="50%" y="80" class="decryptText dec15">a-*8xkWJUjLgPp1J-faF,|*</text>
    <text x="50%" y="80" class="decryptText dec16">aG;ouEKi{U|cBa._q^O(]]w</text>
    <text x="50%" y="80" class="decryptText dec17">v.:N3|-m#5f)JYh$ixYH4Te</text>
    <text x="50%" y="80" class="decryptText dec18">!Fn9H:lcr!D/ne=0Utf&lr%</text>
    <text x="50%" y="80" class="decryptText dec19">IhrIaW!|DQA*o^lQI9[OTMb</text>
    <text x="50%" y="80" class="decryptText dec20">?xmxgSw>OxRFJLvab60rDZR</text>
    <text x="50%" y="80" class="decryptText dec21">]#1*8PQd@Ov=^w&Qa[Qh$7s</text>
    <text x="50%" y="80" class="decryptText dec22">cH#*TlD_T/RwK;^<u&MOBY+</text>
    <text x="50%" y="80" class="decryptText dec23">(GR?bhmEaJD>.Z-<1E.E#Ld</text>
    <text x="50%" y="80" class="decryptText dec24">XxHV0xhiyorZ7&Od|&w*F?T</text>
    <text x="50%" y="80" class="decryptText dec25">lo(AB42Ej=3KGq]|Se*){4I</text>
    <text x="50%" y="80" class="decryptText dec26">4Ogd<=HlnAj:Qp!_l,uwDx)</text>
    <text x="50%" y="80" class="decryptText dec27">0k5W[rbeSBEUnY#@17r{!vy</text>
    <text x="50%" y="80" class="decryptText dec28">,tzN@Wz+n:{dlHFR(|/H1<L</text>
    <text x="50%" y="80" class="decryptText dec29">y*3lL4zu6AIHiyp1@p,,Ke?</text>
    <text x="50%" y="80" class="decryptText dec30">T5LeJ4Z^/qfAbuXPDL&@sCD</text>
  </g>

  <g class="finalReveal">
    <!-- === GLITCH GHOST COPIES (RGB split behind main text) === -->
    <text x="46%" y="80" class="glitchR">Hello, World! I'm Kevin</text>
    <text x="46%" y="80" class="glitchL">Hello, World! I'm Kevin</text>

    <!-- Base Text -->
    <text x="46%" y="80" class="title">Hello, World! I'm Kevin</text>
        <g class="neonServer" transform="translate(18, 0)">
      <rect x="648" y="32" width="34" height="46" rx="4" fill="none" stroke="#00f2fe" stroke-width="2" />
      
      <rect x="652" y="36" width="26" height="10" rx="2" fill="none" stroke="#00f2fe" stroke-width="1.5" />
      <line x1="656" y1="41" x2="662" y2="41" stroke="#00f2fe" stroke-width="1.5" />
      <circle cx="672" cy="41" r="1.5" fill="#39ff14" class="neonBlink1" />
      
      <!-- Cloud Symbol in Middle -->
      <g transform="translate(658, 49) scale(0.6)">
        <path d="M19.7,11.4c0-4.3-3.5-7.8-7.8-7.8c-2.3,0-4.4,1-5.8,2.7C5.3,5.5,4,5.1,2.5,5.1C-0.3,5.1-2.5,7.3-2.5,10.2 c0,2.8,2.3,5.1,5.1,5.1h14.7c1.4,0,2.5-1.1,2.5-2.5C19.8,12.5,19.7,11.4,19.7,11.4z" fill="none" stroke="#fbbf24" stroke-width="2.5" />
      </g>
      
      <rect x="652" y="64" width="26" height="10" rx="2" fill="none" stroke="#00f2fe" stroke-width="1.5" filter="url(#neonGlow)" />
      <line x1="656" y1="69" x2="662" y2="69" stroke="#00f2fe" stroke-width="1.5" filter="url(#neonGlow)" />
      <circle cx="672" cy="69" r="1.5" fill="#39ff14" class="neonBlink3" filter="url(#neonGlow)" />
    </g>

      </g>
  <text x="50%" y="125" class="sub1">I push directly to main.</text>
  <text x="50%" y="155" class="sub2">(Just kidding, I use CI/CD pipelines like a responsible adult 🛠️)</text>

  <!-- === HOVER EASTER EGG (Hidden funny text revealed on hover) === -->
  <text x="50%" y="195" class="easterEgg">"There is no cloud, just someone else's computer."</text>

</svg>
"""

os.makedirs("assets", exist_ok=True)
with open("assets/header.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("Generated glitch storm header SVG.")
