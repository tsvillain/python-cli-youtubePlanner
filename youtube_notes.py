import os
import sqlite3 as lite


class DatabaseHandler(object):
    def __init__(self):
        global conn
        try:
            conn = lite.connect('notes.db')
            with conn:
                cur = conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS ytnotes(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, desc TEXT, tags TEXT)")
        except Execption:
            print("Database failed.")
    
    def insert_data(self, data):
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO ytnotes(title, desc, tags) VALUES (?,?,?)", data)
                return True
        except Execption:
            print("Failed to Insert Data!")
    
    def fetch_data(self):
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM ytnotes")
                return cur.fetchall()
        except Execption:
            return False

    def delete_data(seld, id):
        try:
            with conn:
                cur = conn.cursor()
                sql = "DELETE FROM ytnotes WHERE id = ?"
                cur.execute(sql, [id])
                return True
        except Execption:
            return False



def ui():
    print("*"*40)
    print("\n :: YouTube Planner :: \n")
    print("*"*40)
    print("\n")

    db = DatabaseHandler()

    while 1:
        print("#"*40)
        print("1. Insert new Note \n")
        print("2. Show all Notes \n")
        print("3. Delete a Note (NEED ID OF Note) \n")
        print("Press any Key to Exit \n")
        print("#"*40)
        print("\n")

        choice = input("\n Enter a choice: ")

        if choice == "1":
            title = input("\n Enter Title: ")
            desc = input("\n Enter Description: ")
            tags = input("\n Enter a tags separated by (,): ")

            if db.insert_data([title, desc, tags]):
                print("Record inserted.")
            else:
                print("OOPS something went wrong.")
        elif choice == "2":
            print("\n :: YouTube Notes ::")
            for index, ytnotes in enumerate(db.fetch_data()): 
                print("Note ID : " + str(ytnotes[0]))
                print("Title : " + str(ytnotes[1]))
                print("Description : " + str(ytnotes[2]))
                tag = ytnotes[3]
                print("Tags : " + str(tag.split(',')))
                print("\n")

        elif choice == "3":
            noteID = input("Enter note ID: ")
            if db.delete_data(noteID):
                print("Note Deleted")
            else:
                print("Unable to Delete")
        
        else:
            break

ui()

