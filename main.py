import tkinter as tk
from tkinter import messagebox
from BikeRental import BikeRental
from Customer import Customer
import datetime


class BikeRentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bike Rental System")

        # Set background color of the root window
        self.root.configure(bg='red')

        self.shop = BikeRental(10)
        self.customer = Customer()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Bike Rental System", font=("Helvetica", 16), bg='red', fg='white').pack(pady=10)

        # Label to display available bikes
        self.label_stock = tk.Label(self.root, text=f"Available bikes: {self.shop.display_stock()}", bg='red',
                                    fg='white')
        self.label_stock.pack()

        # Frame for rental options
        frame_rental = tk.Frame(self.root, bg='red')
        frame_rental.pack(pady=10)

        tk.Label(frame_rental, text="Select Rental Option:", bg='red', fg='white').pack(side=tk.LEFT)

        # Rental buttons
        tk.Button(frame_rental, text="Hourly ($5)", command=lambda: self.rent_bike(1), bg='white').pack(side=tk.LEFT,
                                                                                                        padx=5)
        tk.Button(frame_rental, text="Daily ($20)", command=lambda: self.rent_bike(2), bg='white').pack(side=tk.LEFT,
                                                                                                        padx=5)
        tk.Button(frame_rental, text="Weekly ($60)", command=lambda: self.rent_bike(3), bg='white').pack(side=tk.LEFT,
                                                                                                         padx=5)

        # Frame for return option
        frame_return = tk.Frame(self.root, bg='red')
        frame_return.pack(pady=10)

        tk.Button(frame_return, text="Return Bike", command=self.return_bike, bg='white').pack()

        # Exit button
        tk.Button(self.root, text="Exit", command=self.root.quit, bg='white').pack(pady=10)

    def rent_bike(self, basis):
        if self.customer.bikes == 0:
            n = self.ask_integer_dialog("Rent Bike", "How many bikes would you like to rent?", initialvalue=1)
            if n is not None:
                message = ""
                if basis == 1:
                    message = self.shop.rent_bike_on_hourly_basis(n)
                elif basis == 2:
                    message = self.shop.rent_bike_on_daily_basis(n)
                elif basis == 3:
                    message = self.shop.rent_bike_on_weekly_basis(n)

                if "You have rented" in message:
                    self.customer.request_bike(n)
                    self.customer.set_rental_basis(basis)
                    self.customer.set_rental_time(datetime.datetime.now())
                    self.update_stock_label()

                messagebox.showinfo("Rental Information", message)

    def return_bike(self):
        rental_info = self.customer.return_bike()
        if rental_info:
            message = self.shop.return_bike(rental_info)
            self.customer.set_rental_basis(0)
            self.customer.set_rental_time(None)
            self.customer.bikes = 0
            self.update_stock_label()
            messagebox.showinfo("Return Information", message)
        else:
            messagebox.showwarning("Return Information", "No active rental found.")

    def update_stock_label(self):
        self.label_stock.config(text=f"Available bikes: {self.shop.display_stock()}")

    def ask_integer_dialog(self, title, prompt, initialvalue=0):
        top = tk.Toplevel(self.root)
        top.title(title)
        top.configure(bg='red')

        frame = tk.Frame(top, bg='red')
        frame.pack(padx=10, pady=10)

        tk.Label(frame, text=prompt, bg='red', fg='white').pack()

        var = tk.IntVar()
        entry = tk.Entry(frame, textvariable=var)
        entry.pack()

        var.set(initialvalue)

        def on_ok():
            top.destroy()

        btn_ok = tk.Button(frame, text="OK", command=on_ok, bg='white')
        btn_ok.pack()

        entry.focus_set()
        top.wait_window()
        return var.get()

if __name__ == "__main__":
    root = tk.Tk()
    app = BikeRentalApp(root)
    root.mainloop()
