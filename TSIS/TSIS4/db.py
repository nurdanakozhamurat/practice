import psycopg2
from config import *

def connect():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS players (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS game_sessions (
        id SERIAL PRIMARY KEY,
        player_id INTEGER REFERENCES players(id),
        score INTEGER NOT NULL,
        level_reached INTEGER NOT NULL,
        played_at TIMESTAMP DEFAULT NOW()
    );
    """)

    conn.commit()
    cur.close()
    conn.close()

def get_or_create_player(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    res = cur.fetchone()

    if res:
        pid = res[0]
    else:
        cur.execute("INSERT INTO players(username) VALUES(%s) RETURNING id", (username,))
        pid = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return pid

def save_score(player_id, score, level):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO game_sessions(player_id, score, level_reached)
    VALUES (%s, %s, %s)
    """, (player_id, score, level))

    conn.commit()
    cur.close()
    conn.close()

def get_top10():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    SELECT username, score, level_reached, played_at
    FROM game_sessions
    JOIN players ON players.id = game_sessions.player_id
    ORDER BY score DESC
    LIMIT 10
    """)

    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def get_best_score(player_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT MAX(score) FROM game_sessions WHERE player_id=%s", (player_id,))
    res = cur.fetchone()[0]

    cur.close()
    conn.close()
    return res if res else 0