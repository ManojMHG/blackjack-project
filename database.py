import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Asdffdsa17",
        database="blackjack_db"
    )
def save_result(username, player_score, dealer_score, result):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO results (username, player_score, dealer_score, result, timestamp) VALUES (%s, %s, %s, %s, NOW())",
        (username, player_score, dealer_score, result)
    )
    conn.commit()
    conn.close()

def view_scores(username):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT player_score, dealer_score, result, timestamp FROM results WHERE username = %s", (username,))
    rows = cursor.fetchall()
    conn.close()
    print("\nYour Game History:")
    print("Date & Time           | Player | Dealer | Result")
    print("-" * 50)
    for row in rows:
        timestamp = row[3].strftime('%d/%m/%Y %H:%M:%S')
        print(f"{timestamp} |   {row[0]}   |   {row[1]}   | {row[2]}")