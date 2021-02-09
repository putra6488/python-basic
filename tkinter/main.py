import tkinter

root = tkinter.Tk()

def event_tekan():
    label2 = tkinter.Label(root, text="masuk")
    label2.pack()

label = tkinter.Label(root, text="putra prasetyo")
tombol = tkinter.Button(root, text="go", command = event_tekan)

label.pack()
tombol.pack()
root.mainloop()