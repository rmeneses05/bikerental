class Customer:
    def __init__(self):
        self.bikes = 0
        self.rental_basis = 0
        self.rental_time = None

    def request_bike(self, n):
        if n <= 0:
            return "Number of bikes should be positive!"
        else:
            self.bikes = n
            return f"Requested {n} bike(s)"

    def return_bike(self):
        if self.rental_basis != 0 and self.rental_time is not None and self.bikes != 0:
            return self.rental_time, self.rental_basis, self.bikes
        else:
            return None

    def set_rental_basis(self, basis):
        self.rental_basis = basis

    def set_rental_time(self, time):
        self.rental_time = time
