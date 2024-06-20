import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to handle user authentication
def authenticate_user():
    username = username_entry.get()
    password = password_entry.get()

    try:
        # Connect to MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="host",  # Replace with your MySQL username
            password="12345678",  # Replace with your MySQL password
            database="zomato_clone"
        )

        if db.is_connected():
            print("Connected to MySQL database")

        cursor = db.cursor()

        # Check if the entered credentials exist in the Users table
        query = "SELECT * FROM Users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            welcome_message = "Welcome to Zomato, {}!".format(username)
            messagebox.showinfo("Login Successful", welcome_message)
            # Here you can proceed to open the main application window or perform other actions
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error connecting to database: {err}")
        print(f"Error: {err}")

    finally:
        # Close database connection
        if 'db' in locals() and db.is_connected():
            cursor.close()
            db.close()
            print("MySQL connection closed")

# Function to open the signup window
def open_signup_window():
    global signup_window, signup_username_entry, signup_password_entry, signup_email_entry, signup_profile_info_entry

    signup_window = tk.Toplevel(root)
    signup_window.title("Zomato Clone - Signup")

    tk.Label(signup_window, text="Username:").pack()
    signup_username_entry = tk.Entry(signup_window, width=30)
    signup_username_entry.pack()

    tk.Label(signup_window, text="Password:").pack()
    signup_password_entry = tk.Entry(signup_window, width=30, show="*")
    signup_password_entry.pack()

    tk.Label(signup_window, text="Email:").pack()
    signup_email_entry = tk.Entry(signup_window, width=30)
    signup_email_entry.pack()

    tk.Label(signup_window, text="Profile Info:").pack()
    signup_profile_info_entry = tk.Entry(signup_window, width=30)
    signup_profile_info_entry.pack()

    signup_button = tk.Button(signup_window, text="Signup", command=register_user)
    signup_button.pack()

def register_user():
    signup_username = signup_username_entry.get()
    signup_password = signup_password_entry.get()
    signup_email = signup_email_entry.get()
    signup_profile_info = signup_profile_info_entry.get()

    try:
        db = mysql.connector.connect(
            host="localhost",
            user="host",  # Replace with your MySQL username
            password="12345678",  # Replace with your MySQL password
            database="zomato_clone"
        )

        if db.is_connected():
            print("Connected to MySQL database")

        cursor = db.cursor()

        query = "INSERT INTO Users (username, password, email, other_profile_info) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (signup_username, signup_password, signup_email, signup_profile_info))
        db.commit()

        messagebox.showinfo("Signup Successful", "Account created successfully! Please log in.")
        signup_window.destroy()  # Close the signup window after successful registration

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error connecting to database: {err}")
        print(f"Error: {err}")

    finally:
        # Close database connection
        if 'db' in locals() and db.is_connected():
            cursor.close()
            db.close()
            print("MySQL connection closed")

root = tk.Tk()
root.title("Zomato Clone - Login")

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root, width=30)
username_entry.pack()

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack()

# Login button
login_button = tk.Button(root, text="Login", command=authenticate_user)
login_button.pack()

# Signup button
signup_button = tk.Button(root, text="Signup", command=open_signup_window)
signup_button.pack()

root.mainloop()

