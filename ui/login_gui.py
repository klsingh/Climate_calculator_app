import tkinter as tk
from tkinter import messagebox
from src.user_authentication import UserAuthentication


class LoginGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Climate Calculator - Login")
        self.master.geometry("400x200")

        self.username_label = tk.Label(self.master, text="Username")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()

        self.password_label = tk.Label(self.master, text="Password")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.master, text="Login", command=self.login)
        self.login_button.pack()

        self.create_account_button = tk.Button(self.master, text="Create Account", command=self.create_account)
        self.create_account_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user_auth = UserAuthentication()

        if user_auth.authenticate_user(username, password):
            messagebox.showinfo("Success", "Login successful!")
            self.master.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def create_account(self):
        from ui.create_account_gui import CreateAccountGUI
        create_account_window = tk.Toplevel(self.master)
        create_account_gui = CreateAccountGUI(create_account_window)
