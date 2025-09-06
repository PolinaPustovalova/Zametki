import psycopg2


def create_databases() -> None:
    conn = psycopg2.connect(
        dbname="zametki",
        user="postgres",
        password="",
        port=5432,
        host="localhost"
    )

    with conn.cursor() as cursor:
        cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    user_id serial PRIMARY KEY,
    note_id INT,
    note varchar(1000) NOT NULL
);
        """)

    conn.commit()
    conn.close()


def save_data(note_id: int, note: str):
    conn = psycopg2.connect(
        dbname="zametki",
        user="postgres",
        password="",
        port=5432,
        host="localhost"
    )

    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO notes(note_id,note) VALUES ((%s), (%s));", (note_id, note))

    conn.commit()
    conn.close()


def show_notes_from_db()->list:
    conn = psycopg2.connect(
        dbname="zametki",
        user="postgres",
        password="",
        port=5432,
        host="localhost"
    )

    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM public.notes")

        result = cursor.fetchall()

        conn.commit()
        conn.close()

        return result


def delete_note_from_db(note_id: int):
    conn = psycopg2.connect(
        dbname="zametki",
        user="postgres",
        password="",
        port=5432,
        host="localhost"
    )

    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM notes WHERE note_id > 15")

        conn.commit()
        conn.close()

