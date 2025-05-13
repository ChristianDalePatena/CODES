import customtkinter as ctk
import tkinter.ttk as ttk
from tkinter import messagebox

def create_seller_dashboard(root):
    root.title("Seller Dashboard")
    root.geometry("800x600")
    root.configure(bg="#26547C")

    cart_items = []

    def clear_entries():
        item_name_entry.delete(0, ctk.END)
        description_entry.delete(0, ctk.END)
        quantity_entry.delete(0, ctk.END)

    def update_cart_list():
        cart_list.delete(*cart_list.get_children())
        for item in cart_items:
            cart_list.insert('', 'end', values=(item["name"], item["description"], item["price"], item["quantity"]))

    def add_to_cart():
        name = item_name_entry.get()
        description = description_entry.get()
        quantity_str = quantity_entry.get()

        if name and description and quantity_str:
            try:
                quantity = int(quantity_str)
                if quantity <= 0:
                    messagebox.showerror("Input Error", "Quantity must be greater than zero!")
                    return
                price = quantity * 10
                cart_items.append({"name": name, "description": description, "price": price, "quantity": quantity})
                update_cart_list()
                clear_entries()
            except ValueError:
                messagebox.showerror("Input Error", "Invalid quantity. Please enter a valid number!")
        else:
            messagebox.showerror("Input Error", "All fields must be filled!")

    def update_cart_item():
        selected_item = cart_list.selection()
        if selected_item:
            item_index = cart_list.index(selected_item)
            name = item_name_entry.get()
            description = description_entry.get()
            quantity_str = quantity_entry.get()

            if name and description and quantity_str:
                try:
                    quantity = int(quantity_str)
                    if quantity <= 0:
                        messagebox.showerror("Input Error", "Quantity must be greater than zero!")
                        return
                    price = quantity * 10
                    cart_items[item_index] = {"name": name, "description": description, "price": price, "quantity": quantity}
                    update_cart_list()
                    clear_entries()
                except ValueError:
                    messagebox.showerror("Input Error", "Invalid quantity. Please enter a valid number!")
            else:
                messagebox.showerror("Input Error", "All fields must be filled!")
        else:
            messagebox.showwarning("Select Item", "Please select an item in the cart to update.")

    def remove_from_cart():
        selected_item = cart_list.selection()
        if selected_item:
            item_index = cart_list.index(selected_item)
            del cart_items[item_index]
            update_cart_list()
            clear_entries()
        else:
            messagebox.showwarning("Select Item", "Please select an item to remove from the cart.")

    def logout():
        response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if response:
            root.destroy()

    # UI Components
    ctk.CTkLabel(root, text="Welcome Seller, Kyla!", text_color="#FFFFF0",
                 font=("Helvetica", 24, "bold")).place(relx=0.5, rely=0.05, anchor="n")

    # Item Name
    ctk.CTkLabel(root, text="Item Name", text_color="#FFFFF0").place(x=50, y=80, anchor="w")
    item_name_entry = ctk.CTkEntry(root, width=250, text_color="black")
    item_name_entry.place(x=50, y=105, anchor="w")

    # Description
    ctk.CTkLabel(root, text="Description", text_color="#FFFFF0").place(x=50, y=140, anchor="w")
    description_entry = ctk.CTkEntry(root, width=250, text_color="black")
    description_entry.place(x=50, y=165, anchor="w")

    # Quantity
    ctk.CTkLabel(root, text="Quantity", text_color="#FFFFF0").place(x=50, y=200, anchor="w")
    quantity_entry = ctk.CTkEntry(root, width=250, text_color="black")
    quantity_entry.place(x=50, y=225, anchor="w")

    # Buttons Frame
    button_frame = ctk.CTkFrame(root, fg_color="#26547C", width=260, height=110)
    button_frame.place(x=50, y=270, anchor="nw")

    ctk.CTkButton(button_frame, text="Add to Cart", command=add_to_cart,
                  fg_color="#FFFFF0", text_color="black", hover_color="#FFD166").place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.25)
    ctk.CTkButton(button_frame, text="Update Cart Item", command=update_cart_item,
                  fg_color="#FFFFF0", text_color="black", hover_color="#FFD166").place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.25)
    ctk.CTkButton(button_frame, text="Remove from Cart", command=remove_from_cart,
                  fg_color="#FFFFF0", text_color="black", hover_color="#FFD166").place(relx=0.05, rely=0.7, relwidth=0.9, relheight=0.25)

    # Logout Button
    ctk.CTkButton(root, text="Logout", command=logout,
                  fg_color="#06D6A0", text_color="black", hover_color="#FFFFF0").place(relx=0.97, rely=0.05, anchor="ne")

    # Cart Frame
    cart_frame = ctk.CTkFrame(root, fg_color="#26547C")
    cart_frame.place(relx=0.6, rely=0.15, relwidth=0.38, relheight=0.8, anchor="nw")

    cart_list = ttk.Treeview(cart_frame, columns=("Name", "Description", "Price", "Quantity"), show='headings')
    cart_list.heading("Name", text="Name", anchor="w")
    cart_list.heading("Description", text="Description", anchor="w")
    cart_list.heading("Price", text="Price", anchor="w")
    cart_list.heading("Quantity", text="Quantity", anchor="w")
    cart_list.column("Name", width=int(0.38 * 800 * 0.25), anchor="w")
    cart_list.column("Description", width=int(0.38 * 800 * 0.4), anchor="w")
    cart_list.column("Price", width=int(0.38 * 800 * 0.15), anchor="w")
    cart_list.column("Quantity", width=int(0.38 * 800 * 0.15), anchor="w")
    cart_list.place(relx=0, rely=0, relwidth=1, relheight=1)

# Run the function-based UI
if __name__ == "__main__":
    root = ctk.CTk()
    create_seller_dashboard(root)
    root.mainloop()
