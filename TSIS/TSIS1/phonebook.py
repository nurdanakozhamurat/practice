import json
import csv
from connect import connection

#add contact
def add_contact():
    conn = connection()
    cur = conn.cursor()

    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")
    group = input("Group: ")
    phone = input("Phone: ")
    ptype = input("Type (home/work/mobile): ")

    cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
    g = cur.fetchone()

    if not g:
        cur.execute("INSERT INTO groups(name) VALUES(%s) RETURNING id", (group,))
        g_id = cur.fetchone()[0]
    else:
        g_id = g[0]


    #update
    cur.execute("SELECT id FROM contacts WHERE name=%s",(name,))
    c = cur.fetchone()

    if not c:
        cur.execute("""
        INSERT INTO contacts(name, email, birthday, group_id)
        VALUES (%s, %s, %s, %s)
        RETURNING id
        """, (name, email, birthday, g_id))
        c_id = cur.fetchone()[0]
    else:
        c_id = c[0]
        cur.execute("""
        UPDATE contacts
        SET email=%s, birthday=%s, group_id=%s
        WHERE id=%s
    """, (email,birthday, g_id, c_id))


    cur.execute("""
        INSERT INTO phones(contact_id, phone, type)
        VALUES (%s, %s, %s)
    """, (c_id, phone, ptype))

    conn.commit()
    conn.close()


#filter by group
def filter_group():
    conn = connection()
    cur = conn.cursor()

    group = input("Group: ")

    cur.execute("""
        SELECT c.name, c.email
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s
    """, (group,))

    for row in cur.fetchall():
        print(row)

    conn.close()


#search email
def search_email():
    conn = connection()
    cur = conn.cursor()

    query = input("Email: ")

    cur.execute("""
        SELECT name, email
        FROM contacts
        WHERE email ILIKE %s
    """, ('%' + query + '%',))

    for row in cur.fetchall():
        print(row)

    conn.close()


#sort
def sort_contacts():
    conn = connection()
    cur = conn.cursor()

    query = input("Sort by name/birthday: ")

    if query not in ["name", "birthday"]:
        print("Invalid query")
        return

    cur.execute(f"""
        SELECT name, email, birthday
        FROM contacts
        ORDER BY {query}
    """)

    for row in cur.fetchall():
        print(row)

    conn.close()


#pagination
def paginate():
    conn = connection()
    cur = conn.cursor()

    limit = 2
    offset = 0

    while True:
        cur.execute("""
            SELECT name, email
            FROM contacts
            ORDER BY name
            LIMIT %s OFFSET %s
        """, (limit, offset))

        for r in cur.fetchall():
            print(r)

        control = input("next / prev / quit: ")

        if control == "next":
            offset += limit
        elif control == "prev":
            offset = max(0, offset - limit)
        elif control == "quit":
            break

    conn.close()


#export json
def export_json():
    conn = connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
    """)

    data = cur.fetchall()

    with open("contacts.json", "w") as f:
        json.dump(data, f, default=str)

    conn.close()


#import json
def import_json():
    conn = connection()
    cur = conn.cursor()

    with open("contacts.json") as f:
        data = json.load(f)

    for row in data:
        name, email, birthday, group, phone, ptype = row

        cur.execute("SELECT id FROM contacts WHERE name=%s", (name,))
        exists = cur.fetchone()

        if exists:
            choice = input(f"{name} exists (skip/overwrite): ")
            if choice == "skip":
                continue
            else:
                cur.execute("DELETE FROM contacts WHERE name=%s", (name,))


        cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
        g = cur.fetchone()

        if not g:
            cur.execute("INSERT INTO groups(name) VALUES(%s) RETURNING id", (group,))
            g_id = cur.fetchone()[0]
        else:
            g_id = g[0]


        cur.execute("""
            INSERT INTO contacts(name, email, birthday, group_id)
            VALUES (%s, %s, %s, %s)
            RETURNING id
        """, (name, email, birthday, g_id))

        c_id = cur.fetchone()[0]

        if phone:
            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES (%s, %s, %s)
            """, (c_id, phone, ptype))

    conn.commit()
    conn.close()


#import csv
def import_csv():
    conn = connection()
    cur = conn.cursor()

    with open("contacts.csv", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            name = row["name"]
            email = row["email"]
            birthday = row["birthday"]
            group = row["group"]
            phone = row["phone"]
            ptype = row["type"]

            cur.execute("SELECT id FROM groups WHERE name=%s", (group,))
            g = cur.fetchone()

            if not g:
                cur.execute("INSERT INTO groups(name) VALUES(%s) RETURNING id", (group,))
                g_id = cur.fetchone()[0]
            else:
                g_id = g[0]

            # контакт
            cur.execute("""
                INSERT INTO contacts(name, email, birthday, group_id)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, (name, email, birthday, g_id))

            c_id = cur.fetchone()[0]

            # телефон
            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES (%s, %s, %s)
            """, (c_id, phone, ptype))

    conn.commit()
    conn.close()



#menu
def menu():
    while True:
        c = input("Choose: ")

        if c == "1":
            add_contact()
        elif c == "2":
            filter_group()
        elif c == "3":
            search_email()
        elif c == "4":
            sort_contacts()
        elif c == "5":
            paginate()
        elif c == "6":
            export_json()
        elif c == "7":
            import_json()
        elif c == "8":
            import_csv()
        elif c == "0":
            break


if __name__ == "__main__":
    menu()
