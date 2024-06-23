from tkinter import *
from _mysql_connector import *
from Main_window import *
from user_authentication_zomato import *

if __name__ == "__main__":
    root = Tk()
    app = UserAuthentication(root)
    root.mainloop()
