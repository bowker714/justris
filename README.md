# Retro Tetris 🕹️

A classic **Tetris** clone built from scratch using **Python** and the **Pygame** library. It features a clean retro color palette, classic 7-piece tetromino mechanics, score tracking, and full arcade-style controls.

---

## ✨ Features

* **Classic Tetris Mechanics:** Includes all 7 standard tetromino shapes (I, O, T, L, J, S, Z) with rotation and collision detection.
* **Score Tracking:** Earn points every time you clear lines.
* **Hard & Soft Drops:** Speed up gameplay with soft drops or instantly place pieces using the hard drop feature.
* **Game Over & Restart:** Integrated game-over detection with an instant restart option (`R` key).
* **Retro Visuals:** Styled with a dark grid background and vibrant block colors.

---

## 🎮 Controls

| Key | Action |
| --- | --- |
| **Left / Right Arrow** | Move piece left or right |
| **Up Arrow** | Rotate piece |
| **Down Arrow** | Move piece down (Soft drop) |
| **Spacebar** | Hard drop (Instant drop) |
| **R** | Restart game (on Game Over) |

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed on your system. You will also need the `pygame` library.

### Installation

1. Clone or download the repository/script.
2. Install the required dependency via pip:
```bash
pip install pygame

```



### Running the Game

Run the script from your terminal:

```bash
python justris.py

```

---

## 🛠️ Code Structure

* **Constants & Setup:** Defines screen dimensions (300x600), block sizes (30px), and the retro color palette.
* **`Tetris` Class:** Handles game logic, including grid initialization, piece generation, collision checking, line clearing, rotation, and movement.
* **Main Game Loop:** Manages delta time (`dt`), frame rate (`60 FPS`), automatic gravity drop, keyboard events, and screen rendering.
