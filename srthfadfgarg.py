import customtkinter as ctk

root =  ctk.CTk()
button1 = ctk.CTkButton(root, text="1",  width=5,  height=2).pack()
button2 = ctk.CTkButton(root, text="2",  x=60, y=30, width=5, height=2).pack()
root.mainloop()