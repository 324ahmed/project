import tkinter as tk
from tkinter import messagebox
import datetime


class User:
    def __init__(self, user_type):
        self.user_type = user_type
        self.reservations = []  # Store reservations for the user

    def calculate_duration(self, start_time, end_time):
        duration = end_time - start_time
        return duration

    def reserve_cart(self):
        college = college_var.get()
        start_time = start_time_entry.get()
        end_time = end_time_entry.get()

        try:
            start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
            end_time = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            messagebox.showerror("Reservation Error", "Invalid date and time format. Please use the format YYYY-MM-DD HH:MM:SS.")
            return

        max_duration = datetime.timedelta(minutes=30)
        if self.get_user_type() == "Employee":
            max_duration = datetime.timedelta(hours=1)
        elif self.get_user_type() == "Faculty":
            max_duration = datetime.timedelta(hours=1, minutes=30)

        if end_time < start_time:
            messagebox.showerror("Reservation Error", "End time cannot be earlier than start time.")
            return

        duration = self.calculate_duration(start_time, end_time)
        if duration > max_duration:
            max_hours = max_duration.total_seconds() // 3600
            max_minutes = (max_duration.total_seconds() % 3600) // 60
            messagebox.showerror("Reservation Error", f"Reservation duration exceeds the allowed limit of {int(max_hours)} hours and {int(max_minutes)} minutes.")
            return

        if self.check_cart_availability(college, start_time, end_time):
            self.reserve_cart_in_database(college, start_time, end_time)
            messagebox.showinfo("Reservation Success", "Cart reserved successfully.")
        else:
            messagebox.showerror("Reservation Error", "No available carts during the given time & date.")

    def show_reservations(self):
        if self.reservations:
            reservation_messages = []
            for index, reservation in enumerate(self.reservations, start=1):
                start_time = reservation["start_time"].strftime("%Y-%m-%d %H:%M:%S")
                end_time = reservation["end_time"].strftime("%Y-%m-%d %H:%M:%S")
                reservation_message = f"Reservation {index}:\nStart Time: {start_time}\nEnd Time: {end_time}"
                reservation_messages.append(reservation_message)
            messagebox.showinfo("Reservations", "\n\n".join(reservation_messages))
        else:
            messagebox.showinfo("Reservations", "No reservations found.")

    def logout(self):

        window.destroy()

        # Create a new instance of the SignUp class to display the Signup window
        from signup import SignUp
        signup_window = SignUp()

    def get_user_type(self):
        return self.user_type

    def check_cart_availability(self, college, start_time, end_time):

        if college == "College of Science" and start_time.hour >= 8 and end_time.hour <= 16:
            return True
        elif college == "College of Computer Science and Information" and start_time.hour >= 9 and end_time.hour <= 17:
            return True
        elif college == "College of Engineering" and start_time.hour >= 10 and end_time.hour <= 18:
            return True
        else:
            return False

    def reserve_cart_in_database(self, college, start_time, end_time):
        # Implement cart reservation in the database
        reservation = {"start_time": start_time, "end_time": end_time}
        self.reservations.append(reservation)


window = tk.Tk()
window.title("KSUGolfCarts")

# Create the college selection dropdown
import CentralDatabase as cd

cursor = cd.conn.cursor()


cursor.execute('SELECT College FROM GOLF_CART')


rows = cursor.fetchall()


colleges = []
depts = ('IS', 'CS', 'CE', 'IT', 'SE')
for row in rows:
    colleges.append(row[0])




college_var = tk.StringVar()


college_dropdown = tk.OptionMenu(window, college_var, *colleges)
college_dropdown.pack()

start_time_label = tk.Label(window, text="Enter start time and date of the reservation (YYYY-MM-DD HH:MM:SS):")
start_time_label.pack()
start_time_entry = tk.Entry(window, bd=5)
start_time_entry.pack()

end_time_label = tk.Label(window, text="Enter end time and date of thereservation (YYYY-MM-DD HH:MM:SS):")
end_time_label.pack()
end_time_entry = tk.Entry(window, bd=5)
end_time_entry.pack()


user = User("Employee") 

reserve_cart_button = tk.Button(window, text="Reserve Cart", command=user.reserve_cart)
reserve_cart_button.pack()

show_reservations_button = tk.Button(window, text="Show Reservations", command=user.show_reservations)
show_reservations_button.pack()

logout_button = tk.Button(window, text="Logout", command=user.logout)
logout_button.pack()

# Start the main event loop
window.mainloop()
