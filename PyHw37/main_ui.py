import tkinter as tk


class Gui(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(Gui, self).__init__(*args, **kwargs)

        self.geometry("200x50")
        self.configure(padx=20, pady=20, bg="#ccc")


        self.output_text = tk.StringVar()
        self.output_text.set("0")

        self.entry = tk.Entry(self, justify="center", textvariable=self.output_text)
        self.entry.grid(columnspan=5,column=2, row=0)

        btn_plus = tk.Button(self, text="+", command= self.do_addition)
        btn_plus.grid(column=1 ,row=0)

        btn_minus = tk.Button(self, text="-", command= self.do_subtraction)
        btn_minus.grid(column=7 ,row=0)

    def do_addition(self):
        try:

            if self.output_text.get().isalpha():
                pass
            else:
                result = float(self.output_text.get()) + 1
                self.output_text.set(str(result))
        except ValueError:
            return

    def do_subtraction(self):
        try:

            if self.output_text.get().isalpha():
                pass
            else:
                result = float(self.output_text.get()) - 1
                self.output_text.set(str(result))
        except ValueError:
            return






    def run(self):
        self.mainloop()

if __name__ == '__main__':
    gui = Gui()
    gui.run()