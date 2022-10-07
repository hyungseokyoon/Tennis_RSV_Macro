import tkinter

window=tkinter.Tk()

window.title("Mokdong Tennis Application")
window.geometry("640x400+100+100")
window.resizable(False, False)

label_date=tkinter.Label(window, text="날짜")
label_date.pack()
label_courtnum=tkinter.Label(window, text="코트번호")
label_courtnum.pack()
label_courtnum=tkinter.Label(window, text="시작시간")
label_courtnum.pack()
label_courtnum=tkinter.Label(window, text="코트번호")
label_courtnum.pack()


window.mainloop()