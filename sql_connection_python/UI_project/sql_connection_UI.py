import tkinter,add_user,remove_user,show_user

main = tkinter.Tk()
main.geometry("300x300")
main.title("SQL Management Panel")

button1 = tkinter.Button(main, text="Kullanıcı Ekle", command=add_user.add_user)
button1.place(x=20,y=20)

button2 = tkinter.Button(main, text="Kullanıcı Sil", command=remove_user.remove_user)
button2.place(x=20,y=50)

button3 = tkinter.Button(main, text="Kullanıcıları Göster")
button3.place(x=20,y=80)

main.mainloop()
