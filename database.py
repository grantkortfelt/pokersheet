import sqlite3

def create_tables():
    conn = sqlite3.connect('poker.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS player (name TEXT PRIMARY KEY, net REAL)")
    cur.execute("CREATE TABLE IF NOT EXISTS session (id INTEGER PRIMARY KEY, month INTEGER, day INTEGER, buyin REAL)")
    cur.execute("CREATE TABLE IF NOT EXISTS play (name TEXT, session INTEGER, net REAL, buyins INTEGER, cash REAL, PRIMARY KEY (name, session))")
    conn.commit()
    conn.close()

def add_player(name):
    conn = sqlite3.connect('poker.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO player (name, net) VALUES (?, 0)", (name,))
    conn.commit()
    conn.close()

def add_session(month, day, buyin):
    conn = sqlite3.connect('poker.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO session (month, day, buyin) VALUES (?, ?, ?)", (month, day, buyin))
    conn.commit()
    conn.close()

def add_play(name, session, net, buyins, cash):
    conn = sqlite3.connect('poker.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO play (name, session, net, buyins, cash) VALUES (?, ?, ?, ?, ?)", (name, session, net, buyins, cash))
    conn.commit()
    conn.close()

def get_player(name):
    conn = sqlite3.connect('poker.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM player WHERE name=?", (name,))
    player = cur.fetchone()
    conn.close()
    return player

def get_session(id):
    conn = sqlite3.connect('poker.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM session WHERE id=?", (id,))
    session = cur.fetchone()
    conn.close()
    return session

def get_play(name, session):
    conn = sqlite3.connect('poker.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM play WHERE name=? AND session=?", (name, session))
    play = cur.fetchone()
    conn.close()
    return play