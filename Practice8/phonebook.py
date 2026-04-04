
from connect import connection

#pattern-search function
def search():
    pattern = input("enter pattern: ")

    conn=connection()
    cur=conn.cursor()

    cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
    rows=cur.fetchall()

    for i in rows:
        print(i)

    cur.close()
    conn.close()



#upsert procedure
def insert():
    name = input("enter name: ")
    phone = input("enter phone: ")

    conn=connection()
    cur=conn.cursor()

    cur.execute("CALL insert_user(%s, %s);", (name, phone))
    conn.commit()

    print("User inserted/updated")

    cur.close()
    conn.close()



#bulk-insert procedure
def bulk_insert():
    names = input("Enter names: ").split(",")
    phones = input("Enter phones: ").split(",")

    conn = connection()
    cur = conn.cursor()

    cur.execute("CALL bulk_insert(%s, %s)", (names, phones))
    conn.commit()

    print("Bulk insert done")

    cur.close()
    conn.close()



#paginated query function
def pagination():
    limit = int(input("enter limit: "))
    offset = int(input("enter offset: "))

    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts(%s, %s)", (limit, offset))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()



#delete procedure (by username or phone)
def delete():
    value = input("enter name/phone to delete: ")

    conn = connection()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s)", (value,))
    conn.commit()

    print("Deleted")

    cur.close()
    conn.close()



def main():
    while True:
        print("1-Search")
        print("2-Insert/Update (Upsert)")
        print("3-Bulk Insert")
        print("4-Pagination")
        print("5-Delete")
        print("0-Exit")

        c = input("Choose: ")

        if c == "1":
            search()
        elif c == "2":
            insert()
        elif c == "3":
            bulk_insert()
        elif c == "4":
            pagination()
        elif c == "5":
            delete()
        elif c == "0":
            break


if __name__ == "__main__":
    main()


