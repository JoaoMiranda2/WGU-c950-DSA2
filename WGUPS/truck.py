"""
Joao Marcelo Martins Miranda
Student ID: 010548237
"""

class Truck:
    """
    Represents a delivery truck.
    """

    def __init__(self, truck_id, capacity, speed, load, packages, mileage, address, depart_time):
        """
        Initializes a Truck.

        Args:
            truck_id (int): Truck ID.
            capacity (int): Truck capacity.
            speed (int): Truck speed.
            load (any): Current load.
            packages (list): Package IDs.
            mileage (float): Truck mileage.
            address (str): Current address.
            depart_time (datetime.timedelta): Departure time.
        """
        self.truck_id = truck_id
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time
        self.delivered_packages = []

    def print_mileage(self):
        """
        Prints the truck mileage.
        """
        print(f"Truck ID: {self.truck_id}, Mileage: {self.mileage} miles")

    def __str__(self):
        """
        Returns a string representation of the truck.

        Returns:
            str: Truck details.
        """
        return (f"Truck ID: {self.truck_id}, Capacity: {self.capacity}, Speed: {self.speed}, "
                f"Load: {self.load}, Packages: {self.packages}, Mileage: {self.mileage}, "
                f"Address: {self.address}, Depart Time: {self.depart_time}")