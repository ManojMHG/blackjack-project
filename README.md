# blackjack-project
🎲 A terminal-based Blackjack game with secure login, game history tracking, win/loss streaks, and a dynamic leaderboard — built with Python and MySQL.


## 🚀 Features

- 🔐 **Login & Signup**: Secure user authentication
- 🎮 **Blackjack Gameplay**: Classic hit/stand logic with dealer AI
- 📊 **Leaderboard**: Tracks wins, losses, total games, and win rate
- 📈 **Streaks**: Win/loss streak tracking per player
- 🗂️ **Game History**: View past games with scores and timestamps
- 🧠 **Outcome Normalization**: Smart parsing of game results for accurate stats

## 🛠️ Tech Stack

- **Python 3**
- **MySQL** (via `mysql-connector-python`)
- Modular structure:
  - `main.py` — game loop and user interface
  - `blackjack.py` — gameplay logic
  - `auth.py` — login/signup
  - `database.py` — DB connection and queries
  - `game_tracker.py` — history, streaks, leaderboard

