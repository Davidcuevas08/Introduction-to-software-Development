import tkinter as tk
from tkinter import ttk, messagebox

# Function to switch to the order summary window
def show_order_summary():
    """
    Validates user inputs and displays the order summary window.
    Ensures that flavor, size, and decoration are selected before proceeding.
    """
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
    """
    Confirms the order and returns the user to the main window.
    Displays a thank-you message upon confirmation.
    """
    messagebox.showinfo("Order Confirmed", "Thank you for your order!")
    summary_window.withdraw()
    main_window.deiconify()

# Function to exit the application
def exit_app():
    """
    Closes the application gracefully when the user selects the Exit button.
    """
    main_window.destroy()

# Main window
main_window = tk.Tk()  # Create the main application window
main_window.title("Moritas'Cake - Cake Order Form")  # Set the window title
main_window.geometry("600x500")  # Define the size of the window

# Variables for user input
flavor_var = tk.StringVar()  # Stores the selected cake flavor
size_var = tk.StringVar()    # Stores the selected cake size
decoration_var = tk.StringVar()  # Stores the selected decoration

# Load images for the thumbnails
try:
    image1 = tk.PhotoImage(file="images/image1.png").subsample(3, 3)  # Load and resize image 1
    image2 = tk.PhotoImage(file="images/image2.png").subsample(3, 3)  # Load and resize image 2
    image3 = tk.PhotoImage(file="images/image3.png").subsample(3, 3)  # Load and resize image 3
except Exception as e:
    messagebox.showerror("Image Error", f"Error loading images: {e}")  # Display error if images fail to load
    image1 = image2 = image3 = None  # Set images to None if loading fails

# Widgets for the main window
title_label = tk.Label(main_window, text="Moritas'Cake", font=("Arial", 24, "bold"), fg="purple")
# Title label for the application
title_label.pack(pady=10)  # Add padding to the title label

subtitle_label = tk.Label(main_window, text="Cake Order Form", font=("Arial", 16), fg="black")
# Subtitle label for the application
subtitle_label.pack(pady=5)

flavor_label = tk.Label(main_window, text="Choose Flavor:", font=("Arial", 12))  # Label for flavor selection
flavor_label.pack()
flavor_menu = ttk.Combobox(main_window, textvariable=flavor_var, font=("Arial", 12))
# Dropdown menu for selecting flavor
flavor_menu['values'] = ("Pineapple", "Tres Leches", "Chocolate")  # Set flavor options
flavor_menu.pack(pady=5)

size_label = tk.Label(main_window, text="Choose Size:", font=("Arial", 12))  # Label for size selection
size_label.pack()
size_menu = ttk.Combobox(main_window, textvariable=size_var, font=("Arial", 12))
# Dropdown menu for selecting size
size_menu['values'] = ("Small", "Medium", "Large")  # Set size options
size_menu.pack(pady=5)

decoration_label = tk.Label(main_window, text="Choose Decoration:", font=("Arial", 12))  # Label for decoration selection
decoration_label.pack()
decoration_menu = ttk.Combobox(main_window, textvariable=decoration_var, font=("Arial", 12))
# Dropdown menu for selecting decoration
decoration_menu['values'] = ("Fruits", "Whipped Cream", "No Decoration")  # Set decoration options
decoration_menu.pack(pady=5)

continue_button = tk.Button(main_window, text="Show Order", command=show_order_summary, bg="lightgreen", font=("Arial", 12))
# Button to proceed to order summary
continue_button.pack(pady=20)

exit_button = tk.Button(main_window, text="Exit", command=exit_app, bg="red", font=("Arial", 12), fg="white")
# Button to exit the application
exit_button.pack(pady=10)

# Add the three small images at the bottom
thumbnail_frame = tk.Frame(main_window)  # Frame to hold the thumbnails
thumbnail_frame.pack(pady=10)

if image1:  # Display the first image if it loaded successfully
    img1_label = tk.Label(thumbnail_frame, image=image1)
    img1_label.pack(side="left", padx=10)

if image2:  # Display the second image if it loaded successfully
    img2_label = tk.Label(thumbnail_frame, image=image2)
    img2_label.pack(side="left", padx=10)

if image3:  # Display the third image if it loaded successfully
    img3_label = tk.Label(thumbnail_frame, image=image3)
    img3_label.pack(side="left", padx=10)

# Summary window
summary_window = tk.Toplevel(main_window)  # Create the order summary window
summary_window.title("Order Summary")  # Set the title of the summary window
summary_window.geometry("600x400")  # Define the size of the summary window
summary_window.withdraw()  # Hide the summary window initially

summary_label = tk.Label(summary_window, text="Selected Order Summary", font=("Arial", 20, "bold"))
# Title label for the summary window
summary_label.pack(pady=20)

summary_flavor_label = tk.Label(summary_window, text="Flavor: ", font=("Arial", 12))  # Label to display selected flavor
summary_flavor_label.pack()
summary_size_label = tk.Label(summary_window, text="Size: ", font=("Arial", 12))  # Label to display selected size
summary_size_label.pack()
summary_decoration_label = tk.Label(summary_window, text="Decoration: ", font=("Arial", 12))  # Label to display selected decoration
summary_decoration_label.pack()

confirm_button = tk.Button(summary_window, text="Confirm Order", command=confirm_order, bg="lightgreen", font=("Arial", 12))
# Button to confirm the order
confirm_button.pack(pady=20)

# Run the application
main_window.mainloop()  # Start the main event loop
