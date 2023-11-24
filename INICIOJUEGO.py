import tkinter

window =tkinter.Tk()
window.title("Juego piedra papel o tijera")
window.geometry("1020x520")
window.configure(background='sea green')
e3=tkinter.Label(window,text='BIENVENIDO A NUESTRO JUEGO',background="black",fg="white")
e3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tkinter.X)

window.mainloop()
