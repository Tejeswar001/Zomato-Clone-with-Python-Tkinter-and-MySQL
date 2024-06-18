from tkinter import *
import mysql.connector
from functools import partial

class Zomato():
    
    conn = mysql.connector.connect(**{'host':'localhost', 'user':'root','password':'Tejeswar2006','database':'zomato_clone'})
    print("Connected")

    def __init__(self, root):
        self.root = root
        self.root.title('Welcome to Zomato Clone')
        self.root.geometry('350x250')
        self.root.configure(bg='light blue')

    def home_page(self):
        self.root.destroy()
        self.hop = Tk()
        self.hop.title('Welcome to Zomato Clone')
        self.hop.geometry('350x250')
        self.hop.configure(bg='light blue')

        head = Label(self.hop, text='Zomato Clone', width=20,fg='red', font=('arial', 20), bg='light blue')
        head.pack(pady=20)

        rest = Button(self.hop, text='Restaurants', command=self.rest_page_1)
        rest.pack(pady=10)

        history = Button(self.hop, text='Order History')
        history.pack(pady=10)

        logout = Button(self.hop, text='Log out', command=self.hop.destroy)
        logout.pack(pady=10)

    def rest_page_1(self):
        self.hop.destroy()

        self.cus = Tk()
        self.cus.geometry('400x350')
        self.cus.title('Restaurants')
        self.cus.configure(bg='light blue')

        c = self.conn.cursor()
        c.execute('SELECT DISTINCT cuisine FROM Restaurants;')
        r = c.fetchall()
        cus_names = [row[0] for row in r]

        Label(self.cus, text='Select your type of Cuisine from the List',font=('arial',15),bg='light blue').pack(pady=20)

        for i in cus_names:
            Button(self.cus, text=f'{i}', font=('arial',15), width=20, height=2, command=partial(self.rest_page_2, i)).pack(pady=10)
        
    def rest_page_2(self, cuisine):
        self.cus.destroy()

        self.rest = Tk()
        self.rest.title('Restaurants')
        self.rest.geometry('600x450')
        self.rest.configure(bg='light blue')

        c = self.conn.cursor()
        c.execute(f"SELECT name FROM Restaurants WHERE cuisine = '{cuisine}'")
        r = c.fetchall()
        rest_names = [row[0] for row in r]

        Label(self.rest, text="Click on a restaurant to view it's menu items", font=("arial",15), bg='light blue').pack(pady=20)
        
        for i in rest_names:
            Button(self.rest, text=f'{i}', font=('arial',15),width=20, height=2).pack(pady=10)

root = Tk()
app = Zomato(root)
app.home_page()
root.mainloop()
