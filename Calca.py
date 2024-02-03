import customtkinter as ctk

root =  ctk.CTk()
root.geometry("450x500")
entry =  ctk.CTkLabel(root, text="Calca",width=350, )
entry.grid(row=0, column=0)
button1 = ctk.CTkButton(root, text="1")
button1.grid(row=2, column=2)
button2 = ctk.CTkButton(root, text="2")
button2.grid(row=2, column=3)
button3 =  ctk.CTkButton(root, text="3")
button3.grid(row=2, column=4)
root.mainloop()