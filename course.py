import sqlite3 as lite


class DatabaseManage(object):

    def __init__(self):
        global con
        try:
            con=lite.connect('courses.db')
            with con:
                cur=con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,description TEXT,price TEXT,is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create a db")

            
    def insert_data(self,data):
        try:
             with con:
                cur=con.cursor()
                cur.execute("INSERT INTO course(name,description,price,is_private) VALUES (?,?,?,?)",data)
        except Exception:
            return False

    def fetch_data(self):
        try:
             with con:
                cur=con.cursor()
                cur.execute("SELECT * FROM courses")
                return cur.fetchall()
        except Exception:
            return False


    def delete_data(self,id):
        try:
            with con:
                cur=con.cursor()
                sql="DELETE FROM course WHERE id=?"
                cur.execute(sql,[id])
        except Exception:
            return False

# TODO USER INTERFACE

def main():
    print("*"*40)
    print("\n:: COURSE MANAGEMENT ::\n")
    print("*"*40)
    print("\n")

    db=DatabaseManage()

    print("#"*40)
    print("\n:: USER MANUAL ::\n")
    print("#"*40)

    print("\npress 1.Insert a new course\n")
    print("press 2.show all courses\n")
    print("press 3.Delete a course(NEED ID OF COURSE)\n")
    print("#"*40)
    print("\n")

    choice=input("\n Enter a choice: ")
     
    if choice == "1":
        name=input('\n Enter course name: ')
        description=input('\n Enter course description: ')
        price=input('\n Enter course price: ')
        private=input('\n Is this course private(0/1): ')

        if db.insert_data([name,description,price,private]):
            print("Course was inserted successfully")
        else:
            print("OOPS something went wrong")

    elif choice=="2":
        print("\n:: COURSE LIST ::")

        for item in enumerate(db.fetch_data()):
            print("course id: "+str(item[0]))
            print("course name: "+str(item[1]))
            print("course description: "+str(item[2]))
            print("course price: "+str(item[3]))
            private='yes' if item[4] else 'NO'
            print("Is private: "+private)
            print("\n")

    elif choice=="3":
        record_id=input("Enter the course id: ")

        if db.delete_data(record_id):
            print("Course deleted successfully")
        else:
            print("OOPS something went wrong")
    else:
        print("\n BAD CHOICE")


if __name__ == '__main__':
    main()

