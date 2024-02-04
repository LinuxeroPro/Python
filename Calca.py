import customtkinter as ctk

root = ctk.CTk()
root.geometry("600x240")
root.resizable(0,0)

entry = ctk.CTkEntry(root)
entry.grid(row=1, column=5, columnspan=2, pady=5)


def FunBot0():
    pass
def FunBot1():
    pass
def FunBot2():
    pass
def FunBot3():
    pass
def FunBot4():
    pass
def FunBot5():
    pass
def FunBot6():
    pass
def FunBot7():
    pass
def FunBot8():
    pass
def FunBot9():
    pass
def FunBot1Pl():
    pass
def FunBotLe():
    pass
def FunBotDiv():
    pass
def FunBotMul():
    pass
def FunBotEq():
    pass
def FunBotCE():
    pass

button1 = ctk.CTkButton(root, text="1", command=FunBot1)
button1.grid(row=2, column=2, columnspan=2, padx=5, pady=10)
button2 = ctk.CTkButton(root, text="2", command=FunBot2)
button2.grid(row=2, column=4, columnspan=2, padx=5, pady=10)
button3 = ctk.CTkButton(root, text="3", command=FunBot3)
button3.grid(row=2, column=6, columnspan=2, padx=5, pady=10)
button4 = ctk.CTkButton(root, text="4", command=FunBot4)
button4.grid(row=3, column=2, columnspan=2, padx=5, pady=10)
button5 = ctk.CTkButton(root, text="5", command=FunBot5)
button5.grid(row=3, column=4, columnspan=2, padx=5, pady=10)
button6 = ctk.CTkButton(root, text="6", command=FunBot6)
button6.grid(row=3, column=6, columnspan=2, padx=5, pady=10)
button7 = ctk.CTkButton(root, text="7", command=FunBot7)
button7.grid(row=4, column=2, columnspan=2, padx=5, pady=10)
button8 = ctk.CTkButton(root, text="8", command=FunBot8)
button8.grid(row=4, column=4, columnspan=2, padx=5, pady=10)
button9 = ctk.CTkButton(root, text="9", command=FunBot9)
button9.grid(row=4, column=6, columnspan=2, padx=5, pady=10)
button0 = ctk.CTkButton(root, text="0", command=FunBot0)
button0.grid(row=5, column=4, columnspan=2, padx=5, pady=10)
buttonplus = ctk.CTkButton(root, text="+", command=FunBot1Pl)
buttonplus.grid(row=2, column=8, columnspan=2, padx=5, pady=10)
buttonless = ctk.CTkButton(root, text="-", command=FunBotLe)
buttonless.grid(row=3, column=8, columnspan=2, padx=5, pady=10)
buttonmult = ctk.CTkButton(root, text="x", command=FunBotMul)
buttonmult.grid(row=5, column=8, columnspan=2, padx=5, pady=10)
buttondiv = ctk.CTkButton(root, text="/", command=FunBotDiv)
buttondiv.grid(row=4, column=8, columnspan=2, padx=5, pady=10)
buttonequals = ctk.CTkButton(root, text="=",  command=FunBotEq)
buttonequals.grid(row=5, column=6, columnspan=2, padx=5, pady=10)
buttonCE = ctk.CTkButton(root, text="CE", command=FunBotCE)
buttonCE.grid(row=5, column=2, columnspan=2, padx=5, pady=10)




root.mainloop()