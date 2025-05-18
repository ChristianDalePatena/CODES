import tkinter
import pyodbc
from tkinter import *
from tkinter import messagebox, ttk, Toplevel
import customtkinter as ctk
from FUNCTIONS_DBMS import *
from customtkinter import *
from PIL import Image, ImageTk

set_appearance_mode("System")
set_default_color_theme("blue")  # Base theme, but we'll customize colors

# Colors extracted from your image
THEME_COLOR = "#26547c"      # Navy blue background
ACCENT_COLOR_ORANGE = "#ff6c00"  # Orange from "Farmers"
ACCENT_COLOR_GREEN = "#00b83f"   # Green from "Cubao"
ACCENT_COLOR_YELLOW = "#c8ff00"  # Yellow outline
FONT_COLOR = "white"        # White font for contrast
BUTTON_HOVER_COLOR = "#ff8a30"  # Lighter orange for hover

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Farmers Cubao")
        self.geometry("800x550")
        self.configure(fg_color=THEME_COLOR)  # Set the background to navy blue
        self.resizable(False, False)
        self.init_ui()

    def init_ui(self):
        try:
            # Load the logo image
            logo_path = r"C:\Users\Landaos\PycharmProjects\PythonProject\vibes.png"
            logo_image = ctk.CTkImage(light_image=Image.open(logo_path),
                                    dark_image=Image.open(logo_path),
                                    size=(300, 300))  # Keeping your size

            # Create a label with the image only (no text)
            self.logo_label = ctk.CTkLabel(self, image=logo_image, text="")
            self.logo_label.place(x=250, y=20)  # Position in top middle
        except Exception as e:
            print(f"Error loading image: {e}")

        # Username Entry - updated colors only
        self.user_id_input = ctk.CTkEntry(self,
                                        font=("Arial", 14),
                                        width=200, height=30,
                                        text_color=FONT_COLOR,
                                        fg_color="#1a3b5c",  # Slightly lighter than background
                                        border_color=ACCENT_COLOR_YELLOW,
                                        border_width=1)
        self.user_id_input.insert(0, "Please enter your username")
        self.user_id_input.place(x=300, y=250)
        self.user_id_input.bind("<FocusIn>", self.clear_placeholder_username)
        self.user_id_input.bind("<FocusOut>", self.add_placeholder_username)

        # Password Entry - updated colors only
        self.password_input = ctk.CTkEntry(self,
                                        font=("Arial", 14),
                                        width=200, height=30,
                                        text_color=FONT_COLOR,
                                        fg_color="#1a3b5c",  # Slightly lighter than background
                                        border_color=ACCENT_COLOR_YELLOW,
                                        border_width=1)
        self.password_input.insert(0, "Please enter your password")
        self.password_input.place(x=300, y=300)
        self.password_input.bind("<FocusIn>", self.clear_placeholder_password)
        self.password_input.bind("<FocusOut>", self.add_placeholder_password)

        # Login Button - orange from "Farmers"
        self.login_button = ctk.CTkButton(self, text="Login",
                                        command=self.login_function,
                                        fg_color=ACCENT_COLOR_ORANGE,
                                        text_color=FONT_COLOR,
                                        hover_color=BUTTON_HOVER_COLOR,
                                        font=("Arial", 14),
                                        width=105, height=40,
                                        border_width=1,
                                        border_color=ACCENT_COLOR_YELLOW)
        self.login_button.place(x=290, y=350)

        # Sign Up Button - green from "Cubao"
        self.signup_button = ctk.CTkButton(self, text="Sign Up",
                                        command=lambda: SignUpWindow(self),
                                        fg_color=ACCENT_COLOR_GREEN,
                                        text_color=FONT_COLOR,
                                        hover_color="#00d64a",  # Lighter green
                                        font=("Arial", 14),
                                        width=105, height=40,
                                        border_width=1,
                                        border_color=ACCENT_COLOR_YELLOW)
        self.signup_button.place(x=410, y=350)

    def clear_placeholder_username(self, event):
        if self.user_id_input.get() == "Please enter your username":
            self.user_id_input.delete(0, END)

    def add_placeholder_username(self, event):
        if not self.user_id_input.get():
            self.user_id_input.insert(0, "Please enter your username")

    def clear_placeholder_password(self, event):
        if self.password_input.get() == "Please enter your password":
            self.password_input.delete(0, END)
            self.password_input.configure(show="*")

    def add_placeholder_password(self, event):
        if not self.password_input.get():
            self.password_input.configure(show="")
            self.password_input.insert(0, "Please enter your password")

    def login_function(self):
        username = self.user_id_input.get()
        password = self.password_input.get()
        print(username, password)

        information = Login(username, password)

        if information:
            userID = information[0]
            userNAME = information[2]
            role = information[1]

            if role == "Consumer":
                self.create_consumer_dashboard(userID, userNAME)
            elif role == "Seller":
                self.create_seller_dashboard(userID, userNAME)
            elif role == "Admin":
                # Pass the admin ID and username to the dashboard
                create_admin_dashboard(userID, userNAME)
            else:
                messagebox.showerror("Login Failed", "Invalid user role.")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    class MainWindow(ctk.CTk):
        def __init__(self):
            super().__init__()
            self.title("Farmers Cubao")
            self.geometry("800x550")
            self.configure(fg_color=THEME_COLOR)  # Set the background to navy blue
            self.resizable(False, False)
            self.init_ui()

        def init_ui(self):
            try:
                # Load the logo image
                logo_path = r"C:\Users\Landaos\PycharmProjects\PythonProject\vibes.png"
                logo_image = ctk.CTkImage(light_image=Image.open(logo_path),
                                          dark_image=Image.open(logo_path),
                                          size=(300, 300))  # Keeping your size

                # Create a label with the image only (no text)
                self.logo_label = ctk.CTkLabel(self, image=logo_image, text="")
                self.logo_label.place(x=250, y=20)  # Position in top middle
            except Exception as e:
                print(f"Error loading image: {e}")

            # Username Entry - updated colors only
            self.user_id_input = ctk.CTkEntry(self,
                                              font=("Arial", 14),
                                              width=200, height=30,
                                              text_color=FONT_COLOR,
                                              fg_color="#1a3b5c",  # Slightly lighter than background
                                              border_color=ACCENT_COLOR_YELLOW,
                                              border_width=1)
            self.user_id_input.insert(0, "Please enter your username")
            self.user_id_input.place(x=300, y=250)
            self.user_id_input.bind("<FocusIn>", self.clear_placeholder_username)
            self.user_id_input.bind("<FocusOut>", self.add_placeholder_username)

            # Password Entry - updated colors only
            self.password_input = ctk.CTkEntry(self,
                                               font=("Arial", 14),
                                               width=200, height=30,
                                               text_color=FONT_COLOR,
                                               fg_color="#1a3b5c",  # Slightly lighter than background
                                               border_color=ACCENT_COLOR_YELLOW,
                                               border_width=1)
            self.password_input.insert(0, "Please enter your password")
            self.password_input.place(x=300, y=300)
            self.password_input.bind("<FocusIn>", self.clear_placeholder_password)
            self.password_input.bind("<FocusOut>", self.add_placeholder_password)

            # Login Button - orange from "Farmers"
            self.login_button = ctk.CTkButton(self, text="Login",
                                              command=self.login_function,
                                              fg_color=ACCENT_COLOR_ORANGE,
                                              text_color=FONT_COLOR,
                                              hover_color=BUTTON_HOVER_COLOR,
                                              font=("Arial", 14),
                                              width=105, height=40,
                                              border_width=1,
                                              border_color=ACCENT_COLOR_YELLOW)
            self.login_button.place(x=290, y=350)

            # Sign Up Button - green from "Cubao"
            self.signup_button = ctk.CTkButton(self, text="Sign Up",
                                               command=lambda: SignUpWindow(self),
                                               fg_color=ACCENT_COLOR_GREEN,
                                               text_color=FONT_COLOR,
                                               hover_color="#00d64a",  # Lighter green
                                               font=("Arial", 14),
                                               width=105, height=40,
                                               border_width=1,
                                               border_color=ACCENT_COLOR_YELLOW)
            self.signup_button.place(x=410, y=350)

        def clear_placeholder_username(self, event):
            if self.user_id_input.get() == "Please enter your username":
                self.user_id_input.delete(0, END)

        def add_placeholder_username(self, event):
            if not self.user_id_input.get():
                self.user_id_input.insert(0, "Please enter your username")

        def clear_placeholder_password(self, event):
            if self.password_input.get() == "Please enter your password":
                self.password_input.delete(0, END)
                self.password_input.configure(show="*")

        def add_placeholder_password(self, event):
            if not self.password_input.get():
                self.password_input.configure(show="")
                self.password_input.insert(0, "Please enter your password")

        def login_function(self):
            username = self.user_id_input.get()
            password = self.password_input.get()
            print(username, password)

            information = Login(username, password)

            if information:
                userID = information[0]
                userNAME = information[2]
                role = information[1]

                if role == "Consumer":
                    self.create_consumer_dashboard(userID, userNAME)
                elif role == "Seller":
                    self.create_seller_dashboard(userID, userNAME)
                elif role == "Admin":
                    # Pass the admin ID and username to the dashboard
                    create_admin_dashboard(userID, userNAME)
                else:
                    messagebox.showerror("Login Failed", "Invalid user role.")
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")

    def create_seller_dashboard(self, userID, userNAME):
        seller_window = ctk.CTkToplevel(self)
        seller_window.title("Seller Dashboard")
        seller_window.geometry("800x600")

        # Modern color scheme (matching consumer dashboard)
        primary_color = "#3a7ebf"
        accent_color = "#f0f0f0"
        text_color = "#333333"
        highlight_color = "#4CAF50"

        seller_window.configure(fg_color=accent_color)

        cart_items = []

        def clear_entries():
            item_name_entry.delete(0, ctk.END)
            description_entry.delete(0, ctk.END)
            quantity_entry.delete(0, ctk.END)

        def update_cart_list():
            cart_list.delete(*cart_list.get_children())
            for item in cart_items:
                cart_list.insert('', 'end', values=(item["name"], item["description"], item["price"], item["quantity"]))

        def update_cart_item():
            item_name_entry.configure(state=NORMAL)
            description_entry.configure(state=NORMAL)

            Product_Name = item_name_entry.get()
            Desc = description_entry.get()
            Quan = quantity_entry.get()
            Price = price_entry.get()

            update_check = update(Product_Name, Desc, Quan, Price)

            if update_check is True:
                messagebox.showinfo("Success", "Updated Market.")
                item_name_entry.delete(0, END)
                description_entry.delete(0, END)
                quantity_entry.delete(0, END)
                price_entry.delete(0, END)
            else:
                messagebox.showerror("Error", "Failed Update Market.")

        def remove_from_cart():
            item_name_entry.configure(state=NORMAL)
            description_entry.configure(state=NORMAL)

            Product_Name = item_name_entry.get()
            Desc = description_entry.get()
            Quan = quantity_entry.get()
            Price = price_entry.get()

            Remove_check = Remove(Product_Name, Desc, Quan, Price)

            if Remove_check is True:
                messagebox.showinfo("Success", "Remove from Market")
                item_name_entry.delete(0, END)
                description_entry.delete(0, END)
                quantity_entry.delete(0, END)
                price_entry.delete(0, END)

        def check_add_to_cart_result(item_name_entry, description_entry, quantity_entry, price_entry):
            result = add_to_cart(userID, userNAME, item_name_entry, description_entry, quantity_entry,
                                 price_entry)
            print("add_to_cart returned:", result)  # Print to console
            if result is True:
                messagebox.showinfo("Success", "Item added to market.")
            else:
                messagebox.showerror("Error", "Failed to add item.")

        def SELECTED(e):
            selected = cart_list.focus()
            values = cart_list.item(selected, 'values')
            if not values or len(values) < 4:
                return  # Prevents IndexError

            item_name_entry.delete(0, END)
            description_entry.delete(0, END)
            quantity_entry.delete(0, END)
            price_entry.delete(0, END)

            item_name_entry.insert(0, values[0])
            description_entry.insert(0, values[1])
            quantity_entry.insert(0, values[2])
            price_entry.insert(0, values[3])

            item_name_entry.configure(state=DISABLED)
            description_entry.configure(state=DISABLED)

        def refresh_market():
            products = refresh(userID, userNAME)
            item_name_entry.configure(state=NORMAL)
            description_entry.configure(state=NORMAL)

            if products:
                for item in cart_list.get_children():
                    cart_list.delete(item)

                counter = 1
                for product in products:
                    counter += 1
                    cart_list.insert('', 'end', text=f'{counter}', values=(
                        f'{product[3]}', f'{product[4]}', f'{product[5]}', f'{product[6]}'))

        def logout():
            response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
            if response:
                seller_window.destroy()  # Close the seller window

        # Header frame
        header_frame = ctk.CTkFrame(seller_window, fg_color=primary_color, corner_radius=0, height=70)
        header_frame.pack(fill="x")

        # Welcome message
        welcome_label = ctk.CTkLabel(
            header_frame,
            text=f"Welcome Seller, {userNAME}!",
            text_color="white",
            font=("Arial", 20, "bold")
        )
        welcome_label.place(x=18, y=18)

        # Logout Button
        logout_button = ctk.CTkButton(
            header_frame,
            text="Logout",
            fg_color="#e74c3c",  # Red color for logout
            text_color="white",
            width=100,
            height=30,
            hover_color="#c0392b",
            corner_radius=5,
            command=logout
        )
        logout_button.place(x=680, y=20)

        # Content frame
        content_frame = ctk.CTkFrame(seller_window, fg_color=accent_color)
        content_frame.pack(fill="both", expand=True, padx=0, pady=0)

        # Left panel for product input
        input_panel = ctk.CTkFrame(content_frame, fg_color="#f8f9fa", corner_radius=10, width=280)
        input_panel.pack(side="left", fill="y", padx=10, pady=10)

        # Product input fields
        input_title = ctk.CTkLabel(
            input_panel,
            text="Product Information",
            font=("Arial", 14, "bold"),
            text_color=text_color
        )
        input_title.pack(pady=(15, 15))

        # Item Name
        item_name_label = ctk.CTkLabel(input_panel, text="Product Name", text_color=text_color)
        item_name_label.pack(anchor="w", padx=15, pady=(10, 0))
        item_name_entry = ctk.CTkEntry(input_panel, width=250, text_color=text_color)
        item_name_entry.pack(padx=15, pady=(5, 10))

        # Description
        description_label = ctk.CTkLabel(input_panel, text="Description", text_color=text_color)
        description_label.pack(anchor="w", padx=15, pady=(10, 0))
        description_entry = ctk.CTkEntry(input_panel, width=250, text_color=text_color)
        description_entry.pack(padx=15, pady=(5, 10))

        # Quantity
        quantity_label = ctk.CTkLabel(input_panel, text="Quantity", text_color=text_color)
        quantity_label.pack(anchor="w", padx=15, pady=(10, 0))
        quantity_entry = ctk.CTkEntry(input_panel, width=250, text_color=text_color)
        quantity_entry.pack(padx=15, pady=(5, 10))

        # Price
        price_label = ctk.CTkLabel(input_panel, text="Price", text_color=text_color)
        price_label.pack(anchor="w", padx=15, pady=(10, 0))
        price_entry = ctk.CTkEntry(input_panel, width=250, text_color=text_color)
        price_entry.pack(padx=15, pady=(5, 10))

        # Buttons Frame
        button_frame = ctk.CTkFrame(input_panel, fg_color="transparent", width=260)
        button_frame.pack(pady=20, fill="x", padx=15)

        # Add to Market Button
        add_button = ctk.CTkButton(
            button_frame,
            text="Add to Market",
            command=lambda: check_add_to_cart_result(item_name_entry.get(), description_entry.get(),
                                                     quantity_entry.get(), price_entry.get()),
            fg_color=highlight_color,
            text_color="white",
            hover_color="#3daa40",
            height=35
        )
        add_button.pack(fill="x", pady=(0, 10))

        # Update Market Button
        update_button = ctk.CTkButton(
            button_frame,
            text="Update Market",
            command=update_cart_item,
            fg_color="#3498db",
            text_color="white",
            hover_color="#2980b9",
            height=35
        )
        update_button.pack(fill="x", pady=(0, 10))

        # Remove Market Button
        remove_button = ctk.CTkButton(
            button_frame,
            text="Remove from Market",
            command=remove_from_cart,
            fg_color="#e74c3c",
            text_color="white",
            hover_color="#c0392b",
            height=35
        )
        remove_button.pack(fill="x", pady=(0, 10))

        # Refresh Market Button
        refresh_button = ctk.CTkButton(
            button_frame,
            text="Refresh Market",
            command=refresh_market,
            fg_color="#f39c12",
            text_color="white",
            hover_color="#d35400",
            height=35
        )
        refresh_button.pack(fill="x", pady=(0, 10))

        # Right panel for market items
        market_panel = ctk.CTkFrame(content_frame, fg_color="white", corner_radius=10)
        market_panel.pack(side="right", fill="both", expand=True, padx=10, pady=10, ipadx=10, ipady=10)

        # Market title
        market_title = ctk.CTkLabel(
            market_panel,
            text="Your Market Items",
            font=("Arial", 16, "bold"),
            text_color=text_color
        )
        market_title.pack(pady=(15, 15))

        # Create Treeview for product list
        style = ttk.Style()
        style.configure("Treeview",
                        background="white",
                        foreground="black",
                        rowheight=22,
                        fieldbackground="white")
        style.map('Treeview', background=[('selected', primary_color)])

        # Treeview frame
        tree_frame = ctk.CTkFrame(market_panel, fg_color="white")
        tree_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Scrollbar for the Treeview (using traditional tkinter)
        scrollbar = Scrollbar(tree_frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Treeview
        cart_list = ttk.Treeview(
            tree_frame,
            columns=("Name", "Description", "Price", "Quantity"),
            show='headings',
            yscrollcommand=scrollbar.set
        )

        # Configure columns
        cart_list.heading("Name", text="Name", anchor="w")
        cart_list.heading("Description", text="Description", anchor="w")
        cart_list.heading("Price", text="Price", anchor="w")
        cart_list.heading("Quantity", text="Quantity", anchor="w")

        cart_list.column("Name", width=110, anchor="w")
        cart_list.column("Description", width=180, anchor="w")
        cart_list.column("Price", width=70, anchor="w")
        cart_list.column("Quantity", width=70, anchor="w")

        cart_list.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.config(command=cart_list.yview)

        # Bind selection event
        cart_list.bind("<ButtonRelease-1>", SELECTED)

        # Load market items on start
        refresh_market()

    def create_consumer_dashboard(self, User_ID, userNAME):
        import customtkinter as ctk
        from PIL import Image, ImageTk
        import pyodbc
        from tkinter import messagebox

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        window = ctk.CTk()
        window.title("Consumer Dashboard")
        window.geometry("900x600")
        window.resizable(False, False)

        # Modern color scheme
        primary_color = "#3a7ebf"
        accent_color = "#f0f0f0"
        text_color = "#333333"
        highlight_color = "#4CAF50"

        # Create frames for layout
        header_frame = ctk.CTkFrame(window, fg_color=primary_color, corner_radius=0, height=70)
        header_frame.pack(fill="x")

        content_frame = ctk.CTkFrame(window, fg_color=accent_color)
        content_frame.pack(fill="both", expand=True, padx=0, pady=0)

        # Header elements
        header_label = ctk.CTkLabel(
            header_frame,
            text=f"Welcome, {userNAME}!",
            text_color="white",
            font=("Arial", 22, "bold")
        )
        header_label.place(x=20, y=20)

        # Cart and items count display
        cart_items = 0
        cart_label = ctk.CTkLabel(
            header_frame,
            text=f"Cart: {cart_items} items",
            text_color="white",
            font=("Arial", 14)
        )
        cart_label.place(x=700, y=15)

        logout_button = ctk.CTkButton(
            header_frame,
            text="Logout",
            fg_color="#e74c3c",
            text_color="white",
            width=100,
            height=30,
            hover_color="#c0392b",
            corner_radius=5,
            command=window.quit
        )
        logout_button.place(x=780, y=20)

        # Left sidebar for actions
        sidebar_frame = ctk.CTkFrame(content_frame, fg_color="#2c3e50", width=200, corner_radius=0)
        sidebar_frame.pack(side="left", fill="y", padx=0, pady=0)

        # Product display area
        product_area = ctk.CTkFrame(content_frame, fg_color="white", corner_radius=0)
        product_area.pack(side="right", fill="both", expand=True)

        # Shopping cart to store selected items (now includes quantity)
        shopping_cart = []
        products = []  # Initialize products in the outer scope

        # Function to add product to cart
        # Function to add product to cart
        def add_to_cart(product_id):
            nonlocal cart_items
            nonlocal products
            selected_product_row = next((p for p in products if p[0] == product_id), None)
            if selected_product_row:
                selected_product_tuple = tuple(selected_product_row)  # Convert pyodbc.Row to tuple
                # For simplicity, let's assume adding always adds 1 kg.
                # In a real application, you'd have a quantity input.
                shopping_cart.append(selected_product_tuple + (1,))  # Add a tuple with quantity (1)
                cart_items += 1
                cart_label.configure(text=f"Cart: {cart_items} items")
                update_cart_display()

        # Function to remove product from cart
        def remove_from_cart(product_id):
            nonlocal cart_items
            for i, item in enumerate(shopping_cart):
                if item[0] == product_id:
                    shopping_cart.pop(i)
                    cart_items -= 1
                    cart_label.configure(text=f"Cart: {cart_items} items")
                    update_cart_display()
                    break

        # Function to view cart
        def view_cart():
            cart_window = ctk.CTkToplevel(window)
            cart_window.title("Your Shopping Cart")
            cart_window.geometry("600x400")

            if not shopping_cart:
                empty_label = ctk.CTkLabel(
                    cart_window,
                    text="Your cart is empty",
                    font=("Arial", 16)
                )
                empty_label.pack(pady=30)
            else:
                # Display items in cart
                header_frame = ctk.CTkFrame(cart_window)
                header_frame.pack(fill="x", padx=10, pady=10)

                ctk.CTkLabel(header_frame, text="Product", font=("Arial", 14, "bold")).grid(row=0, column=0, padx=10)
                ctk.CTkLabel(header_frame, text="Quantity (kg)", font=("Arial", 14, "bold")).grid(row=0, column=1,
                                                                                                  padx=10)
                ctk.CTkLabel(header_frame, text="Price", font=("Arial", 14, "bold")).grid(row=0, column=2, padx=10)
                ctk.CTkLabel(header_frame, text="Actions", font=("Arial", 14, "bold")).grid(row=0, column=3, padx=10)

                cart_frame = ctk.CTkScrollableFrame(cart_window, height=250)
                cart_frame.pack(fill="both", expand=True, padx=10)

                total = 0
                for i, item in enumerate(shopping_cart):
                    product_id, product_name, description, price, quantity_in_stock, purchased_quantity = item
                    total += price * purchased_quantity

                    ctk.CTkLabel(cart_frame, text=product_name).grid(row=i, column=0, sticky="w", padx=10, pady=5)
                    ctk.CTkLabel(cart_frame, text=str(purchased_quantity)).grid(row=i, column=1, padx=10, pady=5)
                    ctk.CTkLabel(cart_frame, text=f"₱{price * purchased_quantity:.2f}").grid(row=i, column=2, padx=10,
                                                                                             pady=5)

                    remove_btn = ctk.CTkButton(
                        cart_frame,
                        text="Remove",
                        fg_color="#e74c3c",
                        text_color="white",
                        width=80,
                        command=lambda pid=product_id: remove_from_cart(pid)
                    )
                    remove_btn.grid(row=i, column=3, padx=10, pady=5)

                total_frame = ctk.CTkFrame(cart_window)
                total_frame.pack(fill="x", padx=10, pady=10)

                ctk.CTkLabel(
                    total_frame,
                    text=f"Total: ₱{total:.2f}",
                    font=("Arial", 16, "bold")
                ).pack(side="left", padx=10)

                checkout_btn = ctk.CTkButton(
                    total_frame,
                    text="Proceed to Checkout",
                    fg_color=highlight_color,
                    text_color="white",
                    width=150,
                    command=lambda: checkout()
                )
                checkout_btn.pack(side="right", padx=10)

        def checkout():
            if not shopping_cart:
                return

            checkout_window = ctk.CTkToplevel(window)
            checkout_window.title("Checkout")
            checkout_window.geometry("400x300")

            ctk.CTkLabel(
                checkout_window,
                text="Order Completed!",
                font=("Arial", 20, "bold")
            ).pack(pady=20)

            total = sum(
                item[3] * item[5] for item in shopping_cart)  # Calculate total based on price and purchased quantity

            ctk.CTkLabel(
                checkout_window,
                text=f"Total paid: ₱{total:.2f}",
                font=("Arial", 16)
            ).pack(pady=10)

            ctk.CTkLabel(
                checkout_window,
                text=f"Thank you for your purchase, {userNAME}!",
                font=("Arial", 14)
            ).pack(pady=10)

            # Clear cart after checkout
            shopping_cart.clear()
            nonlocal cart_items
            cart_items = 0
            cart_label.configure(text=f"Cart: {cart_items} items")

            close_btn = ctk.CTkButton(
                checkout_window,
                text="Close",
                command=checkout_window.destroy
            )
            close_btn.pack(pady=20)

        # Function to update cart display (currently empty)
        def update_cart_display():
            pass

        # Create sidebar buttons
        button_data = [
            {"text": "View Products", "command": lambda: display_products()},
            {"text": "View Cart", "command": lambda: view_cart()},
            {"text": "My Orders", "command": lambda: display_message("Order history will be shown here")},
            {"text": "My Profile", "command": lambda: display_message(f"Profile for {userNAME} (ID: {User_ID})")},
            {"text": "Settings", "command": lambda: display_message("Settings will be shown here")},
        ]

        for i, btn in enumerate(button_data):
            action_btn = ctk.CTkButton(
                sidebar_frame,
                text=btn["text"],
                fg_color="transparent",
                text_color="white",
                hover_color="#34495e",
                anchor="w",
                height=40,
                command=btn["command"]
            )
            action_btn.pack(fill="x", padx=10, pady=(10 if i == 0 else 5))

        # Display a message in the product area
        def display_message(message):
            for widget in product_area.winfo_children():
                widget.destroy()

            message_label = ctk.CTkLabel(
                product_area,
                text=message,
                font=("Arial", 16)
            )
            message_label.pack(pady=50)

        # Display products in the product area
        def display_products():
            nonlocal products
            for widget in product_area.winfo_children():
                widget.destroy()

            scroll_frame = ctk.CTkScrollableFrame(product_area)
            scroll_frame.pack(fill="both", expand=True, padx=20, pady=20)

            header_frame = ctk.CTkFrame(scroll_frame)
            header_frame.pack(fill="x", pady=(0, 10))

            headers = ["Product", "Description", "Price", "Available (kg)", "Action"]
            for i, header in enumerate(headers):
                label = ctk.CTkLabel(
                    header_frame,
                    text=header,
                    font=("Arial", 14, "bold")
                )
                label.grid(row=0, column=i, padx=10, sticky="w")

            try:
                cursor = connect.cursor()
                cursor.execute(
                    "SELECT Product_ID, Product_Name, Description, Price, Quantity FROM Products")
                products = cursor.fetchall()

                for i, product in enumerate(products):
                    frame = ctk.CTkFrame(scroll_frame, fg_color=("#f9f9f9" if i % 2 == 0 else "white"))
                    frame.pack(fill="x", pady=5)

                    ctk.CTkLabel(
                        frame,
                        text=product[1],
                        font=("Arial", 13)
                    ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

                    ctk.CTkLabel(
                        frame,
                        text=product[2],
                        font=("Arial", 13)
                    ).grid(row=0, column=1, padx=10, pady=10, sticky="w")

                    ctk.CTkLabel(
                        frame,
                        text=f"₱{product[3]:.2f}",
                        font=("Arial", 13, "bold")
                    ).grid(row=0, column=2, padx=10, pady=10, sticky="w")

                    ctk.CTkLabel(
                        frame,
                        text=str(product[4]),
                        font=("Arial", 13)
                    ).grid(row=0, column=3, padx=10, pady=10, sticky="w")

                    add_button = ctk.CTkButton(
                        frame,
                        text="Add to Cart",
                        fg_color=highlight_color,
                        text_color="white",
                        width=100,
                        height=30,
                        corner_radius=5,
                        command=lambda pid=product[0]: add_to_cart(pid)
                    )
                    add_button.grid(row=0, column=4, padx=10, pady=10)

            except pyodbc.Error as e:
                messagebox.showerror("Database Error", f"Error fetching products: {e}")

        # Show products by default when the dashboard opens
        display_products()

        window.mainloop()


def create_admin_dashboard(admin_id, admin_name):
    """
    Creates an admin dashboard window that displays all user accounts
    with options to delete any account.

    Args:
        admin_id: The ID of the admin user
        admin_name: The username of the admin user
    """
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("800x550")
    root.title("Admin Dashboard")
    root.resizable(False, False)
    root.configure(fg_color="#26547C")  # Using fg_color instead of bg for CTk

    # --- Welcome Label ---
    welcome_label = ctk.CTkLabel(
        root, text=f"Welcome Admin, {admin_name}!",
        font=('Arial', 20, 'bold'),
        text_color="white"
    )
    welcome_label.place(x=20, y=20)

    # --- Logout Button ---
    logout_button = ctk.CTkButton(
        root, text="Logout",
        width=70, height=30,
        fg_color="#A8E6CF", text_color="black",
        hover_color="#96dbc6", corner_radius=12,
        command=root.destroy
    )
    logout_button.place(x=700, y=20)

    # --- Accounts List Frame ---
    accounts_frame = ctk.CTkFrame(
        root, fg_color="white",
        corner_radius=20, width=550, height=450
    )
    accounts_frame.place(x=30, y=70)

    header_label = ctk.CTkLabel(
        accounts_frame, text="All User Accounts",
        text_color="black", font=('Arial', 16, 'bold')
    )
    header_label.place(x=200, y=10)

    # Configure treeview style
    style = ttk.Style()
    style.configure("Treeview",
                    background="#F0F0F0",
                    foreground="black",
                    rowheight=25,
                    fieldbackground="#F0F0F0")
    style.map('Treeview', background=[('selected', '#3584e4')])

    # Create Treeview with standard scrollbar (not CTkScrollbar)
    # Standard tkinter Frame to hold the treeview and scrollbar
    tree_frame = Frame(accounts_frame, bg="white")
    tree_frame.place(x=10, y=45, width=530, height=390)

    # Standard tkinter Scrollbar
    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Create Treeview
    accounts_tree = ttk.Treeview(tree_frame,
                                 columns=("ID", "Username", "Role", "Status"),
                                 show='headings',
                                 yscrollcommand=tree_scroll.set)

    # Configure columns
    accounts_tree.heading("ID", text="User ID")
    accounts_tree.heading("Username", text="Username")
    accounts_tree.heading("Role", text="Role")
    accounts_tree.heading("Status", text="Status")

    accounts_tree.column("ID", width=50, anchor="center")
    accounts_tree.column("Username", width=150, anchor="w")
    accounts_tree.column("Role", width=100, anchor="center")
    accounts_tree.column("Status", width=100, anchor="center")

    # Pack treeview
    accounts_tree.pack(side=LEFT, fill=BOTH, expand=True)

    # Connect scrollbar to treeview
    tree_scroll.config(command=accounts_tree.yview)

    # --- Action Buttons ---
    buttons_frame = ctk.CTkFrame(
        root, fg_color="#26547C",
        corner_radius=20, width=180, height=300
    )
    buttons_frame.place(x=600, y=100)

    # Refresh button
    refresh_button = ctk.CTkButton(
        buttons_frame, text="Refresh List",
        width=150, height=40,
        fg_color="#DCEDC1", text_color="black",
        hover_color="#C8E6B7",
        corner_radius=12,
        command=lambda: load_all_accounts(accounts_tree)
    )
    refresh_button.place(x=15, y=20)

    # Delete account button
    delete_button = ctk.CTkButton(
        buttons_frame, text="Delete Account",
        width=150, height=40,
        fg_color="#FF6B6B", text_color="white",
        hover_color="#FF4949",
        corner_radius=12,
        command=lambda: delete_selected_account(accounts_tree)
    )
    delete_button.place(x=15, y=80)

    # Function to load all accounts from database
    def load_all_accounts(tree):
        # Clear existing items
        for item in tree.get_children():
            tree.delete(item)

        try:
            # Connect to database
            cursor = connect.cursor()

            # Fetch all accounts
            cursor.execute(
                "SELECT User_Id, Username, Role_type, CASE WHEN Verified IS NULL THEN 'Pending' WHEN Verified = 1 THEN 'Verified' ELSE 'Rejected' END as Status FROM Users")
            accounts = cursor.fetchall()

            # Insert accounts into treeview
            for account in accounts:
                # Skip the admin viewing the dashboard to prevent self-deletion
                if account[0] != admin_id:
                    tree.insert("", "end", values=(account[0], account[1], account[2], account[3]))

        except pyodbc.Error as e:
            messagebox.showerror("Database Error", f"Failed to load accounts: {str(e)}")

    # Function to delete selected account
    def delete_selected_account(tree):
        selected_item = tree.selection()

        if not selected_item:
            messagebox.showwarning("No Selection", "Please select an account to delete.")
            return

        account_values = tree.item(selected_item, "values")
        user_id = account_values[0]
        username = account_values[1]

        # Confirm deletion
        confirm = messagebox.askyesno("Confirm Deletion",
                                      f"Are you sure you want to delete account:\n\nID: {user_id}\nUsername: {username}?\n\nThis action cannot be undone.")

        if confirm:
            try:
                cursor = connect.cursor()

                # First delete any related records
                # For example: delete from Consumers, Sellers or Admin tables first
                cursor.execute("DELETE FROM Consumers WHERE Users_ID_FK = ?", (user_id,))
                cursor.execute("DELETE FROM Sellers WHERE User_ID_FK = ?", (user_id,))
                cursor.execute("DELETE FROM Admin WHERE User_ID_FK = ?", (user_id,))

                # Then delete the main user record
                cursor.execute("DELETE FROM Users WHERE User_Id = ?", (user_id,))
                connect.commit()

                # Remove from treeview
                tree.delete(selected_item)

                messagebox.showinfo("Success", f"Account '{username}' has been deleted.")

            except pyodbc.Error as e:
                connect.rollback()
                messagebox.showerror("Delete Error", f"Failed to delete account: {str(e)}")

    # Load accounts when the dashboard is opened
    load_all_accounts(accounts_tree)

    root.mainloop()


class SignUpWindow(ctk.CTkToplevel):
    def __init__(self, main_window):
        super().__init__(main_window)  # Correct super() call
        self.main_window = main_window
        self.title("Sign Up")
        self.geometry("450x320")
        self.configure(fg_color=THEME_COLOR)
        self.resizable(False, False)
        self.init_ui()

    def init_ui(self):
        self.title_label = ctk.CTkLabel(self, text="Create an Account",
                                      fg_color="transparent",
                                      text_color=ACCENT_COLOR_YELLOW,
                                      font=("Arial", 20, "bold"))
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        self.username_input = ctk.CTkEntry(self, font=("Arial", 14),
                                         text_color=FONT_COLOR,
                                         fg_color="#1a3b5c",
                                         border_color=ACCENT_COLOR_YELLOW,
                                         border_width=1,
                                         width=250, height=30)
        self.username_input.place(relx=0.5, rely=0.3, anchor="center")

        self.password_input = ctk.CTkEntry(self, font=("Arial", 14),
                                         text_color=FONT_COLOR,
                                         fg_color="#1a3b5c",
                                         border_color=ACCENT_COLOR_YELLOW,
                                         border_width=1,
                                         width=250, height=30)
        self.password_input.place(relx=0.5, rely=0.45, anchor="center")

        self.role_label = ctk.CTkLabel(self, text="Sign-up as?",
                                     fg_color="transparent",
                                     text_color=ACCENT_COLOR_YELLOW)
        self.role_label.place(relx=0.5, rely=0.6, anchor="center")

        self.role_combo = ctk.CTkOptionMenu(self,
                                          values=["Consumer", "Seller", "Admin"],
                                          fg_color="#1a3b5c",
                                          button_color=ACCENT_COLOR_ORANGE,
                                          button_hover_color=BUTTON_HOVER_COLOR,
                                          dropdown_fg_color="#1a3b5c",
                                          dropdown_hover_color=BUTTON_HOVER_COLOR,
                                          text_color=FONT_COLOR,
                                          width=250, height=30)
        self.role_combo.place(relx=0.5, rely=0.75, anchor="center")

        self.signup_button = ctk.CTkButton(self, text="Submit",
                                         command=self.submit_signup,
                                         fg_color=ACCENT_COLOR_ORANGE,
                                         text_color=FONT_COLOR,
                                         hover_color=BUTTON_HOVER_COLOR,
                                         font=("Arial", 14),
                                         border_width=1,
                                         border_color=ACCENT_COLOR_YELLOW,
                                         width=100, height=40)
        self.signup_button.place(relx=0.5, rely=0.9, anchor="center")

        self.back_button = ctk.CTkButton(self, text="🡸",
                                       command=self.back_function,
                                       fg_color=ACCENT_COLOR_ORANGE,
                                       text_color=FONT_COLOR,
                                       hover_color=BUTTON_HOVER_COLOR,
                                       width=50, height=30)
        self.back_button.place(x=10, y=10)

    def clear_placeholder_username(self, event):  # Corrected method name
        if self.username_input.get() == "Create a username":
            self.username_input.delete(0, ctk.END)

    def add_placeholder_username(self, event): # Corrected method name
        if not self.username_input.get():
            self.username_input.insert(0, "Create a username")

    def clear_placeholder_password(self, event): # Corrected method name
        if self.password_input.get() == "Create a password":
            self.password_input.delete(0, ctk.END)
            self.password_input.configure(show="●")

    def add_placeholder_password(self, event): # Corrected method name
        if not self.password_input.get():
            self.password_input.configure(show="")
            self.password_input.insert(0, "Create a password")

    def submit_signup(self):
        username = self.username_input.get()
        password = self.password_input.get()
        role = self.role_combo.get()

        #  Assume SignUp  handles the  actual  database  interaction
        try:
            SignUp(role, username, password) #  Call  your  SignUp  function
            messagebox.showinfo("Success", "Account created successfully!")
            self.destroy() # close window on success
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create account: {e}")

    def back_function(self):
        self.destroy()


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()