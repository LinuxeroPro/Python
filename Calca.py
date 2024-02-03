import customtkinter as ctk

root = ctk.CTk()
root.geometry("600x300")
root.resizable(0,0)

entry = ctk.CTkEntry(root)
entry.grid(row=1, column=5, columnspan=2)

button1 = ctk.CTkButton(root, text="1")
button1.grid(row=2, column=2, columnspan=2, padx=5, pady=10)
button2 = ctk.CTkButton(root, text="2", command="")
button2.grid(row=2, column=4, columnspan=2, padx=5, pady=10)
button3 = ctk.CTkButton(root, text="3")
button3.grid(row=2, column=6, columnspan=2, padx=5, pady=10)
button4 = ctk.CTkButton(root, text="4")
button4.grid(row=3, column=2, columnspan=2, padx=5, pady=10)
button5 = ctk.CTkButton(root, text="5")
button5.grid(row=3, column=4, columnspan=2, padx=5, pady=10)
button6 = ctk.CTkButton(root, text="6")
button6.grid(row=3, column=6, columnspan=2, padx=5, pady=10)
button7 = ctk.CTkButton(root, text="7")
button7.grid(row=4, column=2, columnspan=2, padx=5, pady=10)
button8 = ctk.CTkButton(root, text="8")
button8.grid(row=4, column=4, columnspan=2, padx=5, pady=10)
button9 = ctk.CTkButton(root, text="9")
button9.grid(row=4, column=6, columnspan=2, padx=5, pady=10)
button0 = ctk.CTkButton(root, text="0")
button0.grid(row=6, column=5, columnspan=2, padx=5, pady=10)
buttonplus = ctk.CTkButton(root, text="+")
buttonplus.grid(row=2, column=8, columnspan=2, padx=5, pady=10)
buttonless = ctk.CTkButton(root, text="-")
buttonless.grid(row=3, column=8, columnspan=2, padx=5, pady=10)
buttonmult = ctk.CTkButton(root, text="x")
buttonmult.grid(row=6, column=8, columnspan=2, padx=5, pady=10)
buttondiv = ctk.CTkButton(root, text="/")
buttondiv.grid(row=4, column=8, columnspan=2, padx=5, pady=10)
buttonequals = ctk.CTkButton(root, text="=")
buttonequals.grid(row=6, column=8, columnspan=2, padx=5, pady=10)





root.mainloop()