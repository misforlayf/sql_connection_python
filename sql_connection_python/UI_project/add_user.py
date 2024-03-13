import random,pyodbc,tkinter

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-76NBGCK\SQLEXPRESS'
DATABASE_NAME = 'trial_database'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

def add_user():
    window = tkinter.Tk()
    window.title("SQL User Add Panel")
    window.geometry("300x300")

    name_ = tkinter.Entry(window)
    name_.place(x=20,y=20)
    phone_number_ = tkinter.Entry(window)
    phone_number_.place(x=20,y=50)

    def add_user_connection():
        name_var = name_.get()
        phone_number_var = phone_number_.get()
        id = random.randint(0,100)

        conn = pyodbc.connect(connection_string)

        if conn:
            try:
                cursor = conn.cursor()
                sql_query = "INSERT INTO users (ıd, name, phone_number) VALUES (?,?,?)"
                cursor.execute(sql_query,(id,name_var,phone_number_var))
                print("Kişi Başarıyla Eklendi")
            except Exception as e:
                print(f"Hata: {e}")
            finally:
                conn.commit()
                conn.close()
                window.destroy()
        else:
            print("Bağlantı Hatası")
            window.destroy()
            exit()
    save = tkinter.Button(window,text="Save", command=add_user_connection)
    save.place(x=20,y=80)

    window.mainloop()
