
import tkinter as tk
from tkinter import ttk
import mysql.connector #type:ignore

# Database connection to python ra
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='manohar',
    database='zomato_clone'
)

login_in_store = None # to store the user_id of user who has logged in 

if connection.is_connected():
    print("connected")

cursor = connection.cursor()

def order_history(user_id): # This function fetches all the orderdetails of the user that has logged in
    query = '''
   SELECT
    o.order_id,
    o.order_date,
    r.name AS restaurant_name,
    GROUP_CONCAT(m.item_name) AS menu_items,
    GROUP_CONCAT(od.quantity) AS quantities,
    SUM(od.price * od.quantity) AS total_price
FROM Orders o
JOIN OrderDetails od ON o.order_id = od.order_id
JOIN Menus m ON od.menu_id = m.menu_id
JOIN Restaurants r ON o.restaurant_id = r.restaurant_id
WHERE o.user_id = %s    
GROUP BY o.order_id, o.order_date, r.name
ORDER BY o.order_id;
    '''
    cursor.execute(query, (user_id,))
    return cursor.fetchall()

def order_history_window():
    order_history_win = tk.Toplevel(root) #type:ignore
    order_history_win.title("Order History Window")
    order_history_win.geometry("800x600")

    label = tk.Label(order_history_win, text="Order History", font=("Helvetica", 16))
    label.pack(pady=20)

# we are using treeview widget to keep data in awell mannered structure

    tree = ttk.Treeview(order_history_win)
    tree.pack(fill="both", expand=True)

    tree['columns'] = ('Order Date', 'Restaurant Name','Menu Item', 'Quantity','Total Price')

    tree.column('#0', width=0, stretch=tk.NO)
    tree.column('Order Date', anchor=tk.W, width=150)
    tree.column('Restaurant Name', anchor=tk.W, width=200)
    tree.column('Menu Item', anchor=tk.W, width=200)
    tree.column('Quantity', anchor=tk.W, width=150)
    tree.column('Total Price', anchor=tk.W, width=100)

    tree.heading('#0', text='Order ID', anchor=tk.W)
    tree.heading('Order Date', text='Order Date', anchor=tk.W)
    tree.heading('Restaurant Name', text='Restaurant Name', anchor=tk.W)
    tree.heading('Menu Item', text='Menu Item', anchor=tk.W)
    tree.heading('Quantity', text='Quantity', anchor=tk.W)
    tree.heading('Total Price', text='Total Price', anchor=tk.W)

    order = order_history()
    for orders in order:
        if orders:
            for order in orders:
                order_id, order_date, restaurant_name, menu_item, quantity, total_price = order
                tree.insert(parent='', index='end', iid=order_id, text='', values=(order_id, order_date, restaurant_name, menu_item, quantity, total_price))
            tree.pack()
    else:
        label = tk.Label(order_history_win, text="No orders to display.")
        label.pack(pady=20)
    
    close_button = tk.Button(order_history_win, text="Close", command=order_history_win.destroy)
    close_button.pack(pady=20)