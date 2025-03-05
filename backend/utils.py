import os

import mysql.connector


def connect_sql():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return conn


def insert_data_to_db(sex, age, fare, familysize, survived):
    conn = connect_sql()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO passengers (sex, age, fare, familysize, survived)
        VALUES (%s, %s, %s, %s, %s)
    """, (sex, age, fare, familysize, survived))
    conn.commit()
    cursor.close()
    conn.close()


def fetch_recent_history():
    conn = connect_sql()
    cursor = conn.cursor()
    cursor.execute("""
            SELECT sex, age, fare, familysize, survived, created_at
            FROM passengers
            ORDER BY created_at DESC
            LIMIT 10
        """)
    rows = cursor.fetchall()
    history = []
    for row in rows:
        history.append({
            "sex": row[0],
            "age": row[1],
            "fare": row[2],
            "familysize": row[3],
            "survived": row[4],
            "created_at": row[5]
        })
    cursor.close()
    conn.close()
    return history
