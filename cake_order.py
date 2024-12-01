import tkinter as tk
from tkinter import ttk, messagebox

# Function to switch to the order summary window
def show_order_summary():
    flavor = flavor_var.get()
    size = size_var.get()
    decoration = decoration_var.get()

    # Validate inputs
    if not flavor or not size or not decoration:
        messagebox.showerror("Input Error", "Please select all options!")
        return

    # Update labels in the summary window
    summary_flavor_label.config(text=f"Flavor: {flavor}")
    summary_size_label.config(text=f"Size: {size}")
    summary_decoration_label.config(text=f"Decoration: {decoration}")

    # Show the summary window
    main_window.withdraw()
    summary_window.deiconify()

# Function to confirm the order
def confirm_order():
    messagebox.showinfo("Order Confirmed", "Thank you for your order!")
    summary_window.withdraw()
    main_window.deiconify()

# Function to exit the application
def exit_app():
    main_window.destroy()

# Main window
main_window = tk.Tk()
main_window.title("Moritas'Cake - Cake Order Form")
main_window.geometry("600x400")

# Variables for user input
flavor_var = tk.StringVar()
size_var = tk.StringVar()
decoration_var = tk.StringVar()

# Widgets for the main window
title_label = tk.Label(main_window, text="Moritas'Cake", font=("Arial", 24, "bold"), fg="purple")
title_label.pack(pady=10)

subtitle_label = tk.Label(main_window, text="Cake Order Form", font=("Arial", 16), fg="black")
subtitle_label.pack(pady=5)

flavor_label = tk.Label(main_window, text="Choose Flavor:", font=("Arial", 12))
flavor_label.pack()
flavor_menu = ttk.Combobox(main_window, textvariable=flavor_var, font=("Arial", 12))
flavor_menu['values'] = ("Pineapple", "Tres Leches", "Chocolate")
flavor_menu.pack(pady=5)

size_label = tk.Label(main_window, text="Choose Size:", font=("Arial", 12))
size_label.pack()
size_menu = ttk.Combobox(main_window, textvariable=size_var, font=("Arial", 12))
size_menu['values'] = ("Small", "Medium", "Large")
size_menu.pack(pady=5)

decoration_label = tk.Label(main_window, text="Choose Decoration:", font=("Arial", 12))
decoration_label.pack()
decoration_menu = ttk.Combobox(main_window, textvariable=decoration_var, font=("Arial", 12))
decoration_menu['values'] = ("Fruits", "Whipped Cream", "No Decoration")
decoration_menu.pack(pady=5)

continue_button = tk.Button(main_window, text="Show Order", command=show_order_summary, bg="lightgreen", font=("Arial", 12))
continue_button.pack(pady=20)

exit_button = tk.Button(main_window, text="Exit", command=exit_app, bg="red", font=("Arial", 12), fg="white")
exit_button.pack()

# Summary window
summary_window = tk.Toplevel(main_window)
summary_window.title("Order Summary")
summary_window.geometry("600x400")
summary_window.withdraw()

summary_label = tk.Label(summary_window, text="Selected Order Summary", font=("Arial", 20, "bold"))
summary_label.pack(pady=20)

summary_flavor_label = tk.Label(summary_window, text="Flavor: ", font=("Arial", 12))
summary_flavor_label.pack()
summary_size_label = tk.Label(summary_window, text="Size: ", font=("Arial", 12))
summary_size_label.pack()
summary_decoration_label = tk.Label(summary_window, text="Decoration: ", font=("Arial", 12))
summary_decoration_label.pack()

confirm_button = tk.Button(summary_window, text="Confirm Order", command=confirm_order, bg="lightgreen", font=("Arial", 12))
confirm_button.pack(pady=20)

# Run the application
main_window.mainloop()
