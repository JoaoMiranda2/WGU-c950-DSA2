import datetime

class Package:
    """
    Represents a package.
    """

    def __init__(self, ID, address, city, state, zipcode, deadline_time, weight, status):
        """
        Initializes a Package.

        Args:
            ID (int): Package ID.
            address (str): Delivery address.
            city (str): Delivery city.
            state (str): Delivery state.
            zipcode (str): Delivery ZIP code.
            deadline_time (datetime.timedelta): Delivery deadline time.
            weight (str): Package weight.
            status (str): Current status.
        """
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline_time = deadline_time
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None
        if deadline_time == datetime.timedelta(hours=23, minutes=59, seconds=59):
            self.deadline_str = "EOD"
        else:
            deadline_datetime = datetime.datetime.min + deadline_time
            self.deadline_str = deadline_datetime.strftime("%I:%M:%S %p")

    def __str__(self):
        """
        Returns a string representation of the package.

        Returns:
            str: Package details.
        """
        if self.delivery_time:
            if isinstance(self.delivery_time, datetime.datetime):
                delivery_time_str = self.delivery_time.strftime("%I:%M:%S %p")
            else:
                total_seconds = int(self.delivery_time.total_seconds())
                delivery_time_str = (datetime.datetime.min + datetime.timedelta(seconds=total_seconds)).strftime(
                    "%I:%M:%S %p")
        else:
            delivery_time_str = "Not yet delivered"

        return (f"Package ID: {self.ID}, Address: {self.address}, City: {self.city}, State: {self.state}, "
                f"ZIP Code: {self.zipcode}, Deadline: {self.deadline_str}, Weight: {self.weight}, "
                f"Delivery Time: {delivery_time_str}, Status: {self.status}")

    def update_status(self, current_time):
        """
        Updates the package status based on the current time.

        Args:
            current_time (datetime.timedelta or datetime.datetime): Current time.
        """
        # If current_time is a timedelta, convert it to a datetime object.
        if isinstance(current_time, datetime.timedelta):
            current_time = datetime.datetime.min + current_time

        # If departure_time is set and is a timedelta, convert it to a datetime object.
        if self.departure_time:
            if isinstance(self.departure_time, datetime.timedelta):
                self.departure_time = datetime.datetime.min + self.departure_time

        # If delivery_time is set and is a timedelta, convert it to a datetime object.
        if self.delivery_time:
            if isinstance(self.delivery_time, datetime.timedelta):
                self.delivery_time = datetime.datetime.min + self.delivery_time

        # Update the package status based on the current time.
        if self.delivery_time and current_time >= self.delivery_time:
            # If the current time is past the delivery time, set status to "Delivered".
            self.status = "Delivered"
        elif self.departure_time and current_time >= self.departure_time:
            # If the current time is past the departure time but before the delivery time, set status to "En Route".
            self.status = "En Route"
        else:
            # If the current time is before the departure time, set status to "At Hub".
            self.status = "At Hub"