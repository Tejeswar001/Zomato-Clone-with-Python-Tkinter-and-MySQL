
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
    r.location,
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
    order_history_win.configure(bg="#FFCCCC")

    title_frame = tk.Frame(order_history_win, bg="#FFCCCC")
    title_frame.pack(fill="x", padx=10, pady=10)

    label = tk.Label(title_frame, text="Order History", font=("Segoe UI", 16, "bold"), fg="#CB202D", bg="#FFCCCC")
    label.pack(side="left", padx=50)

    order_history_frame = tk.Frame(order_history_win, bg="#f7f7f7")
    order_history_frame.pack(fill="both", expand=True, padx=20, pady=20)

    canvas = tk.Canvas(order_history_frame, width=760, height=560, bg="#f7f7f7")
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(order_history_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.configure(yscrollcommand=scrollbar.set)

    inner_frame = tk.Frame(canvas, bg="#f7f7f7")
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")
    inner_frame.pack(fill="both", expand=True, padx=20, pady=20)

    orders = order_history(login_in_store)

    if orders:
        for order in orders:
            order_id, order_date, location, other_info, restaurant_name, menu_items, quantities, total_price = order

            order_frame = tk.Frame(inner_frame, bg="#f7f7f7", highlightbackground="gray", highlightthickness=1, padx=10, pady=10)
            order_frame.pack(fill="x", padx=20, pady=10)

            # Header frame for restaurant name, description, and view menu button
            header_frame = tk.Frame(order_frame, bg="#f7f7f7")
            header_frame.pack(fill="x", pady=10)

            restaurant_label = tk.Label(header_frame, text=restaurant_name, font=("Segoe UI", 14, "bold"), fg="black", bg="#f7f7f7")
            restaurant_label.pack(side="left")

            restaurant_description_label = tk.Label(header_frame, text=other_info, font=("Segoe UI", 12), fg="gray", bg="#f7f7f7")
            restaurant_description_label.pack(side="left", padx=10)

            view_menu_button = tk.Button(header_frame, text="View Menu", command=lambda restaurant_id=order_id: view_menu(restaurant_id), bg="#33cc33", fg="white", font=("Segoe UI", 10, "bold"))
            view_menu_button.pack(side="right", padx=10)

            # Location label (assuming restaurant_address exists)
            #restaurant_address = "Sample Address"  # Replace with actual address from data if available
            location_label = tk.Label(order_frame, text=f"{location}", font=("Segoe UI", 12), fg="black", bg="#f7f7f7")
            location_label.pack(anchor="w", pady=10)

            items = menu_items.split(',')
            quantities = quantities.split(',')

            items_frame = tk.Frame(order_frame, bg="#f7f7f7")
            items_frame.pack(pady=10)

            for item, quantity in zip(items, quantities):
                item_label = tk.Label(items_frame, text=f"{item} x {quantity}", font=("Segoe UI", 12), fg="black", bg="#f7f7f7")
                item_label.pack(anchor="w")

            # Footer frame for order date and total price
            footer_frame = tk.Frame(order_frame, bg="#f7f7f7")
            footer_frame.pack(fill="x", pady=10)

            order_date_label = tk.Label(footer_frame, text=f" {order_date}", font=("Segoe UI", 12), fg="black", bg="#f7f7f7")
            order_date_label.pack(side="left")

            total_price_label = tk.Label(footer_frame, text=f"Total Price: ₹{total_price}", font=("Segoe UI", 12, "bold"), fg="black", bg="#f7f7f7")
            total_price_label.pack(side="right")

    else:
        label = tk.Label(inner_frame, text="No orders to display.", font=("Segoe UI", 12), fg="gray")
        label.pack(pady=20)

    close_button = tk.Button(order_history_win, text="Back", command=order_history_win.destroy, bg="#ff9900", fg="white", font=("Segoe UI", 12))
    close_button.pack(pady=20)

def fetch_menu(restaurant_id):
    query = """
    SELECT m.menu_id, m.item_name, m.price
    FROM Menus m
    WHERE m.restaurant_id = %s
    """
    cursor.execute(query, (restaurant_id,))
    return cursor.fetchall()

def view_menu(restaurant_id):
    menu_window = tk.Toplevel(root) #type:ignore
    menu_window.title("Menu")
    menu_window.geometry("400x400")
    menu_window.configure(bg="#F7D2C4")

    menu_frame = tk.Frame(menu_window, bg="#f7f7f7")
    menu_frame.pack(fill="both", expand=True, padx=20, pady=20)

    menu = fetch_menu(restaurant_id)

    for item in menu:
        menu_id, food_name, price = item
        label = tk.Label(menu_frame, text=f"{food_name} - ₹{price}", font=("Segoe UI", 12), fg="black", bg="#f7f7f7")
        label.pack(pady=10)

    close_button = tk.Button(menu_window, text="Close", command=menu_window.destroy, bg="#ff9900", fg="white")
    close_button.pack(pady=20)

