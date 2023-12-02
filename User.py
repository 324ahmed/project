import tkinter as tk
from tkinter import messagebox

def reserve_cart():
    # Retrieve selected college, start time, and end time from user inputs
    college = college_var.get()
    start_time = start_time_entry.get()
    end_time = end_time_entry.get()

    # Retrieve user type from a global variable or any other appropriate source
    user_type = get_user_type()

    # Perform reservation duration validation
    # Adjust the duration rules based on user type (student, employee, faculty)
    max_duration = 30 if user_type == "Student" else 60 if user_type == "Employee" else 90
    duration = calculate_duration(start_time, end_time)
    if duration > max_duration:
        messagebox.showerror("Reservation Error", "Reservation duration exceeds the allowed limit.")
        return

    # Check cart availability and perform the reservation
    if check_cart_availability(college, start_time, end_time):
        reserve_cart_in_database(college, start_time, end_time)
        messagebox.showinfo("Reservation Success", "Cart reserved successfully.")
    else:
        messagebox.showerror("Reservation Error", "No available carts during the given time & date.")
def show_reservations():
    # Retrieve and display the list of active reservations for the current user
    reservations = retrieve_user_reservations()
    # Display the reservations in a suitable format (e.g., in a listbox or a table)

def logout():
    # Perform logout functionality, such as closing the current window and returning to the sign-up window
    pass

# Create the main window
window = tk.Tk()
window.title("KSUGolfCarts")

# Create the college selection dropdown
colleges = ["College of Since ", " College of Computer Scince And Information ", " College of Engenerinig  "]  # Replace with actual college names
college_var = tk.StringVar()
college_dropdown = tk.OptionMenu(window, college_var, *colleges)
college_dropdown.pack()

# Create start time input field
start_time_label = tk.Label(window, text="Enter start time and date of the reservation:")
start_time_label.pack()
start_time_entry = tk.Entry(window)
start_time_entry.pack()

# Create end time input field
end_time_label = tk.Label(window, text="Enter end time and date of the reservation:")
end_time_label.pack()
end_time_entry = tk.Entry(window)
end_time_entry.pack()

# Create reserve button
reserve_button = tk.Button(window, text="Reserve", command=reserve_cart)
reserve_button.pack()

# Create show button
show_button = tk.Button(window, text="Show Reservations", command=show_reservations)
show_button.pack()

# Create logout button
logout_button = tk.Button(window, text="Logout", command=logout)
logout_button.pack()

# Run the main event loop
window.mainloop()
