from database import get_connection

def record_game(username, player_score, dealer_score, outcome):
    conn = get_connection()
    cursor = conn.cursor()

    valid_outcomes = {"Win", "Lose", "Draw"}
    if outcome not in valid_outcomes:
        print(f"⚠️ Invalid outcome '{outcome}' — game not recorded.")
        conn.close()
        return

    query = """
        INSERT INTO game_history (username, player_score, dealer_score, outcome)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (username, player_score, dealer_score, outcome))
    conn.commit()

    update_streaks(username, outcome, conn)
    update_leaderboard(username, outcome, conn)

    conn.close()

def update_streaks(username, outcome, conn):
    cursor = conn.cursor()

    cursor.execute("SELECT win_streak, loss_streak FROM players WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result is None:
        cursor.execute("INSERT INTO players (username, win_streak, loss_streak) VALUES (%s, 0, 0)", (username,))
        win_streak, loss_streak = 0, 0
    else:
        win_streak, loss_streak = result

    if outcome == "Win":
        win_streak += 1
        loss_streak = 0
    elif outcome == "Lose":
        loss_streak += 1
        win_streak = 0
    else:
        win_streak = 0
        loss_streak = 0

    cursor.execute("""
        UPDATE players SET win_streak = %s, loss_streak = %s WHERE username = %s
    """, (win_streak, loss_streak, username))
    conn.commit()

def update_leaderboard(username, outcome, conn):
    cursor = conn.cursor()

    cursor.execute("SELECT total_games, wins, losses FROM leaderboard WHERE username = %s", (username,))
    result = cursor.fetchone()

    if result:
        total_games, wins, losses = result  # ✅ This was missing earlier
        total_games += 1

        if outcome == "Win":
            wins += 1
        elif outcome == "Lose":
            losses += 1
        # Draws don't affect wins/losses

        win_rate = round((wins / total_games) * 100, 2)

        cursor.execute("""
            UPDATE leaderboard
            SET total_games = %s, wins = %s, losses = %s, win_rate = %s
            WHERE username = %s
        """, (total_games, wins, losses, win_rate, username))

    else:
        total_games = 1
        wins = 1 if outcome == "Win" else 0
        losses = 1 if outcome == "Lose" else 0
        win_rate = round((wins / total_games) * 100, 2)

        cursor.execute("""
            INSERT INTO leaderboard (username, total_games, wins, losses, win_rate)
            VALUES (%s, %s, %s, %s, %s)
        """, (username, total_games, wins, losses, win_rate))

    conn.commit()

def view_game_history(username):
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT player_score, dealer_score, outcome, played_at
        FROM game_history
        WHERE username = %s
        ORDER BY played_at DESC
    """
    cursor.execute(query, (username,))
    results = cursor.fetchall()
    conn.close()

    print("\n📜 Your Game History:")
    print("Date & Time           | Player | Dealer | Outcome")
    print("-" * 50)
    for row in results:
        timestamp = row[3].strftime('%d/%m/%Y %H:%M:%S')
        print(f"{timestamp} |   {row[0]}   |   {row[1]}   | {row[2]}")

def show_leaderboard():
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        SELECT username, total_games, wins, losses, win_rate
        FROM leaderboard
        ORDER BY wins DESC, win_rate DESC
        LIMIT 10
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    print("\n🏆 Leaderboard:")
    print("Rank | Username | Total | Wins | Losses | Win Rate (%)")
    print("-" * 60)
    for i, row in enumerate(results, 1):
        print(f"{i:>4} | {row[0]:<14} | {row[1]:<5} | {row[2]:<4} | {row[3]:<6} | {row[4]:>10.2f}")