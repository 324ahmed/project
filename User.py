import tkinter as tk

class User:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("User Window")
        self.window.geometry('800x800')

        self.buttonBack = tk.Button(self.window, text='Logout', command=self.logout)

        self.buttonBack.pack()
        self.window.mainloop()

    def logout(self):
        self.window.destroy()
        import Signup
        Signup.Signup()
    def reservebutton(self):

