import bcrypt
from database import get_connection

def signup(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players WHERE username = %s", (username,))
    if cursor.fetchone():
        return "Username already exists"
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    cursor.execute("INSERT INTO players (username, password) VALUES (%s, %s)", (username, hashed.decode()))
    conn.commit()
    conn.close()
    return "Signup successful"

def login(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM players WHERE username = %s", (username,))
    result = cursor.fetchone()
    conn.close()
    if result and bcrypt.checkpw(password.encode(), result[0].encode()):
        return True
    return Falses