import tkinter as tk




class EnterName(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(EnterName, self).__init__(*args, **kwargs)
        self.lbl = tk.Label(self, text="Введите ваше имя")
        self.entr = tk.Entry()
        self.lbl.pack()
        self.entr.pack()

    def run(self):
        self.mainloop()

if __name__ == '__main__':
    app = EnterName()
    app.run()
