from tkinter import *
from tkinter import messagebox
from src.user_authentication import register_user

class CreateAccount:
    def __init__(self, master):
        self.master = master
        master.title("Climate Calculator - Create Account")

        self.label = Label(master, text="Create Account")
        self.label.pack()

        self.username_label = Label(master, text="Username")
        self.username_label.pack()

        self.username_entry = Entry(master)
        self.username_entry.pack()

        self.password_label = Label(master, text="Password")
        self.password_label.pack()

        self.password_entry = Entry(master, show="*")
        self.password_entry.pack()

        self.confirm_password_label = Label(master, text="Confirm Password")
        self.confirm_password_label.pack()

        self.confirm_password_entry = Entry(master, show="*")
        self.confirm_password_entry.pack()

        self.register_button = Button(master, text="Register", command=self.register_user)
        self.register_button.pack()

        self.cancel_button = Button(master, text="Cancel", command=master.quit)
        self.cancel_button.pack()

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        result, msg = register_user(username, password)
        if result:
            messagebox.showinfo("Success", msg)
            self.master.destroy()
        else:
            messagebox.showerror("Error", msg)

def main():
    root = Tk()
    app = CreateAccount(root)
    root.mainloop()

if __name__ == '__main__':
    main()
