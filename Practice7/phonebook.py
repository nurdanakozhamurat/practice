import csv
from connect import connect

#1 insert from console
def insert1():
    conn=connect()
    cur=conn.cursor()

    name=input("Enter name:")
    phone=input("Enter phone:")

    cur.execute(
        "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
       (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()



#2 insert from CSV
def insert2():
    conn=connect()
    cur=conn.cursor()
    with open("contacts.csv", "r") as f:
       r=csv.reader(f)
       for i in r:
            cur.execute(
                "INSERT INTO phonebook (username, phone) VALUES (%s, %s)",
               (i[0], i[1])
            )

    conn.commit()
    cur.close()
    conn.close()



#3 update contacts
def update():
    conn=connect()
    cur=conn.cursor()

    name=input("Enter name to change:")
    new_phone=input("Enter new phone:")

    cur.execute(
        "UPDATE phonebook SET phone=%s WHERE username=%s",
        (new_phone, name)
    )

    conn.commit()
    cur.close()
    conn.close()



#4 quere with name
def search_name():
    conn=connect()
    cur=conn.cursor()

    name=input("Enter name:")

    cur.execute(
        "SELECT * FROM phonebook WHERE username=%s",
        (name,)
    )
    print(cur.fetchall())

    conn.commit()
    cur.close()
    conn.close()


#5 quere with prefix
def search_prefix():
    conn=connect()
    cur=conn.cursor()

    prefix=input("Enter pre:")

    cur.execute(
        "SELECT * FROM phonebook WHERE phone LIKE %s",
        (prefix + "%",)
    )

    res=cur.fetchall()
    print(res)

    conn.commit()
    cur.close()
    conn.close()



#6 delete contacts
def delete():
    conn=connect()
    cur=conn.cursor()

    name=input("Enter name to delete:")

    cur.execute(
        "DELETE FROM phonebook WHERE username=%s",
        (name,)
    )

    conn.commit()
    cur.close()
    conn.close()



while True:
    ch=input("Choose what do you want to see:")
    if ch=="1":
        insert1()
    elif ch=="2":
        insert2()
    elif ch=="3":
        update()
    elif ch=="4":
        search_name()
    elif ch=="5":
        search_prefix()
    elif ch=="6":
        delete()
    elif ch=="0":
        print("Not found!")
        break
    else:
        print("Invalid!")