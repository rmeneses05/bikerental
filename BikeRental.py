import datetime

class BikeRental:
    def __init__(self, stock=0):
        self.stock = stock

    def display_stock(self):
        return self.stock

    def rent_bike_on_hourly_basis(self, n):
        if n <= 0:
            return "Number of bikes should be positive!"
        elif n > self.stock:
            return f"Sorry! We have currently {self.stock} bikes available to rent."
        else:
            now = datetime.datetime.now()
            message = (f"You have rented {n} bike(s) on hourly basis today at {now.hour} hours.\n"
                       "You will be charged $5 for each hour per bike.\n"
                       "We hope that you enjoy our service.")
            self.stock -= n
            return message

    def rent_bike_on_daily_basis(self, n):
        if n <= 0:
            return "Number of bikes should be positive!"
        elif n > self.stock:
            return f"Sorry! We have currently {self.stock} bikes available to rent."
        else:
            now = datetime.datetime.now()
            message = (f"You have rented {n} bike(s) on daily basis today at {now.hour} hours.\n"
                       "You will be charged $20 for each day per bike.\n"
                       "We hope that you enjoy our service.")
            self.stock -= n
            return message

    def rent_bike_on_weekly_basis(self, n):
        if n <= 0:
            return "Number of bikes should be positive!"
        elif n > self.stock:
            return f"Sorry! We have currently {self.stock} bikes available to rent."
        else:
            now = datetime.datetime.now()
            message = (f"You have rented {n} bike(s) on weekly basis today at {now.hour} hours.\n"
                       "You will be charged $60 for each week per bike.\n"
                       "We hope that you enjoy our service.")
            self.stock -= n
            return message

    def return_bike(self, request):
        rental_time, rental_basis, num_of_bikes = request
        bill = 0

        if rental_time and rental_basis and num_of_bikes:
            self.stock += num_of_bikes
            now = datetime.datetime.now()
            rental_period = now - rental_time

            if rental_basis == 1:
                bill = round(rental_period.seconds / 3600) * 5 * num_of_bikes
            elif rental_basis == 2:
                bill = round(rental_period.days) * 20 * num_of_bikes
            elif rental_basis == 3:
                bill = round(rental_period.days / 7) * 60 * num_of_bikes

            if 3 <= num_of_bikes <= 5:
                bill *= 0.7

            message = (f"Thanks for returning your bike. Hope you enjoyed our service!\n"
                       f"That would be ${bill}")
            return message
        else:
            return "Are you sure you rented a bike with us?"
