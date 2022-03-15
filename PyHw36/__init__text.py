import tkinter as tk


class MyButton(tk.Button):
    def __init__(self, *args, **kwargs):
        super(MyButton, self).__init__(text="Мой класс - MyButton", *args, **kwargs)



class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        for i in range(30):
            MyButton().pack()


    def run(self):
        self.mainloop()


if __name__ == '__main__':
    window = Window()
    window.run()




