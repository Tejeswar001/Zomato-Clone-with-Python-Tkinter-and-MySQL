import tkinter as tk
from PIL import Image, ImageTk

class ZomatoRegisterPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Zomato Registration")
        self.geometry("1000x600")
        self.configure(bg="#f0ead6")

        self.create_widgets()

    def create_widgets(self):
        # Left section for branding and image
        left_frame = tk.Frame(self, bg="#000000", width=500)
        left_frame.grid(row=0, column=0, sticky="nsew")
        left_frame.pack_propagate(False)  # Prevents the frame from resizing

        # Load and display the image
        image_path = "G:/Tkinter/zomato clone tkinter mysql/zomato.jpg" 
        image = Image.open(image_path)
        width, height = image.size
        aspect_ratio = width / height
        new_height = 600
        new_width = int(new_height * aspect_ratio)
        image = image.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)

        image_label = tk.Label(left_frame, image=photo, bg="#000000")
        image_label.image = photo  # Keep a reference to avoid garbage collection
        image_label.place(relx=0.5, rely=0.5, anchor="center")

        # Right section for the registration form
        right_frame = tk.Frame(self, bg="#ffffff")
        right_frame.grid(row=0, column=1, sticky="nsew", padx=50)
        right_frame.grid_columnconfigure(0, weight=1)

        # Form title
        title_label = tk.Label(right_frame, text="Register", font=("Helvetica", 28, "bold"), bg="#ffffff", fg="#333333")
        title_label.grid(row=0, column=0, pady=20)

        form_frame = tk.Frame(right_frame, bg="#ffffff")
        form_frame.grid(row=1, column=0, pady=10, sticky="ew")

        self.create_form_row(form_frame, "Username:", 0)
        self.create_form_row(form_frame, "Password:", 1, show='*')
        self.create_form_row(form_frame, "Phone no:", 2)

        # Buttons
        button_frame = tk.Frame(right_frame, bg="#ffffff")
        button_frame.grid(row=2, column=0, pady=20)

        sign_in_button = tk.Button(button_frame, text="Sign Up", font=("Helvetica", 14, "bold"), bg="red", fg="white", width=15, height=2)
        sign_in_button.grid(row=0, column=0, pady=10)

        log_in_button = tk.Button(button_frame, text="Log In", font=("Helvetica", 14, "bold"), bg="#2980b9", fg="white", width=15, height=2)
        log_in_button.grid(row=1, column=0, pady=10)

        # Grid configuration for responsiveness
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def create_form_row(self, parent, label_text, row, **kwargs):
        label = tk.Label(parent, text=label_text, font=("Helvetica", 16), bg="#ffffff", fg="#333333")
        label.grid(row=row, column=0, padx=20, pady=10, sticky="w")

        entry = tk.Entry(parent, font=("Helvetica", 16), **kwargs)
        entry.grid(row=row, column=1, padx=20, pady=10, sticky="ew")

        parent.grid_columnconfigure(1, weight=1)

if __name__ == "__main__":
    app = ZomatoRegisterPage()
    app.mainloop()
