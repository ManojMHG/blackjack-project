CREATE TABLE users (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(100)
);

CREATE TABLE game_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    player_score INT,
    dealer_score INT,
    outcome VARCHAR(10),
    played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE players (
    username VARCHAR(50) PRIMARY KEY,
    win_streak INT DEFAULT 0,
    loss_streak INT DEFAULT 0
);

CREATE TABLE leaderboard (
    username VARCHAR(50) PRIMARY KEY,
    total_games INT DEFAULT 0,
    wins INT DEFAULT 0,
    losses INT DEFAULT 0,
    win_rate FLOAT DEFAULT 0.0
);
