import pyodbc,tkinter

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-76NBGCK\SQLEXPRESS'
DATABASE_NAME = 'trial_database'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
"""

def remove_user():
    window = tkinter.Tk()
    window.title("SQL User Remove Panel")
    window.geometry("300x300")

    id_ = tkinter.Entry(window)
    id_.place(x=20,y=20)

    def add_user_connection():
        id_var= id_.get()

        conn = pyodbc.connect(connection_string)
        if conn:
            try:
                cursor = conn.cursor()
                sql_query = "DELETE FROM users WHERE ıd = ?"
                cursor.execute(sql_query,(id_var))
                print("Kişi Başarıyla Silindi.")
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