# Chess AI Engine: PGN-Driven Machine Learning Bot

An interactive Python chess engine and GUI combining classic Minimax search with heuristic positional evaluation and a PGN dataset pipeline.

**Author** | Ewan Robertson
**Dataset Source** | Lichess Open Database (Standard Games PGN)
**Repository** | [github.com/3wanr/chess-ai-bot](https://github.com/3wanr/chess-ai-bot)

---

## 📌 Executive Summary

Traditional chess engines such as Stockfish rely primarily on handcrafted position evaluation heuristics and deep search trees (e.g., Alpha-Beta pruning) to determine optimal moves. While exceptionally strong, this computational strategy consumes significant processing power and lacks human-like positional intuition.

This project develops a Python-based Chess AI Engine and Graphical User Interface. The system combines classic Minimax search with a rule-based evaluation model utilizing material counts and piece-square position tables. Built using `python-chess` for move validation and `Pygame` for an interactive board interface, the project allows human players to play directly against the AI in real time.

---

## 🛠️ Architecture & Core Modules

The repository is organized into modular components for clarity and maintainability:

| Module | Component | Purpose |
| :--- | :--- | :--- |
| `gui.py` | **Pygame Interface** | Handles window event loops, interactive 8x8 grid board rendering, sprite graphics, user input, and asynchronous threading to keep UI responsive during search. |
| `engine.py` | **Search Engine** | Executes Minimax decision-tree search with Alpha-Beta pruning, move ordering heuristics, and search depth controls. |
| `evaluator.py` | **Evaluation Module** | Computes static board scores combining piece material counts, piece-square tables (PST), king safety, pawn structure, and center control metrics. |
| `dataset.py` | **PGN Data Pipeline** | Parses Lichess PGN dumps, filters high-ELO games (≥2000), and generates 8x8 tensor state encodings and feature vectors for learning models. |
| `main.py` | **Application Entry** | Initializes application modules and launches the interactive game loop. |

---

## 📊 Dataset & PGN Data Pipeline

The pipeline leverages raw game archives from the [Lichess Open Database](https://database.lichess.org/):

1. **PGN Parsing & Extraction:** Streams and parses large `.pgn` database dumps using `python-chess`.
2. **Quality Filtering:** Retains high-quality games where player ELO ≥ 2000 to eliminate tactical blunders and focus on strong positional play.
3. **Tensor State Encoding:** Converts FEN strings into 8x8 spatial tensor representation maps (bitboard planes representing piece positions, active side, castling rights, en passant targets, and repetition counters).
4. **Feature Vector Extraction:** Extracts heuristic vectors (material balance, mobility, pawn structure, and center control) mapped to outcome targets (+1 for White win, -1 for Black win, 0 for draw).

---

## 💻 Tech Stack

* **Core Engine Language:** Python 3.x
* **Chess Rules & Logic:** `python-chess`
* **GUI Library:** `Pygame`
* **Data Processing & Math:** `numpy`, `zstandard`
* **Version Control:** Git / GitHub

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher
* `pip` package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/3wanr/chess-ai-bot.git](https://github.com/3wanr/chess-ai-bot.git)
   cd chess-ai-bot