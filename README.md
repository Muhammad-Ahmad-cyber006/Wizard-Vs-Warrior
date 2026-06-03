# ⚔️ Wizard vs Warrior

Wizard vs Warrior is a two-player fighting game built with Python and Pygame. One player controls a sword-wielding Warrior 🗡️ while the other plays as a magic-casting Wizard 🧙. The goal is simple: knock out your opponent by draining their health bar before they drain yours.

Each round starts with a 3-second countdown ⏳. Once it hits zero, both players are free to move, jump, and attack. When a fighter's health drops to zero, the surviving player scores a point 🏆, a victory screen flashes briefly, and a new round begins with both fighters restored to full health. Scores carry over across rounds so you can keep playing as long as you like.

## 🎮 Controls

| Action     | Player 1 — Warrior 🗡️ | Player 2 — Wizard 🧙 |
|------------|----------------------|----------------------|
| Move Left  | A                    | Left Arrow           |
| Move Right | D                    | Right Arrow          |
| Jump       | W                    | Up Arrow             |
| Attack 1   | R                    | M                    |
| Attack 2   | T                    | N                    |

## ✨ Features

Each character has seven distinct animation states: idle, running, jumping, two attack types, taking a hit, and death 💀. Attacks have a short cooldown to keep things balanced. Both fighters are pulled down by gravity 🌍, can't walk off the edges of the screen, and automatically face each other as they move. Background music 🎵 plays throughout the game and each attack type triggers its own sound effect 🔊.

## 📁 Project Structure

```
Wizard-Vs-Warrior/
├── main.py              # Game loop, rendering, round management
├── fighter.py           # Fighter class (movement, animation, combat)
├── Turok.ttf            # Custom font for score and countdown display
├── victory.png          # Victory screen image
├── images/
│   ├── background/      # Background image
│   ├── warrior/         # Warrior sprite sheet
│   └── wizard/          # Wizard sprite sheet
└── music_and_sound/
    ├── music.flac       # Background music
    ├── sword_attack.wav # Warrior attack sound
    └── magic.wav        # Wizard attack sound
```

## 🚀 Getting Started

Make sure you have Python 3 and Pygame installed, then clone the repo and run the game.

```bash
git clone https://github.com/Muhammad-Ahmad-cyber006/Wizard-Vs-Warrior.git
cd Wizard-Vs-Warrior
pip install pygame
python main.py
```

## 🤝 Contributing

Pull requests are welcome! Feel free to open an issue for bugs or feature ideas.

## 👤 Author

Muhammad Ahmad — [@Muhammad-Ahmad-cyber006](https://github.com/Muhammad-Ahmad-cyber006)